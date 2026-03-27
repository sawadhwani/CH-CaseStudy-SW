# Illustrative data for demo purposes — scores based on Medicaid expansion status,
# telehealth parity laws, and behavioral health reimbursement environment.

_STATES = [
    # (abbr, name, score, medicaid_expanded, ch_active, medicaid_covered,
    #  telehealth_policy, key_regulatory_notes, recent_developments)
    ("AL", "Alabama", 2, False, False, False,
     "Limited telehealth parity",
     "No Medicaid expansion; restrictive IOP billing rules; weak mental health parity enforcement",
     "2024: Expansion bill failed again in legislature; some telehealth billing reforms stalled"),

    ("AK", "Alaska", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; remote-first regulations suit virtual IOP; low population density = high unmet need",
     "2024: Pandemic telehealth provisions made permanent; Medicaid managed care overhaul underway"),

    ("AZ", "Arizona", 7, True, True, True,
     "Moderate telehealth parity",
     "Medicaid expanded (2013); AHCCCS covers behavioral health broadly; IOP reimbursement improving",
     "2024: New behavioral health workforce initiative; increased IOP reimbursement rates proposed"),

    ("AR", "Arkansas", 5, True, False, False,
     "Moderate parity, complex waiver structure",
     "Expanded via private option waiver; complex managed care structure; IOP coverage inconsistent",
     "2024: Work requirements waiver under review; telehealth billing guidance updated"),

    ("CA", "California", 9, True, True, True,
     "Nation-leading telehealth parity",
     "Medi-Cal covers virtual IOP; strong mental health parity; SB 855 dramatically expanded coverage",
     "2024: CalAIM expansion continues; Medi-Cal behavioral health carve-in rolling out statewide"),

    ("CO", "Colorado", 9, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; SB21-137 expanded behavioral health access; robust IOP reimbursement",
     "2024: Behavioral Health Administration launched; new crisis system funding $400M+"),

    ("CT", "Connecticut", 8, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; strong mental health laws; HUSKY covers behavioral health broadly",
     "2024: Telehealth permanence legislation passed; new youth mental health initiative"),

    ("DE", "Delaware", 7, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; small state with concentrated payer relationships; IOP coverage in place",
     "2024: DHSS launched behavioral health roadmap; Medicaid rate increases announced"),

    ("FL", "Florida", 4, False, True, False,
     "Moderate telehealth parity, no Medicaid expansion",
     "No Medicaid expansion; large commercial market; IOP coverage varies by payer; Baker Act reform ongoing",
     "2024: Medicaid expansion ballot measure campaign underway; telehealth licensing reciprocity improved"),

    ("GA", "Georgia", 3, False, True, False,
     "Limited telehealth parity",
     "No full expansion; limited waiver program; commercial market exists but Medicaid gap large",
     "2024: Pathways waiver (limited expansion) enrollment slow; legislature rejected full expansion"),

    ("HI", "Hawaii", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; unique island geography favors telehealth; QUEST Integration covers IOP",
     "2024: Telehealth reimbursement parity legislation strengthened; behavioral health shortage addressed"),

    ("ID", "Idaho", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020 ballot initiative); regulatory environment improving for virtual care",
     "2024: Medicaid managed care contracts updated to include telehealth; IOP provider shortage"),

    ("IL", "Illinois", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; HB2595 strengthened parity enforcement; IOP well-reimbursed via Medicaid",
     "2024: Mental health workforce expansion bill passed; Medicaid rates increased 10%"),

    ("IN", "Indiana", 6, True, True, False,
     "Moderate parity, HIP waiver structure",
     "Expanded via HIP 2.0 waiver; complex eligibility; IOP reimbursement available but navigating MCOs required",
     "2024: HIP reauthorization includes expanded behavioral health benefits; telehealth rules updated"),

    ("IA", "Iowa", 7, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; IA Health Link managed care; IOP reimbursement in place",
     "2024: Managed care oversight reforms; behavioral health crisis funding increased"),

    ("KS", "Kansas", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2022); early implementation phase; IOP coverage establishing",
     "2024: KanCare expansion rollout; behavioral health community mental health centers expanding"),

    ("KY", "Kentucky", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; KCHIP covers youth; strong legislative support for behavioral health",
     "2024: Behavioral health safety net investments; telehealth parity bill signed"),

    ("LA", "Louisiana", 6, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded (2016); Medicaid managed care covers IOP; rural access gaps present",
     "2024: Medicaid redetermination impact; telehealth billing guidance updated for IOP"),

    ("ME", "Maine", 7, True, False, False,
     "Strong telehealth parity",
     "Expanded Medicaid (2019 ballot initiative); MaineCare covers behavioral health; rural focus",
     "2024: Crisis receiving center network expansion; telehealth permanence legislation"),

    ("MD", "Maryland", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; Maryland has strong parity enforcement; HealthChoice covers IOP well",
     "2024: Medicaid rate increases for behavioral health; crisis system transformation funded"),

    ("MA", "Massachusetts", 9, True, True, True,
     "Nation-leading telehealth and parity laws",
     "Medicaid expanded; Chapter 224 parity law strongest in nation; MassHealth covers virtual IOP",
     "2024: BHSA carve-out to MassHealth; mental health access commission recommendations adopted"),

    ("MI", "Michigan", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; Michigan has integrated behavioral/physical health managed care",
     "2024: Behavioral health integration transformation; Medicaid rates increased for IOP"),

    ("MN", "Minnesota", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; strong DHS behavioral health infrastructure; good IOP reimbursement",
     "2024: Behavioral health workforce bill passed; crisis system investments $150M"),

    ("MS", "Mississippi", 2, False, False, False,
     "Minimal telehealth parity",
     "No Medicaid expansion; last state holdout; very limited commercial IOP coverage",
     "2024: Expansion legislation again failed; governor opposed; significant coverage gap remains"),

    ("MO", "Missouri", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2021 ballot initiative); implementation still maturing; MCO contracting complex",
     "2024: MO HealthNet expansion ongoing; behavioral health integration improving"),

    ("MT", "Montana", 6, True, True, False,
     "Moderate telehealth parity",
     "Medicaid expanded; rural state with high behavioral health need; IOP reimbursement in place",
     "2024: Medicaid expansion reauthorized; rural telehealth investments"),

    ("NE", "Nebraska", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2020); Heritage Health managed care; IOP coverage developing",
     "2024: MCO contracts updated; behavioral health access plan released"),

    ("NV", "Nevada", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; SB292 strengthened telehealth parity; IOP reimbursement solid",
     "2024: Behavioral health workforce shortage addressed via new training programs"),

    ("NH", "New Hampshire", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded via NHHPP waiver; small state, concentrated payer relationships",
     "2024: Medicaid expansion reauthorized; SUD treatment expansion"),

    ("NJ", "New Jersey", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; NJ FamilyCare covers IOP; strong parity enforcement",
     "2024: Behavioral health crisis services expansion; Medicaid rate increases"),

    ("NM", "New Mexico", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; Centennial Care 2.0 covers behavioral health broadly; rural access need",
     "2024: Behavioral health system transformation; IOP reimbursement improved"),

    ("NY", "New York", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MHPAEA enforcement strong; Medicaid covers IOP well via managed care",
     "2024: 1115 waiver for social determinants; OMH investments in virtual care"),

    ("NC", "North Carolina", 7, True, True, True,
     "Strong telehealth parity",
     "Expanded Medicaid (2023); Medicaid Transformation to managed care; behavioral health carve-in",
     "2024: Medicaid expansion enrollment exceeding projections; behavioral health managed care launched"),

    ("ND", "North Dakota", 6, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; Sanford/Essentia dominant market; IOP coverage available",
     "2024: Telehealth permanence bill signed; behavioral health workforce investments"),

    ("OH", "Ohio", 7, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; OhioRISE for youth behavioral health; IOP well-reimbursed",
     "2024: OhioRISE expansion; Medicaid managed care rebid; behavioral health rates increased"),

    ("OK", "Oklahoma", 5, True, False, False,
     "Moderate parity, early expansion",
     "Expanded Medicaid (2021 SQ820); implementation still maturing; IOP billing guidance evolving",
     "2024: SoonerCare expansion enrollment growing; behavioral health services expanding"),

    ("OR", "Oregon", 8, True, True, True,
     "Nation-leading telehealth parity",
     "Medicaid expanded; OHA Behavioral Health Division active; CCO model covers IOP well",
     "2024: Measure 110 recriminalization impact; OHA behavioral health investments"),

    ("PA", "Pennsylvania", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded; MA HealthChoices covers IOP; strong parity enforcement",
     "2024: Medicaid managed care rebid; behavioral health crisis system investments"),

    ("RI", "Rhode Island", 8, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; small state, concentrated market; HealthSource RI covers behavioral health",
     "2024: Behavioral health workforce bill; Medicaid IOP reimbursement updated"),

    ("SC", "South Carolina", 3, False, False, False,
     "Limited telehealth parity",
     "No Medicaid expansion; large coverage gap; commercial market exists but limited",
     "2024: Expansion bill introduced but unlikely to pass; telehealth licensing update"),

    ("SD", "South Dakota", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded Medicaid (2023 ballot initiative); implementation beginning; IOP coverage developing",
     "2024: First year of expansion; enrollment growing; behavioral health provider network building"),

    ("TN", "Tennessee", 3, False, False, False,
     "Limited telehealth parity",
     "No Medicaid expansion; TennCare limited to narrow populations; large coverage gap",
     "2024: Legislature rejected expansion; TennCare waiver revision under federal review"),

    ("TX", "Texas", 4, False, True, False,
     "Moderate telehealth parity, no Medicaid expansion",
     "No expansion; large commercial market; Medicaid limited; STAR Health covers some youth behavioral health",
     "2024: 1115 waiver for Medicaid expansion alternative under negotiation; large uninsured population"),

    ("UT", "Utah", 6, True, False, False,
     "Moderate telehealth parity",
     "Expanded via limited waiver (2020); full expansion phased; IOP coverage improving",
     "2024: Full Medicaid expansion still limited; behavioral health crisis system funding"),

    ("VT", "Vermont", 8, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded; Green Mountain Care Board; strong behavioral health infrastructure",
     "2024: All-payer model includes behavioral health; telehealth permanence"),

    ("VA", "Virginia", 8, True, True, True,
     "Strong telehealth parity",
     "Medicaid expanded (2019); strong parity enforcement; DMAS covers IOP via Medallion 4.0",
     "2024: Behavioral health budget investments $200M+; IOP reimbursement rates increased"),

    ("WA", "Washington", 9, True, True, True,
     "Nation-leading telehealth parity",
     "Medicaid expanded; Apple Health covers IOP broadly; strong telehealth parity laws",
     "2024: Behavioral health crisis system expansion; Medicaid rates increased; new IOP billing codes"),

    ("WV", "West Virginia", 6, True, False, False,
     "Moderate telehealth parity",
     "Medicaid expanded; high SUD need; WV Medicaid covers behavioral health; rural access gaps",
     "2024: SUD crisis response investments; telehealth access improvements"),

    ("WI", "Wisconsin", 7, True, False, False,
     "Strong telehealth parity",
     "Medicaid expanded (partial via BadgerCare waiver); IOP reimbursement available",
     "2024: Medicaid rate increases; behavioral health workforce bill signed"),

    ("WY", "Wyoming", 3, False, True, False,
     "Limited telehealth parity",
     "No Medicaid expansion; smallest state by population; limited commercial market",
     "2024: Expansion legislation failed; telehealth licensing compact joined"),
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
