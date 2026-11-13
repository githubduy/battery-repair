# Diagnosis and Repair Procedures for Lithium Battery Packs (NMC / LiFePO4) and their BMS — Bench Notes (as of Nov 2026)

Source-quality legend used throughout:
- **[MFR/STD]** = manufacturer datasheet, manufacturer manual, TI reference manual, or a standard.
- **[REF]** = Battery University (Cadex) — widely used reference, not a standard.
- **[HOBBY]** = forum / DIY community / vendor blog opinion. Treat as rule of thumb only.

Research limitations (read first): Endless Sphere was blocked by bot protection, the Daly PDFs exceeded the fetch size limit, and several datasheet PDFs could only be read through search snippets. Items that I could not source are listed under "Gaps" and are NOT asserted as fact. Numbers under "Inferences" are my own arithmetic or synthesis.

---

## 1. Step-by-step diagnostic flow and numeric thresholds (cells vs BMS vs wiring vs charger)

### Takeaway
The defensible bench sequence is: safety stop check -> charger output -> pack voltage at output (P+/P-) vs at cell stack (B+/B-) -> per-group voltages on the balance leads -> load/IR/self-discharge tests. "Stack voltage normal but output low/zero" isolates the fault to BMS/fuse/FET; "one group far off" isolates it to cells or a broken sense wire. Hard numbers exist for voltage windows (manufacturer/Battery University); IR and self-discharge reject limits are mostly hobbyist rules of thumb and must be benchmarked against the cell datasheet.

### Cited Findings

**A. Safety stop points (before any measurement)**
- Swelling, leaking, smoke or strong burnt odour = stop; do not attempt repair, route to safe disposal. [HOBBY/vendor] — [Letrigo BMS diagnosis guide](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- External inspection items: casing cracks/dents/swelling; connector pins for green/white corrosion, burn marks, bent pins; charge port debris. Internal: MOSFETs cracked/discoloured, brown PCB near FETs (overheating), dull/grainy/cracked solder joints, solder bridges, arcing marks, chafed or detached balance (sense) wires. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)

**B. Cell voltage windows**
- NMC/cobalt-blend Li-ion: charge to 4.20 V/cell, tolerance +/-50 mV/cell. [REF] — [Battery University BU-409](https://batteryuniversity.com/article/bu-409-charging-lithium-ion)
- LiFePO4: nominal 3.20 V, charge to 3.65 V. [REF] — [Battery University BU-409](https://batteryuniversity.com/article/bu-409-charging-lithium-ion)
- Li-ion should not be discharged below 2.50 V/cell. [REF] — [Battery University BU-802b](https://batteryuniversity.com/article/bu-802b-what-does-elevated-self-discharge-do)
- Example NMC cell datasheet (Samsung INR18650-35E): charging voltage 4.2 V, nominal 3.60 V, discharge cut-off 2.65 V, standard charge 0.5C (1,700 mA) with 0.02C (68 mA) cut-off, charge temperature 0 to 45 C, discharge -10 to 60 C, shipping voltage 3.49-3.69 V, initial AC 1 kHz impedance <= 35 mOhm. [MFR/STD] — [Samsung INR18650-35E specification (reseller-hosted copy)](https://cdn.shopify.com/s/files/1/0613/3327/4870/files/35eDatasheet.pdf)
- Example LFP prismatic (EVE LF280K): charge cut-off 3.65 V, discharge cut-off 2.5 V, AC 1 kHz internal resistance <= 0.25 mOhm, self-discharge listed by resellers as <= 3 %/month, charging allowed 0 to 55 C, discharge -20 to 55 C. [MFR figures via reseller listings; no official EVE PDF retrieved] — [Gobel Power LF280K listing](https://www.gobelpower.com/eve-32v-280ah-rechargeable-lifepo4-battery-cell_p6:b793f0b1376f2c250f55165a62e68daf.html); [lifepo4.com.au LF280K listing](https://lifepo4.com.au/shop/cells-lifepo4/eve/automotive-grade/280aha/eve-280ah-lf280k-v3-automotive-grade/)
- Protection circuits must stop any cell exceeding 4.30 V on charge; prolonged charging above 4.30 V on a 4.20 V cell plates metallic lithium. [REF] — [Battery University BU-304b](https://batteryuniversity.com/article/bu-304b-making-lithium-ion-safe); [Battery University BU-304a](https://batteryuniversity.com/article/safety-concerns-with-li-ion)
- Protection circuit under-voltage cut-off varies by maker between 2.2 and 2.9 V/cell. [REF] — [Battery University BU-808a](https://batteryuniversity.com/article/bu-808a-how-to-awaken-a-sleeping-li-ion)
- Pack protection typically disconnects when the weakest cell reaches 2.80 V/cell or lower; cells should not exceed 4.25 V/cell on charge (most Li-ion). [REF] — [Battery University BU-803a](https://batteryuniversity.com/article/bu-803a-cell-matching-and-balancing)

**C. Deep-discharge / scrap thresholds**
- Do NOT boost Li-ion that has dwelled below 1.5 V/cell for a week or longer: copper shunts may have formed, risking partial or total short. [REF] — [Battery University BU-808a](https://batteryuniversity.com/article/bu-808a-how-to-awaken-a-sleeping-li-ion)
- "Li-ion must not dip below 2 V/cell for any length of time"; copper shunts raise self-discharge or cause a partial short. [REF] — [Battery University BU-304a](https://batteryuniversity.com/article/safety-concerns-with-li-ion)
- Copper dendrites grow if a cell dwells in a low-voltage state for longer than a week. [REF] — [Battery University BU-802b](https://batteryuniversity.com/article/bu-802b-what-does-elevated-self-discharge-do)
- During boost: "Discard the pack if the voltage does not rise to a normal level within a minute while on boost." [REF] — [Battery University BU-808a](https://batteryuniversity.com/article/bu-808a-how-to-awaken-a-sleeping-li-ion)
- Samsung cell specifications (INR18650-29E, -30Q) list a pre-charging voltage range of 1.0 V to 3.0 V at a pre-charge current of 0.1C to 0.5C. [MFR, but read from Scribd-hosted copies via search snippet — verify against the current official spec] — [Samsung INR18650-29E (Scribd copy)](https://www.scribd.com/document/676224823/ACCU-INR18650-29E); [Samsung INR18650-30Q (Scribd copy)](https://www.scribd.com/document/733192032/INR18650-30Q-Samsung)
- TI gauge firmware treats deep under-voltage as a possible copper-deposition condition: the SUV permanent-fail check can be run on wake from shutdown with CHG and DSG FETs disabled "to prevent an applied charge voltage from masking a copper deposition condition". [MFR/STD] — [TI BQ40Z50-R5 Technical Reference Manual SLUUCN4](https://www.ti.com/lit/pdf/SLUUCN4)

**D. Pack-level voltage tests and decision points**
- Charger first: measure open-circuit charger output; expect about 42 V for a 36 V (10S) system and 54.6 V for a 48 V (13S) system. Zero or wrong output = charger fault, not battery. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- 48 V NMC pack reference: about 54.6 V full, about 42 V empty. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- Compare B+/B- (cell stack) with P+/P- (output). If B+/B- is normal but P+/P- is much lower or zero (example about 0.9 V on a 48 V pack), the BMS has cut discharge or the FET stage/fuse is faulty; possible causes are over-discharge, over-current, imbalance, faulty MOSFET, blown internal fuse. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- Daly manual check after activation: voltage B+ to B- and voltage P+ to P- should be consistent. [MFR/STD, via manual mirror] — [Daly manual mirror (manuals.plus)](https://manuals.plus/asin/B0B3TH6XRB)
- Balance-lead check: black probe on B-, probe B1, B2, B3... in sequence; each reading must rise cumulatively by one group voltage. A group clearly higher/lower than the rest = imbalance; a low group can shut down the whole pack. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- Measure cell voltages both at the cells and at the BMS balance-connector solder pads; if good at the pads, the problem is elsewhere (not harness). [HOBBY] — [Endless Sphere, "Need help diagnosing and repairing a BMS" (search excerpt only)](https://endless-sphere.com/sphere/threads/need-help-diagnosing-and-repairing-a-bms.69797)
- Field case: output read 33.1 V with balance harness unplugged and dropped to 0.9 V with harness connected — i.e. BMS was reacting to what it sensed on the harness, not dead. [HOBBY] — [Endless Sphere thread index (search excerpt)](https://endless-sphere.com/sphere/threads/best-of-dnmun-bms-info-battery-fix-etc.85951/latest)
- Load test: measure at rest then under resistive load; small drop is normal, sharp drop = capacity loss / high resistance or BMS limiting. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)

**E. Group delta / imbalance thresholds**
- LFP at end of charge: cells within 50 mV = balanced, no top balance needed; more than 150 mV apart = top balance; 50-150 mV = judgement call. Resting voltages after cut-off are NOT a good balance indicator. [HOBBY, widely cited DIY Solar Forum tutorial] — [DIY Solar Forum top-balance tutorial](https://www.diysolarforum.com/resources/top-balancing-lifepo4-cells-using-a-low-cost-benchtop-power-supply.65/)
- JK BMS balance trigger: recommended 0.005 V for batteries above 50 Ah and 0.01 V below 50 Ah. [MFR/STD] — [JK Smart BMS Bluetooth manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- Capacity tolerance between cells in an industrial battery should be +/-2.5 %; in aged 2P4S packs with 5/6/7/12 % section mismatch, the 12 % pack lost the most capacity over 18 cycles. [REF] — [Battery University BU-803a](https://batteryuniversity.com/article/bu-803a-cell-matching-and-balancing)
- Packs above 24 V should have balancing. [REF] — [Battery University BU-803a](https://batteryuniversity.com/article/bu-803a-cell-matching-and-balancing)

**F. Internal resistance (IR)**
- Measure with an AC 1 kHz impedance meter (this is the method cell makers specify). [MFR/STD] — [Samsung INR18650-35E specification](https://cdn.shopify.com/s/files/1/0613/3327/4870/files/35eDatasheet.pdf)
- Rule of thumb: fresh 18650 at AC 1 kHz measures 20-40 mOhm, end-of-life cells typically exceed 80 mOhm; replace if IR has doubled versus baseline. Second-life acceptance gate suggested at SOH >= 80 %. [HOBBY/vendor blog] — [Industrial Monitor Direct, capacity-matching article](https://industrialmonitordirect.com/no/blogs/knowledgebase/capacity-matching-18650-cells-in-excel-a-field-engineers)
- Another hobbyist threshold: healthy 18650 IR below 100 mOhm. [HOBBY] — [Instructables, re-using laptop cells](https://www.instructables.com/Re-using-Lithium-Ion-Cells-From-Laptop-Batteries)

**G. Self-discharge test**
- Normal Li-ion: about 5 % in first 24 h after charge, then 1-2 %/month; protection circuit adds about 3 %/month. Monthly loss at full charge: 6 % at 0 C, 20 % at 25 C, 35 % at 60 C; at 40-60 % SoC: 2 % / 4 % / 15 %. [REF] — [Battery University BU-802b](https://batteryuniversity.com/article/bu-802b-what-does-elevated-self-discharge-do)
- General (not Li-ion-specific) discard threshold: self-discharge reaching 30 % in 24 h. Elevated self-discharge often precedes an internal short; cells previously deep-discharged show higher self-discharge. [REF] — [Battery University BU-802b](https://batteryuniversity.com/article/bu-802b-what-does-elevated-self-discharge-do)
- Hobbyist screen for salvaged NMC cells: fully charge, rest a couple of weeks, reject cells that fall below about 4.1 V; other sources use 24 h, 7 or 7-14 day rests. [HOBBY] — [CandlePowerForums salvaged 18650 thread](https://www.candlepowerforums.com/threads/how-to-check-if-a-salvaged-18650-cell-is-good.483706/)
- A cell that gets very warm during charging may have a serious internal short and should be discarded. [HOBBY] — [Instructables](https://www.instructables.com/Re-using-Lithium-Ion-Cells-From-Laptop-Batteries)

### Inferences
- Decision tree skeleton (synthesised from the above):
  1. Visual/smell/swelling fail -> STOP, quarantine.
  2. Charger open-circuit voltage wrong -> charger fault. (Expected CV = cells-in-series x 4.20 V for NMC, x 3.65 V for LFP; e.g. 10S NMC 42.0 V, 13S 54.6 V, 14S 58.8 V, 16S 67.2 V, 20S 84.0 V; 4S LFP 14.6 V, 8S 29.2 V, 16S 58.4 V. My arithmetic; LFP figures match the DIY Solar tutorial.)
  3. P+/P- approximately equals B+/B- and in the normal window -> pack side OK; look at connector, vehicle/controller, charger port wiring.
  4. B+/B- normal, P+/P- near zero -> read all groups. All groups in window and balanced -> BMS latched (try reset/charge wake) or FET/fuse/shunt/protection IC fault. One or more groups under UVP (roughly 2.5-2.9 V NMC depending on BMS) -> BMS is correctly protecting; fault is cells or a parasitic drain on that group.
  5. A group reads wrong at the BMS connector but right at the cell -> balance wire/connector/corroded pad. A reading of roughly 0 V or roughly 2x on adjacent channels is the classic signature of one broken sense wire (inference; not found stated in a retrievable source).
  6. B+/B- itself low or zero -> open series link, blown cell-level fuse/weld, or deeply discharged cells; read each group at the cells.
- Scrap rule that can be defended from sources: any cell/group found below 1.5 V with unknown or > 1 week dwell = scrap (BU-808a). Between 1.5 V and the cell's cut-off (2.5-2.65 V) = candidate for controlled pre-charge, then mandatory self-discharge and capacity/IR retest. Samsung's 1.0 V lower pre-charge bound is the manufacturer's charger-design window for cells in normal service, not a licence to revive cells that sat for months; the stricter BU rule is the safer workshop policy.
- IR limits should be defined relative to the datasheet value of the specific cell (e.g. reject at about 2x initial spec) because absolute mOhm depends heavily on cell format (0.25 mOhm for a 280 Ah LFP vs 35 mOhm for an 18650).

### Gaps
- No manufacturer or standard source found giving a numeric "maximum allowed group delta at rest" for NMC e-bike packs. Common shop practice figures (e.g. flag > 30-50 mV at rest, fail > 100 mV) could not be sourced and should be marked as house rules.
- No authoritative self-discharge reject threshold in mV/day for LFP or NMC cells was found; only hobbyist rest-test rules.
- DC IR (pulse) test method and pass limits were not found in a retrievable primary source.
- An EU project report on second-life cell selection (IR, impedance, self-discharge protocol) exists at [Zenodo D3.4](https://zenodo.org/records/6674934/files/D3.4-Labeling_and_certif_protocols_2nd_life_batteries.pdf) but was not read.

---

## 2. Common BMS failure modes, symptoms, diagnosis, repair — and when to replace the whole BMS

### Takeaway
Most "dead pack" cases are the BMS doing its job (UVP/OVP/short latch) or a harness fault; true board faults cluster around the power stage (FETs, solder joints) and sense inputs. Smart-gauge packs (TI BQ40Z50 family in laptops/OEM packs) add firmware-latched Permanent Failure states that cut all FETs, may blow a chemical fuse, and are not field-clearable without the OEM's keys — for those, and for any board with heat/corrosion damage, replacement is the realistic repair.

### Cited Findings

**Power stage (MOSFETs, diodes, joints)**
- With the pack disconnected: zero ohms between any two terminals of a FET (usually drain-source) = shorted FET. [HOBBY] — [Endless Sphere, "Need help diagnosing and repairing a BMS" (search excerpt)](https://endless-sphere.com/sphere/threads/need-help-diagnosing-and-repairing-a-bms.69797)
- Basic N-channel functional check: short gate-source to discharge the gate; drain-source should read high/OL; charge the gate with the meter (red on gate, black on source), drain-source should now read low. Still high = open; near 0 ohm in both states = shorted. Diode check: about 0.2 V Schottky, 0.5-0.7 V silicon, OL reversed; near 0 both ways = shorted, open both ways = failed open. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- After pulling the FETs, the control logic can be tested separately to see whether the gates get the correct on/off signal; measuring gate voltage is the way to tell a stuck driver from a bad FET. [HOBBY] — [Endless Sphere (search excerpt)](https://endless-sphere.com/sphere/threads/need-help-diagnosing-and-repairing-a-bms.69797)
- Pack voltage present internally but not at output points to output fuse, contactor or MOSFET stage. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- Why a failed FET matters for safety: a faulty protection circuit can leave a battery that "functions normally but fails to provide protection". [REF] — [Battery University BU-304b](https://batteryuniversity.com/article/bu-304b-making-lithium-ion-safe)
- Protection FETs are placed back-to-back (often common-drain) so both charge and discharge paths can be blocked; they are controlled independently. [MFR/STD] — [TI, MOSFET selection for battery protection (SSZT769)](https://ti.com/lit/pdf/sszt769); [TI training deck SLYP856](https://www.ti.com/lit/ml/slyp856/slyp856.pdf)

**Balance / sense harness**
- Bridging two balance wires shorts a cell group and trips BMS short-circuit protection; reset by cycling the switch. [HOBBY] — [electric-skateboard.builders, Bestech thread](https://electric-skateboard.builders/t/bestech-no-throughput/55364)
- Detached sense wire causes apparent imbalance and BMS shutdown. [HOBBY/vendor] — [Letrigo](https://letrigo.com/blogs/knowledge/diagnose-faulty-ebike-bms)
- JK BMS self-measures "balance wire resistance"; when a line exceeds a limit it is shown in yellow and balancing is inhibited — a built-in indicator of wrong wiring or poor contact. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- Reversed/mis-ordered sampling wiring can damage the BMS. [MFR/STD via mirror] — [Daly manual mirror](https://manuals.plus/asin/B0B3TH6XRB)

**Single-cell protection IC (DW01A-class)**
- DW01A (Fortune): overcharge protection 4.25 / 4.30 / 4.35 V (min/typ/max); over-discharge protection 2.30 / 2.40 / 2.50 V. Another vendor variant: overcharge 4.28 V, release 4.08 V, over-discharge 2.40 V, release 3.00 V. Values vary by vendor (e.g. CJDW01A over-discharge 2.5 V +/-100 mV) — always check the exact part. [MFR/STD] — [DW01A datasheet (Fortune)](https://uelectronics.com/wp-content/uploads/2021/05/Datasheet-DW01A.pdf); [CJDW01A](https://en.sekorm.com/doc/2195926.html)

**Multi-cell AFE (TI BQ769x0 family)**
- BQ76940 (up to 15S) provides hardware protection for over-current in discharge, short circuit in discharge, over-voltage and under-voltage, with integrated cell-balancing FETs; OV threshold range roughly 3.15-4.7 V. [MFR/STD] — [TI BQ76940 product page](https://www.ti.com/product/bq76940); [TI BQ769x0 datasheet SLUSBK2](https://www.ti.com/document-viewer/lit/html/SLUSBK2I/GUID-346401A1-5122-46BE-B38B-21E8D4E37C00)

**Latched smart gauges (TI BQ40Z50-R5 — typical of laptop / OEM smart packs)**
- On any PFStatus bit: precharge, charge and discharge FETs are turned off; ChargingCurrent() and ChargingVoltage() are forced to 0; black-box and safety data are written to data flash; data flash writing is then disabled; the FUSE pin is driven to blow the chemical fuse if configured and pack voltage is above Min Blow Fuse Voltage or on CHG/DSG FET failure. [MFR/STD] — [TI BQ40Z50-R5 TRM SLUUCN4](https://www.ti.com/lit/pdf/SLUUCN4)
- PF causes implemented: safety cell under-voltage (SUV), safety cell over-voltage (SOV), over-current charge/discharge, over-temperature cell/FET, QMax imbalance, cell-balancing fail, impedance, capacity degradation, voltage imbalance at rest / active, charge FET fail, discharge FET fail, chemical fuse fail, AFE register / AFE communication fail, PTC, second-level protector, instruction-flash checksum, data-flash fail, open thermistor (TS1-TS4), cell over-voltage latch, manual PF. [MFR/STD] — [TI SLUUCN4](https://www.ti.com/lit/pdf/SLUUCN4)
- Clearing requires access level: device is SEALED in the field; unsealing needs a two-word key written to ManufacturerAccess() within 4 s (TI default 0x0414 then 0x3672 — OEMs change it); "Permanent Fail Data Reset" is MAC command 0x0029 and "Device Reset" is 0x0041, both documented as production-test aids. A sealed gauge returns to SEALED after power-on reset. [MFR/STD] — [TI SLUUCN4](https://www.ti.com/lit/pdf/SLUUCN4)
- TI's stated position is that unsealing in the field is not recommended; a user who could unseal a BQ40Z50-R5 via bqStudio still reported being unable to clear PF (no confirmed fix in the retrieved thread). [MFR forum] — [TI E2E: how to clear PF on BQ40Z50](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1499512/bq40z50-how-to-clear-permanent-failure-pf-on-bq40z50); [TI E2E: BQ40Z50-R2 sealed/unsealed after reset](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1185728/bq40z50-r2-seale-unseale-status-after-reset)
- Documented brick scenario: compound CUV and charge faults can leave a BQ40Z50-R2 pack unusable. [MFR forum] — [TI E2E bricked pack thread](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1476782/bq40z50-r2-bricked-pack-during-compound-cuv-and-chgc-faults)

**"Sleeping" (not failed) BMS**
- JK BMS has no power switch and uses charge activation: it needs a charger at least 4 V above pack voltage to start (e.g. 50 V pack -> min 54 V charger), and the B+ supply wire must be on pack positive with pack voltage above 40 V (below 36 V a 12->48 V / 24->48 V booster is required). Listed "cannot start" causes: B+ wire not connected, charger not >4 V above pack, charger has no output, configured series count does not match the actual pack. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- Daly: activate by activation button / key switch / Bluetooth-module button / app, or by connecting a charger; listed non-start causes are incorrect wiring, BMS not activated, low battery voltage. [MFR/STD via mirrors] — [Daly manual mirror 1](https://manuals.plus/asin/B0B3TH6XRB); [Daly manual mirror 2](https://manuals.plus/asin/B0B49Y8G5L)
- JK auto-shutdown voltage: BMS powers itself off when the highest cell falls below this value (must be set below cell UVP). [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)

### Inferences
- Symptom -> fault mapping for the decision tree (synthesis; items marked * are standard electronics reasoning not found verbatim in a source):
  - Discharges but will not charge (or vice versa) -> the corresponding FET bank is open/not driven, or BMS is in OVP/UVP/temperature inhibit. Check app status flags first on smart BMS (JK shows Charge MOS / Discharge MOS on/off).
  - Charges past OVP or discharges past UVP, output never turns off -> FET shorted drain-source*; pack is unprotected -> mandatory BMS replacement or FET bank replacement plus full cut-off verification.
  - Output present but current reading wrong / immediate over-current trip -> shunt damaged or current calibration lost* (JK manual: both B- and P- leads must be connected, and current is re-calibrated against a clamp meter).
  - One group persistently low while its neighbours are fine and the cells test healthy off-pack -> stuck-on balance (bleed) channel on that group*.
  - Temperature fault at ambient or "NA" -> open/shorted NTC or its connector (JK displays NA when no sensor present; TI gauges have an open-thermistor PF).
  - Smart pack reports 0 V / no SMBus charge request and has healthy cells -> PF latched; check for blown chemical fuse.
- Replace-whole-BMS criteria (synthesis): (a) FET shorted in a generic BMS where the cause (gate driver/IC) is unknown; (b) burn/carbonised PCB or electrolyte-corroded multilayer traces; (c) fixed-parameter "hardware" BMS whose thresholds cannot be verified; (d) OEM pack with latched PF where keys/firmware are unavailable (then either OEM board swap or conversion to a generic BMS with loss of CAN/UART handshake); (e) labour cost of component-level rework exceeds the price of a generic JK/JBD/Daly board. Component-level repair is justified mainly for proprietary boards that must retain OEM communication.

### Gaps
- Could not retrieve the Endless Sphere repair threads in full (bot protection), so step-level community procedures for gate-voltage values, shunt replacement and balance-resistor testing are not sourced.
- No sourced procedure for unlocking proprietary OEM packs (Bosch, Shimano, Specialized, power-tool makers, laptop OEM keys). Evidence found only shows that owners of locked OEM packs seek third-party options ([EMTB Forums thread](https://www.emtbforums.com/posts/706254/)); success rates and methods are unverified.
- No sourced data on relative frequency of each failure mode.
- Burnt shunt, failed balance resistor, corroded-trace repair (jumper wire) procedures: no primary source retrieved; IPC-7711/7721 is the governing rework standard but its text was not accessible.

---

## 3. PCB cleaning and rework (solvents, ultrasonic, drying, coating, soldering, MOSFET selection)

### Takeaway
Retrievable guidance supports: neutralise/remove residue -> high-purity IPA with soft ESD brush -> dry -> inspect/test -> recoat; ultrasonic cleaning of populated boards is contested and should be limited (>= 40 kHz, short exposure, avoid crystal/sensitive parts). Most of this is vendor/forum guidance — I could not access IPC texts, and I found no authoritative source specifically on neutralising Li-ion electrolyte (LiPF6/HF) residue on a BMS.

### Cited Findings
- Sequence commonly recommended for battery-leak corrosion: identify chemistry, neutralise, remove reacted residue, then clean with high-purity isopropyl alcohol (90 %+ ) and a soft ESD-safe brush, air dry. IPA is a cleaner, not a neutraliser. Sources conflict on neutraliser (baking soda vs diluted vinegar) because they mostly address alkaline/zinc-carbon leaks, not Li-ion electrolyte. [HOBBY/vendor] — [EEVblog forum: cleaning leaked batteries](https://www.eevblog.com/forum/beginners/electronics-cleaning-leaked-batteries/); [BestPCBs blog](https://www.bestpcbs.com/blog/2025/04/how-to-remove-battery-corrosion-from-electronics/?format=md)
- Use light pressure — excessive scrubbing lifts pads/traces; do not soak relays, microphones, displays, unsealed trimmers or parts of unknown wash compatibility; untreated corrosion keeps spreading along traces and through vias; corrosion already indicates damage that cleaning alone cannot fix — test electrically afterwards. [HOBBY/vendor] — [BestPCBs blog](https://www.bestpcbs.com/blog/2025/04/how-to-remove-battery-corrosion-from-electronics/?format=md)
- Ultrasonic: lower frequency = more aggressive cavitation; 40 kHz or higher with frequency sweep is the usual recommendation; keep exposure under about 10 minutes; kHz-range tuning-fork crystals (32.768 kHz) are at higher risk and ultrasonic cleaning is "not recommended" for them; one reading of J-STD-001D discourages ultrasonic cleaning of populated boards, while other experts say damage with modern equipment is rare. IPC-TM-650 2.6.9.1 is the test method for ultrasonic compatibility of components. [Industry expert Q&A / forum; standards quoted second-hand] — [Circuitnet expert panel](https://www.circuitnet.com/experts/52525.html); [DigiKey forum: ultrasonic cleaning with crystals](https://forum.digikey.com/t/ultrasonic-cleaning-of-pcb-s-with-crystals/8814); [IPC-TM-650 2.6.9.1](https://www.electronics.org/sites/default/files/test_methods_docs/2.6.9.1.pdf)
- Conformal coating families: acrylic, silicone, urethane, epoxy, parylene; IPC-CC-830 is the governing qualification spec (superseded MIL-I-46058). Thickness figures vary by source: acrylic 25-75 um, urethane 35-100 um, silicone 50-125 um (vendor guide); 30-130 um for acrylic/epoxy/urethane and 50-210 um for silicone (Wikipedia citing IPC); target 25-75 um dry for liquid coatings, above 100 um risks cracking and impaired heat dissipation (IPC-HDBK-830 as quoted second-hand). [Vendor/secondary] — [Wikipedia: Conformal coating](https://en.wikipedia.com/wiki/Conformal_film); [pcbandassembly.com coating guide](https://pcbandassembly.com/?p=8310)
- Rework/removal: acrylic is easiest to strip with solvent; silicone needs specific solvents or mechanical removal; urethane is significantly harder (solvent-resistant). IPC-7711/7721 defines coating-removal and rework procedures. [Vendor] — [Techspray guide to identification and removal of conformal coating](https://www.techspray.com/essential-guide-to-the-identification-and-removal-of-conformal-coating)
- MOSFET selection rules (design-side, usable as replacement rules): choose FETs able to carry max charge/discharge current; derate voltage — e.g. a 30 V abs-max VDS part is typically used to 24 V max; examples from TI designs: 25 V / 7.5 mOhm at VGS 3.5 V (single-cell protector), 30 V / 8.2 mOhm at 8 V gate drive (BQ40Z50 reference). Rds(on) must be specified at the gate voltage the BMS actually provides. Charge and discharge FETs may need different selection depending on series vs parallel configuration. [MFR/STD] — [TI SSZT769](https://ti.com/lit/pdf/sszt769); [TI BQ2970 datasheet](https://ti.com/document-viewer/BQ2971/datasheet/GUID-8ECA38E5-CD71-4A4A-A891-8EF764E1EA9B); [TI BQ769142 datasheet](https://www.tij.co.jp/document-viewer/jp/BQ769142/datasheet/GUID-F8F23D9C-AAA8-4958-8BD1-C3B9E7F9E2AD)
- JK BMS default FET thermal limits (fixed): MOS over-temperature protection 75 C, recovery 65 C. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)

### Inferences
- Replacement MOSFET rule set (derived from the TI derating guidance): same channel type and package/pinout; VDS rating such that max pack voltage <= about 80 % of abs-max VDS (so a 13S 54.6 V pack needs >= 68 V, i.e. an 80 V or 100 V class part; a 20S 84 V pack needs >= 105 V, i.e. 120-150 V class); Rds(on) equal or lower at the board's actual gate drive; equal or higher continuous/pulse current and SOA; replace ALL paralleled FETs in a bank with the same part/lot so current shares evenly, and replace gate resistor/zener if the old FET failed gate-shorted. The 80 % figure is TI's example; the pack arithmetic and the "replace the whole bank" rule are my extrapolation / common practice, not sourced.
- Because sources for battery-leak neutralisers concern alkaline cells, they should not be transferred uncritically to Li-ion electrolyte residue. A defensible SOP wording: remove residue mechanically, flush with IPA (and DI water if salts are present), dry fully, inspect under magnification, and scrap the board if copper under the mask is undercut.

### Gaps
- IPC-CH-65 (cleaning guidelines) and IPC-7711/7721 text not accessed — no direct quotations possible; all IPC references above are second-hand.
- No source retrieved for: recommended DI-water rinse practice, bake/dry temperature and time after wet cleaning, flux-remover product selection, or soldering iron/hot-air temperature settings for leaded vs lead-free rework on high-copper BMS boards. These should be filled from IPC J-STD-001 / solder-alloy and component datasheets before being written into the SOP.
- No authoritative source found on safe neutralisation of Li-ion electrolyte (LiPF6 hydrolysis -> HF) contamination on PCBs, nor PPE specifics; check cell manufacturer SDS (e.g. [Samsung 35E SDS](https://www.18650batterystore.com/cdn/shop/files/Samsung-35E-18650-SDS.pdf), not read).
- No sourced guidance on which conformal coating BMS manufacturers actually apply, or on re-coating after repair.

---

## 4. BMS disconnection/connection sequence, balance-lead verification, activation, smart-BMS configuration

### Takeaway
Manufacturer manuals agree on the principle: main negative (B-) first, sense harness wired to the cells and verified with a multimeter while UNPLUGGED from the BMS, then plug the harness in, then activate and confirm B+/B- equals P+/P-. Removal is the reverse (harness out first). Parameter values must come from the cell datasheet; JK publishes the clearest parameter semantics, while JBD/Daly/ANT defaults vary by model and could not be verified.

### Cited Findings
- Daly sequence: connect main B- wire from pack total negative to the BMS B- terminal; wire and verify all sampling wires on the pack; only then insert the sampling connector into the BMS. "Do not insert the BMS connector until all balance wires are properly connected and verified." [MFR/STD via manual mirrors] — [Daly smart active balance BMS manual mirror](https://manuals.plus/ae/1005010148694914); [Daly manual mirror](https://manuals.plus/asin/B0B3TG2ZL4)
- Daly harness order: start at B0 (negative of first cell) and proceed in sequence up the stack; verify by measuring voltage between adjacent wires — each should be one cell voltage and consistent. [MFR/STD via mirror] — [Daly manual mirror](https://manuals.plus/asin/B0B3TH6XRB)
- JK sequence and check: "Connect from the negative pole to the positive pole. After the equalization line is connected, use a multimeter to confirm again, and then insert the BMS after confirming that it is correct." Pin 1 = B- (pack negative), then B1 = cell 1 +, B2 = cell 2 + ... ; the last wire B+ (BMS power) must go to pack positive. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- JK listing check: voltage between adjacent balance wires should be a single-cell value, with differences between strings less than 1 V. [MFR listing mirror] — [JK BD6A24S manual mirror](https://manuals.plus/ae/1005010296649319)
- Disconnect order: balance connector first, then main terminals. [HOBBY; not found in a Daly/JK manual] — [Endless Sphere, help replacing BMS (search excerpt)](https://endless-sphere.com/sphere/threads/help-replacing-bms.130330/)
- JK prohibits modifying the BMS power leads (causes uneven current sharing and burns the BMS); both B- leads and both P- leads must be connected in parallel or current measurement is wrong. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- JK activation: charger >= 4 V above pack voltage; then app connect (default connection password "1234", parameter-change password "123456"); then set battery type (one-key LFP / one-key ternary presets), exact cell count (BMS will not work properly if wrong) and capacity. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- JK parameter semantics: cell UVP turns off discharge MOS until all cells exceed UVP-recovery; cell OVP turns off charge MOS until all cells fall below OVP-recovery; OVP/UVP adjustable 1.2-4.35 V; charge/discharge over-current with delay and auto-release times (2-120 s); max balance current must not exceed 0.1C (20 Ah -> 2 A); voltage calibration = enter multimeter-measured total voltage; current calibration = enter clamp-meter current (larger current = better accuracy); SOC/capacity only becomes accurate after a full discharge-to-cut-off then uninterrupted full charge. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- JK LFP example settings in circulation: cell OVP 3.65 V, OVP recovery 3.4 V, UVP 2.6 V, balance trigger 0.01 V (Gobel 314 Ah sheet); wiki example OVP 3.620 V, UVP 2.800 V, start-balance 3.45 V, trigger 0.010 V, balance current 1-2 A. Balancer only runs when highest cell is above start-balance voltage AND delta exceeds trigger. [Vendor sheet / community wiki] — [Gobel Power JK settings 314Ah](https://gobelpower.com/download/files/JKBMS-Settings-314Ah.pdf); [Akkudoktor JK inverter-BMS wiki](https://akkudoktor.net/t/wiki-jk-inverter-bms-dokumentation-der-einstellungen-ab-fw-xx-35/30073)
- Setting OVP recovery too close to OVP causes charge-control oscillation/alarms with inverter-chargers. [HOBBY] — [Victron community thread](https://community.victronenergy.com/t/multiplus-forcing-jk-bms-into-high-voltage-alarm-while-jk-bms-in-controll/35178.md?page=2)
- JBD: hardware-type boards have thresholds fixed by components (example 16-20S NMC board: OVP 4.250 V typ, UVP 2.800 V typ); software boards are adjustable via PC tool/app and shipped defaults vary and may not suit the pack. Community-reported Xiaoxiang app default balance threshold 30 mV. [MFR datasheets + HOBBY] — [JBD TP20S001 datasheet](https://robu.in/wp-content/uploads/2024/05/JBD-TP20S001-NMC-Series-（17S-NMC-40A.pdf); [esk8.news Xiaoxiang app help](https://forum.esk8.news/t/smart-bms-xiaoxiang-app-help/59458)
- Temperature limits to configure against: Li-ion fast charge 5-45 C, reduce current below 5 C, no charging below freezing. [REF] — [Battery University BU-410](https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures)

### Inferences
- SOP sequence for BMS swap (synthesis of the manuals):
  REMOVE: disconnect charger/load -> unplug balance connector(s) -> disconnect P-/C- -> disconnect B- last (insulate every freed lead).
  INSTALL: (1) confirm BMS chemistry/series count/current rating; (2) solder/bolt B- to pack negative; (3) with harness unplugged from BMS, meter every pin: pin-to-B- voltage must step up by one cell voltage per pin (about 3.2-3.4 V LFP, 3.0-4.2 V NMC) and top pin must equal pack voltage; no reversed/duplicated/zero steps; (4) plug harness lowest connector first on multi-connector boards; (5) connect P-/C-; (6) activate (charger/button); (7) confirm P+/P- equals B+/B-; (8) on smart BMS set type, cell count, capacity, OVP/UVP/recoveries, currents, temperatures, balance settings, then calibrate voltage and current.
  The removal order (harness first) is hobbyist-sourced and logically mirrors the manufacturers' install order; "lowest connector first" is my assumption.
- Suggested parameter starting points must be tied to the cell datasheet: OVP at or slightly below the cell's max charge voltage (4.20-4.25 V NMC; 3.60-3.65 V LFP), UVP at or above the datasheet cut-off (2.5-2.8 V), per the Samsung/EVE/Battery University figures cited in section 1.

### Gaps
- Daly's official PDFs could not be fetched (file size); Daly content is from manuals.plus mirrors of model-specific manuals — verify against the manual of the exact board.
- No official Daly or JBD default-parameter tables retrieved; no ANT BMS documentation retrieved at all (activation method, app password, parameter names are unverified).
- No manufacturer statement found on removal order or on which connector to plug first on multi-plug harnesses.
- JK appendix tables of default LFP / ternary values (Appendix 1/2 of the manual) were referenced but not legible in the extracted text.

---

## 5. Cell-level work: matching, spot welding, nickel sizing, no-solder rule, over-discharge recovery, balancing

### Takeaway
Match on capacity (industrial tolerance +/-2.5 %), IR (AC 1 kHz) and voltage before paralleling; join by spot welding with energy tuned on scrap cells and proven by a destructive pull test; recover over-discharged cells only above about 1.5 V with a current-limited pre-charge and discard if voltage does not rise promptly. Spot-weld settings and nickel ampacity are hobbyist-sourced and machine-specific.

### Cited Findings
- Matching: capacity tolerance +/-2.5 % between cells for industrial batteries, tighter for high-voltage/high-load packs. Typical second-life spread reported: 5-15 % capacity and 20-80 % IR variance. [REF; HOBBY/vendor] — [Battery University BU-803a](https://batteryuniversity.com/article/bu-803a-cell-matching-and-balancing); [Industrial Monitor Direct](https://industrialmonitordirect.com/no/blogs/knowledgebase/capacity-matching-18650-cells-in-excel-a-field-engineers)
- Before paralleling LFP cells: if cells differ by more than about 0.15 V, bring the lower ones up first. [HOBBY] — [DIY Solar Forum top-balance tutorial](https://www.diysolarforum.com/resources/top-balancing-lifepo4-cells-using-a-low-cost-benchtop-power-supply.65/)
- No soldering on cells: Samsung ICR18650-26A spec says "Don't solder on the battery directly"; LG INR18650-M29 spec lists "Do not solder". [MFR/STD, via Scribd/SlideShare copies in search snippets] — [Samsung ICR18650-26A (Scribd copy)](https://www.scribd.com/document/626051128/ICR18650-26A-Samsung); [LG INR18650 M29 (SlideShare copy)](https://www.slideshare.net/plsbattery/lg-inr18650m29)
- Nickel strip: 0.1 or 0.15 mm pure nickel, 8-10 mm wide is the common choice for 18650 packs; an entry-level welder manual limits pure nickel to 0.05-0.15 mm (0.2 mm only for nickel-plated steel); pure nickel (Ni200/Ni201) gives best weld quality and lowest contact resistance. [Vendor/HOBBY] — [18650BatteryStore nickel strip](https://18650batterystore.com/products/3p-pure-nickel-strip-1kg-roll-for-battery-spot-welding-18650-21700); [Sunkko 737G manual](https://manuals.online/sunkko/welding-system/737g/user-manual/1lcvl); [Think Robotics guide](https://thinkrobotics.com/es/blogs/learn/diy-spot-welder-for-18650-batteries-complete-build-guide-for-perfect-battery-packs)
- Spot-weld energy (kWeld, user reports): 0.15 mm pure nickel about 25-30 J; 0.2 mm pure nickel reports range 20-35 J up to 50-60 J (one user: 50-55 J on negative end, 35-45 J on positive end); guide values 0.1 mm = 20 J, 0.2 mm = 50 J. Principle: lowest energy that forms a solid weld. [HOBBY] — [foil.zone kWeld settings thread](https://foil.zone/t/kweld-welder-setting-for-different-cell-types/19248); [The Makers Chest spot-welding guide](https://themakerschest.com/blogs/spot-welding-hub/how-to-spot-weld-battery-tabs-settings-technique-and-common-mistakes)
- Weld pass criterion: on a pull test the strip should tear, leaving weld nuggets on the can, before the bond releases; start low on scrap cells and raise energy until pull tests pass; a weld that holds mechanically can still have high contact resistance and run hot. [HOBBY] — [The Makers Chest](https://themakerschest.com/blogs/spot-welding-hub/how-to-spot-weld-battery-tabs-settings-technique-and-common-mistakes); [esk8.news "How strong should welds be?"](https://forum.esk8.news/t/how-strong-should-welds-be/76953)
- Over-discharge recovery: apply small "boost" current to wake the protection circuit; proceed to normal charge only if voltage reaches a correct level; discard if it does not rise to normal within a minute; never boost cells that sat below 1.5 V for a week or more; verify polarity first (a sleeping pack shows no voltage, and reverse voltage causes permanent damage). Field data (Cadex, 294 phone batteries): 30 % needed boost, 91 % restored to >= 80 % capacity, 9 % unserviceable. [REF] — [Battery University BU-808a](https://batteryuniversity.com/article/bu-808a-how-to-awaken-a-sleeping-li-ion)
- Manufacturer pre-charge window: 1.0-3.0 V cell voltage at 0.1C-0.5C (Samsung 29E / 30Q). [MFR via Scribd snippets — verify] — [Samsung INR18650-29E (Scribd copy)](https://www.scribd.com/document/676224823/ACCU-INR18650-29E)
- Cells stressed by deep discharge show higher self-discharge afterwards. [REF] — [Battery University BU-802b](https://batteryuniversity.com/article/bu-802b-what-does-elevated-self-discharge-do)
- LFP top-balance procedure (DIY Solar Forum tutorial, hobbyist but de-facto reference): (a) optional series pre-charge with BMS set to cut at 3.65 V/cell (or 3.6 V), supply at <= 0.2C, pack target 14.6 / 29.2 / 58.4 V for 4S/8S/16S; (b) wire all cells in parallel; (c) set bench supply to 3.65 V and <= 0.2C of combined Ah BEFORE connecting; connect diagonally across the parallel bank; (d) do not raise the voltage to speed things up; cells rise quickly after about 3.5 V; verify supply voltage with a multimeter (cheap supplies drift about 0.02 V); (e) hold until current is zero or near zero; (f) disconnect — do not leave cells at 3.65 V for days; do not leave unattended at 3.65 V (drop to 3.55-3.6 V if unattended). Do not top-balance below 3.5 V. [HOBBY] — [DIY Solar Forum tutorial](https://www.diysolarforum.com/resources/top-balancing-lifepo4-cells-using-a-low-cost-benchtop-power-supply.65/); [PDF copy](http://akkudoktor.net/uploads/short-url/vOC45OkdCtbnpmlWX6HgypZRQRG.pdf)
- Counter-view: merely wiring cells in parallel does not by itself balance them (flat LFP curve) — they must be driven to the top knee. [HOBBY] — [Panbo DIY LiFePO4 article](https://panbo.com/building-a-diy-lifepo4-battery/)
- Balancing methods: passive bleeds high cells through a resistor during charge; active transfers charge from high to low cells. JK active balancers move 0.6-2 A depending on model. [REF; MFR/STD] — [Battery University BU-803a](https://batteryuniversity.com/article/bu-803a-cell-matching-and-balancing); [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)

### Inferences
- Recovery decision rule for the SOP: V < 1.5 V (or unknown dwell, swelling, heat, reversed polarity) -> scrap. 1.5 V <= V < cut-off -> pre-charge at about 0.1C (lower end of Samsung's window; conservative) with voltage clamp and temperature monitoring until 3.0 V, then normal CC/CV; abort if no rise within about 1 minute (BU) or if the cell warms; afterwards require capacity, IR and a multi-day self-discharge hold before reuse. Recovering an individual group inside a pack means charging that group directly through its balance taps with a current-limited single-cell supply — this is common bench practice but I found no primary source describing it.
- When replacing a group in an aged pack, new cells should be matched to the measured capacity/IR of the remaining groups, not to the nameplate, otherwise the BU-803a mismatch effect reappears (inference from the 12 % mismatch result).

### Gaps
- No authoritative nickel-strip ampacity table (A per mm^2 or per strip size) was retrieved; forum tables exist on Endless Sphere but were inaccessible. Do not publish current ratings without a source.
- Spot-weld parameters for non-kWeld machines (pulse ms, dual-pulse settings, electrode force) not sourced; copper/nickel sandwich methods not researched.
- The 35E datasheet copy retrieved did not include the pack-design/handling annex; Samsung/LG soldering prohibitions and pre-charge figures rest on search snippets of third-party-hosted copies.
- No sourced maximum allowable voltage difference (in mV) for paralleling NMC cylindrical cells.

---

## 6. Post-repair QC protocol, acceptance criteria and records

### Takeaway
No public standard prescribes a repair-shop end-of-line test; a defensible protocol can be assembled from manufacturer BMS functions (OVP/UVP/OCP behaviour, calibration), cell datasheet test conditions (standard charge/discharge definitions) and the test categories used in production EOL (insulation, capacity, protection). Numeric acceptance limits therefore have to be set by the workshop from the cell/BMS datasheets.

### Cited Findings
- Functional expectations to verify: at cell OVP the BMS turns off the charge MOS and only re-enables after all cells fall below the recovery value; at cell UVP it turns off the discharge MOS and only re-enables after all cells exceed UVP recovery; over-current trips after the configured delay and auto-releases after the release time; MOS over-temperature cut at 75 C / recover 65 C (JK). [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- Post-activation check: B+/B- voltage equals P+/P- voltage. [MFR/STD via mirror] — [Daly manual mirror](https://manuals.plus/asin/B0B3TH6XRB)
- Capacity test reference conditions (cell maker definition): standard charge CC/CV to 4.2 V with 0.02C cut-off at 23 C; standard discharge at 0.2C to cut-off (2.65 V for 35E), measured within 1 h of charge; rated capacity at 1C must be >= 97 % of standard capacity for that cell. [MFR/STD] — [Samsung INR18650-35E specification](https://cdn.shopify.com/s/files/1/0613/3327/4870/files/35eDatasheet.pdf)
- BMS capacity/SOC gauge only becomes valid after a complete discharge to cut-off followed by an uninterrupted full charge. [MFR/STD] — [JK Smart BMS manual](https://cdn.shopify.com/s/files/1/0559/0830/2937/files/JK_BMS_Active-Bluetooth-BMS-Manual.pdf)
- End-of-charge balance criterion (LFP): cells within 50 mV at the end of charge = acceptable; > 150 mV = rebalance. [HOBBY] — [DIY Solar Forum tutorial](https://www.diysolarforum.com/resources/top-balancing-lifepo4-cells-using-a-low-cost-benchtop-power-supply.65/)
- Service-ability benchmark: Cadex counts a battery as restored at >= 80 % capacity; second-life acceptance gate suggested at SOH >= 80 %. [REF; HOBBY/vendor] — [Battery University BU-808a](https://batteryuniversity.com/article/bu-808a-how-to-awaken-a-sleeping-li-ion); [Industrial Monitor Direct](https://industrialmonitordirect.com/no/blogs/knowledgebase/capacity-matching-18650-cells-in-excel-a-field-engineers)
- Insulation: an IEC 62133-2 test report lists a requirement of insulation resistance >= 5 MOhm between positive terminal and externally exposed metal surfaces (type-test criterion, applies where exposed metal exists). [STD as quoted in a third-party test report] — [IEC 62133-2 test report (RS-hosted)](https://docs.rs-online.com/21d2/A700000014536126.pdf)
- Production EOL systems test insulation resistance, dielectric strength and capacity among other items; EN 50604-1 is the safety standard for LEV (e-bike) lithium batteries, IEC 62619 for industrial/stationary. [Vendor] — [HORIBA EOL battery tester](https://horiba.com/usa/products/detail/action/show/Product/x-hvt-6503); [Inventus Power standards overview](https://inventuspower.com/?p=3864)
- Thermal sanity: a cell that becomes very warm on charge is suspect and should be rejected. [HOBBY] — [Instructables](https://www.instructables.com/Re-using-Lithium-Ion-Cells-From-Laptop-Batteries)
- Charge temperature window for the test bench: 5-45 C for fast charge; no charging below freezing. [REF] — [Battery University BU-410](https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures)

### Inferences
- Proposed QC sequence with pass/fail (synthesis; limits marked "house" are not sourced and must be set by the workshop):
  1. Visual/mechanical: insulation (fish paper, heat-shrink), strain relief, no loose hardware. Pass = no exposed conductors.
  2. Static: B+/B- = P+/P- after activation (Daly); all groups within window; record each group voltage and delta.
  3. Insulation: >= 5 MOhm pack terminal to any exposed metal case (IEC 62133-2 type-test figure used as a floor).
  4. Charge test with the customer's charger: charger CV = N x 4.20 V (NMC) or N x 3.65 V (LFP) +/-50 mV/cell (BU-409 tolerance); charge terminates; end-of-charge delta <= 50 mV (LFP hobbyist figure; house limit for NMC).
  5. OVP verification: raise OVP-trigger condition (on smart BMS, temporarily lower OVP setting below present cell voltage, or continue charge on a bench supply) -> charge MOS must open; restore setting. UVP verification likewise (raise UVP setting above present voltage or discharge to cut-off) -> discharge MOS must open and recover only above the recovery threshold. Using the settings trick avoids actually over-stressing cells — bench practice, not sourced.
  6. Load/capacity: discharge at 0.2C (datasheet-standard) or the application current to BMS cut-off; pass = >= 80 % of nominal (house, anchored to the Cadex 80 % service criterion) and no group collapsing early; record Ah/Wh and lowest-group identity.
  7. Thermal: IR camera/thermocouples during load — FETs must remain below the BMS over-temperature threshold (75 C on JK); welds/busbars with no hot spots relative to neighbours (house).
  8. Over-current/short-circuit function: verify trip using an electronic load above the OCP setting (do not dead-short); record trip current and delay.
  9. Rest/self-discharge hold: record group voltages after 24 h and again after a longer hold where possible; any group drifting relative to the others = fail (house; thresholds unsourced).
  10. Records: pack ID, chemistry, S/P config, incoming fault and voltages, parts replaced (BMS model/firmware, FET part numbers, cell batch), BMS parameter set (export/screenshot), per-group voltages before/after, IR per group, capacity result, cut-off test results, max temperatures, insulation value, technician/date.

### Gaps
- EN 50604-1, IEC 62133-2, IEC 62619 and UL 2271/2849 texts were not accessed; no end-of-line or post-repair acceptance criteria could be quoted from them. The 5 MOhm figure comes from a single third-party test report.
- No published repair-industry QC protocol (trade association or training body) was found within the search budget.
- No sourced numeric criteria for post-repair delta at rest, temperature rise limits on welds/busbars, or self-discharge hold duration.
- Regulatory status of third-party pack repair as of 2026 (e.g. EU Battery Regulation repairability provisions, national rules on e-bike battery repair, insurer/OEM positions) was not researched here and may constrain what a workshop is allowed to do.
