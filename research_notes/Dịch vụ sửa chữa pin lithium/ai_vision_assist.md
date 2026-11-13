# AI computer vision and vision-language models as a technician assistant in a small lithium battery pack repair workshop (state as of Nov 2026)

Reading guide for the report writer:
- Tags used below: **[STUDY]** = measured result in a paper/preprint; **[OFFICIAL]** = vendor's own documentation or price list (reliable for price/spec, not for performance); **[VENDOR CLAIM]** = marketing or self-reported case study, no methodology; **[SECONDARY]** = aggregator/law-firm/review summary, not checked against the primary text.
- Almost every accuracy number below comes from factory or benchmark imagery (bare boards, production-line cells, fixed lighting). I found **no published study on AI vision in a battery repair workshop** (used packs, hand-held phone photos, dirty/corroded BMS boards). Treat all figures as upper bounds for workshop conditions.
- Search results were returned by a US-only search tool; Vietnamese retail prices were not obtained.

## 1. Use cases and evidence: what can vision AI recognise at each repair stage, and with what accuracy?

### Takeaway
Published evidence is strong for narrow, trained detectors on controlled images (bare-PCB defects ~93-99% mAP@0.5; production-line cell defects ~80-94% mAP) and weak or absent for the workshop's real needs (burnt/corroded assembled BMS boards, used-cell swelling/leakage, hand-made nickel spot welds, real early thermal-runaway warning). General VLMs are well below human experts on defect judgement (best 74.9% vs 86.7%) and poor at reading precise instrument values (~30% value accuracy), so they suit explanation, OCR-style reading and guidance rather than pass/fail decisions.

### Cited Findings

**PCB / BMS board inspection**
- [STUDY] PCB-YOLO (YOLOv8n-based): 98.4% mAP@0.5, 97.4% recall, 96.1% precision on PKU-Market-PCB with 2.4M parameters at 224 FPS; 99.0% mAP@0.5 but only 80.4% mAP@0.5:0.95 on DeepPCB — [MDPI Electronics 14(17):3383](https://mdpi.com/2079-9292/14/17/3383)
- [STUDY] SME-YOLO (YOLOv11n-based): 97.0% mAP on PKU-Market-PCB, +2.2 points over baseline YOLOv11n — [arXiv 2601.11402](https://arxiv.org/html/2601.11402v1)
- [STUDY] YOLO-iDAT (YOLOv11-based): precision 0.941, mAP50 0.93, recall 0.895 on PKU-Market-PCB — [Information Technology and Control](https://itc.ktu.lt/index.php/ITC/article/view/43456)
- [STUDY] Pruned YOLOv8n with group convolution: 96.7% mAP@0.5 on an enhanced PKU-Market-PCB (+1.7 over YOLOv8n) — [PeerJ CS 3243](https://peerj.com/articles/cs-3243)
- Important scope limit: these benchmark datasets cover six **bare-board copper defects** (open, short, mousebite, spur, pin hole, spurious copper), not burnt components, corrosion, cracked solder joints or swollen capacitors on assembled boards — [Labelbox DeepPCB page](https://labelbox.com/datasets/deeppcb-printed-circuit-board-pcb-defect-dataset)

**Component identification and marking OCR (MOSFET / protection-IC part numbers)**
- [STUDY] An end-to-end three-branch model for IC marking inspection reached 96.34% recall at ~30 fps on a real SMT chip dataset; authors note diverse marking appearance and annotation cost make this hard — reported via [search summary of IEEE Transactions paper, catalogue record](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........43ffff892a9555a15b22ba8f639c2bb8) (numbers not verified in the full text)
- [STUDY] A 2021 survey of deep-learning text recognition for PCB optical inspection stresses the lack of well-annotated PCB marking data and that automatic marking recognition is "important and challenging" for bill-of-materials extraction — [Ghosh et al., IEEE PAINE survey record](https://www.aminer.org/pub/622a5fee5aee126c0f31ffc7/deep-learning-based-approaches-for-text-recognition-in-pcb-optical-inspection-a); framework paper at [arXiv 2307.13105](https://arxiv.org/pdf/2307.13105)
- A patent application notes conventional OCR is poorly suited to component text because it may be silk-printed, laser-engraved or cast — [USPTO 12406355](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12406355) (patent, not peer-reviewed)
- [STUDY] In the MMAD benchmark, general VLMs are strongest at identifying *what the object is*: object classification 94.98% (GPT-4o), 91.47% (Gemini-1.5-flash), 85.19% (Claude-3.5-sonnet) — far better than their defect scores — [MMAD, arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)

**Cell defect detection (swelling, dents, leakage, rust, damaged wrap)**
- [STUDY] YOLOv3 on cylindrical-cell bottom defects: 94% mAP at 25 fps (custom validation set) — [SPIE author profile listing](https://ebooks.spiedigitallibrary.org/profile/Yuzhong.Zhang-4164254)
- [STUDY] Improved YOLOv5s on a custom cylindrical coated-cell dataset: 82.4% average detection rate (+2.3 over YOLOv5s) — [Engineering Letters 32(7)](https://engineeringletters.com/issues_v32/issue_7/EL_32_7_26.pdf)
- [STUDY] YOLO-MDD on battery-shell end faces: 80% mAP overall, rust spots only 74.1%; authors had to build their own dataset because no public battery-shell defect dataset existed — [Minimal Defect Detection on End Face of Lithium Battery Shells](https://www.bohrium.com/en/paper-details/minimal-defect-detection-on-end-face-of-lithium-battery-shells/1069840321614970969-3177)
- [STUDY] 18650 steel casings are reflective; one study needed a line-focused laser illumination rig with YOLOv5 to get reliable defect images — [Informatica](https://www.informatica.si/index.php/informatica/article/view/7556/6314)
- [STUDY] A YOLOv11n pouch-cell study used 15,312 production-line images at 1024×1024 — [Sustainability 16(23):10502 record](https://ideas.repec.org/a/gam/jsusta/v16y2024i23p10502-d1533431.html)

**Spot-weld quality inspection**
- No peer-reviewed study reporting image-based deep-learning accuracy for **manual nickel-strip resistance spot welds** was found. Closest work: CU-Net for laser-weld spots in battery production (faster and more accurate than U-Net / Mask R-CNN / PSPNet; exact figure not retrieved) — [IEEE TIE 2020 record, HIT](https://scholar.hit.edu.cn/en/publications/real-time-cu-net-based-welding-quality-inspection-algorithm-in-ba/)
- [STUDY] Ultrasonic (non-visual) + deep learning classifies tab-to-can resistance spot welds into non-welded / insufficient / good / excessive — [MDPI Batteries 8(3):21](https://mdpi.com/2313-0105/8/3/21)
- [STUDY] In-situ thermal imaging with an ML pipeline to classify laser welds between nickel-plated steel and stainless steel (2026; accuracy not retrieved) — [Hoang et al. 2026](https://cse.sc.edu/~adowney2/publications/conference/Hoang2026SituThermalImaging.pdf)
- [VENDOR CLAIM] "99.2% accuracy" for porosity/crack/undercut detection on battery tab/busbar laser welds, no published methodology — [iFactory](https://ifactoryapp.com/industries/automotive-manufacturing/battery-tab-busbar-laser-weld-ai); similar vendor material from [Overview.ai](https://www.overview.ai/blog/battery-weld-inspection/)

**Thermal (IR) hot-spot analysis and thermal-runaway early warning**
- [STUDY] IR hotspot-guided early warning under mechanical abuse: hotspot-only model ROC-AUC 0.945 vs 0.881 for a sensor-only model at 20-frame-ahead warning; thermal-gradient rise gave mean lead time 40.3 frames vs 21.0 frames for a voltage-drop threshold — [arXiv 2608.20383](https://arxiv.org/pdf/2608.20383)
- [STUDY] Optical + IR classification of "thermal runaway" on a production line (shallow CNN, ResNet-50, ViT; 832 samples = 412 baseline + 420 event): ResNet and ViT reached ROC-AUC 1.00, but IR-only shallow CNN only 0.87 ROC-AUC / 0.77 PR-AUC. Events were **simulated** with resistance heaters (>35 °C) and a fog machine, only at an advanced stage; authors say the perfect scores may mean the dataset was too easy and that false-positive/false-negative costs were not analysed — [arXiv 2504.08632v2](https://arxiv.org/html/2504.08632v2)
- [STUDY] Unsupervised anomaly detection on thermal images of commercial PHEV pouch cells exists as a research direction (feature-adapted unsupervised AD) — [University of Luxembourg](https://orbilu.uni.lu/bitstream/10993/63428/1/AI-enabled%20thermal%20monitoring%20of%20commercial%20%28PHEV%29%20Li-ion%20pouch%20cells%20with%20Feature-Adapted%20Unsupervised%20Anomaly%20Detection.pdf)
- [VENDOR CLAIM] Raytron press release on AI thermal imaging for EV battery thermal-runaway prevention gives no validated accuracy metrics — [PR Newswire](https://tools.prnewswire.com/en-us/live/20813/release/20251107EN18642)

**Reading multimeter / tester displays**
- [STUDY] MeasureBench (CVPR 2026; 2,442 images, includes digital-style displays): frontier VLMs reach only ~30% overall value accuracy while unit recognition exceeds 90% — [arXiv 2510.26865](https://arxiv.org/abs/2510.26865v1)
- [STUDY] InSituMeasure (2,922 real industrial gauge-reading tasks, includes unsupported prompts to probe hallucination): unit recognition consistently easier than numeric reading; value accuracy stays low — [arXiv 2609.04014](https://arxiv.org/pdf/2609.04014)
- [STUDY] Frontier VLMs (GPT-5 and Gemini 3 variants) on video of analog gauges are "not yet reliable enough for safety-critical monitoring" — [arXiv 2604.22829](https://arxiv.org/pdf/2604.22829)
- [VENDOR CLAIM] "95–99% accuracy on legible digital LCDs" with no test set cited — [imagetotable.ai blog](https://imagetotable.ai/blog/can-ai-read-meter-from-photo)

**Safety monitoring (PPE, smoke/flame)**
- [STUDY] PPE detection: DETR and YOLOv11n tied at mAP@0.5:0.95 = 0.770, YOLOv8 0.763 (Dec 2025 comparison) — [JAIC, Politeknik Negeri Batam](https://jurnal.polibatam.ac.id/index.php/JAIC/article/download/11593/3246/37036)
- [STUDY] A Vietnamese study on a custom PPE dataset reported YOLOv8l/x mAP 0.958 — [Journal of Technical Education Science (jte.edu.vn)](https://www.jte.edu.vn/index.php/jte/article/download/1637/1406/13425)
- [STUDY] YOLOv8 PPE system in a palm-oil plant: mAP 67.3%, precision 96.5%, recall 85.4% — shows how much results swing with dataset — [ILKOM journal](https://jurnal.fikom.umi.ac.id/index.php/ILKOM/article/download/2544/pdf)
- [STUDY] Review of fire detection: fused IR+RGB network 85.6% detection accuracy at 30 FPS; a thermal+visible fusion approach 94.3% — [MDPI Fire 8:214](https://mdpi-res.com/d_attachment/fire/fire-08-00214/article_deploy/fire-08-00214.pdf)
- [STUDY] A chemical-park safety paper notes deployed models often show low detection rates with frequent false positives/negatives; smoke and workers are easily missed under occlusion or backlight — [AIMS Electronics and Electrical Engineering 9(3)](https://aimspress.com/aimspress-data/electreng/2025/3/PDF/electreng-09-03-013.pdf)

**General VLMs on defect judgement (applies to every stage)**
- [STUDY] MMAD benchmark (ICLR 2025; 39,672 questions on 8,366 industrial images, 7 subtasks): average accuracy GPT-4o 74.92%, Gemini-1.5-pro 73.09%, Gemini-1.5-flash 68.90%, Claude-3.5-sonnet 68.36%; human expert 86.65%, ordinary human 78.69%, random 28.57% — [arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- [STUDY] Same benchmark, GPT-4o by subtask: anomaly discrimination (is it defective?) 68.63%, defect classification 65.80%, defect localisation 55.62%, defect description 73.21%, defect analysis 83.41%, object classification 94.98%. Human experts: 95.24% discrimination, 92.31% localisation — [arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- The MMAD authors conclude the best result "falls far short of industrial requirements" — [MMAD ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d91ffbe9c126765755ff52d36b715683-Abstract-Conference.html)

### Inferences
Use-case map (stage → what AI vision can plausibly do → evidence strength → who decides). Evidence ratings are my synthesis of the findings above.

| Workflow stage | AI vision role | Best-fit technique | Evidence strength | Decision owner |
|---|---|---|---|---|
| Intake | Photograph pack + label; extract model, voltage, capacity, chemistry into the job ticket; flag visible swelling/burn marks for triage | VLM via API (reading printed text and naming objects is the VLMs' strongest area) | Moderate (object ID ~85-95% in MMAD; no battery-label study found) | Technician confirms extracted fields |
| Diagnosis | Capture meter/tester screens into the record; suggest next test from SOP | VLM + SOP retrieval; typed entry as fallback | Weak for numeric reading (~30% value accuracy on mixed instruments) | Technician re-keys or confirms every value |
| BMS/PCB inspection | Highlight suspected burnt parts, corrosion, missing parts; read MOSFET/IC markings and look up datasheet | VLM for explanation and marking reading; trained detector or golden-board anomaly detection later | Weak for assembled-board damage (benchmarks are bare-board); marking OCR is a known hard problem | Technician |
| Cell grading | Flag dents, rust, leakage, torn wrap as a pre-screen before electrical tests | Trained YOLO detector on own images; diffuse lighting needed for reflective cans | Moderate in factories (80-94% mAP), untested on used cells | Electrical tests (capacity, IR, self-discharge) and technician; vision is only a pre-screen |
| Welding QC | Photo of each weld row attached to the ticket; check count/position of welds; flag obviously burnt or missing spots | Checklist + photo evidence first; custom detector only after data exists | None for manual nickel spot welds | Pull test / technician |
| Final QC | Enforced photo checklist (insulation, fishpaper, wire routing, label), IR photo under load | App checklist + VLM completeness check + thermal camera | No direct study | Senior technician signs off |
| Safety monitoring | Fixed thermal camera on charge/test bench with temperature and rate-of-rise alarm; optional smoke/PPE detector | Simple thresholding first; learned models later | Research-stage; best paper used simulated events | Never a substitute for smoke detectors, fire containment and supervision |

- VLMs' profile (good at naming and describing, poor at "is this defective" and "where exactly") suggests using them as an explainer and form-filler, and using trained detectors for any repetitive pass/fail screen.
- Because 18650 cans are reflective and one study needed special illumination, lighting control (light box or ring light with diffuser) is likely more important than model choice for cell and weld photos.
- For hot-spot detection on a discharging pack, a plain temperature threshold and cell-to-cell temperature difference from the camera's radiometric data probably delivers most of the value without any ML; the cited research adds lead time, not basic detection.

### Gaps
- No study found on vision inspection of **used/aged** cells (swelling, electrolyte leakage residue) or of **repair-shop BMS boards**; all sources are manufacturing lines.
- No peer-reviewed accuracy for image-based inspection of hand-made nickel spot welds; weld strength is not visually determinable in the sources found.
- No published accuracy figure for VLMs reading seven-segment multimeter displays specifically; benchmarks mix analog and digital instruments.
- No battery-label OCR benchmark found (cell model codes such as laser-etched markings on 18650 wraps).
- Exact accuracy figures of the IC-marking papers and CU-Net were not retrieved from full texts.
- Swollen-capacitor and cracked-solder-joint detection: no specific study retrieved.

## 2. Technology options: cloud VLMs vs trained detectors vs on-device models

### Takeaway
A cloud VLM costs a fraction of a US cent to about two cents per photo and needs no training, which makes it the cheapest way to start, but its defect judgement is measurably unreliable and it needs connectivity. Trained detectors and anomaly models give repeatable, offline, millisecond-level results on Android but need the workshop's own labelled images; on-device Gemini Nano accepts image input but only on a short list of flagship phones.

### Cited Findings

**Cloud VLM pricing and image cost (official pages, fetched Nov 2026)**
- [OFFICIAL] Anthropic list prices per million tokens (input / output): Claude Haiku 5.5 $0.10 / $0.50 (prompts up to 100k tokens); Claude Sonnet 5.5 $2 / $10; Claude Opus 5.5 $4 / $20; Claude Fable 5.2 $8 / $40; Claude Haiku 4.5 $1 / $5. Batch processing is half price (e.g. Sonnet 5.5 $1 / $5) — [Claude pricing docs](https://platform.claude.com/en/docs/about-claude/pricing)
- [OFFICIAL] Claude image cost: each 28×28-pixel patch is one visual token, so an image costs ⌈width/28⌉ × ⌈height/28⌉ tokens. A 1000×1000 image = 1,296 tokens. Newer models (Claude 4.7 and later) accept up to 2,576 px on the long edge (max 4,784 visual tokens); older ones downsize to 1,568 px (max 1,568 tokens). Maximum image dimensions 8000×8000 px — [Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- [OFFICIAL] Anthropic's own cost examples: a 1000×1000 image is about $1.30 per thousand images on Haiku 4.5 and about $5.18 per thousand on Opus 5.5; a 4K image on Opus 5.5 about $19.14 per thousand — [Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- [OFFICIAL] Anthropic's stated vision limitations: Claude "might hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels"; coordinate/localisation outputs are approximate and should be verified; counts may be imprecise "especially with large numbers of small objects" — [Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- [OFFICIAL] Gemini API paid-tier prices per million tokens (input text/image / output): Gemini 3.1 Flash-Lite $0.25 / $1.50; Gemini 3.5 Flash-Lite $0.30 / $2.50; Gemini 3.8 Flash $0.75 / $3.75 until 31 Dec 2026, then $1.50 / $7.50; Gemini 3.1 Pro Preview $2 / $12 (prompts ≤200k). Batch tier is 50% cheaper — [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- [OFFICIAL] Gemini Flash and Flash-Lite models have a free tier, but free-tier data **is used to improve Google products**; paid-tier data is not — [Gemini API pricing](https://aistudio.google.com/docs/pricing)

**VLM accuracy and ways to improve it**
- [STUDY] Adding retrieval (RAG with domain knowledge) raised MMAD average accuracy by about 5.4–6.8 points for open models (e.g. InternVL2-40B 69.59 → 76.35), with defect classification gaining roughly 17–20 points; anomaly discrimination changed inconsistently (−1.57 to +5.56) — [arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- [STUDY] Feeding outputs of specialist anomaly models (AnomalyCLIP, PatchCore) into a VLM mostly lowered discrimination/classification, though PatchCore highlighting improved localisation by +5.01; ground-truth text descriptions gave +24.89 (discrimination) and +28.01 (localisation), i.e. VLMs reason well when told accurately what is there — [arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)

**Trained detectors (YOLO family)**
- [STUDY] Nano-size YOLO variants reach 93–98% mAP@0.5 on PCB benchmarks with ~2.4M parameters (see section 1) — [MDPI Electronics](https://mdpi.com/2079-9292/14/17/3383)
- [OFFICIAL] Ultralytics supports a one-call export to LiteRT (successor of TFLite, which Ultralytics now labels deprecated) with FP32, INT8 and INT16-activation quantisation; Ultralytics' own figure for YOLO26n is ~8.4–8.6 ms GPU inference (device not named) — [Ultralytics LiteRT docs](https://docs.ultralytics.com/integrations/tflite)
- [OFFICIAL] An official Ultralytics Flutter plugin runs these exports on Android with live camera inference and GPU acceleration — [ultralytics_yolo on pub.dev](https://pub.dev/documentation/ultralytics_yolo/latest)
- [OFFICIAL] Ultralytics YOLO is AGPL-3.0; a closed-source commercial product or service requires a paid Enterprise License (price on request) — [Ultralytics license page](https://www.ultralytics.com/license)

**Anomaly detection (train on "good" images only)**
- [STUDY] PatchCore reaches 99.1% image-level AUROC on MVTec AD in the full-data setting — [arXiv 2106.08265](https://arxiv.org/abs/2106.08265v1)
- [STUDY] Few-shot PatchCore tuned on top of the Anomalib implementation: image AUROC about 85.3 (1 normal image), 88.9 (2), 91.9 (4) in the reported table (dataset attribution of that table not verified; paper claims state of the art on VisA) — [arXiv 2307.10792](https://arxiv.org/pdf/2307.10792)

**On-device generative models (Android)**
- [OFFICIAL] ML Kit GenAI Prompt API lets an Android app send an image plus a text prompt to on-device Gemini Nano; current dependency `com.google.mlkit:genai-prompt:1.0.0-beta2` (still beta) — [ML Kit Prompt API get-started](https://developers.google.com/ml-kit/genai/prompt/android/get-started)
- [OFFICIAL] Prompt API performs best on the Pixel 10 series (Gemini Nano nano-v3) — [Android Developers Blog](https://developer.android.com/blog/posts/ml-kit-s-prompt-api-unlock-custom-on-device-gemini-nano-experiences)
- [SECONDARY] Also available on Pixel 9 series, Samsung Galaxy Z Fold7, Xiaomi 15 and others with the weaker nano-v2 model; battery quotas are enforced and background execution is not supported — [InfoQ](https://www.infoq.com/news/2025/11/android-genai-prompt-api)

### Inferences
Comparison table (cost figures in the first row are my arithmetic from the official prices above, assuming one 1000×1000 photo = 1,296 input tokens plus ~500 output tokens of guidance, excluding the system prompt/SOP context):

| Option | Cost per photo | Needs training data | Offline | Speed | Main risk |
|---|---|---|---|---|---|
| Claude Haiku 5.5 | ≈ $0.0004 | No | No | Not measured in sources | Hallucinated defect or part number |
| Claude Sonnet 5.5 | ≈ $0.008 | No | No | Not measured | Same, lower likelihood expected but not measured for this domain |
| Claude Opus 5.5, full-resolution 4K photo | ≈ $0.03 (4,784 image tokens ≈ $0.019 + output) | No | No | Not measured | Cost if many photos per job |
| Gemini 3.1 Flash-Lite | Same order as Haiku-class (image token count per photo not retrieved) | No | No | Not measured | Free tier trains on customer photos |
| YOLO nano detector on phone (LiteRT) | ~0 marginal | Yes (hundreds–thousands of labelled images) | Yes | ~10 ms class on phone GPU per vendor | Blind to defect types not in training set; AGPL licence |
| PatchCore/Anomalib "golden sample" | ~0 marginal | Only good images (a handful to hundreds) | Typically PC/edge box rather than phone | Not measured | Needs fixed camera pose and lighting; false alarms on benign variation |
| Gemini Nano on device | 0 | No | Yes | Not measured | Only on a few flagship phones; weaker model; beta API |

- At roughly 20 photos per job and Sonnet-class pricing, API cost is on the order of $0.15–0.20 per job; with a Haiku-class model about one US cent. API spend is therefore negligible next to labour; the binding constraints are accuracy and connectivity, not price.
- The MMAD ablation implies a sound architecture: let a deterministic source (detector output, technician-entered measurements, SOP text) supply the facts and let the VLM explain and sequence the steps, rather than asking the VLM to find defects unaided.
- Sending the full-resolution crop of an IC marking (rather than a whole-board photo) matters: Anthropic states errors rise for very small image regions, and whole-board photos are downsized to at most 2,576 px on the long edge.
- For a workshop with mid-range Android phones, on-device Gemini Nano is not a dependable base; a small LiteRT detector is the realistic offline component.

### Gaps
- OpenAI GPT vision pricing and limits were not retrieved in this session.
- RT-DETR, MediaPipe Object Detector/Model Maker and ONNX Runtime Mobile were not researched to sourced detail; no measured Android latency on mid-range phones was found (only a vendor figure on an unnamed device).
- No measured end-to-end latency for cloud VLM photo analysis over Vietnamese mobile networks.
- No published hallucination rate for VLMs on electronics part-number reading; Vietnamese-language output quality of the named models was not benchmarked in any source found (all current frontier models support Vietnamese, but I have no measured figure).
- Ultralytics Enterprise License price is not public.

## 3. Datasets and tooling

### Takeaway
Public PCB datasets are useful for pre-training and for learning the pipeline but do not contain repair-type damage, and no public dataset of used-battery or spot-weld defects was found, so the workshop must build its own image set from daily jobs. Ultralytics' rule of thumb is ~1,500 images and ~10,000 labelled instances per class for best results, and free self-hosted labelling tools exist.

### Cited Findings
- DeepPCB: 1,500 image pairs (defect-free template + aligned tested image) with bounding boxes for six bare-board defect types (open, short, mousebite, spur, pin hole, spurious copper) — [Labelbox DeepPCB page](https://labelbox.com/datasets/deeppcb-printed-circuit-board-pcb-defect-dataset)
- HRIPCB (the PKU-Market-PCB family): synthesised dataset of 1,386 images with 6 defect kinds per the original 2019 paper; a YOLO-format release in circulation has 693 images — [HRIPCB paper record](https://www.bohrium.com/paper-details/hripcb-a-challenging-dataset-for-pcb-defects-detection-and-classification/812635263699255300-32229); [arXiv 2605.24726](https://arxiv.org/pdf/2605.24726)
- FICS-PCB: 8,685 images of 31 PCB samples with 75,965 annotated **components** (useful for component detection/classification rather than defects) — [Lu et al., IACR ePrint 2020/366](https://eprint.iacr.org/2020/366)
- A University of Florida group publishes a "Text Recognition for PCBs" dataset for component-marking recognition — [physicaldb.ece.ufl.edu](https://physicaldb.ece.ufl.edu/?p=425)
- Battery shell researchers report no publicly available battery-shell defect dataset and built their own — [YOLO-MDD paper](https://www.bohrium.com/en/paper-details/minimal-defect-detection-on-end-face-of-lithium-battery-shells/1069840321614970969-3177)
- [OFFICIAL] Ultralytics guidance: ≥1,500 images per class and ≥10,000 labelled instances per class recommended; add 0–10% background images (no labels) to cut false positives; images must be representative of the deployment environment — [Ultralytics tips for best training results](https://docs.ultralytics.com/yolov5/tutorials/tips_for_best_training_results)
- Community experience on the Ultralytics forum: thousands of images per class are common for good results, and class imbalance biases the model to the majority class — [Ultralytics community thread](https://community.ultralytics.com/t/yolo11-training-with-custom-dataset/697)
- [STUDY] Anomaly detection needs far fewer images and only good ones: PatchCore few-shot AUROC ~85–92 with 1–4 normal images versus 99.1% with full data on MVTec — [arXiv 2307.10792](https://arxiv.org/pdf/2307.10792); [arXiv 2106.08265](https://arxiv.org/abs/2106.08265v1)
- CVAT: free self-hosted open-source edition under MIT licence; hosted/team features are paid — [CVAT blog](https://www.cvat.ai/blog/cvat-or-label-studio-which-one-to-choose)
- Label Studio: open-source self-hosted Community Edition; cloud hosting from $99/month — [Averroes comparison](https://averroes.ai/blog/cvat-vs-label-studio-vs-visionrepo) [SECONDARY]
- Roboflow: third-party trackers disagree on the current free tier — one reports an October 2026 change to a free tier of 10 credits plus Core at $39/month, another reports 15 credits/month; older descriptions say the free Public plan publishes datasets and models openly. Roboflow's own blog says Public Plan workspaces move to a Core Plan free tier — [Roboflow blog](https://roboflow.com/blog/making-it-easier-cheaper-to-deploy-with-roboflow); [usagepricing.com tracker](https://www.usagepricing.com/blueprint/activity/roboflow-2026-10-04-core-price-cut-free-credits) [SECONDARY, conflicting]

### Inferences
- The 1,500-per-class figure is a target for best results, not a minimum; published battery/PCB papers and transfer learning from pretrained weights suggest a usable first detector for a handful of visually obvious classes (e.g. dented can, rust, torn wrap, burnt component) from a few hundred labelled images per class, but I found no source that measures this threshold for these classes — treat it as a pilot assumption to be validated.
- Practical data-collection practice that follows from the sources ("representative of deployed environment", reflective cans, fixed-pose requirement of anomaly detection): fix a photo station (same phone mount, distance, diffuse light, plain background); make the job-ticket app require standard shots at each stage; have the senior technician tag each photo with the true outcome (defect type, pass/fail after electrical test). In 3–6 months of normal work this yields a labelled dataset as a by-product of record-keeping.
- At 5–10 packs/day with 13–100+ cells per pack, cell images accumulate fast, but defect classes will be heavily imbalanced (most cells look fine), which favours anomaly detection or deliberate collection of scrap cells.
- Customer photos should stay off any public/free plan that publishes datasets (Roboflow public, Gemini free tier); self-hosted CVAT or Label Studio avoids this.

### Gaps
- No public dataset of used lithium cells (swollen pouch, leaking 18650), nickel spot welds, or damaged BMS boards was found.
- No source quantifying the minimum images needed for acceptable recall on these specific defect classes.
- Current official Roboflow pricing was not confirmed from roboflow.com.
- The figures "9,912 images / 77,347 components" sometimes quoted for FICS-PCB were not confirmed; the paper found states 8,685 / 75,965.

## 4. Guidance delivery: RAG over SOPs, AR/phone guided work instructions, enforced checklists, photo evidence

### Takeaway
Retrieval of domain knowledge measurably improves VLM answers on industrial images (about +6 points overall, +17–20 on defect classification), which supports grounding guidance in the shop's own SOPs and datasheets. Evidence that guided digital/AR work instructions cut time and errors exists, but the large numbers come almost entirely from vendors and big aerospace firms, and no AI-guided battery or electronics repair deployment with measured results was found.

### Cited Findings
- [STUDY] RAG with domain knowledge raised VLM accuracy on industrial inspection questions by ~5.4–6.8 points on average and ~17–20 points on defect classification — [MMAD, arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- [STUDY] A comparison of paper vs head-mounted AR assembly instructions found significant reductions in error rate and task completion time with AR — [NSF-hosted paper](https://par.nsf.gov//servlets/purl/10541419)
- [STUDY, secondary citation inside a preprint] 20–30% faster task completion and 15–25% fewer errors with AR guidance for maintenance personnel; the preprint's own contribution is hands-free speech interaction — [arXiv 2511.13918](https://arxiv.org/pdf/2511.13918v1)
- [STUDY] A PHM Society paper proposes an AI+AR framework for guided visual diagnosis and states that, to the authors' knowledge, no prior work existed on visual assistance systems for diagnosis — a framework, not a field result — [PHM Society 2024](https://papers.phmsociety.org/index.php/phmconf/article/download/3909/phmc_24_3909)
- [CONSULTANCY] BCG: technicians using AR with no prior training completed work in only slightly more time than a trained technician — [BCG 2018](https://bcg.com/publications/2018/rolling-out-augmented-reality-field)
- [VENDOR/INDUSTRY CLAIM] Boeing wiring with AR guidance: ~25% less production time and error rate near zero — [Reality Atlas blog](https://www.reality-atlas.com/blog/ar-work-instructions-vs-paper-manuals)
- [VENDOR CLAIM] Aerospace MRO case study: inspection time from 4 h to 2.5 h and training-related damage incidents down 90% — [AR Genie case study](https://www.casestudies.com/company/ar-genie/case-study/enhancing-landing-gear-inspection-maintenance-technician-training-with-ar-genie-work-assist)
- [VENDOR CLAIM] Projected-AR work instructions for electronics repair at a tech-insurance company reduced ramp-up time to proficiency (no number given) — [LightGuide via Automation Alley](https://Automationalley.com/case-studies/tech-insurance-company-transforms-electronics-repair-processes-with-ar)
- [VENDOR CLAIM] "Cut training time for complex tasks by 60%" with AI vision operator assistance, unsourced — [OxMaint](https://oxmaint.com/industries/steel-plant/ai-vision-for-operator-assistance-in-manufacturing)
- Reference architecture exists for a multimodal agentic "automotive technician" assistant on AWS (photo/audio in, guided diagnosis out) — [AWS Solutions guidance](https://aws.amazon.com/solutions/guidance/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws)
- Trade press reports independent auto repair shops using AI diagnostic assistants, framed around freeing time for customers — [MOTOR, Oct 2025](https://www.motor.com/2025/10/shops-using-ai-to-serve-customers-better)

### Inferences
System architecture for the diagram (my synthesis; each layer maps to sourced components above):

1. **Capture layer** — Android phone camera (primary); USB-C thermal camera dongle; USB/digital microscope for BMS close-ups; optional fixed bench camera over the weld and charge stations. Every image is tagged with job-ticket ID, workflow stage and shot type.
2. **Pre-check on device** — blur/exposure check and guided framing; optional small LiteRT detector (cell defects, PPE) running offline.
3. **Model layer** — cloud VLM API for label/marking reading, description and step guidance; trained detector / anomaly model for repetitive pass/fail screens; plain thresholds for thermal data.
4. **Knowledge layer** — the shop's SOPs, safety rules, pack-type notes, BMS and cell datasheets, past job tickets; retrieved by pack type and stage and injected into the prompt so answers cite a specific SOP step.
5. **Guidance layer** — Vietnamese step-by-step cards with reference photos; checklist with hard gates (cannot proceed without required photo or measurement); escalation button to the senior technician; confidence shown as "needs senior review" rather than a number.
6. **Records layer** — job ticket with photo evidence per stage, measurements, AI output, who approved, final outcome; this store doubles as the training dataset and the audit trail for warranty disputes.

- The strongest lever for a small shop is probably not AR or model accuracy but the **enforced checklist with photo evidence**: it standardises work, creates accountability and generates training data, and it works even when the AI is wrong.
- Smartphone delivery is the realistic channel; the AR studies cited used head-mounted or projected systems in large firms, and no cost-effective smart-glasses evidence for a small workshop was found.
- Vietnamese output: write SOPs in Vietnamese and instruct the model to answer only from retrieved SOP text, keeping part numbers and units verbatim; this limits translation drift and hallucination. (Design recommendation, not a measured result.)

### Gaps
- No product or study found for AI-assisted **battery pack repair** or e-bike/e-scooter battery service specifically.
- Named platforms for connected-worker instructions (e.g. Tulip, Dozuki, Augmentir, Aquant, Bosch) returned no retrievable case studies with measured results in this session; their pricing was not researched.
- Smart-glasses options and prices were not researched.
- No independent controlled trial of *AI-generated* (as opposed to pre-authored AR) work instructions for repair technicians was found.

## 5. Hardware: cameras, microscopes, thermal cameras, edge devices

### Takeaway
A phone plus a ~$250 USB-C thermal dongle (256×192 sensor) covers most capture needs; a dedicated edge box (Jetson Orin Nano Super at $249 launch price, or Raspberry Pi 5 + AI HAT+ at $70–110 launch price for the HAT) is only justified for an always-on fixed camera such as charge-bench safety monitoring.

### Cited Findings
- InfiRay P2 Pro and Topdon TC001 both use a 256×192 thermal sensor; at the time of AnandTech's 2023 review they were priced roughly $250–300 and $230–280 respectively; FLIR One Pro has a lower 160×120 sensor and was priced higher — [AnandTech capsule review (mirror)](https://at-web1.www.anandtech.com/show/21200/infiray-p2-pro-and-topdon-tc001-thermal-cameras-capsule-review)
- A 2026 buyer's guide lists the InfiRay P2 Pro at about $249 and positions it for close-up electronics and small heat sources (it has a macro lens option), with the TC001 better for general scanning; the TC001 is bulkier but ships with an extension cable — [logix4u PCB-debugging thermal camera guide](https://www.logix4u.net/best-thermal-imaging-cameras-for-pcb-debugging/) [SECONDARY, affiliate-style]; macro lens noted in [Notebookcheck P2 review](https://www.notebookcheck.net/InfiRay-P2-smartphone-infrared-camera-review-Tiny-even-with-a-macro-lens.747278.0.html)
- Reviewers differ on image quality: one found FLIR One Pro images often look better thanks to processing despite lower resolution; another stresses P2 Pro's higher resolution and frame rate — [HotHardware review](https://hothardware.com/reviews/infiniray-p2-pro-thermal-imaging-camera-for-smartphones-review); [AnandTech](https://at-web1.www.anandtech.com/show/21200/infiray-p2-pro-and-topdon-tc001-thermal-cameras-capsule-review)
- NVIDIA Jetson Orin Nano Super Developer Kit launched at $249 (Dec 2024) — [CNX Software](https://www.cnx-software.com/2024/12/18/249-nvidia-jetson-orin-nano-super-developer-kit-targets-generative-ai-applications-at-the-edge/?amp=1)
- Raspberry Pi AI HAT+ launched at $70 (13 TOPS) and $110 (26 TOPS) and requires a Raspberry Pi 5 host — [Tom's Hardware](https://tomshardware.com/raspberry-pi/raspberry-pi-release-higher-performance-ai-hat-13-and-26-tops-variants); [Raspberry Pi product page](https://www.raspberrypi.com/products/ai-hat/)
- Street prices for the 26 TOPS HAT have since been higher at some retailers: $132 at SparkFun, ~$186–190 in other listings — [SparkFun](https://www.sparkfun.com/raspberry-pi-ai-hat-26-tops.html)
- Reflective 18650 cans needed purpose-built illumination (line-focused laser) for reliable defect imaging in one study — [Informatica](https://www.informatica.si/index.php/informatica/article/view/7556/6314)

### Inferences
Indicative hardware budget (prices are the sourced USD figures; items marked * are my estimates with no source in this session and must be checked locally):

| Item | Purpose | Indicative price |
|---|---|---|
| Existing Android phones | Capture, guidance, on-device detector | $0 (already owned) |
| Phone stand + ring light/light box* | Repeatable, glare-free cell/weld/PCB photos | low tens of USD* |
| USB digital microscope* | MOSFET/IC markings, solder joints | tens of USD* |
| InfiRay P2 Pro or Topdon TC001 (256×192) | Hot-spot check under load, BMS MOSFET heating | ~$230–300 |
| Raspberry Pi 5 + AI HAT+ or Jetson Orin Nano Super | Always-on fixed camera for charge/test bench | HAT $70–190 plus Pi 5* ; Jetson $249 at launch |

- A phone-first setup with one thermal dongle and a light box is plausibly under $400 total; an always-on monitoring station roughly doubles that.
- The phone thermal dongles are designed for hand-held spot checks; using one as a 24/7 fixed monitor is outside the use shown in the reviews, so the always-on safety camera should be treated as a later-phase item.
- 256×192 resolution with a macro lens is adequate for locating a hot MOSFET or one hot cell in a group; it does not replace contact temperature probes for absolute accuracy (emissivity of shiny nickel and steel is low — general thermography knowledge, not sourced here).

### Gaps
- No current (2026) verified price for FLIR One models; no Vietnamese retail prices for any item.
- Digital microscope models and prices were not researched to a citable source.
- Fixed industrial/bench cameras and lighting kits were not priced.
- No source on thermal-dongle SDK availability for third-party Android apps (needed to read radiometric data inside the workshop app).

## 6. Human-in-the-loop, safety limits, validation, liability and privacy

### Takeaway
The measured gap between VLMs and human experts on defect judgement (68.6% vs 95.2% on "is it defective?") and the low numeric-reading accuracy mean AI output must be advisory: a qualified technician must own every safety-relevant decision. Validation should be organised around false negatives on safety defects, and customer photos fall under Vietnam's personal-data law when they contain personal information and are sent to overseas APIs.

### Cited Findings
- [STUDY] On anomaly discrimination, human experts scored 95.24% and ordinary humans 86.90%, versus 68.63% for the best VLMs; on defect localisation humans 92.31% vs 55.62–58.56% — [MMAD, arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- [STUDY] MMAD notes false positives and false negatives in anomaly discrimination and that a domain-specific model (AnomalyGPT) performed worst overall because it could only handle the task it was trained on — [arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)
- [OFFICIAL] Anthropic warns Claude may hallucinate on low-quality, rotated or very small images and that localisation outputs must be verified before relying on them — [Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- [STUDY] Frontier VLMs are "not yet reliable enough for safety-critical monitoring" for gauge reading — [arXiv 2604.22829](https://arxiv.org/pdf/2604.22829)
- [STUDY] The thermal-runaway vision paper reported perfect ROC-AUC on simulated late-stage events and explicitly did not analyse false-positive/false-negative costs or early-stage detection — [arXiv 2504.08632v2](https://arxiv.org/html/2504.08632v2)
- [STUDY] Deployed safety-vision models often show low detection rates with frequent false positives and negatives in real plants — [AIMS Electronics and Electrical Engineering](https://aimspress.com/aimspress-data/electreng/2025/3/PDF/electreng-09-03-013.pdf)
- Vietnam's Law on Personal Data Protection No. 91/2025/QH15 was passed 26 June 2025 and took effect 1 January 2026 — [Global Vietnam Lawyers legal alert](https://gvlawyers.com.vn/wp-content/uploads/2025/09/EN_Legal-alert-_Law-on-PDP-2025.pdf); [LuatVietnam](https://english.luatvietnam.vn/dan-su/law-on-personal-data-protection-law-no-91-2025-qh15-405135-d1.html)
- [SECONDARY] Cross-border transfer of personal data requires a Cross-Border Transfer Impact Assessment filed with the Ministry of Public Security within 60 days of the transfer; it is a filing, not an approval — [Baker McKenzie Connect on Tech](https://connectontech.bakermckenzie.com/?p=5530)
- [SECONDARY] Penalties for cross-border violations are reported as up to 5% of previous-year revenue; one summary adds "or VND 3 billion, whichever is higher" (wording not confirmed across sources) — [Allen & Gledhill](https://www.allenandgledhill.com/vn/publication/articles/31075/upcoming-changes-to-vietnam-s-personal-data-protection-regime)
- [OFFICIAL] Gemini free-tier content is used to improve Google products; paid tier is not — [Gemini API pricing](https://aistudio.google.com/docs/pricing)

### Inferences
- **Decisions that should stay with a qualified technician** (my recommendation, derived from the accuracy gaps above): declaring a pack safe to return; accepting or rejecting cells with any sign of swelling, leakage, heat damage or deep discharge; judging weld strength (pull test); any BMS bypass or protection-parameter change; charging supervision; disposal/quarantine decisions. AI may *escalate* (flag for review) on its own but should never *clear* a safety item on its own.
- **Asymmetric thresholds**: for safety classes (swollen cell, leakage, burnt board, hot spot), tune for recall and accept false alarms; a false alarm costs a minute of senior time, a miss can cost a fire. For convenience tasks (label reading), optimise for precision and require confirmation of extracted values.
- **Validation method**: before trusting any use case, run it in "shadow mode" on a few hundred real jobs with the senior technician's verdict as ground truth; report a confusion matrix per defect class, with recall on safety classes as the headline metric and a pre-agreed minimum; re-test after every model or prompt change, because cloud model versions change. For readings, compare AI-extracted values against typed values and measure exact-match rate.
- **Handling uncertainty**: force structured output with an explicit "cannot determine / retake photo" option, require the model to cite the SOP step it relied on, cross-check extracted part numbers against a local parts table, and reject numeric readings outside the physically possible range for the pack.
- **Liability**: the workshop, not the model vendor, carries responsibility to the customer; the per-job photo and approval log is the main protective measure. (General reasoning; no legal source specific to AI-assisted repair liability in Vietnam was found.)
- **Privacy practice**: photos of packs and boards are mostly not personal data, but job tickets (name, phone, address, vehicle plate, anything visible in the background) are. Keep customer identifiers out of images and prompts sent to overseas APIs, use paid API tiers that do not train on data, obtain consent in the intake form, and store originals locally.

### Gaps
- The official Vietnamese text of Law 91/2025/QH15 and its implementing decree were not read directly; consent conditions and whether a micro-business exemption applies were not confirmed. Legal review is needed.
- No source found on product-liability or insurance treatment of AI-assisted repair decisions in Vietnam.
- No applicable Vietnamese or international standard for AI use in battery repair was found; battery-repair safety standards themselves were outside this note's scope.
- Data-retention terms of each API provider were not checked in this session.

## 7. Staffing impact: does AI guidance shorten onboarding or let one senior supervise more juniors?

### Takeaway
The best rigorous evidence is from customer support, not repair: generative-AI assistance raised productivity 14% on average and 34% for novices, with little gain for experts. For hands-on technical work the supportive numbers are AR-instruction studies and vendor case studies; no measured result exists for AI-guided battery or electronics repair, so staffing savings should be presented as a hypothesis to test in a pilot.

### Cited Findings
- [STUDY] Brynjolfsson, Li and Raymond: access to a generative-AI assistant raised issues resolved per hour by 14% on average and by 34% for novice and low-skilled workers, with minimal impact on experienced workers; data from about 5,000 support agents; mechanism suggested is dissemination of the best workers' practices, moving new workers down the experience curve — [NBER Working Paper 31161](https://www.nber.org/papers/w31161) (published in QJE 140(2), per [RePEc](https://econpapers.repec.org/paper/eclstabus/4141.htm))
- [STUDY] The same paper reports AI assistance may slightly lower the quality of the most skilled agents' work — [NBER w31161 PDF](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf)
- [STUDY] AR vs paper instructions for assembly: significant reductions in errors and completion time — [NSF-hosted paper](https://par.nsf.gov//servlets/purl/10541419)
- [CONSULTANCY] BCG: untrained technicians with AR finished in only slightly more time than trained technicians — [BCG](https://bcg.com/publications/2018/rolling-out-augmented-reality-field)
- [VENDOR CLAIM] Training time reduced "from 3 weeks to 3 days" in an AR work-instruction deployment; Lockheed Martin/Orion technician training time reportedly down 85% (not verified) — [Frontline.io blog](https://www.frontline.io/post/ai-xr-convergence-industrial-training); [IoT For All](https://www.iotforall.com/ar-vr-iot-workplace-learning)
- [VENDOR CLAIM] AR remote-assist in aircraft engine repair: 3.5 hours saved per repair and 100% first-time quality — [AR Genie case study](https://www.casestudies.com/company/ar-genie/case-study/revolutionizing-aircraft-engine-fan-blade-repair-with-ar-genie-remote-assist)
- [VENDOR CLAIM] Error reductions of 50–90% and "96% error reduction" for an AR product in aircraft maintenance, unsourced — [Reality Atlas blog](https://www.reality-atlas.com/blog/ar-work-instructions-vs-paper-manuals)
- [STUDY] Human experts still outperform the best VLMs on industrial defect questions by ~12 points on average (86.65% vs 74.92%), while ordinary humans (78.69%) are only slightly above the best VLM — [MMAD, arXiv 2410.09453v3](https://arxiv.org/html/2410.09453v3)

### Inferences
- The consistent pattern (largest gains for novices, little for experts) fits the workshop's goal: AI guidance is most likely to help juniors do standardised steps (intake, disassembly photos, cell sorting, checklist QC) correctly, while the senior concentrates on diagnosis sign-off, welding supervision and final release.
- A plausible staffing model to test: one senior reviewing flagged items and signing off jobs for several juniors via the photo log, instead of standing beside each one. How many juniors per senior this supports is unmeasured; the pilot should track rework rate, senior interruptions per job, time per job and time until a new hire completes standard jobs unaided.
- The MMAD human baselines suggest a VLM is roughly at "ordinary person" level on defect questions: useful as a second pair of eyes for a junior, not a replacement for the senior.
- Phased roadmap implied by the evidence and costs (my synthesis):

| Phase | Duration (assumed) | Scope | Cost drivers (sourced where available) | Accuracy expectation | Main risks |
|---|---|---|---|---|---|
| 0. Standardise | 2–4 weeks | Write Vietnamese SOPs; define required photos per stage; photo station with lighting | Staff time; light box/stand (unsourced, low) | n/a | SOPs not followed |
| 1. Digital ticket + cloud VLM assistant | 1–3 months | Job-ticket app with enforced checklist and photo log; VLM for label/marking reading, SOP Q&A, photo completeness; thermal dongle spot checks | App development; API at well under $0.01–0.03 per photo; thermal camera ~$250 | Naming/reading tasks good but must be confirmed; defect yes/no around 60–75% unaided per MMAD, so advisory only | Hallucinated part numbers or readings; connectivity; privacy of uploads |
| 2. Own-data detectors | Months 4–9 | Train YOLO-class detector for a few cell/BMS defect classes and/or golden-sample anomaly check, exported to LiteRT for offline phone use | Labelling time (free self-hosted CVAT/Label Studio); training compute; Ultralytics licence question | Factory studies report 80–98% mAP; expect lower on used parts until validated in shadow mode | Too few defect examples; class imbalance; lighting drift |
| 3. Fixed monitoring and scaling | Month 9+ | Always-on thermal/visual camera on charge and test bench with alarms; dashboards for senior supervising several juniors | Edge box $249 (Jetson launch price) or Pi 5 + HAT ($70–190); fixed camera (unsourced) | Research-stage; simple thresholds first | False alarms causing alarm fatigue; over-reliance on camera instead of fire precautions |

### Gaps
- No controlled study of AI-guided work instructions for repair technicians (electronics, battery, automotive) with measured onboarding time was found; all hands-on figures are AR-instruction studies or vendor claims from large enterprises.
- No evidence on senior-to-junior supervision ratios enabled by AI guidance.
- No data on Vietnamese technician labour costs or typical onboarding duration for battery repair was collected here, so labour savings cannot be quantified in money terms.
- App development cost for the Android job-ticket/assistant app was not estimated from any source.
