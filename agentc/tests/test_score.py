import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import score  # noqa: E402

EX = os.path.join(ROOT, "examples")
GOLD = os.path.join(EX, "answer_key.json")
PRED = os.path.join(EX, "pred_good.json")
XML = os.path.join(EX, "kicad_netlist.xml")


class ScoreTests(unittest.TestCase):
    def test_norm_value(self):
        self.assertEqual(score.norm_value("10kΩ"), "10k")
        self.assertEqual(score.norm_value("10 K ohm"), "10k")
        self.assertEqual(score.norm_value(None), "")

    def test_kind_of(self):
        self.assertEqual(score.kind_of("U12"), "U")
        self.assertEqual(score.kind_of("R3"), "R")
        self.assertEqual(score.kind_of("TH1"), "TH")

    def test_perfect_match_scores_one(self):
        r = score.score(GOLD, GOLD, False, 0, 0)
        self.assertEqual(r["components"]["f1"], 1.0)
        self.assertEqual(r["nets"]["score"], 1.0)
        self.assertEqual(r["nets"]["exact"], 3)
        self.assertTrue(r["passed"])

    def test_example_prediction(self):
        r = score.score(GOLD, PRED, False, 0, 0)
        self.assertAlmostEqual(r["components"]["precision"], 0.8)
        self.assertAlmostEqual(r["components"]["recall"], 1.0)
        self.assertAlmostEqual(r["nets"]["score"], (1 + 1 + 0.75) / 3)
        self.assertEqual(r["nets"]["exact"], 2)
        self.assertEqual(r["nets"]["unmatched_pred"], 1)

    def test_xml_matches_json_gold(self):
        gc, gn = score.load_json(GOLD)
        xc, xn = score.load_kicad_xml(XML)
        self.assertEqual(sorted(c["key"] for c in gc), sorted(c["key"] for c in xc))
        self.assertEqual(set(gn), set(xn))

    def test_xml_prediction_scores_like_gold(self):
        r = score.score(GOLD, XML, True, 0, 0)
        self.assertTrue(r["opens_in_kicad"])
        self.assertEqual(r["components"]["f1"], 1.0)
        self.assertEqual(r["nets"]["score"], 1.0)
        self.assertTrue(r["passed"])

    def test_require_open_fails_when_open_unknown(self):
        r = score.score(GOLD, PRED, True, 0, 0)
        self.assertIsNone(r["opens_in_kicad"])
        self.assertFalse(r["passed"])

    def test_threshold_gate(self):
        r = score.score(GOLD, PRED, False, 0.95, 0.5)
        self.assertFalse(r["passed"])
        self.assertTrue(any("F1" in x for x in r["reasons"]))


if __name__ == "__main__":
    unittest.main()
