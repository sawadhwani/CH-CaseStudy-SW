# State data informed by:
# - Charlie Health locations page (March 2026): active in all states EXCEPT SD, KS, OK, AR, MS, AL, WV, ME, CT, RI
# - KFF Medicaid expansion tracker (2025)
# - CCHP State Telehealth Laws & Reimbursement Policies Report, Fall 2025
# - The Lund Report / Oregon Capital Chronicle reporting on Charlie Health Oregon controversy
# - CMS IOP billing guidance, state Medicaid agency updates
# Favorability scores (1–10): Medicaid expansion (+2), telehealth parity (+1), IOP reimbursement quality (+1),
# progressive BH policy (+1), no expansion (−2), active regulatory conflict (−2), restrictive licensing (−1)

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
     "Expanded via private option waiver; CH not active; complex MCO structure makes entry difficult; IOP coverage inconsistent across plans",
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
     "Medicaid expanded; HOWEVER out-of-state telehealth provider registration expired June 30, 2025 with no replacement — high barrier for CH entry as an out-of-state virtual provider",
     "2025: Telehealth registration lapse creates major licensing barrier; no legislation introduced to reinstate; monitor closely"),

    ("DE", "Delaware", 7, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; small state with concentrated payer relationships; IOP coverage available via DMAP managed care",
     "2025: DHSS launched behavioral health roadmap; Medicaid rate increases announced for BH providers"),

    ("FL", "Florida", 4, False, True, False,
     "Moderate telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; large commercial market; IOP coverage varies by payer; Baker Act reform ongoing; strong commercial opportunity despite Medicaid gap",
     "2025: Medicaid expansion ballot campaign active; telehealth licensing reciprocity improved; large uninsured coverage gap persists"),

    ("GA", "Georgia", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No full expansion; limited Pathways waiver has slow enrollment; commercial market exists but large Medicaid gap limits reach",
     "2025: Pathways waiver enrollment stagnant; full expansion repeatedly rejected by legislature"),

    ("HI", "Hawaii", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; island geography makes virtual IOP strategically important; QUEST Integration covers IOP",
     "2025: Telehealth parity legislation strengthened; behavioral health provider shortage addressed via virtual-first policy"),

    ("ID", "Idaho", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020 ballot initiative); regulatory environment improving; IOP provider shortage creates demand opportunity",
     "2025: Medicaid managed care contracts include expanded telehealth; IOP prior auth requirements updated"),

    ("IL", "Illinois", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; HB2595 strengthened parity enforcement; IOP well-reimbursed via Medicaid managed care; strong state BH infrastructure",
     "2025: Mental health workforce expansion bill passed; Medicaid rates increased ~10% for behavioral health services"),

    ("IN", "Indiana", 6, True, True, True,
     "Moderate parity; HIP 2.0 waiver structure",
     "Expanded via HIP 2.0 waiver; complex eligibility rules; IOP reimbursement available but navigating multiple MCO contracts required",
     "2025: HIP reauthorization includes expanded behavioral health benefits; telehealth rules updated to clarify IOP coverage"),

    ("IA", "Iowa", 7, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; Iowa Health Link MCO structure; IOP reimbursement in place; strong rural virtual care demand",
     "2025: Managed care oversight reforms; behavioral health crisis funding increased"),

    ("KS", "Kansas", 5, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2022); implementation still maturing; CH not yet active; IOP coverage developing under KanCare",
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
     "Medicaid expanded (2019 ballot initiative); MaineCare covers behavioral health broadly; rural population = high virtual IOP demand; CH not active despite favorable environment",
     "2025: Crisis receiving center network expanding; telehealth permanence legislation passed; strong expansion opportunity for CH"),

    ("MD", "Maryland", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; HealthChoice MCO covers IOP well; strong parity enforcement; high commercial insurance penetration",
     "2025: Medicaid rate increases for behavioral health; crisis system transformation funded; BH integration initiative"),

    ("MA", "Massachusetts", 9, True, True, True,
     "Nation-leading telehealth and parity laws",
     "Medicaid expanded; Chapter 224 parity law among nation's strongest; MassHealth covers virtual IOP; BHSA carve-out improving access",
     "2025: Mental health access commission recommendations adopted; BHSA operational; strong reimbursement environment"),

    ("MI", "Michigan", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; integrated BH/physical health managed care; IOP reimbursement strong; active state BH infrastructure",
     "2025: Behavioral health integration transformation ongoing; Medicaid rates increased for IOP services"),

    ("MN", "Minnesota", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; strong DHS behavioral health infrastructure; good IOP reimbursement; high commercial coverage rates",
     "2025: Behavioral health workforce bill passed; crisis system investments $150M+; IOP capacity expanding"),

    ("MS", "Mississippi", 2, False, False, False,
     "Minimal telehealth parity",
     "No Medicaid expansion — last major holdout; very limited commercial IOP coverage; poorest state BH infrastructure nationally",
     "2025: Expansion again rejected by legislature; governor opposed; significant coverage gap leaves 200K+ uninsured"),

    ("MO", "Missouri", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2021 ballot initiative); MO HealthNet implementation maturing; MCO contracting complex but manageable",
     "2025: MO HealthNet expansion stabilizing; behavioral health integration improving; IOP reimbursement clarified"),

    ("MT", "Montana", 6, True, True, True,
     "Moderate telehealth parity",
     "Medicaid expanded; rural state with high behavioral health need; IOP reimbursement in place; Charlie Health's home state",
     "2025: Medicaid expansion reauthorized by legislature; rural telehealth investments; CH well-positioned as Montana-based company"),

    ("NE", "Nebraska", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020); Heritage Health managed care; IOP coverage developing; rural access gaps present",
     "2025: MCO contracts updated to include virtual behavioral health; IOP prior authorization requirements loosened"),

    ("NV", "Nevada", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; SB292 strengthened telehealth parity; IOP reimbursement solid; growing population with rising BH demand",
     "2025: Behavioral health workforce expansion; AI therapy regulation passed (restricts chatbot-only care, favors CH's human-led model)"),

    ("NH", "New Hampshire", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded via NHHPP waiver; small state with concentrated payer relationships; strong SUD treatment infrastructure",
     "2025: Medicaid expansion reauthorized; SUD + mental health integration expanding; telehealth parity confirmed"),

    ("NJ", "New Jersey", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; NJ FamilyCare covers IOP; strong parity enforcement; high commercial insurance density",
     "2025: Behavioral health crisis services expansion funded; Medicaid rate increases for IOP; dense commercial market"),

    ("NM", "New Mexico", 7, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; Centennial Care 2.0 covers behavioral health broadly; rural access need favors virtual IOP",
     "2025: Behavioral health system transformation ongoing; IOP reimbursement improved under MCO contracts"),

    ("NY", "New York", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MHPAEA enforcement strong; OMH investments in virtual care; large commercial market",
     "2025: 1115 waiver for social determinants active; OMH virtual care investments; strong IOP reimbursement via managed care"),

    ("NC", "North Carolina", 7, True, True, True,
     "Strong telehealth parity",
     "Expanded Medicaid (December 2023); Medicaid Transformation to managed care; behavioral health carve-in active; enrollment exceeding projections",
     "2025: Medicaid expansion enrollment surpassing forecasts; behavioral health MCO contracts operational; strong growth opportunity"),

    ("ND", "North Dakota", 6, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; Sanford/Essentia dominate market; IOP coverage available; rural state favors virtual delivery",
     "2025: Telehealth permanence bill signed; behavioral health workforce investments; rural access gap creates demand"),

    ("OH", "Ohio", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; OhioRISE for youth behavioral health; IOP well-reimbursed; strong managed care infrastructure",
     "2025: OhioRISE expansion ongoing; Medicaid managed care rebid completed; behavioral health rates increased"),

    ("OK", "Oklahoma", 4, True, False, False,
     "Moderate parity; early expansion implementation",
     "Expanded Medicaid (2021 SQ820); CH not active; SoonerCare implementation still maturing; IOP billing guidance still evolving",
     "2025: SoonerCare enrollment growing; behavioral health services expanding; near-term entry opportunity for CH"),

    ("OR", "Oregon", 6, True, True, True,
     "Strong parity laws; ACTIVE REGULATORY CONFLICT with Charlie Health",
     "MAJOR ISSUE: OHA investigating CH for using out-of-state unlicensed providers while billing $85M+ to Oregon Medicaid; CH launched misleading ad campaign; Gov. Kotek publicly criticized CH; lawmakers pushed OHA to probe CH; CH could resolve by using Oregon-licensed providers but has resisted",
     "2025: OHA considering termination of CH operating agreement; Trauma Informed Oregon published critical report; 'Save Virtual Care OR' campaign run by CH called misleading by governor; June 2025 corporate healthcare influence bill signed — nation's strictest"),

    ("PA", "Pennsylvania", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MA HealthChoices MCO covers IOP well; strong parity enforcement; large commercial market",
     "2025: Medicaid managed care rebid completed; behavioral health crisis system investments; IOP reimbursement stable"),

    ("RI", "Rhode Island", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; small state, concentrated market; HealthSource RI covers behavioral health; CH not active despite favorable environment",
     "2025: Behavioral health workforce bill passed; Medicaid IOP reimbursement updated; strong expansion opportunity for CH"),

    ("SC", "South Carolina", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; large coverage gap; commercial market exists but limited BH reimbursement",
     "2025: Expansion bill introduced but failed; telehealth licensing compact joined but no parity law; large underserved population"),

    ("SD", "South Dakota", 5, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2023 ballot initiative); implementation in early stages; IOP coverage framework developing; CH not active",
     "2025: First full year of expansion; enrollment growing; behavioral health provider network building; entry opportunity"),

    ("TN", "Tennessee", 4, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; TennCare limited to narrow populations; large commercial market; CH active for commercial payers only",
     "2025: TennCare waiver revision under federal review; expansion rejected again; CH commercial-only market"),

    ("TX", "Texas", 4, False, True, False,
     "Moderate telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; largest coverage gap nationally; large commercial market; STAR Health covers limited youth behavioral health",
     "2025: 1115 waiver alternative to expansion under federal negotiation; large commercial opportunity despite Medicaid exclusion"),

    ("UT", "Utah", 6, True, True, False,
     "Moderate telehealth parity",
     "Expanded via limited waiver (Medicaid expansion phased); full expansion limited; IOP coverage improving under managed care",
     "2025: Full Medicaid expansion scope still restricted; behavioral health crisis system funding; telehealth parity bill advancing"),

    ("VT", "Vermont", 8, True, True, False,
     "Strong telehealth parity",
     "Medicaid expanded; Green Mountain Care Board all-payer model includes behavioral health; strong BH infrastructure",
     "2025: All-payer model active; telehealth permanence confirmed; strong reimbursement environment for virtual IOP"),

    ("VA", "Virginia", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded (2019); strong parity enforcement; DMAS covers IOP via Medallion 4.0; $200M+ BH budget investments",
     "2025: BH budget investments active; IOP reimbursement rates increased; growing suburban/rural virtual care demand"),

    ("WA", "Washington", 9, True, True, True,
     "Nation-leading telehealth parity",
     "Medicaid expanded; Apple Health covers IOP broadly; some of nation's strongest telehealth parity laws; CH well-established",
     "2025: Behavioral health crisis system expansion funded; Medicaid rates increased; new IOP billing codes clarified"),

    ("WV", "West Virginia", 5, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; highest SUD rate in nation = high need; CH not active; WV Medicaid covers BH; rural access gaps throughout",
     "2025: SUD crisis response investments; telehealth access improvements; untapped market with high clinical need"),

    ("WI", "Wisconsin", 6, False, True, False,
     "Moderate telehealth parity; partial Medicaid (BadgerCare only)",
     "NOT full ACA expansion — BadgerCare covers limited adult population; IOP reimbursement available but Medicaid reach limited; strong commercial market",
     "2025: Medicaid expansion repeatedly blocked by legislature; BadgerCare rate increases; strong commercial insurance density compensates"),

    ("WY", "Wyoming", 3, False, True, False,
     "Limited telehealth parity; no Medicaid expansion",
     "No Medicaid expansion; smallest state by population; limited commercial market; CH active but low volume expected",
     "2025: Expansion legislation failed; telehealth licensing compact joined; minimal near-term Medicaid opportunity"),
]

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
    }
    for (abbr, name, score, medicaid_expanded, ch_active, medicaid_covered,
         telehealth, notes, recent) in _STATES
}
