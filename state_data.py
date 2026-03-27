# State data informed by:
# - Charlie Health locations page (March 2026): active in all states EXCEPT SD, KS, OK, AR, MS, AL, WV, ME, CT, RI, HI
# - KFF Medicaid expansion tracker (2025)
# - CCHP State Telehealth Laws & Reimbursement Policies Report, Fall 2025
# - The Lund Report / Oregon Capital Chronicle on Charlie Health Oregon controversy
# - SAMHSA 2023 National Survey on Drug Use and Health (SMI rates by state)
# - US Census Bureau 2024 population estimates
# Favorability scores (1–10): Medicaid expansion (+2), telehealth parity (+1), IOP reimbursement quality (+1),
# progressive BH policy (+1), no expansion (−2), active regulatory conflict (−2), restrictive licensing (−1)
#
# Opportunity model:
#   Addressable IOP patients = adult_population × smi_rate × 0.15
#   Medicaid split: 35% of addressable in expanded states, 20% in non-expanded
#   Revenue: $12,000/Medicaid patient · $18,000/commercial patient

_STATES = [
    # (abbr, name, score, medicaid_expanded, ch_active, medicaid_covered,
    #  telehealth_policy, key_regulatory_notes, recent_developments)

    ("AL", "Alabama", 2, False, False, False,
     "Limited telehealth parity",
     "No Medicaid expansion; restrictive IOP billing; weak mental health parity enforcement; no payment parity for telehealth",
     "2025: Expansion bills failed again; no meaningful behavioral health telehealth reform"),

    ("AK", "Alaska", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; remote-first geography favors virtual IOP; pandemic telehealth provisions made permanent",
     "2024: Permanent telehealth expansion signed into law; Medicaid managed care overhaul underway"),

    ("AZ", "Arizona", 7, True, True, True,
     "Moderate telehealth parity",
     "Medicaid expanded (2013); AHCCCS covers behavioral health broadly; IOP reimbursement improving via managed care",
     "2024: New behavioral health workforce initiative; increased IOP reimbursement rates under AHCCCS"),

    ("AR", "Arkansas", 4, True, False, False,
     "Moderate parity, complex waiver structure",
     "Expanded via private option waiver; CH not active; complex MCO structure makes entry difficult; IOP coverage inconsistent",
     "2025: Work requirements waiver under federal review; no significant IOP-specific reforms"),

    ("CA", "California", 9, True, True, True,
     "Nation-leading telehealth parity",
     "Medi-Cal covers virtual IOP; SB 855 (2020) dramatically expanded behavioral health coverage; nation's strongest parity enforcement",
     "2025: CalAIM expansion continues statewide; Medi-Cal behavioral health carve-in fully operational"),

    ("CO", "Colorado", 9, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; SB21-137 expanded behavioral health access; Behavioral Health Administration launched 2022; robust IOP reimbursement",
     "2025: $400M+ BHA investment active; new crisis system operational; IOP provider capacity growing"),

    ("CT", "Connecticut", 4, True, False, False,
     "Limited — out-of-state telehealth registration expired June 2025",
     "Medicaid expanded; HOWEVER out-of-state telehealth provider registration expired June 30, 2025 with no replacement — high barrier for CH entry",
     "2025: Telehealth registration lapse creates major licensing barrier; no legislation introduced to reinstate"),

    ("DE", "Delaware", 7, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; small state with concentrated payer relationships; IOP coverage available via DMAP managed care",
     "2025: DHSS launched behavioral health roadmap; Medicaid rate increases announced for BH providers"),

    ("FL", "Florida", 4, False, True, False,
     "Moderate telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; large commercial market; IOP coverage varies by payer; strong commercial opportunity despite Medicaid gap",
     "2025: Medicaid expansion ballot campaign active; telehealth licensing reciprocity improved; large uninsured gap persists"),

    ("GA", "Georgia", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No full expansion; limited Pathways waiver has slow enrollment; commercial market exists but large Medicaid gap limits reach",
     "2025: Pathways waiver enrollment stagnant; full expansion repeatedly rejected by legislature"),

    ("HI", "Hawaii", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; island geography makes virtual IOP strategically important; QUEST Integration covers IOP; CH not active",
     "2025: Telehealth parity legislation strengthened; behavioral health provider shortage addressed via virtual-first policy; strong entry opportunity"),

    ("ID", "Idaho", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020 ballot initiative); regulatory environment improving; IOP provider shortage creates demand",
     "2025: Medicaid managed care contracts include expanded telehealth; IOP prior auth requirements updated"),

    ("IL", "Illinois", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; HB2595 strengthened parity enforcement; IOP well-reimbursed via Medicaid managed care",
     "2025: Mental health workforce expansion bill passed; Medicaid rates increased ~10% for behavioral health"),

    ("IN", "Indiana", 6, True, True, True,
     "Moderate parity; HIP 2.0 waiver structure",
     "Expanded via HIP 2.0 waiver; complex eligibility rules; IOP reimbursement available but navigating multiple MCOs required",
     "2025: HIP reauthorization includes expanded behavioral health benefits; telehealth rules updated"),

    ("IA", "Iowa", 7, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; Iowa Health Link MCO structure; IOP reimbursement in place; strong rural virtual care demand",
     "2025: Managed care oversight reforms; behavioral health crisis funding increased"),

    ("KS", "Kansas", 5, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2022); implementation maturing; CH not yet active; IOP coverage developing under KanCare",
     "2025: KanCare behavioral health rollout progressing; early-stage opportunity for CH entry"),

    ("KY", "Kentucky", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; KCHIP covers youth; strong legislative support for behavioral health; IOP reimbursement solid",
     "2025: Behavioral health safety net investments; telehealth parity bill signed; Medicaid rates increased"),

    ("LA", "Louisiana", 6, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded (2016); Medicaid managed care covers IOP; rural access gaps create virtual care demand",
     "2025: Medicaid redetermination stabilizing; telehealth billing guidance updated for IOP services"),

    ("ME", "Maine", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded (2019); MaineCare covers behavioral health broadly; rural population = high virtual IOP demand; CH not active despite favorable environment",
     "2025: Crisis receiving center network expanding; telehealth permanence passed; strong untapped opportunity for CH"),

    ("MD", "Maryland", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; HealthChoice MCO covers IOP well; strong parity enforcement; high commercial insurance penetration",
     "2025: Medicaid rate increases for behavioral health; crisis system transformation funded"),

    ("MA", "Massachusetts", 9, True, True, True,
     "Nation-leading telehealth and parity laws",
     "Medicaid expanded; Chapter 224 parity law among nation's strongest; MassHealth covers virtual IOP",
     "2025: Mental health access commission recommendations adopted; BHSA operational; strong reimbursement environment"),

    ("MI", "Michigan", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; integrated BH/physical health managed care; IOP reimbursement strong",
     "2025: Behavioral health integration transformation ongoing; Medicaid rates increased for IOP services"),

    ("MN", "Minnesota", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; strong DHS behavioral health infrastructure; good IOP reimbursement; high commercial coverage rates",
     "2025: Behavioral health workforce bill passed; crisis system investments $150M+"),

    ("MS", "Mississippi", 2, False, False, False,
     "Minimal telehealth parity",
     "No Medicaid expansion — last major holdout; very limited commercial IOP coverage; poorest state BH infrastructure nationally",
     "2025: Expansion again rejected; governor opposed; 200K+ remain without coverage"),

    ("MO", "Missouri", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2021 ballot initiative); MO HealthNet implementation maturing; MCO contracting complex",
     "2025: MO HealthNet expansion stabilizing; behavioral health integration improving"),

    ("MT", "Montana", 6, True, True, True,
     "Moderate telehealth parity",
     "Medicaid expanded; rural state with high behavioral health need; IOP reimbursement in place; Charlie Health's home state",
     "2025: Medicaid expansion reauthorized; rural telehealth investments; CH well-positioned as Montana-based company"),

    ("NE", "Nebraska", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020); Heritage Health managed care; IOP coverage developing; rural access gaps present",
     "2025: MCO contracts updated; IOP prior authorization requirements loosened"),

    ("NV", "Nevada", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; SB292 strengthened telehealth parity; IOP reimbursement solid; growing population with rising BH demand",
     "2025: Behavioral health workforce expansion; AI therapy regulation passed — favors CH's human-led model"),

    ("NH", "New Hampshire", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded via NHHPP waiver; small state with concentrated payer relationships; strong SUD infrastructure",
     "2025: Medicaid expansion reauthorized; SUD + mental health integration expanding"),

    ("NJ", "New Jersey", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; NJ FamilyCare covers IOP; strong parity enforcement; high commercial insurance density",
     "2025: Behavioral health crisis services expansion funded; Medicaid rate increases for IOP"),

    ("NM", "New Mexico", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; Centennial Care 2.0 covers behavioral health broadly; rural access need favors virtual IOP",
     "2025: Behavioral health system transformation ongoing; IOP reimbursement improved under MCO contracts"),

    ("NY", "New York", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MHPAEA enforcement strong; OMH investments in virtual care; large commercial market",
     "2025: 1115 waiver for social determinants active; OMH virtual care investments; strong IOP reimbursement"),

    ("NC", "North Carolina", 7, True, True, True,
     "Strong telehealth parity",
     "Expanded Medicaid (December 2023); Medicaid Transformation to managed care; behavioral health carve-in active",
     "2025: Medicaid expansion enrollment surpassing forecasts; behavioral health MCO contracts operational"),

    ("ND", "North Dakota", 6, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; Sanford/Essentia dominate market; IOP coverage available; rural state favors virtual delivery",
     "2025: Telehealth permanence bill signed; behavioral health workforce investments"),

    ("OH", "Ohio", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; OhioRISE for youth behavioral health; IOP well-reimbursed; strong managed care infrastructure",
     "2025: OhioRISE expansion ongoing; Medicaid managed care rebid completed; rates increased"),

    ("OK", "Oklahoma", 4, True, False, False,
     "Moderate parity; early expansion implementation",
     "Expanded Medicaid (2021); CH not active; SoonerCare implementation maturing; IOP billing guidance evolving",
     "2025: SoonerCare enrollment growing; behavioral health services expanding; near-term entry opportunity"),

    ("OR", "Oregon", 6, True, True, True,
     "Strong parity laws; ACTIVE REGULATORY CONFLICT with Charlie Health",
     "MAJOR ISSUE: OHA investigating CH for using out-of-state unlicensed providers while billing $85M+ to Oregon Medicaid; Gov. Kotek publicly criticized CH's ad campaign as 'misleading'; lawmakers pushed OHA probe; June 2025 corporate healthcare influence bill signed — nation's strictest",
     "2025: OHA considering termination of CH operating agreement; 'Save Virtual Care OR' campaign by CH called misleading; Trauma Informed Oregon published critical report"),

    ("PA", "Pennsylvania", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MA HealthChoices MCO covers IOP well; strong parity enforcement; large commercial market",
     "2025: Medicaid managed care rebid completed; behavioral health crisis investments; IOP reimbursement stable"),

    ("RI", "Rhode Island", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; small state, concentrated market; HealthSource RI covers behavioral health; CH not active despite favorable environment",
     "2025: Behavioral health workforce bill passed; Medicaid IOP reimbursement updated; strong entry opportunity"),

    ("SC", "South Carolina", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; large coverage gap; commercial market exists but limited BH reimbursement",
     "2025: Expansion bill introduced but failed; telehealth licensing compact joined but no parity law"),

    ("SD", "South Dakota", 5, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2023 ballot initiative); implementation in early stages; CH not active; IOP framework developing",
     "2025: First full year of expansion; enrollment growing; BH provider network building; entry opportunity"),

    ("TN", "Tennessee", 4, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; TennCare limited to narrow populations; CH active for commercial payers only",
     "2025: TennCare waiver revision under federal review; expansion rejected again"),

    ("TX", "Texas", 4, False, True, False,
     "Moderate telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; largest coverage gap nationally; large commercial market; STAR Health covers limited youth BH",
     "2025: 1115 waiver alternative under federal negotiation; large commercial opportunity despite Medicaid exclusion"),

    ("UT", "Utah", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded via limited waiver; IOP coverage improving under managed care; growing population",
     "2025: Full Medicaid expansion scope still restricted; BH crisis system funding; telehealth parity bill advancing"),

    ("VT", "Vermont", 8, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; Green Mountain Care Board all-payer model includes behavioral health; strong BH infrastructure",
     "2025: All-payer model active; telehealth permanence confirmed; strong reimbursement environment"),

    ("VA", "Virginia", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded (2019); strong parity enforcement; DMAS covers IOP via Medallion 4.0; $200M+ BH budget",
     "2025: BH budget investments active; IOP reimbursement rates increased; growing suburban/rural virtual care demand"),

    ("WA", "Washington", 9, True, True, True,
     "Nation-leading telehealth parity",
     "Medicaid expanded; Apple Health covers IOP broadly; nation's strongest telehealth parity laws; CH well-established",
     "2025: BH crisis system expansion funded; Medicaid rates increased; new IOP billing codes clarified"),

    ("WV", "West Virginia", 5, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; highest SUD rate in nation = high need; CH not active; rural access gaps throughout",
     "2025: SUD crisis response investments; telehealth access improvements; untapped market with high clinical need"),

    ("WI", "Wisconsin", 6, False, True, False,
     "Moderate telehealth parity; partial Medicaid (BadgerCare only)",
     "NOT full ACA expansion — BadgerCare covers limited adult population; IOP reimbursement available but Medicaid reach limited",
     "2025: Expansion repeatedly blocked by legislature; BadgerCare rate increases; strong commercial density compensates"),

    ("WY", "Wyoming", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; smallest state by population; limited commercial market; CH active but low volume",
     "2025: Expansion failed; telehealth licensing compact joined; minimal near-term Medicaid opportunity"),
]

# Adult population (18+) estimates — US Census 2024
# SMI rates — SAMHSA 2023 National Survey on Drug Use and Health
# IOP-eligible: ~15% of SMI population requires IOP-level care
# Medicaid % of addressable: 35% in expanded states, 20% in non-expanded, 25% in partial
_POPULATION_DATA = {
    "AL": {"adult_pop": 3_800_000, "smi_rate": 0.057},
    "AK": {"adult_pop": 555_000,   "smi_rate": 0.070},
    "AZ": {"adult_pop": 5_900_000, "smi_rate": 0.056},
    "AR": {"adult_pop": 2_200_000, "smi_rate": 0.058},
    "CA": {"adult_pop": 30_200_000,"smi_rate": 0.054},
    "CO": {"adult_pop": 4_700_000, "smi_rate": 0.058},
    "CT": {"adult_pop": 2_900_000, "smi_rate": 0.050},
    "DE": {"adult_pop": 850_000,   "smi_rate": 0.055},
    "FL": {"adult_pop": 17_200_000,"smi_rate": 0.053},
    "GA": {"adult_pop": 8_300_000, "smi_rate": 0.054},
    "HI": {"adult_pop": 1_100_000, "smi_rate": 0.045},
    "ID": {"adult_pop": 1_500_000, "smi_rate": 0.059},
    "IL": {"adult_pop": 9_800_000, "smi_rate": 0.056},
    "IN": {"adult_pop": 5_200_000, "smi_rate": 0.058},
    "IA": {"adult_pop": 2_500_000, "smi_rate": 0.055},
    "KS": {"adult_pop": 2_200_000, "smi_rate": 0.056},
    "KY": {"adult_pop": 3_400_000, "smi_rate": 0.063},
    "LA": {"adult_pop": 3_500_000, "smi_rate": 0.057},
    "ME": {"adult_pop": 1_100_000, "smi_rate": 0.065},
    "MD": {"adult_pop": 5_000_000, "smi_rate": 0.053},
    "MA": {"adult_pop": 5_600_000, "smi_rate": 0.055},
    "MI": {"adult_pop": 7_700_000, "smi_rate": 0.058},
    "MN": {"adult_pop": 4_500_000, "smi_rate": 0.054},
    "MS": {"adult_pop": 2_200_000, "smi_rate": 0.058},
    "MO": {"adult_pop": 4_900_000, "smi_rate": 0.058},
    "MT": {"adult_pop": 850_000,   "smi_rate": 0.070},
    "NE": {"adult_pop": 1_500_000, "smi_rate": 0.055},
    "NV": {"adult_pop": 2_600_000, "smi_rate": 0.057},
    "NH": {"adult_pop": 1_100_000, "smi_rate": 0.056},
    "NJ": {"adult_pop": 7_200_000, "smi_rate": 0.051},
    "NM": {"adult_pop": 1_600_000, "smi_rate": 0.065},
    "NY": {"adult_pop": 15_500_000,"smi_rate": 0.053},
    "NC": {"adult_pop": 8_600_000, "smi_rate": 0.055},
    "ND": {"adult_pop": 600_000,   "smi_rate": 0.057},
    "OH": {"adult_pop": 9_000_000, "smi_rate": 0.059},
    "OK": {"adult_pop": 3_000_000, "smi_rate": 0.060},
    "OR": {"adult_pop": 3_400_000, "smi_rate": 0.065},
    "PA": {"adult_pop": 10_100_000,"smi_rate": 0.057},
    "RI": {"adult_pop": 870_000,   "smi_rate": 0.055},
    "SC": {"adult_pop": 4_100_000, "smi_rate": 0.054},
    "SD": {"adult_pop": 700_000,   "smi_rate": 0.056},
    "TN": {"adult_pop": 5_500_000, "smi_rate": 0.057},
    "TX": {"adult_pop": 22_100_000,"smi_rate": 0.053},
    "UT": {"adult_pop": 2_600_000, "smi_rate": 0.045},
    "VT": {"adult_pop": 520_000,   "smi_rate": 0.063},
    "VA": {"adult_pop": 6_800_000, "smi_rate": 0.053},
    "WA": {"adult_pop": 6_300_000, "smi_rate": 0.058},
    "WV": {"adult_pop": 1_400_000, "smi_rate": 0.070},
    "WI": {"adult_pop": 4_700_000, "smi_rate": 0.055},
    "WY": {"adult_pop": 450_000,   "smi_rate": 0.057},
}

STATE_DATA = {
    abbr: {
        "name": name,
        "favorability_score": score,
        "medicaid_expanded": medicaid_expanded,
        "medicaid_status": "Expanded" if medicaid_expanded else "Not Expanded",
        "charlie_health_active": ch_active,
        "medicaid_covered": medicaid_covered,
        "telehealth_policy": telehealth,
        "key_regulatory_notes": notes,
        "recent_developments": recent,
        "adult_population": _POPULATION_DATA[abbr]["adult_pop"],
        "smi_rate": _POPULATION_DATA[abbr]["smi_rate"],
    }
    for (abbr, name, score, medicaid_expanded, ch_active, medicaid_covered,
         telehealth, notes, recent) in _STATES
}
