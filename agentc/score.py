#!/usr/bin/env python3
"""Chấm bài test AgentC so với đáp án đo tay.

Cách dùng:
  python3 agentc/score.py --gold GOLD.json --pred PRED [--require-open]
                          [--min-comp-f1 X] [--min-net-score Y]

PRED có thể là:
  .json        cùng định dạng với đáp án; không kiểm được việc KiCad mở file
  .xml         KiCad netlist XML đã xuất sẵn (kicad-cli sch export netlist --format kicadxml)
  .kicad_sch   cần kicad-cli trên máy; nếu KiCad không mở được thì bị tính là không mở được

In báo cáo JSON ra stdout. Thoát 0 nếu đạt, 1 nếu không đạt.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter


def norm_value(text):
    """Chuẩn hóa giá trị để 10kΩ, 10K, 10 k ohm cùng thành '10k'."""
    if not text:
        return ""
    return text.lower().replace("ω", "").replace("ohm", "").replace(" ", "")


def kind_of(ref):
    """Loại linh kiện lấy từ tiền tố ký hiệu: U, R, C, L, D, Q, J, F, TH, ..."""
    m = re.match(r"[A-Za-z]+", ref or "")
    return m.group(0).upper() if m else "?"


def keep_net(pins):
    """Net chỉ có một chân không phải kết nối, bỏ qua khi chấm."""
    return len(pins) >= 2


def load_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    comps = [
        {"ref": c["ref"], "key": (kind_of(c["ref"]), norm_value(c.get("value") or c.get("part")))}
        for c in data.get("components", [])
    ]
    nets = [frozenset(n["pins"]) for n in data.get("nets", [])]
    return comps, [n for n in nets if keep_net(n)]


def load_kicad_xml(path):
    root = ET.parse(path).getroot()
    comps = []
    for c in root.iter("comp"):
        ref = c.get("ref", "")
        lib = c.find("libsource")
        part = lib.get("part", "") if lib is not None else ""
        comps.append({"ref": ref, "key": (kind_of(ref), norm_value(c.findtext("value") or part))})
    nets = []
    for n in root.iter("net"):
        pins = frozenset(f"{nd.get('ref')}.{nd.get('pin')}" for nd in n.findall("node"))
        if keep_net(pins):
            nets.append(pins)
    return comps, nets


def load_pred(path):
    """Trả về (components, nets, opens). opens: True/False nếu kiểm được KiCad, None nếu không kiểm được."""
    if path.endswith(".json"):
        comps, nets = load_json(path)
        return comps, nets, None
    if path.endswith(".xml"):
        comps, nets = load_kicad_xml(path)
        return comps, nets, True
    if path.endswith(".kicad_sch"):
        kicad = shutil.which("kicad-cli")
        if kicad is None:
            sys.exit("Không tìm thấy kicad-cli. Cài KiCad 8 trở lên, hoặc xuất netlist XML rồi truyền file .xml.")
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "netlist.xml")
            proc = subprocess.run(
                [kicad, "sch", "export", "netlist", "--format", "kicadxml", "--output", out, path],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0 or not os.path.exists(out):
                return [], [], False
            try:
                comps, nets = load_kicad_xml(out)
            except ET.ParseError:
                return [], [], False
            return comps, nets, True
    sys.exit(f"Định dạng không hỗ trợ: {path}")


def multiset_f1(gold_keys, pred_keys):
    g, p = Counter(gold_keys), Counter(pred_keys)
    matched = sum((g & p).values())
    precision = matched / sum(p.values()) if p else 0.0
    recall = matched / sum(g.values()) if g else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1, "matched": matched,
            "gold": sum(g.values()), "pred": sum(p.values())}


def net_scores(gold_nets, pred_nets):
    """Ghép mỗi net đáp án với net dự đoán chưa dùng có Jaccard lớn nhất (tham lam)."""
    unused = list(pred_nets)
    jaccards = []
    exact = 0
    for g in gold_nets:
        best, best_j = None, 0.0
        for p in unused:
            j = len(g & p) / len(g | p)
            if j > best_j:
                best, best_j = p, j
        if best is not None:
            unused.remove(best)
        if best_j == 1.0:
            exact += 1
        jaccards.append(best_j)
    score = sum(jaccards) / len(gold_nets) if gold_nets else 0.0
    return {"gold_nets": len(gold_nets), "pred_nets": len(pred_nets),
            "exact": exact, "score": score, "unmatched_pred": len(unused)}


def score(gold_path, pred_path, require_open, min_comp_f1, min_net_score):
    gold_comps, gold_nets = load_json(gold_path)
    pred_comps, pred_nets, opens = load_pred(pred_path)

    comp = multiset_f1([c["key"] for c in gold_comps], [c["key"] for c in pred_comps])
    net = net_scores(gold_nets, pred_nets)

    reasons = []
    if require_open and opens is not True:
        reasons.append("KiCad không mở được file, hoặc không kiểm được")
    if comp["f1"] < min_comp_f1:
        reasons.append(f"F1 linh kiện {comp['f1']:.3f} < {min_comp_f1}")
    if net["score"] < min_net_score:
        reasons.append(f"điểm net {net['score']:.3f} < {min_net_score}")

    return {
        "opens_in_kicad": opens,
        "components": comp,
        "nets": net,
        "passed": not reasons,
        "reasons": reasons,
    }


def main():
    ap = argparse.ArgumentParser(description="Chấm bài test AgentC")
    ap.add_argument("--gold", required=True, help="đáp án đo tay (.json)")
    ap.add_argument("--pred", required=True, help="kết quả AgentC (.json, .xml hoặc .kicad_sch)")
    ap.add_argument("--require-open", action="store_true", help="bắt buộc KiCad mở được file")
    ap.add_argument("--min-comp-f1", type=float, default=0.0, help="ngưỡng F1 linh kiện")
    ap.add_argument("--min-net-score", type=float, default=0.0, help="ngưỡng điểm net")
    a = ap.parse_args()
    report = score(a.gold, a.pred, a.require_open, a.min_comp_f1, a.min_net_score)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
