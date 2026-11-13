# Safety for a lithium battery pack repair workshop: hazards, controls, emergency response, storage, transport, waste, standards and Vietnamese regulations (status as of Nov 2026)

Reader notes (apply to all sections):
- Scale assumed: small independent workshop, packs about 12–72 V, up to a few kWh each.
- Every item under "Cited Findings" has a source. Items I know from background knowledge but could not source in this session are placed under "Gaps" and marked **[unverified background]**. Do not present those as sourced facts.
- Many search hits were secondary (law-firm summaries, news, vendor pages). Where the primary text was not read, this is flagged.
- "Formal" = law, regulation or published standard. "Best practice" = guidance from fire services, insurers, manufacturers, trade bodies.

---

## 1. Hazards in battery repair work

### Takeaway
The dominant hazard is thermal runaway (fire, explosion, toxic and flammable gas), which no portable agent reliably stops once started; secondary hazards are short-circuit arcs and burns, DC shock above about 60 V DC, electrolyte and HF exposure, and flammable solvents. A 72 V nominal pack sits above the 60 V DC "high voltage" threshold used in UN R100, so the top of the workshop's range needs shock controls, not only short-circuit controls.

### Cited Findings

**Thermal runaway and gas (formal / peer-reviewed)**
- OSHA lists the workplace hazards of Li-ion as thermal runaway causing fire and/or explosion, electrolyte exposure, and flammable and toxic gases including hydrogen fluoride (HF) as a decomposition product — [OSHA Lithium-ion Battery Safety: Control](https://www.osha.gov/lithium-ion-battery-safety/control)
- HF release in fire tests on seven types of commercial Li-ion cells was 20–200 mg per Wh of nominal energy capacity (figure quoted from Larsson's doctoral thesis and summaries of the 2017 Scientific Reports paper; I did not read the paper's own results table) — [Larsson thesis, Chalmers](https://research.chalmers.se/en/publication/251352); [Larsson et al. 2017, Sci. Rep., PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5577247/)
- An earlier conference paper by the same group measured 12–81 mg/Wh HF by online FTIR under propane-burner exposure — [Chalmers 2016](https://research.chalmers.se/en/publication/243272)
- Phosphoryl fluoride (POF3) was measured at 15–22 mg/Wh in some tests; the authors note it may be more toxic than HF — [Larsson et al. 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5577247/)
- Water mist temporarily increased the HF production rate, but total HF emitted was similar with or without water mist — [Larsson thesis](https://research.chalmers.se/en/publication/251352)
- UL FSRI EV tests found metals and particulate fluoride in smoke, suppression runoff water and on firefighter gear, i.e. contamination persists after the fire — [UL Research Institutes](https://ul.org/news/new-research-guides-firefighters-through-ev-battery-fire-response/)
- London Fire Brigade investigators describe failing e-bike batteries and chargers as igniting "with ferocity", with fires developing rapidly — [London Fire Brigade](https://www.london-fire.gov.uk/safety/lithium-batteries/)

**Triggers (mixed quality)**
- Charging below 0 °C: Battery University BU-410 gives a Li-ion charge window of 0 °C to 45 °C, says no charging is permitted below freezing because it can cause lithium plating, and says charge current should be reduced below 5 °C — [Battery University BU-410](https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures)
- Over-discharge: a trade article defines over-discharge as a cell drained below 2 V and links it to anode copper dissolution, higher self-discharge and internal short-circuit risk from dissolved copper — [EE Power](https://eepower.com/technical-articles/examining-failures-in-lithium-ion-batteries/). A research paper puts the actual onset of copper dissolution at cell voltages between −1.3 V and −1.5 V (i.e. reversal), so 2 V is a conservative rule of thumb — [UL Research Institutes library](https://ul.org/library/elucidating-copper-dissolution-phenomenon-li-ion-cells-under-overdischarge-extremes)
- Vietnamese fire police (C07, Bộ Công an): investigations of e-vehicle fires found the main cause was charging of the battery; poorly insulated solder joints and connectors, wet sockets and non-standard wiring were also named — [SGGP](https://www.sggp.org.vn/bo-cong-an-khuyen-cao-sac-xe-dien-an-toan-han-che-chay-no-post698917.html)
- Vietnamese fire-service warnings: charging too long, at high ambient temperature, or immediately while the pack is still hot can cause battery explosion; self-modified ("độ") packs with raised capacity and oversized chargers break the original safety design — [VietnamPlus](https://www.vietnamplus.vn/chay-no-xe-dien-canh-bao-tu-viec-do-pin-sac-sai-cach-post1138397.vnp)

**Electrical**
- UN Regulation No. 100 classes a circuit as "high voltage" when working voltage is >60 V and ≤1,500 V DC, or >30 V and ≤1,000 V AC (rms) (taken from the EU Official Journal copy; only the UN original is authoritative) — [EUR-Lex, UN R100](https://eur-lex.europa.eu/eli/reg/2015/100/oj/eng/pdf)
- HSE (UK) INDG139: most batteries are low voltage with little shock risk, but some large batteries exceed 120 V DC; live conductors must then be insulated or protected and warning labels displayed — [HSE INDG139](https://www.hse.gov.uk/PUBNS/indg139.pdf)
- HSE-derived guidance: short circuits cause extensive arcing, burning and melting of metal objects; shocks can come from both the battery and the charger. INDG139 states at least 25 people a year are seriously injured using batteries at work — [HSE INDG139](https://www.hse.gov.uk/PUBNS/indg139.pdf)

**Solvents**
- Isopropyl alcohol: flash point 53 °F (about 12 °C), LEL 2.0 %, UEL 12.7 % (at 200 °F), Class IB flammable liquid, IDLH 2,000 ppm (10 % LEL), NIOSH REL 400 ppm TWA / 500 ppm STEL — [NIOSH Pocket Guide (archived)](https://webarchive.library.unt.edu/eot2008/20081108192822/http://www.cdc.gov/niosh/npg/npgd0359.html); [OSHA chemical data](https://osha.gov/chemicaldata/475)

### Inferences
- Rough HF scale for the writer: applying 20–200 mg/Wh to a 1 kWh pack gives 20–200 g of HF if the whole pack burns. This is my arithmetic from the cited range, not a measured value, and real release depends on chemistry, state of charge and how much of the pack is involved. It is enough to justify "evacuate and ventilate, do not stand in the smoke" for any indoor pack fire.
- Packs at 60 V nominal and above (e.g. 16S–20S Li-ion, 72 V) exceed the R100 60 V DC threshold when charged; 48 V packs (13S, about 54.6 V full) stay under it. R100 is a vehicle type-approval rule, not a workshop rule, so this is a design benchmark rather than a legal limit on the workshop.
- IPA's flash point (12 °C) is below normal Vietnamese ambient temperature, so vapour is ignitable at room temperature next to spot-welders and soldering irons.

### Gaps
- **[unverified background]** Acetone flash point is commonly given as about −20 °C; the search did not return a source. Check an SDS or the NIOSH entry before printing.
- **[unverified background]** Commonly quoted figures not sourced here: short-circuit currents of e-bike packs (hundreds to thousands of amps), thermal-runaway onset temperatures by chemistry, HF exposure limits (IDLH 30 ppm), DC let-go/fibrillation thresholds from IEC 60479. None should be stated as fact without a source.
- No sourced data found on solder fume (rosin flux) limits or spot-welding spark hazards specific to battery work.
- No source found that states a hard "never recharge below X V" rule; sources describe the damage mechanism only.

---

## 2. Engineering and procedural controls

### Takeaway
Formal sources give a hierarchy-of-controls framework and a few hard items (ventilation/LEV, eyewash, insulated tools to IEC 60900, no metal jewellery, insulate live conductors, follow manufacturer charging instructions); nearly all the numeric workshop practice (charge supervised, in a fire-resistant enclosure, never charge or repair suspect packs) comes from trade and manufacturer guidance rather than standards.

### Cited Findings

**Formal / regulator guidance**
- OSHA says controls should follow the hierarchy of controls. Engineering: ventilation including local exhaust ventilation (LEV) and enclosures, isolation of hazardous materials, continuous flammable/toxic gas monitoring in large storage areas, safety showers and eyewash stations where electrolyte exposure may occur — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)
- OSHA administrative controls: follow manufacturer instructions for storage, use, charging and maintenance; limit stored quantities per NFPA 800 and NFPA 855; do not mix battery types in recycling; train workers to identify defective, damaged or failing batteries in a language they understand; ship per DOT/IATA rules; dispose only via designated recyclers — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)
- OSHA names no specific PPE; it requires a hazard assessment and "appropriate PPE" — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)
- OSHA SHIB (2019): verify NRTL certification of batteries, chargers and associated equipment; remove defective devices from the workplace; act immediately if a battery feels hot, leaks, hisses, bulges, cracks or vents; include lithium incident procedures in the emergency action plan — [OSHA SHIB](https://osha.gov/sites/default/files/publications/shib011819.pdf)
- IEC 60900:2018 covers insulated, insulating and hybrid hand tools for work on or near live parts up to 1,000 V AC and 1,500 V DC; tools carry the double-triangle "1000 V" mark, maker, reference and year — [IEC 60900:2018 summary](https://reference.globalspec.com/ref/4638786/iec-60900-2018); [Boddingtons](https://www.boddingtons-electrical.com/understanding-insulating-tools-to-iec-en-60900-standard.html)
- IEC 60903 / EN 60903 is the standard for insulating gloves for live working (class ratings not retrieved) — [search summary of standards listings](https://document-center.com/standards/ics/13.260)
- HSE INDG139: do not wear a watch, ring, chain, bracelet or other metal item when working with or near batteries; insulate or protect live conductors; display warning labels — [HSE INDG139](https://www.hse.gov.uk/PUBNS/indg139.pdf)

**Best practice (trade, manufacturer, fire service)**
- Specialized retailer guide: never attempt to charge or repair an "at-risk" pack (damage, tampering, abnormal behaviour); always store suspected faulty packs outdoors; never ship them by air — [Specialized Retailer Battery Handling](https://content.specialized.com/wp-content/uploads/2021/11/Retailer-Battery-Handling-Recommended-Practices_English.pdf)
- Bicycle Retailer shop protocol: charge and store in a fire-resistant cabinet, but do not keep damaged packs in that cabinet or anywhere else in the store — [Bicycle Retailer protocols v1.6](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Battery Network (Call2Recycle) retailer guide: well-ventilated storage area, state of charge no higher than 30 % where feasible, incident kit on site — [The Battery Network](https://batterynetwork.org/wp-content/uploads/E-Bike-Battery-Safety-A-Guide-for-Retailers-The-Battery-Network.pdf)
- Vietnamese press summary of QCVN 31:2026 guidance warns against unverified replacement batteries, mismatched specifications, unauthorised voltage increases, controller tampering and motor upgrades without technical assessment — [Báo Lào Cai](https://baolaocai.vn/xe-may-dien-co-quy-chuan-moi-tu-910-chu-xe-co-phai-thay-pin-post911077.html)
- German industry body ZIV has publicly warned against e-bike battery repair offers (headline only; content not read) — [Cycling Industry News](https://cyclingindustry.news/ziv-warns-against-electric-bike-battery-repair-offers)

### Inferences
- Draft hazard → control matrix (synthesised from sections 1–4; the "control" column mixes sourced and conventional practice, see Gaps):

| Hazard | Trigger in workshop | Engineering control | Procedural control | PPE |
|---|---|---|---|---|
| Thermal runaway | Short circuit, overcharge, crushed/punctured cell, charging below 0 °C or deeply discharged cells | Fire-resistant charging enclosure/cabinet; smoke/heat detection; current-limited charger; outdoor quarantine container | Supervised charging only, never overnight; never charge "at-risk" packs; charge only 0–45 °C; temperature check during charge | Eye/face protection; non-melting clothing |
| Short-circuit arc / burn | Dropped tool, exposed nickel strip, loose wire | Non-conductive bench top; insulated tools (IEC 60900); fused test leads | Remove jewellery (HSE); tape/cap exposed terminals; one conductor at a time | Safety glasses or face shield; insulating gloves |
| DC shock (>60 V DC) | 60–72 V packs, series strings on bench | Barriers/insulating covers; isolation of charger | Split pack into <60 V sections before work; one-hand rule; warning labels (HSE) | Insulating gloves to IEC 60903 |
| Toxic/flammable gas (HF, CO, solvents) | Venting cell, fire, solder flux | LEV / fume extraction; general ventilation; eyewash | Evacuate on venting; do not re-enter smoke | Respiratory protection only for trained persons |
| Electrolyte contact | Leaking or opened cell | Eyewash, spill kit, absorbent | Bag and quarantine leaking cells | Chemical-resistant gloves, goggles |
| Solvent fire | IPA/acetone near sparks | Closed containers, small quantities, ventilation | No solvents open during welding/soldering | — |

- Because OSHA names no PPE and the standards found define tools and gloves only by voltage class, the specific PPE list (glove material, face shield rating, FR clothing) will have to be stated as best practice.

### Gaps
- **[unverified background]** Common practices not sourced in this session: one-hand rule, fused test leads, current-limited bench supplies, taping terminals with Kapton/fish paper, non-conductive (wood/ESD mat) benches, ESD wrist straps with 1 MΩ resistor, nitrile gloves for electrolyte, IEC 60903 class 00 (500 V AC / 750 V DC) or class 0 (1,000 V AC / 1,500 V DC) gloves, arc-rated face shields. The glove class voltages in particular were not confirmed by the search.
- No numeric ventilation or fume-extraction rates (air changes per hour, capture velocity) were found for battery repair or soldering.
- No standard was found that specifies "supervised charging" or temperature-monitoring intervals; these are trade-guide recommendations.
- The full text of HSE INDG139 (insulated-tool wording) was not read; only excerpts.

---

## 3. Fire response, suppression agents and quarantine of damaged packs

### Takeaway
Evidence says water (in quantity, for cooling) is the baseline agent, special agents have not been shown to beat water in independent fire-service testing, nothing reliably stops runaway once it starts, and re-ignition can occur hours to days later; fire services tell untrained people not to fight these fires at all. Class D extinguishers are for lithium metal, not Li-ion, and there is still no dedicated Li-ion extinguisher class in NFPA 10.

### Cited Findings

**What works / does not (research and fire services)**
- UL FSRI (EV tests): water from a standard handline is the first-choice tactic; no tested technique halted thermal runaway once started; an added suppression agent was no more effective than water — [FSRI](https://fsri.org/research-update/researchers-release-evidence-based-ev-battery-fire-response-considerations); [UL Research Institutes](https://ul.org/news/new-research-guides-firefighters-through-ev-battery-fire-response/)
- FSRI: fire blankets should not be used indoors or in confined spaces because of deflagration risk (trapped flammable gas) — [FSRI](https://fsri.org/research-update/researchers-release-evidence-based-ev-battery-fire-response-considerations)
- FSRI: after apparent control, responders should stay on breathing apparatus and on alert — [Firehouse summary of FSRI study](https://www.firehouse.com/operations-training/news/55396753/new-fsri-study-details-what-firefighters-need-to-know-about-ev-fires)
- NFCC (UK): for an e-bike, e-scooter or Li-ion battery fire, "do not attempt to extinguish the fire. Get out, stay out, call 999" — [NFCC guidance](https://nfcc.org.uk/wp-content/uploads/2023/09/NFCC_Guidance_E-bikes_and_Scooters_.pdf)
- London Fire Brigade: never try to tackle a lithium battery fire; get away and call the fire service — [London Fire Brigade](https://www.london-fire.gov.uk/safety/lithium-batteries/)
- OSHA SHIB lists ABC dry chemical, Class D (for lithium metal), dirt or sand as media for small lithium device fires — [OSHA SHIB](https://osha.gov/sites/default/files/publications/shib011819.pdf)
- University EHS guidance: an ABC extinguisher or water may be used on Li-ion (not lithium-metal) batteries; small Li-ion cells contain little lithium and do not need Class D — [University of Virginia EHS](https://ehs.virginia.edu/Fire-Safety-Battery-Safety.html); [Oregon State EHS](https://ehs.oregonstate.edu/sites/ehs.oregonstate.edu/files/pdf/si/lithium_fire_prevention_si093.pdf)
- Extinguisher maker Amerex: no standards body has issued a standard for Li-ion battery fire extinguishers — [Amerex](https://amerex-fire.com/learning-center/flashpoint/lithium-ion-battery-fire-extinguishers-the-search-for-a-solution/). An NFPA committee document notes there is presently no "Class L" (Li-ion) classification for portable extinguishers in NFPA 10 — [NFPA 312 public input responses](https://docinfofiles.nfpa.org/files/AboutTheCodes/312/312_A2025_SHI_AAA_PIResponses.pdf)
- A secondary workplace guide says an ABC extinguisher "buys seconds, not a solution", a standard extinguisher volume of water is not enough to cool a pack, and cites NFPA/USFA for a re-ignition risk window of 24–72 hours after apparent extinguishment (secondary; primary not checked) — [safetyregulatory.com](https://safetyregulatory.com/guides/lithium-ion-battery-workplace-safety/)

**Special agents (evidence is thin and partly vendor-sourced)**
- Academic comparison of water mist, F-500 at 2 % v/v and CO2 on NMC pouch cells exists (results not read) — [Ubaldi et al., ENEA](https://iris.enea.it/bitstream/20.500.12079/80908/1/Suppression%20capacity%20and%20environmental%20impact%20of%20three%20extinguishing%20agents%20for%20lithium-ion%20battery%20fires.pdf)
- A 2024 study tested foam and AVD (aqueous vermiculite dispersion) on about 100 Wh NMC pouch cells (results not read) — [Palma et al., Case Studies in Thermal Engineering](https://doaj.org/article/7fa4ffacc84f4a1a9fd6de27facbe142)
- A 2022 Beijing Institute of Technology paper reported 3 % F-500 solution had about three times the cooling capacity of water mist on LFP modules; the copy found is hosted by the F-500 manufacturer — [HCT-hosted paper](https://hct-world.com/wp-content/uploads/2023/08/TR_F5_AM_L_Beijing-Institute-of-Technology-2022.pdf)
- The claim that Kiwa (Netherlands, 2017) found F-500 EA the most effective agent comes from the manufacturer's own chronology — [Hazard Control Technologies](https://hct-world.com/wp-content/uploads/2023/11/CH_F5_AM_L_Chronology-of-Lithium-ion-Battery-Fire-Testing.pdf); this conflicts in spirit with FSRI's finding that an added agent was no better than water — [FSRI](https://fsri.org/research-update/researchers-release-evidence-based-ev-battery-fire-response-considerations)

**Quarantine of damaged / swollen / suspect packs (best practice)**
- Store suspected faulty packs outdoors; never charge or repair them; never ship by air — [Specialized](https://content.specialized.com/wp-content/uploads/2021/11/Retailer-Battery-Handling-Recommended-Practices_English.pdf)
- Do not keep damaged packs in the charging cabinet or anywhere inside the shop — [Bicycle Retailer protocols](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- CFPA Europe Guideline No. 47 (2026) defines quarantine storage as a segregated, controlled area for temporary placement of suspect or defective batteries pending safe transport or disposal (detailed requirements not retrieved) — [CFPA-E Guideline 47:2026](https://cfpa-e.eu/app/uploads/2026/08/CFPA_E_Guideline_No_47_2026_F.pdf)
- Transport packaging for damaged batteries requires non-combustible, non-conductive cushioning (see section 6) — [The Compliance Center](https://www.thecompliancecenter.com/how-to-ship-damaged-or-defective-lithium-batteries/)

### Inferences
- Draft emergency flow (synthesised; step order is mine, each element traces to the findings above or section 5):
  1. **Warning signs** (heat, swelling, hissing, smell, smoke, leak): stop work, disconnect charger/load at the wall or isolator if it can be done without touching the pack.
  2. **No flame yet, pack movable:** using tongs/shovel and PPE, move to the outdoor quarantine container (steel, with sand or vermiculite); keep people upwind; observe.
  3. **Flame or jetting:** raise alarm, evacuate, call 114 (Vietnam fire and rescue number — not sourced in this session, verify). Do not stand in smoke (HF, CO).
  4. **Only if trained, small pack, clear exit behind you:** cool with large amounts of water from a distance, or knock down flame with ABC powder/CO2 and then cool with water. Do not use a fire blanket indoors. Protect neighbouring packs and combustibles.
  5. **After flames stop:** treat as live; keep cooling/observing outdoors; expect re-ignition for at least 24–72 h; ventilate the workshop; treat residue and runoff as contaminated (fluorides, metals).
  6. **Electrolyte leak (no fire):** ventilate, gloves and goggles, absorb with inert material, bag as hazardous waste, wash skin; first aid per section 5.
  7. **Electric shock:** isolate the source or separate the victim with a non-conductive object, call 115 (ambulance number — verify), CPR if needed; see Gaps in section 5.
- The fire-service line ("do not fight it, get out") and the workshop reality (an owner will try to save the shop) conflict. The defensible position for the report is: fight only an incipient fire, only with an escape route, and prioritise moving the pack outdoors before runaway, not during it.

### Gaps
- No authoritative source was retrieved for the commonly recommended "steel drum/ammo box with sand or vermiculite, placed outdoors X metres from buildings, observe N hours/days" quarantine specification. Sources confirm only "outdoors, not in the shop". Distances and observation times should be labelled best practice.
- No independent head-to-head data for AVD vs F-500 vs water on e-bike-size packs; no data retrieved on water-immersion containers (immersion tubs) for small packs.
- NFPA's own consumer/e-bike safety text was not retrieved; the 24–72 h re-ignition window is from a secondary guide.
- FSRI evidence is from EVs; its e-mobility (e-scooter) sprinkler experiments exist but results were not read — [FSRI e-mobility sprinkler tests](https://fsri.org/research-update/fsri-examines-impact-residential-sprinkler-system-during-e-mobility-device).
- Vietnamese emergency numbers (114 fire, 115 ambulance) are from background knowledge, not sourced here.

---

## 4. Storage rules

### Takeaway
Lower state of charge is the one storage variable with consistent support: ≤30 % SoC materially reduces fire severity and is the level at which US fire-code storage rules are relaxed, while insurers quote ranges up to 60 %. Cabinet "standards" are weaker than marketed: EN 14470-1 only tests fire from outside, and inside-out ratings rely on vendor adaptations of EN 1363-1.

### Cited Findings
- Batteries stored at ≤30 % SoC present significantly reduced fire severity and lower likelihood of thermal runaway; the 2024 International Fire Code changes waive Li-ion storage requirements when SoC does not exceed 30 % (from search summaries of insurer/engineering articles; exact page attribution not verified) — [CSE Magazine](https://www.csemag.com/designing-for-safe-lithium-ion-battery-storage-and-emerging-fire-codes/); [FM](https://www.fm.com/insights/lithium-ion-battery-hazards-fm-releases-first-ever-comprehensive-guidance)
- FM Loss Prevention Data Sheet 7-112 (Lithium-ion Battery Manufacturing and Storage) sets protection by state of charge, ceiling height, storage height and packaging; it is free on FM's database — [FM](https://www.fm.com/insights/lithium-ion-battery-hazards-fm-releases-first-ever-comprehensive-guidance)
- Other quoted SoC ranges: 30–50 % (Chubb) — [Chubb risk bulletin](https://www.chubb.com/au-en/brokers/risk-bulletins/lithium-ion-batteries-storage.html); 30–60 % (Towergate) — [Towergate](https://www.towergateinsurance.co.uk/insight/how-to-correctly-store-lithium-ion-batteries); most finished products ship/store at 40–60 % — [Viking paper](https://vikinggroupinc.com/sites/default/files/2024-05/JimLake_Protection-of-Lithium-Ion-Batteries-April2024.pdf)
- Retail trade guide: ≤30 % SoC where feasible, well-ventilated area — [The Battery Network](https://batterynetwork.org/wp-content/uploads/E-Bike-Battery-Safety-A-Guide-for-Retailers-The-Battery-Network.pdf)
- OSHA: store in dry, cool locations; limit quantities per NFPA 800 and NFPA 855; do not mix battery chemistries in recycling streams — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)
- Segregation: damaged packs must not share the cabinet or the shop with good stock — [Bicycle Retailer protocols](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Cabinets: EN 14470-1 Type 90 means 90 minutes fire resistance tested from outside to inside. Inside-to-outside performance is tested by vendors using the EN 1363-1 curve as a basis; claims vary (some 60 min, some >90 min), and one vendor uses a curve scaled up 1.3× for lithium fires. This is vendor practice, not a harmonised battery-cabinet standard — [DENIOS guide](https://www.denios.co.uk/consulting-planning/denios-magazine/guide-to-battery-cabinets-for-lithium-ion-batteries); [asecos](https://www.asecos.com/asecos_ION-LINE_letter-seal_en_se/); [FS Matters](https://www.fsmatters.com/Dual-fire-resistance-for-lithium-battery-storage)
- Vietnam (apartment charging areas, by analogy only): Thông tư 31/2026/TT-BXD requires ≥2 m between charging zones or a solid non-combustible partition ≥2 m high — [VTC News](https://vtcnews.vn/khu-vuc-sac-xe-dien-chung-cu-can-dap-ung-nhung-quy-dinh-an-toan-pccc-nao-ar1032976.html)

### Inferences
- A practical three-zone layout follows from the sources: (a) good stock at ≤30 % SoC (or 30–50 % if the cell maker's long-term storage spec requires it) in a closed metal or rated cabinet; (b) charging/testing zone, separate, supervised; (c) outdoor quarantine for damaged, swollen, water-damaged or unknown packs.
- The 2 m separation / 2 m non-combustible partition rule from the apartment regulation is not legally applicable to a workshop but is the only Vietnamese numeric separation figure found and is a reasonable design reference.

### Gaps
- VDMA 24994 (German test guideline for Li-ion storage cabinets) returned no results; its content and status are unverified.
- No sourced storage temperature range, quantity (kWh or kg) thresholds from NFPA 855 / IFC, or minimum distance from combustibles were retrieved. **[unverified background]**: NFPA 855 is commonly cited with a 20 kWh threshold for stationary Li-ion ESS, and FM guidance with about 3 m separation from combustibles; neither was confirmed here.
- FM DS 7-112 itself was not read.

---

## 5. First aid

### Takeaway
HF is the special case: flush with water briefly (about 5 minutes) and get 2.5 % calcium gluconate gel on the skin quickly, reapplying every 15 minutes until medical care; eyes get water only, 15 minutes or more; every suspected HF exposure needs medical evaluation.

### Cited Findings
- HF skin contact: flush with water about 5 minutes, remove contaminated clothing while flushing, then apply and massage in 2.5 % calcium gluconate gel; reapply every 15 minutes until medical responders take over — [Virginia Tech EHS](https://ehs.vt.edu/content/dam/ehs_vt_edu/first-aid-cpr-aed/hydrofluoric%20acid%20quick%20response.pdf); [Cornell EHS](https://ehs.weill.cornell.edu/sites/default/files/hydrofluoric_acid_print_and_go_sheet.pdf)
- If no gel is available, keep flushing for 15–20 minutes — [Calgonate FAQ](https://cbrnetechindex.com/p/7489/Calgonate-Corp/faq)
- The person applying gel should wear gloves to avoid secondary exposure — [UHCL EHS](https://www.uhcl.edu/about/administrative-offices/environmental-health-safety/documents/hf-calcium-gluconate-calgonate-gel.pdf)
- HF eye contact: flush at an eyewash for at least 15 minutes, keeping contaminated water out of the unaffected eye — [Stanford EHS](https://ehs.stanford.edu/?p=815). Other sheets say at least 5 minutes, or intermittent rinsing for 15–30 minutes until pain relief — [Cornell EHS](https://ehs.weill.cornell.edu/sites/default/files/hydrofluoric_acid_print_and_go_sheet.pdf). Sources conflict on duration; none recommend gel in the eye.
- All HF burns need full medical evaluation whether or not gel was used — [Air Products Safetygram 29](https://prd-in.airproducts.com/-/media/files/en/900/900-14-012-us-hydrofluoric-acid-burns-safetygram-29.pdf)
- OSHA requires eyewash and safety showers where electrolyte exposure may occur and training of responders on decomposition products including HF — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)

### Inferences
- These HF protocols were written for laboratory hydrofluoric acid. In a battery workshop the HF route is mainly smoke/gas and contaminated residue, so the more likely first-aid events are smoke inhalation and eye/skin irritation from electrolyte; stocking calcium gluconate gel is a low-cost precaution rather than a documented requirement for battery shops.
- First-aid kit list implied by sources: eyewash station or bottles, running water, 2.5 % calcium gluconate gel (check expiry), nitrile gloves, burn dressings.

### Gaps
- No sourced first-aid steps were retrieved for HF or smoke inhalation, electrolyte (carbonate solvent/LiPF6) contact specifically, electric shock, or thermal burns. **[unverified background]**: standard practice is fresh air and urgent medical review after any smoke exposure (HF lung effects can be delayed), 20 minutes cool running water for burns, isolate power before touching a shock victim and medical review after any DC shock. A cell or pack SDS should be used to source the electrolyte steps.
- Availability of calcium gluconate gel in Vietnam was not checked.

---

## 6. International standards and transport rules

### Takeaway
Only the transport rule for damaged batteries (ADR SP 376 → P908/LP904, or P911/LP906 if liable to react dangerously) and the tool/voltage standards were verified in this session; the product safety standards the brief lists are widely known but were not individually sourced. Damaged or defective lithium batteries are forbidden in air transport.

### Cited Findings
- ADR Special Provision 376 covers lithium cells/batteries identified as damaged or defective and routes them to packing instruction P908 (packages) or LP904 (large packagings) at Packing Group II performance level — [The Compliance Center](https://www.thecompliancecenter.com/how-to-ship-damaged-or-defective-lithium-batteries/)
- Batteries liable to rapidly disassemble, react dangerously, flame or emit dangerous heat or gas go to P911 / LP906 at Packing Group I performance level — [The Compliance Center](https://www.thecompliancecenter.com/how-to-ship-damaged-or-defective-lithium-batteries/)
- P908: non-combustible, non-conductive cushioning/thermal insulation required; one battery per package when the battery exceeds 30 kg net; LP904 is limited to a single item and does not allow fibreboard (50G) outer packaging — [The Compliance Center](https://www.thecompliancecenter.com/how-to-ship-damaged-or-defective-lithium-batteries/)
- Packages must be marked "DAMAGED/DEFECTIVE" in addition to the proper shipping name, and the transport document must state "Transport in accordance with special provision 376" (as quoted from the UN Model Regulations in an ICAO working paper) — [ICAO DGP working paper](https://www.icao.int:443/safety/DangerousGoods/DGP26/DGP.26.WP.047.6.EN.pdf)
- Damaged/defective lithium batteries are prohibited in air transport — [The Compliance Center](https://www.thecompliancecenter.com/how-to-ship-damaged-or-defective-lithium-batteries/); consistent with manufacturer guidance "never ship them by air" — [Specialized](https://content.specialized.com/wp-content/uploads/2021/11/Retailer-Battery-Handling-Recommended-Practices_English.pdf)
- US equivalents named by OSHA: 49 CFR 172 and 49 CFR 173.185; storage quantity limits per NFPA 800 (Battery Safety Code) and NFPA 855 — [OSHA](https://www.osha.gov/lithium-ion-battery-safety/control)
- IEC 60900:2018 (insulated hand tools to 1,000 V AC / 1,500 V DC) and UN R100 (60 V DC / 30 V AC high-voltage threshold) — see section 1 and 2 sources: [IEC 60900:2018](https://reference.globalspec.com/ref/4638786/iec-60900-2018); [UN R100](https://eur-lex.europa.eu/eli/reg/2015/100/oj/eng/pdf)
- Vietnam has adopted IEC-based TCVN standards for cells, e.g. TCVN 13969:2024 (IEC 63218:2021) and TCVN 12668-4:2020 (IEC 60086-4:2019, safety of primary lithium batteries) — [Thư viện Pháp luật TCVN 13969:2024](https://thuvienphapluat.vn/TCVN/Dien-dien-tu/TCVN-13969-2024-IEC-63218-2021-Cell-pin-thu-cap-chua-kiem-cac-chat-dien-phan-921087.aspx); [TCVN 12668-4:2020](https://thuvienphapluat.vn/TCVN/Dien-dien-tu/TCVN-12668-4-2020-IEC-60086-4-2019-Pin-so-cap-Phan-4-An-toan-cua-pin-lithium-919843.aspx)
- A 2026 Vietnamese analysis says the TCVN 12241 series (traction Li-ion cells) is referenced only voluntarily, not mandatory — [The Saigon Times](https://thesaigontimes.vn/bao-gio-lo-hong-trong-trai-tim-xe-dien-duoc-lap-day/)

### Inferences
- ADR is a European road agreement and does not bind domestic transport in Vietnam; it is the best available packaging benchmark for moving damaged packs to a recycler (rigid outer, each pack individually protected against short circuit, non-combustible non-conductive fill such as vermiculite, "damaged/defective" marking).
- A workshop cannot courier a damaged pack by air under any regime found; customers should be told this at intake.

### Gaps
- **[unverified background]** Not sourced in this session; scopes given from general knowledge and should be checked before publication: IEC 62133-2 (safety of portable sealed Li cells/batteries); IEC 62619 (industrial Li cells/batteries); UN Manual of Tests and Criteria 38.3 (transport tests T1–T8: altitude, thermal, vibration, shock, external short circuit, impact/crush, overcharge, forced discharge); UL 2271 (batteries for light electric vehicles); UL 2849 (e-bike electrical systems); EN 50604-1 (Li batteries for light EVs); NFPA 855 (stationary ESS installation); IATA DGR packing instructions 965–967 and the 30 % SoC limit for air cargo.
- The official ADR text (current edition) was not read; the P908/LP904 details come from a dangerous-goods consultancy summary.
- Vietnamese domestic dangerous-goods transport rules for lithium batteries (Class 9, UN 3480/3481) were not researched.

---

## 7. Vietnam-specific law, technical regulations, waste/EPR and incidents

### Takeaway
The legal base changed substantially in 2025–2026: fire safety is now governed by the Law on Fire Prevention, Fighting and Rescue 2024 with Decree 105/2025 (replacing 136/2020) and penalty Decree 106/2025; e-motorcycle batteries by QCVN 31:2026/BXD (replacing QCVN 91:2024/BGTVT, which itself replaced QCVN 91:2019); EPR by Decree 110/2026 (effective 25/5/2026); and apartment charging by Thông tư 31/2026/TT-BXD (effective 15/12/2026). Several of these were confirmed only through news and law-firm summaries and must be checked against official texts.

### Cited Findings

**Fire safety law (PCCC)**
- Decree 105/2025/NĐ-CP, issued 15/05/2025, effective 01/07/2025, details the Law on Fire Prevention, Fighting and Rescue 2024 and replaces Decree 136/2020/NĐ-CP — [LuatVietnam](https://luatvietnam.vn/tin-van-ban-moi/da-co-nghi-dinh-105-2025-nd-cp-quy-dinh-chi-tiet-luat-pccc-va-cuu-nan-cuu-ho-186-102184-article.html); [Enviliance](https://enviliance.com/regions/southeast-asia/vn/report_14022)
- Replacement is not total: transitional Article 46 keeps some Decree 136/2020 provisions in use (equipment inspection list in Article 38 and Appendix VII; acceptance and design-revision procedures in Articles 13–15 as amended by Decree 50/2024) — [Hệ thống pháp luật, Điều 46](https://hethongphapluat.com/nghi-dinh-105-2025-nd-cp-huong-dan-luat-phong-chay-chua-chay-va-cuu-nan-cuu-ho/dieu-46)
- Administrative penalties are in companion Decree 106/2025/NĐ-CP — [LuatVietnam comparison](https://luatvietnam.vn/tin-phap-luat/da-co-ban-so-sanh-diem-moi-nghi-dinh-105-2025-nd-cp-ve-phong-chay-chua-chay-230-102417-article.html)
- Fire-safety dossier (hồ sơ PCCC) rules formerly in Thông tư 149/2020/TT-BCA are now in the decree itself; forms such as PC06 (facility firefighting plan) apply — [Hệ thống pháp luật](https://hethongphapluat.com/phap-luat/huong-dan/ho-so-pccc-2025-nhung-thay-doi-song-con-va-huong-dan-lap-ho-so-chuan-nghi-dinh-105.html)
- Appendix I of Decree 105/2025 lists 34 types of facility under fire-safety management — [LuatVietnam](https://luatvietnam.vn/linh-vuc-khac/danh-muc-co-so-thuoc-dien-quan-ly-ve-phong-chay-chua-chay-883-102227-article.html); [Appendix I text](https://ketoananpha.vn/phu-luc-i-danh-muc-co-so-thuoc-dien-quan-ly-ve-pccc-theo-nghi-dinh-so-105-2025-nd-cp)
- A reply from the Fire Police Department (C07) dated 30/01/2026 states that a service business with total business floor area of 100 m² or more is classed as "other service business" under item 11 of Appendix I — [LuatVietnam](https://luatvietnam.vn/tin-van-ban-moi/xac-dinh-co-so-pccc-khi-thue-nha-kinh-doanh-cam-do-theo-nghi-dinh-105-2025-nd-cp-186-107032-article.html)
- 44 types of facility must buy compulsory fire and explosion insurance from 1/7/2025 (whether a small battery workshop is included was not checked) — [Tạp chí Công Thương](https://tapchicongthuong.vn/44-co-so-phai-mua-bao-hiem-chay--no-bat-buoc-140759.htm)
- The Government has published a roadmap for handling existing facilities that do not meet fire-safety requirements — [SGGP](https://www.sggp.org.vn/chinh-phu-cong-bo-lo-trinh-xu-ly-doi-voi-cac-co-so-khong-bao-dam-yeu-cau-ve-phong-chay-chua-chay-post796514.html)

**Technical regulations for batteries (QCVN)**
- QCVN 91:2024/BGTVT (batteries for electric motorcycles and mopeds) was issued under Thông tư 48/2024/TT-BGTVT dated 15/11/2024; sources differ on effective date (signing date vs 01/01/2025) — [LuatVietnam](https://luatvietnam.vn/cong-nghiep/quy-chuan-qcvn-912024-bgtvt-ac-quy-su-dung-cho-xe-mo-to-dien-xe-gan-may-dien-385610-d3.html)
- QCVN 31:2026/BXD (batteries for electric motorcycles and mopeds), issued with Thông tư 13/2026/TT-BXD (file dated 09/04/2026), replaces QCVN 91:2024/BGTVT and took effect 9/10/2026 — [Ministry of Construction PDF](https://moc.gov.vn/Images/FileVanBan/BXD_13-2026-TT-BXD_09042026_QCVN31-2026-BXD.pdf); [Báo Lào Cai](https://baolaocai.vn/xe-may-dien-co-quy-chuan-moi-tu-910-chu-xe-co-phai-thay-pin-post911077.html). The companion motor regulation QCVN 30:2026/BXD (Thông tư 12/2026/TT-BXD) replaces QCVN 90:2024/BGTVT on the same date.
- QCVN 31:2026 safety tests depend on battery type and may include overcharge, over-discharge, vibration, short circuit, water immersion and drop tests; it applies to new batteries in manufacture, assembly, import and certification, not to vehicles already in use; owners have no general duty to replace batteries; dossiers received before the effective date are processed under the old rules — [Báo Lào Cai](https://baolaocai.vn/xe-may-dien-co-quy-chuan-moi-tu-910-chu-xe-co-phai-thay-pin-post911077.html)
- E-bicycles: QCVN 76:2019/BGTVT (batteries for electric bicycles) was issued with Thông tư 45/2019/TT-BGTVT, effective 10/5/2020 — [LuatVietnam](https://luatvietnam.vn/giao-thong/thong-tu-45-2019-tt-bgtvt-quy-chuan-ky-thuat-quoc-gia-ve-ac-quy-dong-co-xe-dap-dien-178232-d1.html); [Thư viện Pháp luật](https://thuvienphapluat.vn/TCVN/Dien-dien-tu/QCVN-76-2019-BGTVT-Ac-quy-su-dung-cho-xe-dap-dien-918425.aspx). Its current status was not confirmed.
- A 2024 drafting comparison noted that under the (then draft) road traffic order and safety law, e-bicycles are non-motorised ("xe thô sơ") and QCVN 68 (e-bicycles) would no longer apply; this is a drafting note, not a confirmed repeal — [Government draft comparison table](https://datafiles.chinhphu.vn/cpp/files/duthaovbpl/2024/Thang08/bangsosanhqc.docx)
- QCVN 101:2020/BTTTT covers lithium batteries for handheld devices (not traction packs) — [Thư viện Pháp luật](https://thuvienphapluat.vn/TCVN/Dien-dien-tu/QCVN-101-2020-BTTTT-Pin-lithium-cho-thiet-bi-cam-918704.aspx)

**Hazardous waste and EPR**
- Waste batteries appear in the hazardous-waste / controlled industrial waste list issued with Thông tư 02/2022/TT-BTNMT; a 2025 Hue University paper cites code 16 01 12 for waste batteries and accumulators from households (group 16) — [Hue University Journal of Science](https://jos.hueuni.edu.vn/index.php/hujos-ns/article/download/8088/2287/36898)
- A Toyota Vietnam EPR disclosure classes lead-acid batteries under hazardous-waste code 19 06 01 and other batteries under 19 06 02 / 19 06 05 (company document; does not say which code applies to Li-ion) — [Toyota Vietnam](https://www.toyota.com.vn/media/qhehbmrh/thông-tin-về-các-hạng-mục-thực-hiện-trách-nhiệm-tái-chế-của-công-ty-ô-tô-toyota-việt-nam.pdf)
- The hazardous-waste list sits in Section C, Form 1, Appendix III of Thông tư 02/2022/TT-BTNMT — [Thư viện Pháp luật](https://thuvienphapluat.vn/hoi-dap-phap-luat/839D8EB-hd-danh-muc-chat-thai-nguy-hai-moi-nhat-hien-nay.html)
- Thông tư 07/2025/TT-BTNMT (28/02/2025) amends Thông tư 02/2022 — [legalzone copy](https://legalzone.vn/wp-content/uploads/legal-sources/environment/thong-tu-07-2025-tt-btnmt-sua-doi-thong-tu-02-2022-phan-2.pdf); Circular 44/2025/TT-BNNMT issues a national technical regulation on hazardous-waste thresholds — [Thư viện Pháp luật](https://thuvienphapluat.vn/van-ban/Tai-nguyen-Moi-truong/Circular-44-2025-TT-BNNMT-technical-regulation-on-hazardous-waste-thresholds-673366.aspx)
- Decree 05/2025/NĐ-CP amended Decree 08/2022/NĐ-CP, including EPR scope and an exemption for producers/importers with product revenue under VND 30 billion — [KPMG Vietnam](https://kpmg.com/vn/vi/home/phan-tich-chuyen-sau/2025/02/key-amendments-to-vietnam-environment-protection-regulations.html)
- Decree 110/2026/NĐ-CP, effective 25/5/2026, details Articles 54 (recycling responsibility) and 55 (waste collection/treatment) of the Law on Environmental Protection, integrating and amending provisions of Decree 08/2022 (as amended by 05/2025) and Decree 48/2026 — [VnEconomy](https://vneconomy.vn/cu-the-ty-le-tai-che-san-pham-bao-bi-cua-cac-nha-san-xuat-nhap-khau.htm)
- Mandatory recycling rates under Decree 110/2026: lead-acid batteries 12 %; other accumulators 8 %; rechargeable batteries 8 %; lithium and NiMH batteries for transport vehicles 0 %. Rates are adjusted every 3 years, each increase capped at 10 %, first adjustment in 2029 — [VnEconomy](https://vneconomy.vn/cu-the-ty-le-tai-che-san-pham-bao-bi-cua-cac-nha-san-xuat-nhap-khau.htm)
- Rationale for 0 %: long service life and currently small waste volumes of vehicle lithium batteries — [SGGP](https://www.sggp.org.vn/du-kien-nhieu-quy-dinh-moi-ve-trach-nhiem-nha-san-xuat-lien-quan-thai-bo-tai-che-san-pham-post808988.html)
- The original Appendix XXII of Decree 08/2022 set 8 % for rechargeable batteries (both vehicle and electronics groups), with reuse and export-for-recycling (max 20 %) among permitted routes — [Appendix XXII copy](https://cdn.thuvienphapluat.vn/uploads/tintuc/2024/10/18/PH%E1%BB%A4%20L%E1%BB%A4C%20XXII%20(2).doc)

**Incidents and regulatory responses**
- Trung Kính, Hanoi, 24/5/2024: fire in a 3-storey house used as residence, rented rooms and an e-vehicle sales/repair business; 14 dead. Hanoi police found the cause was an electrical short circuit at the front of an electric motorbike, igniting insulation and spreading to about 20 parked motorbikes/e-bikes in the yard, blocking the only escape route. The alley was about 1.5 m wide and 250 m from the street, so fire engines could not reach it. A criminal case was opened — [PLO](https://plo.vn/cong-an-tp-ha-noi-cong-bo-nguyen-nhan-chay-o-pho-trung-kinh-post797557.html); [VTC News](https://www.vtcnews.vn/nguyen-nhan-vu-chay-nha-tro-khien-14-nguoi-tu-vong-o-ha-noi-ar879613.html); [VietnamPlus](https://www.vietnamplus.vn/khoi-to-xu-ly-nghiem-vu-chay-nha-tro-lam-14-nguoi-chet-tai-trung-kinh-post955441.vnp). Published findings name wiring, not a lithium cell, as the origin.
- Hanoi: the city required mini-apartment buildings to provide a separate charging area with safety distances and banned overnight charging — [The Saigon Times](https://thesaigontimes.vn/saigontimes/ha-noi-khong-duoc-sac-xe-dien-qua-dem-o-chung-cu-mini/)
- Some Hanoi buildings (HH Linh Đàm, CT1 Thạch Bàn) stopped accepting e-vehicles; local authorities objected, noting the fire law does not prohibit parking or charging e-vehicles in apartment buildings — [SGGP](https://www.sggp.org.vn/lung-tung-chuyen-sac-pin-xe-dien-o-chung-cu-post832462.html); [VietNamNet](https://vietnamnet.vn/chung-cu-cam-de-xe-dien-cu-dan-roi-nhu-to-vo-lo-rao-can-khi-chuyen-doi-xanh-2469335.html)
- HCMC: restrictions are building-level, not city law. Example: Him Lam Nam Sài Gòn barred e-vehicles from apartments, lifts and parking areas from 1/1/2026 and set an outdoor charging point at VND 120,000 per vehicle per month; Tín Phong requires charging to be registered before 22:00. HCMC has over 39,500 electric cars and nearly 87,000 electric motorbikes, and approved 20,000 battery-swap cabinets on pavements and public areas — [SGGP](https://www.sggp.org.vn/lung-tung-chuyen-sac-pin-xe-dien-o-chung-cu-post832462.html)
- National: Thông tư 31/2026/TT-BXD (15/6/2026) amends QCVN 04:2021/BXD (Amendment 01:2026), effective 15/12/2026. Key numbers for charging areas: preferred location outdoors at ground level; basement zone ≤25 car chargers or ≤50 two-wheeler chargers; above-ground zone ≤30 car or ≤80 two/three-wheeler chargers; ≥2 m between zones or non-combustible partition ≥2 m high; own fire compartment with REI 90 partitions; automatic fire alarm, automatic suppression, 24/7 CCTV, smoke ventilation, CO and HF detectors; automatic power cut-off on abnormal charging plus emergency stop; basement chargers ≤22 kW each; ≥2 exits per compartment — [VTC News](https://vtcnews.vn/khu-vuc-sac-xe-dien-chung-cu-can-dap-ung-nhung-quy-dinh-an-toan-pccc-nao-ar1032976.html)
- Prime Minister's Công điện 27/CĐ-TTg (31/3/2026) called for charging infrastructure in apartment buildings and completion of fire-safety regulations — [VnEconomy](https://vneconomy.vn/automotive/don-bay-phap-ly-xoa-bo-vung-trang-ve-ha-tang-tram-sac-tai-chung-cu.htm)
- A 2026 analysis says Vietnam lacks a systematic database of battery fire incidents and that cause investigations are often unspecific — [The Saigon Times](https://thesaigontimes.vn/bao-gio-lo-hong-trong-trai-tim-xe-dien-duoc-lap-day/)

### Inferences
- Superseded-document map for the report (as found): Decree 136/2020 → Decree 105/2025 (+106/2025 penalties), with Article 46 carve-outs; Thông tư 149/2020/TT-BCA → content moved into Decree 105/2025; QCVN 91:2019/BGTVT → QCVN 91:2024/BGTVT → QCVN 31:2026/BXD; Decree 08/2022 EPR provisions → amended by 05/2025 → integrated into Decree 110/2026. The brief's "QCVN 91:2019" and "Nghị định 08/2022 EPR rates" are therefore out of date.
- A workshop under 100 m² probably does not fall into Appendix I as an "other service business" (item 11 threshold is 100 m² per the C07 reply), but the Law's general duties (fire-safety conditions, extinguishers, escape route) would still apply; a workshop combined with living space is the exact pattern of the Trung Kính fire. This reading is mine and needs confirmation with the local fire police.
- EPR obligations fall on producers and importers, not on a repair workshop; the workshop's own duty is as a waste generator (classify, store and hand over spent packs to a licensed hazardous-waste carrier/treater). With the vehicle-lithium recycling rate set at 0 % until at least 2029, producer-funded take-back routes for e-bike packs are unlikely to be widely available soon, so the workshop should plan and budget for its own licensed disposal route.
- Lessons from Trung Kính that transfer directly to a repair shop: do not combine workshop, vehicle parking and sleeping accommodation; keep stored vehicles/packs out of the escape route; have a second exit; fix wiring and chargers, since charging and wiring faults (not only cells) are what C07 names as leading causes.
- The apartment-charging regulation shows what regulators now consider adequate for Li-ion charging areas (fire compartment REI 90, automatic detection and suppression, CO/HF detection, automatic charge cut-off, 2 m separation). A workshop can borrow these as a design benchmark.

### Gaps
- The exact hazardous-waste code for lithium-ion batteries in Thông tư 02/2022 (as amended by 07/2025) was not confirmed. Sources conflict or are incomplete: 16 01 12 (household origin, academic paper) vs 19 06 02 / 19 06 05 (company disclosure). The appendix must be read directly; Circular 44/2025 thresholds may also affect classification.
- Whether Thông tư 02/2022 remains in force in late 2026 or has been replaced by Ministry of Agriculture and Environment circulars was not confirmed.
- Decree 110/2026 and Decree 48/2026 were confirmed only via one news article; the official text, and whether Decree 08/2022 is wholly or partly repealed, were not checked.
- Current status of QCVN 76:2019/BGTVT and QCVN 68:2013/BGTVT (e-bicycles) after the Road Traffic Order and Safety Law 2024 and the 2025 ministry merger (BGTVT into BXD) is unconfirmed.
- The specific Appendix I item (if any) for vehicle repair workshops or battery trading, the fire-safety equipment required for a sub-100 m² workshop, and compulsory insurance applicability were not found.
- No official national statistics on e-bike/e-motorbike battery fires were found. The September 2023 Khương Hạ mini-apartment fire (widely reported, 56 deaths) was not researched in this session and is not sourced here.
- The legal document behind Hanoi's overnight-charging ban for mini-apartments (number and date) was not retrieved.
- Vietnamese occupational-safety rules (Luật An toàn, vệ sinh lao động 2015, electrical safety QCVN) applicable to the workshop were not researched.
