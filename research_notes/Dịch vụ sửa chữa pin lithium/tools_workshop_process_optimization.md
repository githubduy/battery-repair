# Tools, Workshop Layout and Process Optimisation for a Lithium Battery Pack Repair Workshop (as of Nov 2026)

Scope: independent workshop, 1–10 technicians, packs ~12–72 V. Prices are snapshots from reseller listings found on 2026-11-13; listing dates are given where the source states one. Many price sources are marketplace aggregators, so treat them as indicative ranges, not quotes. Items under "Inferences" are the researcher's reasoning or general trade knowledge and are NOT sourced; items under "Cited Findings" are sourced.

## 1. Equipment by tier (starter / professional / high-volume): models, specs, price ranges

### Takeaway
A credible starter bench (4-wire AC IR meter, single-channel cell tester, capacitor-discharge spot welder, active balancer) can be assembled from tools individually priced at roughly USD 50–350 each (about 1–2 million VND each for the IR meter, EBC-A20 and NEEY balancer in Vietnam). The step to "professional" is mainly a pack-level equalizer/analyzer, multi-channel grading and a higher-current welder; "high-volume" adds 8+ channel grading cabinets (USD 400–4,500) and optionally a laser welder (USD ~3,900–15,000) or a Hioki-class tester (USD ~3,200–3,500).

### Cited Findings

**AC internal resistance (IR) testers**
- YR1035+ is a true four-wire 1 kHz AC meter; listings give 0–100 V voltage range, resistance up to 200 Ω, max resolution 0.00001 Ω (10 µΩ), stated accuracy 0.7% + 7 digits on the lowest range — [Fruugo listing](https://www.fruugo.ca/yr1035-4-wire-lithiumbattery-internal-resistance-testerb/p-412731860); [BDTronics](https://bdtronics.com/yr1035-battery-internal-resistance-test-instrument.html)
- Independent bench review (HKJ / lygte-info) compared the YR1035 against a Keithley DMM7510 and rated precision "very good"; ranges 20 mΩ / 200 mΩ / 2 Ω / 20 Ω / 200 Ω + auto, volts 1/10/100 V + auto; ohm display 2200 counts, voltmeter 100,000 counts; test signal 1 kHz sine up to ~100 mV rms. Limitations: Chinese-only menus on the reviewed unit, Zero function unreliable, supplied Kelvin clamps "cheap" (the battery-holder fixture gives stable contact), reads high on inductive parts — [lygte-info.dk review](https://lygte-info.dk/review/InternalResistanceMeterYR1035%20UK.html)
- YR1035+ international prices: ~USD 50 (ended eBay kit listing with Kelvin clips), USD 69.98 (reach.dog, "new version"), 74–104 + shipping on Fruugo Canada (currency on that site is likely CAD), USD 143.83 at Walmart — [eBay](https://www.ebay.com/itm/354570291870); [reach.dog](https://reach.dog/shop/cneel-battery-official-store/products/yr1035-tester); [Fruugo CA](https://www.fruugo.ca/yr1035-4-wire-digital-lithium-battery-internal-resistance-tester-w-probes/p-388787425); [Walmart](https://www.walmart.com/ip/11997023404)
- YR1035+ Vietnam prices: ~950,000 VND (Shopee / component shops; a Tiki listing at 949,000 VND, out of stock), 1,150,000 VND with probe set (suapinlaptop.vn), 1,750,000 VND incl. VAT (Thiết Bị SOLACO). An English-language-menu version is sold on Shopee VN. Listing dates are not uniform (one price-comparison page is dated 7/2022) — [Shopee VN](https://shopee.vn/amp/M%C3%A1y-%C4%91o-n%E1%BB%99i-tr%E1%BB%9F-YR1035-ch%C3%ADnh-h%C3%A3ng-phi%C3%AAn-b%E1%BA%A3n-Ti%E1%BA%BFng-Anh-full-box-HP-Battery--i.152801994.7141338428); [Tiki](https://tiki.vn/may-do-chat-luong-pin-ac-quy-yr1035-nguon-0-100v-kiem-tra-dong-xa-pin-ac-quy-chinh-xac-99-9-p56629175.html?spid=56629176); [suapinlaptop.vn](https://suapinlaptop.vn/vi/may-do-noi-tro-yr1035-yr1035-do-pin-va-binh-ac-qui-100v-do-chinh-xac-cao); [SOLACO](https://thietbisolaco.com/products/may-do-noi-tro-yr1035); [sosanhgia 7/2022](https://www.sosanhgia.com/p272226-may-do-noi-tro-yr1035.html)
- Hioki BT3554-50: resistance 3 mΩ range (1 µΩ resolution) to 3 Ω, 4 ranges; accuracy ±0.8% rdg ±6 dgt (3 mΩ range ±1.0% rdg ±8 dgt); battery voltage 6–60 V; ~2 s per battery; Bluetooth via adapter; base -50 unit ships without test leads — [Hioki product page](https://www.hioki.com/us-en/products/resistance-meters/battery/id_6828); [ITM](https://www.itm.com/product/hioki-bt3554-50-battery-tester)
- Hioki BT3554-50 prices: USD 3,160 (TEquipment, no leads/adapter), USD 3,484 (Octopart), GBP 2,008 ex VAT (Farnell UK), EUR 2,128 (TestEquity DE), EUR 2,390 ex VAT (Farnell IE), MYR 14,000 (Techno Malaysia) — [TEquipment](https://tequipment.net/hioki/series_bt3554); [Octopart](https://octopart.com/part/hioki/BT3554-50); [Farnell UK](https://uk.farnell.com/hioki/bt3554-50/batt-tester-portable-6v-to-60v/dp/4666942); [TestEquity DE](https://www.testequity.de/en/products/hioki-bt3554-50-70048751); [Farnell IE](https://ie.farnell.com/hioki/bt3554-50/batt-tester-portable-6v-to-60v/dp/4666942); [Techno MY](https://techno.my/products/hioki-battery-tester-bt3554-50-bt3554-51)

**Cell capacity testers / graders**
- ZKETECH EBC-A40L: 0–5 V, 0.1–40 A charge and discharge, 200 W max discharge, ~5.4 kg, fan cooled, PC connection for logging/graphing, 110/220 V input — [manufacturer manual](https://manuals.plus/m/0b296ded22b67da3b08a20731a03a64dadc2f93d5c2ad49bd4006bf76943913a); [eBay listing](https://www.ebay.com/itm/397331014243); [Solartech](https://solartech.eu/en/?p=11022)
- EBC-A40L prices: USD 196 (Docan Power, out of stock; eBay 196.06); USD 339.50–350.99 (Best Buy marketplace); outliers USD 624–761 (Fruugo, Newegg) — [Docan Power](https://www.docanpower.com/ebc-a40l-battery-tester); [eBay](https://www.ebay.com/itm/397431022500); [Best Buy](https://www.bestbuy.com/product/stock-preferred-ebc-a40l-high-current-lithium-battery-capacity-tester-blue/J45HSKJPCJ); [Newegg](https://www.newegg.ca/p/2VH-024H-00PS5)
- EBC-A20 in Vietnam: ~1,523,000–1,650,000 VND across multiple sellers (BigGo price aggregator snapshot, April 2024) — [BigGo VN](https://vn.biggo.com/s/EBC+A20/)
- 8-channel 5 V 6 A cell charge/discharge capacity grading machine: USD 400–450, MOQ 1 set (Xiamen Acey); 8-channel grading + cycle-aging tester USD 500–1,000 (Shenzhen Jinyuan); an Indian reseller lists an 8-channel 5 V 6 A cabinet at INR 55,000 with 8 independent channels and optional RS485/USB/LAN — [Accio aggregator](https://www.accio.ai/find-product/lithium-cell-grading-machine-price); [aajjo India](https://www.aajjo.com/product/8-battery-cell-capacity-cabinet-5v-6a-skxd-08-5v6a-b473-in-okhla-arbaccessories)
- High-channel option: Dekang DT50W-128 (128 channels) listed at USD 4,467.56, MOQ 1 — [Accio aggregator](https://www.accio.ai/find-product/battery-grading-machine)
- A 512-channel ACEY-CT503-512H appears on the used market (Germany) — [Machineseeker](https://www.machineseeker-india.com/acey-acey-ct503-512h/i-22431417)

**Pack-level equalizers / active balancers / analyzers**
- Heltec HTB-J24S10AC / HTB-J24S15AC "equalizer analyzer": 2–24S (charge mode 10–24S), 10 A or 15 A max balance current (15 A recommended above 100 Ah), charge and discharge balancing (pulse or continuous discharge), ±1 mV voltage accuracy, 5-inch touch screen, per-cell voltage / delta / SOC display, Li-ion / LiFePO4 / LTO; price on request. Vendor claims +10–15% usable capacity and ~20% longer cycle life after balancing, with no methodology given — [Heltec news page](https://www.heltec-energy.com/news/new-product-online-10a15a-lithium-battery-pack-equalizer-analyzer)
- Heltec also lists 2–24S 3 A/4 A and 7 A automatic equalizers (HTB-J24S07A, 1-year warranty), a 2–32S 15/20/25 A model (HTB-J32S25A), and a BMS tester in 1–10S/16S/20S/24S/32S variants — [Heltec 3A/4A equalizer](https://heltec-energy.com/battery-repairer-2-24s-3a-4a-lithium-battery-automatic-equalizer-product); [Heltec HTB-J32S25A](https://www.heltec-energy.com/battery-repairer-htb-j32s25a-2-32s-15a-20a-25a-lithium-battery-automatic-equalizer-product); [Heltec maintenance & test catalogue](https://heltec-energy.com/battery-maintenance-and-test/page/2)
- Heltec Alibaba storefront: "whole-group" pack capacity tester with 20 A charge / 40 A discharge at USD 640–680; a 9–99 V charge/discharge tester at USD 320–680 — [Heltec Alibaba storefront](https://heltecbms.en.alibaba.com/en_US/company_profile.html)
- Third-party prices for Heltec 2–24S 7–8 A balancers are inconsistent (USD 342.80 at one reseller; USD 1,249 at Fruugo) — [Systep](https://systep.cl/products/heltec-lithium-battery-intelligent-automatic-equaliser-2s-24/218473516/); [Fruugo](https://www.fruugo.ca/2-24s-8a-active-equalizer-balancer-with-voltage-measuring-lifepo4-lithium-lipo-for-battery-equalizer-repair-instrument-ht-bv24a8/p-229850332)
- NEEY 4 A smart active balancer (4S–24S, Bluetooth, LiFePO4/Li-ion/LTO) in Vietnam: 1,750,000 VND (down from 2,000,000) — [Linh Kiện Quốc Thái](https://linhkienquocthai.com/mach-can-bang-pin-neey-4a-thong-minh-4s-5s-6s-7s-8s-14s-16s-21s-22s-24s-pin-lifepo-4-lipo-lto-pin)

**Spot welders**
- kWeld (keenlab): energy-regulated pulses (set in Ws = joules), ~1200 A with one kCap module, design target ~1500 A, overcurrent trip 2000 A, welds up to ~0.3 mm nickel / nickel-plated steel. Complete kit EUR 169–177 ex 19% VAT and shipping; includes electronics module with LCD, cables, electrode holders, electrodes, 300 A ANL fuse, foot switch (2 m), bus bars. NOT included: power source (3S LiPo 5000–6000 mAh ~1300–1600 A, car/AGM battery ~1400–1700 A, or kCap ultracap module), XT150 input connector, enclosure — [keenlab kWeld complete kit](https://www.keenlab.de/index.php/product/kweld-complete-kit/)
- kWeld: a supercap bank delivering >2000 A triggers the overcurrent cutoff; the positive electrode is always live; magnetic fields make it unsuitable for people with pacemakers — [keenlab](https://www.keenlab.de/index.php/product/kweld-complete-kit/)
- Glitter 811A: capacitor-discharge, 36 kW / 6000 A peak, marketed for 18650/21700/26650/32650 packs, listing title claims 0.3 mm copper; USD 339–345 (reseller aggregator). A Ukrainian retailer lists the 811A (36 kW, selectable 22.8/27/30/36 kW) at UAH 23,100 — [china.org.ru listing](https://china.org.ru/product/1600737528037); [flasharmy.com.ua](https://flasharmy.com.ua/en/aparat-tochkovogo-zvaryuvannya-akumulyatoriv-glitter-811a-36kvt-eu-plug)
- Glitter 811H (36/42 kW): marketed for 0.3 mm pure nickel and aluminium-to-copper/nickel on LiFePO4 cells; USD 650–668 on eBay — [china.org.ru 811H](https://china.org.ru/product/1600975314015); [eBay](https://www.ebay.com/itm/405366156919); [eBay DE](https://www.ebay.de/itm/135063906613)
- Glitter 812A: USD 329, "2-in-1" capacitor welder, max output ~15 kW (review-site figure) — [pulserevops review](https://pulserevops.com/electronic-reviews/er567)
- Glitter 801H: plug-in capacitor unit (listed 19.8–21 kW); a user reports good results on a 21700 pack with 0.2 mm pure nickel — [desertcart listing](https://www.desertcart.lk/products/483929515-glitter-801h-battery-spot-welder-21-kw-capacitor-energy-storage)
- Sunkko 737G+ (transformer type, 4.3 kW): USD 162.80–185.87 on B2B sites; sold by Elektor in Europe; plain 737G is 1.5 kW; a "801D"-class unit listed at USD 149 — [Accio](https://www.accio.ai/find-product/sunkko-737g-battery-spot-welder); [Elektor](https://elektor.com/products/sunkko-737g-spot-welding-machine-4-3-kw); [Besomi 737G 1.5 kW](https://besomi.com/jo_en/bcbg0005-sunkko-s737g-battery-spot-welding-machine-1-5kw.html)
- Vietnam: a generic (non-Sunkko) 18650 spot welder on Lazada at 1,757,000 VND — [Lazada VN](https://www.lazada.vn/trending/Welding-Tools-Top-AddToCart/1338391786)

**Laser welders**
- 1500 W handheld fiber laser welders: USD 3,888 (marketplace 3-in-1), USD 6,500–6,800 (mini), USD 8,500–8,800, general range USD 5,000–15,000 depending on configuration — [madeinchina listing](https://m.madeinchina.com/mall/show-Portable-Handheld-1500W-Laser-Welding-Machine-2000W-3000W-Fiber-Laser-Weldr-Alloy-Aluminum-Copper-Galvanized-Steel-Metal-Material-3-in-1_959832.html); [FindLight](https://findlight.net/laser-material-processing/laser-welders/handheld-laser-welders/battery-welding); [xTool buyer guide](https://www.xtool.com/blogs/buyer-guide/how-to-choose-the-best-handheld-laser-welder)
- 1500 W galvanometer-head handheld units are marketed for small-batch and repair welding of lithium battery tabs (Al, Ni, Cu) — [Hanten CNC](https://hantencnc.com/product/1500w-handheld-galvanometer-laser-welding-machine); [battery-equipments.com](https://www.battery-equipments.com/handheld-laser-spot-welder-machine-with-optional-1000w-1500w-2000w-3000w-power-for-battery-material-welding_p1408.html)
- A portable 1500 W spec sheet gives max single-side weld thickness 4 mm for steel/aluminium but only ~1 mm for copper; dedicated copper busbar systems are 3,000 W-class cells (e.g. Sunstone SFL 3000) — [FindLight datasheet](https://www.findlight.net/uploads/products/datasheet/1500w-portable-laser-welding-machine_1665227263.pdf); [Sunstone SFL](https://www.sunstonewelders.com/products/sfl-fiber-laser-welding-cell)

**BMS tools / software**
- JBD/Xiaoxiang smart BMS: PC configuration and monitoring through a USB-to-UART box (V1.6 module ~INR 550 in India); Xiaoxiang BMS mobile app is free with a paid Pro tier; an open-source Python library reads JBD packs over UART-USB (usable for automated logging) — [ARB Accessories](https://store.arbaccessories.in/product/uart-communication-box-jbd); [App Store](https://apps.apple.com/my/app/xiaoxiang-bms/id1375405426); [python-jbdtool-bms](https://github.com/fkressmann/python-jbdtool-bms)
- A JBD datasheet (7–24S) warns its UART is non-isolated and must not be used to communicate with chargers/loads — check isolation before wiring a PC to a pack under test — [JBD datasheet](https://cdn.shopify.com/s/files/1/0606/5199/5298/files/JBD-SP22S003_37ea5c42-0b2f-4c30-bb4a-3ba411fcb66e.pdf)

### Inferences
- Proposed tiering built from the cited prices (equipment only, excluding benches/safety/consumables):
  - Starter (1–2 techs): YR1035+ (~USD 50–100 / ~0.95–1.75 M VND), 1× EBC-A20 (~1.5–1.65 M VND) or EBC-A40L (~USD 200–350), NEEY 4 A balancer (~1.75 M VND), capacitor spot welder in the Glitter 801/811A class (~USD 330–350) or kWeld (~EUR 170 + power source), JBD UART box. Order of magnitude USD 800–1,500.
  - Professional (3–5 techs): add 8-channel 5 V 6 A grading cabinet (USD 400–1,000), Heltec 24S 10–15 A equalizer-analyzer (price on request; adjacent models USD ~320–680), pack capacity tester 20 A/40 A (USD 640–680), Glitter 811H-class welder (USD ~650), BMS tester. Order of magnitude USD 3,000–6,000.
  - High-volume (6–10 techs): multiple grading cabinets or a 128-channel unit (~USD 4,500), Hioki BT3554 (USD ~3,200–3,500) for traceable IR measurement, 1500 W galvo laser welder (USD ~4,000–15,000). Order of magnitude USD 15,000–35,000.
- A single-channel EBC tester is a diagnostic tool (one cell or one parallel group at high current); it is not a grading throughput tool. Throughput comes from channel count, not from current rating.
- The Hioki's 6–60 V voltage window and 3 Ω top range suit pack/module-level checks; the YR1035+ (100 V, 200 Ω) covers 72 V packs (84 V full charge) that exceed the Hioki BT3554-50's 60 V limit.

### Gaps
- No reliable 2026 Vietnamese price found for Glitter 801/811, Sunkko 737G+, kWeld, Heltec equalizer-analyzers, EBC-A40L or multi-channel graders; marketplace pages (Shopee/Lazada) did not expose prices to search. VND figures above cover only YR1035+, EBC-A20 and NEEY 4 A, and several are 2022–2024 snapshots.
- Not researched to a citable standard (no sources retrieved): multimeters, programmable DC supplies, DC electronic loads (incl. DL24), soldering/hot-air stations, fume extractors, thermal cameras, insulation testers. These should be treated as unsourced if included in the equipment list.
- JK BMS app/PC tooling and Heltec BMS tester pricing: no source found.
- Endless Sphere threads (primary community source for welder comparisons) were blocked by bot protection and could not be read in full.

## 2. Which tools give the largest productivity/quality gains, and common tool mistakes

### Takeaway
The best-evidenced quality levers are a real 4-wire AC IR meter, genuine pure nickel verified on receipt, and a welder with enough current and energy control for the strip actually used. No source gave measured time savings for any tool; productivity claims are qualitative.

### Cited Findings
- kWeld regulates each pulse to a target energy rather than a fixed time, which community users cite as the reason for consistent welds; a user reported abandoning a Sunkko after using kWeld (anecdotal, forum) — [keenlab](https://www.keenlab.de/index.php/product/kweld-complete-kit/); [Endless Sphere thread](https://endless-sphere.com/sphere/threads/real-spot-welding-machines-which-is-the-better-deal.121064/latest)
- kWeld is a kit that needs an external high-current source; Glitter 801H is described as plug-in and ready to weld — [keenlab](https://www.keenlab.de/index.php/product/kweld-complete-kit/); [desertcart 801H listing](https://www.desertcart.lk/products/483929515-glitter-801h-battery-spot-welder-21-kw-capacitor-energy-storage)
- Vietnamese users (Tinhte, 2022) note that cheap battery-powered mini spot welders weaken as their internal battery ages — [Tinhte thread](https://tinhte.vn/thread/3568153)
- Fake nickel is common even from reputable sellers: in one bench test at 5 A, "nickel-plated steel" strip measured 192 mΩ versus 24 mΩ for genuine pure nickel of the same 0.15 mm thickness, and a sample sold as pure nickel turned out to be carbon steel — [electric-skateboard.builders test](https://www.electric-skateboard.builders/t/carbon-steel-strip-vs-stainless-steel-strip-vs-pure-nickel-strip-fake-nickel-strips-tested-practical-performance-test-results/18633)
- Supplier nickel from a known retailer (NKON) produced showers of sparks on a grinder while known-good nickel produced none (issue reported solved 2019) — [esk8.news](https://forum.esk8.news/t/nkon-nickel-quality-issues-solved-04-09-19/6740)
- YR1035 supplied Kelvin clamps are weak; the cell-holder fixture gives stable readings — [lygte-info.dk](https://lygte-info.dk/review/InternalResistanceMeterYR1035%20UK.html)
- 1500 W handheld lasers are limited to ~1 mm copper; vendor claims on Cu/Ni tab welding are marketing statements, so sample welds on the real stack should be requested before purchase — [FindLight datasheet](https://www.findlight.net/uploads/products/datasheet/1500w-portable-laser-welding-machine_1665227263.pdf)
- Heltec's capacity/cycle-life gains from balancing are vendor claims without methodology — [Heltec](https://www.heltec-energy.com/news/new-product-online-10a15a-lithium-battery-pack-equalizer-analyzer)

### Inferences
- Common mistakes implied by the evidence: (1) buying a 1.5 kW transformer welder (Sunkko 737G) and then trying to weld 0.2–0.3 mm pure nickel; (2) trusting strip labelled "pure nickel" without an incoming test; (3) using a 2-wire multimeter or DC-load "IR" readings and comparing them to 1 kHz AC datasheet values; (4) buying one high-current tester instead of many channels; (5) buying a laser welder for copper busbars at 1500 W.
- Transformer welders load the mains heavily and are sensitive to supply quality; capacitor-discharge units decouple the weld from the mains. This is general trade knowledge and was not confirmed by a retrieved source.
- A pack-level equalizer-analyzer with per-cell display shortens diagnosis because it shows all group voltages at once instead of probing each group; no measured time saving was found.

### Gaps
- No measured time-saving data (minutes per pack, welds per hour, tests per day) for any tool. Any numbers in a final report would have to be estimates.
- No independent test data on "fake capacity" cheap testers or on DL24 accuracy was retrieved.
- No independent head-to-head of kWeld vs Glitter 811A.

## 3. Workshop zoning and layout

### Takeaway
The only formal shop-level guidance found is for e-bike retailers: segregated fire-resistant storage, a separate attended charging station near an exit, damaged packs kept outside the building, and no unattended or overnight charging. ESD limits come from ANSI/ESD S20.20. No published layout specifically for a pack-repair workshop was found, so zoning must be derived.

### Cited Findings
- Store all packs in a fire-resistant cabinet with flame-arresting vents (vent outdoors if practical), sized for peak inventory, in an area free of trash, cardboard, paint, flammables and damp — [Human Powered Solutions protocol v1.6, via Bicycle Retailer](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Never charge inside the storage cabinet; charge on a separate wheeled metal-wire cart with switched power strips, ideally next to an exterior door so the cart can be wheeled outside — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- At the charging station: at least one ABC extinguisher within reach, a smoke detector above the cabinet/charging area, and a lidded 32-gallon (~120 L) plastic bin filled three-quarters with water for immersing a failing pack — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Never charge unattended or overnight; a part-charged pack goes back into the cabinet at closing and charging resumes next day — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Damaged packs are stored OUTSIDE, away from flammables, and never in the fire cabinet or anywhere in the store — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Emergency sequence: immerse the failing pack in the water bin if safe, otherwise move it or wheel the cart outside, move other packs away, close the cabinet, call the fire service; evacuate if not safe. The document states a lithium-ion fire cannot be extinguished, only mitigated — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- UK National Fire Chiefs Council guidance: do not attempt to extinguish a lithium battery fire; get out, stay out, call emergency services — [NFCC](https://www.nationalfirechiefs.org.uk/E-bikes-and-e-scooters-fire-safety-guidance)
- A workshop safety checklist lists a designated isolation area for damaged batteries, a spill kit for electrolyte, a Class D extinguisher, and no water on battery fires — [workshop safety reminders page](https://astro-shop-shepherd-production.pages.dev/quick-start/safety-reminders); this conflicts with the water-immersion bin in the [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf)
- Purpose-built lithium storage cabinets (e.g. asecos ION-LINE) can include smoke detection, temperature sensors, fire suppression and alarm forwarding — [BikeBiz](https://bikebiz.com/e-bike-battery-fires-and-how-to-stop-them/)
- ESD bench (ANSI/ESD S20.20-2021 as summarised by vendors): seated operators must use a wrist strap; wrist-strap system resistance < 3.5 × 10^7 Ω (35 MΩ); footwear/flooring system < 1.0 × 10^9 Ω and < 100 V body voltage; equipment grounding conductor < 1 Ω; auxiliary ground < 25 Ω to equipment ground — [GoToPAC summary of S20.20](https://gotopac.com/art-esd-iso-standards-s20-20)
- Wrist-strap cords should connect to a ground/bonding point, not to the edge of the dissipative mat — [Desco wrist strap manual](https://www.manualslib.com/manual/1393329/Desco-19246.html)
- Both the HPS protocol and a bike-brand consumer guide state packs must never be opened, even for repair — [HPS protocol](https://www.bicycleretailer.com/sites/default/files/downloads/article/battery-protocols-v1.6.pdf); [Diamant](https://www.diamantrad.com/en-GB/blog/e-bike-battery-safety/). A pack-repair business works against this advice, which raises the bar for its own controls.

### Inferences
- Derived zoning, in material-flow order (one-way flow, no backtracking): (1) Intake counter: visual inspection, voltage, photos, job ticket. (2) Quarantine: outdoor or externally vented area for swollen, wet, crushed or 0 V packs, per the "damaged packs outside" rule. (3) Disassembly bench: non-conductive top, insulated tools, scrap bin. (4) Cell test/grading wall: graders and IR meter, on non-combustible shelving, away from the entrance route. (5) Welding/assembly bench: welder, jigs, nickel, insulation materials. (6) Electronics/BMS bench: the only ESD-protected area (mat, wrist strap, soldering, hot air, fume extraction). (7) Charge-discharge test area: nearest the exterior door, on wheeled metal carts, under a smoke detector, with water bin and extinguisher. (8) Storage: three physically separate, labelled locations (good/ready for collection, in-process/suspect, scrap awaiting recycling), with good stock in a fire-resistant cabinet.
- ESD mats are static-dissipative and therefore slightly conductive; they belong on the BMS/electronics bench, not under open cell groups. Cell-handling benches need insulating surfaces (rubber, wood, epoxy/phenolic sheet) and one-pole-at-a-time working. This is an inference; no source addressed the ESD-vs-insulation conflict for battery benches.
- Since long tests cannot run unattended under the cited protocol, the charge-discharge area sets a hard daily capacity: test hours available = staffed hours × number of channels. This makes channel count the main capacity lever.
- The water-bin vs Class D vs "evacuate" conflict should be resolved with the local fire authority; the cited sources agree only that mitigation and evacuation take priority over firefighting.

### Gaps
- No source found giving a floor plan, minimum separations or area per technician for a battery repair workshop.
- No Vietnamese fire-code (PCCC) requirements for lithium battery workshops were retrieved.
- No fire-service or insurer guidance specific to commercial pack repair (as opposed to retail storage) was found.
- IPC rework/soldering workmanship standards (e.g. IPC-7711/7721, J-STD-001) were not researched.

## 4. Process optimisation: SOPs, 5S, traceability, batching, parallelisation, fixtures, software

### Takeaway
Pack-builder communities converge on a staged cell-qualification flow (visual → voltage → charge → rest/self-discharge → capacity → IR → sort into bands) recorded per cell in a spreadsheet; the multi-day rest step and long charge/discharge cycles are the natural bottlenecks. Lean evidence is from electronics assembly, not repair: one documented 5S programme cut cycle time 70% and WIP 60%.

### Cited Findings
- Typical used-cell qualification sequence: visual check (deformation, leaks, rust → discard); voltage check (cells >2 V go to charging; below ~2.5 V likely damaged to some degree); full charge; rest and re-measure (one guide: 24 h, discard if <4.0 V; others: 1 week); capacity test; IR measurement — [Instructables](https://www.instructables.com/Re-using-Lithium-Ion-Cells-From-Laptop-Batteries); [CandlePowerForums](https://www.candlepowerforums.com/threads/how-to-check-if-a-salvaged-18650-cell-is-good.483706/)
- Suggested acceptance gates: SOH ≥ 80% for second-life cells; fresh 18650 measures ~20–40 mΩ at 1 kHz and many workflows reject >60 mΩ for series strings; hobby sources use a looser <100 mΩ; a 7-day rest is "optional but recommended" (single blog source, figures not backed by a primary reference) — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/capacity-matching-18650-cells-in-excel-a-field-engineers)
- Grading discharge is typically at 0.5C or 1 A down to ~2.8 V while integrating mAh — [Accio grading-machine overview](https://www.accio.ai/find-product/lithium-cell-grading-machine-price)
- Spreadsheet method: per-cell columns for SOH, normalised capacity, capacity band, IR band, group key and quality score, so matched sets can be pulled without re-sorting; the same source estimates second-life cell spread at 5–15% capacity and 20–80% IR — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/capacity-matching-18650-cells-in-excel-a-field-engineers)
- Matching rule before assembly: same batch and model in a parallel group, cells within 0.05 V of each other; record OCV, capacity and IR and label each cell (marker or sticker) — [Zbotic cell-matching guide](https://zbotic.in/battery-cell-matching-sort-18650-cells-before-pack-build/)
- Keeping a per-pack spreadsheet of all cell data helps later degradation tracking and replacement of a faulty group — [DIY Powerwall build notes](https://sites.google.com/view/diy-powerwall/18650-25kwh/building)
- Fixtures: parametric 3D-printable jigs for cylindrical cells and 18650/21700 assembly jigs are freely available; builders also use jigs that sit on the cell/nickel stack and index weld position — [MakerWorld parametric jig](https://makerworld.com/en/models/425542); [CGTrader 21700 jig](https://www.cgtrader.com/3d-print-models/tools-organizers/tools/21700-battery-assembly-jig); [esk8.news](https://forum.esk8.news/t/making-a-modular-battery/16731/3)
- 5S results (electronics assembly, Preco Electronics, first year): WIP −60%, cycle time −70%, changeover time −40% (trade-magazine report) — [Assembly Magazine](https://www.assemblymag.com/articles/83658-a-journey-to-the-other-side-of-lean)
- A five-day kaizen was applied to a technical-service/repair operation with growing backlog and lead times (Novanta); the percentage result was not visible in the retrieved text — [Novanta](https://novanta.com/?p=2046)
- Parts availability is a named cause of failed first-time fixes in service operations — [Fieldproxy](https://www.fieldproxy.ai/blog/20-field-service-kpis-every-appliance-repair-business-should-track-d1-38)
- JBD packs can be logged programmatically over UART-USB with an open-source Python library — [python-jbdtool-bms](https://github.com/fkressmann/python-jbdtool-bms)

### Inferences
- Proposed flow with quality gates (G) and holds:
  1. Intake: ID label/QR on pack, photos, customer symptom, pack voltage, charger check. G0: safe to bring indoors? (swelling, water, heat, smell → quarantine/decline).
  2. Non-invasive diagnosis: pack voltage, charge/discharge port behaviour, smart-BMS readout if available. Quote. G1: customer approval.
  3. Open and map: per-group voltages, group IR, visual, thermal check under light load. Decide: BMS fault / connection fault / weak groups / full re-cell.
  4. Disassembly (only if needed), cell harvest.
  5. Cell qualification (batched): charge → rest → capacity → IR → band. G2: cell acceptance criteria.
  6. Rebuild: fixture, insulation rings/fish paper, weld, weld pull test on coupon, BMS wiring. G3: weld and insulation inspection before closing.
  7. Balance and pack-level test: full charge, top balance, capacity discharge at a defined current, protection tests (OVP/UVP/OCP/short where the BMS tester allows), temperature observation. G4: capacity ≥ target, delta-V ≤ limit, no hot spots.
  8. Close, label (job ID, date, cell type, test result), photos, test report, storage at partial charge, hand-over. G5: final checklist sign-off.
- Bottlenecks: (a) self-discharge rest (1–7 days of calendar time, zero labour); (b) capacity cycles (hours per cell or pack, limited by channels and by the attended-charging rule); (c) quote approval wait; (d) parts not in stock.
- Batching and parallelising: run cell grading as a daily batch started first thing so cycles finish within staffed hours; keep a pre-graded, banded stock of common cells so step 5 is skipped for most jobs; start pack-level tests in the morning and do bench work (disassembly, welding, BMS) while they run; one technician can tend many test channels.
- Rough capacity arithmetic for planning (illustrative, not sourced): a 2.5 Ah cell charged at 0.5C and discharged at 0.5C needs roughly 5–6 h per cycle, so an 8-channel grader yields about 8 cells per staffed day, and a 128-channel unit about 128. A 10S4P re-cell needs 40 graded cells, i.e. 5 staffed days on one 8-channel grader. This arithmetic is why channel count, or buying pre-graded new cells, dominates turnaround time.
- Traceability minimum: job ticket ID on pack and on every tray/bin of its parts; before/after photos; per-group voltage table at intake and at release; cell lot and band; welder setting; BMS model and parameter export; final capacity curve file.
- 5S application: shadow boards for insulated tools, colour-coded bins (green good / yellow suspect / red scrap), kanban min-max for nickel, BMS boards, connectors and heat shrink, and a fixed home for each job tray. The 70% cycle-time figure is from assembly and should be presented as an upper-bound analogue, not an expected result.

### Gaps
- No repair-shop management software (ticketing/CRM) was researched or sourced; no evidence found of a battery-specific cell-database tool (searches for such tools returned nothing).
- No measured turnaround or takt data from real battery repair shops was found.
- No peer-reviewed 5S/lean study in an electronics or battery repair workshop with quantified results was retrieved (a 2021 paper on lean in the electronics repair industry exists but its numbers were not seen).
- The rest-period duration (24 h vs 7 days vs weeks) is not settled by the sources; they are hobbyist or blog-level.

## 5. Quality metrics / KPIs and data logging

### Takeaway
General repair-industry benchmarks put first-time-fix rate at roughly 80–90% (top performers >90%) and turnaround for common electronics repairs at 1–3 days, but these come from vendor blogs and KPI-template sellers; no battery-repair-specific benchmark or warranty-return benchmark exists in the sources.

### Cited Findings
- First-time-fix rate benchmarks: ~85–90% for electronics maintenance; ~80–90% for service organisations; appliance repair floor ≥85% with top performers >90% — [FinModelsLab](https://finmodelslab.com/blogs/kpi-metrics/gadget-repair-shop-kpi-metrics); [SimpleKPI](https://www.simplekpi.com/Blog/8-Repair-Center-KPIs-for-improved-performance); [Fieldproxy](https://www.fieldproxy.ai/blog/20-field-service-kpis-every-appliance-repair-business-should-track-d1-38)
- Stricter FTFR definition: the unit is repaired once, returned, and does not come back for the same fault within the warranty period — [Claimlane](https://www.claimlane.com/resources/blog/first-time-fix-rate)
- Turnaround benchmarks: 1–3 days for common gadget repairs; <3 days for standard mobile devices; ~48 h for automotive electronics; 1–2 weeks for vintage electronics — [FinModelsLab gadget repair](https://finmodelslab.com/blogs/kpi-metrics/gadget-repair-shop-kpi-metrics); [Strategy for Industry KPI tree](https://strategyforindustry.com/industry/repair-of-consumer-electronics/kpi-tree/); [FinModelsLab vintage](https://finmodelslab.com/blogs/kpi-metrics/vintage-electronic-repair-shop)
- Return/warranty rate: no numeric benchmark; "varies by specialisation and quality control"; lower is better — [FinModelsLab mobile repair](https://finmodelslab.com/blogs/kpi-metrics/mobile-phone-repair-shop-kpi-metrics)
- Customer satisfaction decomposes into FTFR and turnaround time in a standard repair KPI tree — [Strategy for Industry](https://strategyforindustry.com/industry/repair-of-computers-and-peripheral-equipment/kpi-tree/)

### Inferences
- Suggested KPI set for a pack-repair shop: FTFR (warranty-period definition); warranty return rate by fault category (weld, BMS, cell, connector); turnaround time split into touch time vs waiting (approval, parts, test queue); test coverage (% of released packs with full capacity test + protection test + balance delta recorded); quote-to-approval conversion; tester channel utilisation; scrap/quarantine rate at intake; cell reject rate at grading; safety incidents and near misses.
- Battery repair turnaround will be structurally longer than phone repair because of multi-hour cycles and rest periods; the 1–3 day benchmark is achievable only for BMS/connector faults or when pre-graded cells are stocked.
- Data logging practice: store the pack-level discharge curve (EBC/Heltec PC export) and BMS parameter export against the job ID, and keep per-cell grading data for the life of the warranty.

### Gaps
- No battery-repair-specific KPI benchmarks found; all figures are from adjacent industries and low-authority sources.
- No source on typical warranty terms or return rates for rebuilt e-bike/scooter packs.

## 6. Consumables and materials

### Takeaway
Nickel authenticity is the consumable risk with the best evidence: plated steel has roughly 4–8× the resistance of pure nickel and is sold mislabelled, and the popular salt-water test is not fully reliable on its own. Current capacity is best estimated from cross-section (rule of thumb ~5–7 A/mm² for nickel, ~7–10 for copper, units unconfirmed).

### Cited Findings
- Measured at 5 A, 0.15 mm strip: nickel-plated steel 192 mΩ vs pure nickel 24 mΩ (8×); a different plated strip still had almost 4× the resistance of pure nickel — [electric-skateboard.builders](https://www.electric-skateboard.builders/t/carbon-steel-strip-vs-stainless-steel-strip-vs-pure-nickel-strip-fake-nickel-strips-tested-practical-performance-test-results/18633)
- Grinder spark test: known-good pure nickel gives no (or very few) sparks; steel-based strip gives showers of sparks within a second — [esk8.news](https://forum.esk8.news/t/nkon-nickel-quality-issues-solved-04-09-19/6740); [Endless Sphere](https://endless-sphere.com/sphere/threads/pure-nickel-sparking-when-cut-with-disc.100619/)
- Salt-water test: sellers and Voltlog describe plated steel rusting; but one builder's plated strip showed no rust after days, so the test can give false passes. A stricter variant: soak one 2 cm sample in salt water for 2 weeks and another in vinegar — [US Solid](https://ussolid.com/pure-nickel-strip-battery-connecting-strip-slices-for-18650-battery-pack-building-ni200-n6-material-100pcs.html); [Voltlog #227](https://www.voltlog.com/tag/steel/); [Endless Sphere "Nickel vs Nickel mystery"](https://endless-sphere.com/sphere/threads/nickel-vs-nickel-mistery.104579); [foil.zone](https://foil.zone/t/nickel-strip-quality/6242)
- Ampacity: a calculator lists typical values of 5–7 for pure nickel and 7–10 for copper (units not shown in the retrieved text; presumably A/mm²); a reseller quotes ~7 A for 0.2 × 7 mm pure nickel; ratings scale with conductor cross-section; stacking layers raises capacity — [Fractal Engineering calculator](https://store.fractalengineering.net/?p=8132); [18650BatteryStore](https://www.18650batterystore.com/products/pure-nickel-strip-1kg-roll-for-battery-spot-welding-18650-21700); [esk8.news conductor ratings](https://forum.esk8.news/t/conductor-current-ratings-sro/7660/114)
- Pure nickel strip is sold as Ni200 / N6 grade (≥99.6% Ni claims) — [US Solid](https://ussolid.com/pure-nickel-strip-battery-connecting-strip-slices-for-18650-battery-pack-building-ni200-n6-material-100pcs.html)
- kWeld welds up to ~0.3 mm nickel; Glitter 811H is marketed for 0.3 mm pure nickel — [keenlab](https://www.keenlab.de/index.php/product/kweld-complete-kit/); [china.org.ru 811H](https://china.org.ru/product/1600975314015)

### Inferences
- Incoming-inspection SOP for every new nickel roll: (1) grinder spark test (seconds); (2) 4-wire resistance of a fixed length against a retained known-good sample using the YR1035+ (expected ratio ≥4× for plated steel); (3) optional 2-week salt/vinegar soak as confirmation. Record lot and result. The resistance comparison is the most quantitative and fastest.
- Applying the rule of thumb (if the units are A/mm²): 0.15 × 8 mm = 1.2 mm² → ~6–8 A; 0.2 × 8 mm = 1.6 mm² → ~8–11 A; 0.2 × 10 mm = 2.0 mm² → ~10–14 A per strip. High-current packs therefore need stacked strips, wider strip or copper/nickel sandwich, which in turn drives welder selection.
- Standard stock list to hold under kanban (unsourced, general practice): pure nickel 0.15 and 0.2 mm in 8/10 mm widths and multi-P formed strip; adhesive fish-paper (barley paper) rings and sheet; Kapton tape; 18650/21700 cell holders; epoxy/FR4 sheet and PVC heat shrink in common widths; silicone wire by gauge; XT60/XT90 and Anderson connectors; balance leads (JST-XH); common BMS boards by series count and current; isopropyl alcohol and flux cleaner; neutral-cure silicone or hot glue.

### Gaps
- No sourced data retrieved on: fish paper/barley paper grades and thicknesses, Kapton ratings, cell-holder vs glued construction, epoxy board, heat-shrink sizing, wire gauge ampacity, XT60/XT90/Anderson current ratings, or solvents. These need separate sourcing (manufacturer datasheets, e.g. Amass for XT connectors) before being stated as fact.
- No published, lab-verified ampacity table for specific strip sizes or for nickel-copper sandwich welding was found; the 5–7 figure's units are unconfirmed.
- No Vietnamese supplier prices for nickel, insulation materials or connectors were found.
