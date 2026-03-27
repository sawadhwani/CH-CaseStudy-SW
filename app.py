import os
from datetime import date
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from anthropic import Anthropic
from state_data import STATE_DATA

st.set_page_config(
    page_title="State Expansion Intelligence | Charlie Health",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container { padding-top: 1.5rem; }
    [data-testid="stMetric"] {
        background-color: #1B4F9B;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    [data-testid="stMetricLabel"] p,
    [data-testid="stMetricLabel"] { color: white !important; opacity: 0.85; }
    [data-testid="stMetricValue"] { color: white !important; }
</style>
""", unsafe_allow_html=True)


# ── API client ────────────────────────────────────────────────────────────────

def get_client() -> Anthropic:
    key = (
        st.session_state.get("api_key")
        or st.secrets.get("ANTHROPIC_API_KEY", None)
        or os.environ.get("ANTHROPIC_API_KEY", None)
    )
    if not key:
        st.error("No API key found. Enter your Anthropic API key in the sidebar.")
        st.stop()
    return Anthropic(api_key=key)


# ── Data ──────────────────────────────────────────────────────────────────────

def build_dataframe() -> pd.DataFrame:
    return pd.DataFrame([
        {
            "abbr": abbr,
            "name": d["name"],
            "score": d["favorability_score"],
            "medicaid": d["medicaid_status"],
            "ch_active": "Active" if d["charlie_health_active"] else "Not active",
            "medicaid_covered": "Yes" if d["medicaid_covered"] else "No",
        }
        for abbr, d in STATE_DATA.items()
    ])


# ── Opportunity model ─────────────────────────────────────────────────────────
# Addressable IOP patients = adult_pop × smi_rate × 15% (IOP-eligible share of SMI)
# Medicaid split: 35% of addressable in expanded states, 20% in non-expanded, 25% partial (WI)
# Revenue: $12,000/Medicaid patient · $18,000/commercial patient
# Sources: SAMHSA 2023 NSDUH, CMS IOP billing data, industry benchmarks

def compute_opportunity(abbr: str) -> dict:
    d = STATE_DATA[abbr]
    adult_pop   = d["adult_population"]
    smi_rate    = d["smi_rate"]
    expanded    = d["medicaid_expanded"]
    partial     = (abbr == "WI")

    addressable = adult_pop * smi_rate * 0.15
    medicaid_pct = 0.35 if expanded else (0.25 if partial else 0.20)

    medicaid_pop    = round(addressable * medicaid_pct)
    commercial_pop  = round(addressable * (1 - medicaid_pct))
    medicaid_rev    = medicaid_pop * 12_000
    commercial_rev  = commercial_pop * 18_000

    return {
        "addressable":    round(addressable),
        "medicaid_pop":   medicaid_pop,
        "commercial_pop": commercial_pop,
        "medicaid_rev":   medicaid_rev,
        "commercial_rev": commercial_rev,
        "total_rev":      medicaid_rev + commercial_rev,
    }


# ── Map ───────────────────────────────────────────────────────────────────────

# ── News feed (static placeholder — production would pull from RSS/news API) ──

NEWS_FEED = [
    {
        "tag": "Federal",
        "tag_color": "#1B4F9B",
        "title": "CMS Extends Telehealth Behavioral Health Flexibilities Through 2026",
        "source": "CMS.gov",
        "date": "Mar 15, 2026",
        "summary": "CMS finalized extensions allowing audio-only IOP sessions and home-based originating sites for behavioral health through 2026, providing regulatory continuity for virtual IOP providers.",
        "url": "https://www.cms.gov/newsroom/fact-sheets/cy-2025-medicare-hospital-outpatient-prospective-payment-system-ambulatory-surgical-center-payment",
    },
    {
        "tag": "Oregon",
        "tag_color": "#c0392b",
        "title": "Oregon OHA Investigating Charlie Health Over Unlicensed Provider Billing",
        "source": "The Lund Report",
        "date": "Feb 2026",
        "summary": "Oregon Health Authority is reviewing Charlie Health's operating agreement after finding the company billed $85M+ to Oregon Medicaid using providers not licensed in-state. Gov. Kotek called CH's public pressure campaign 'misleading.'",
        "url": "https://www.thelundreport.org/content/kotek-calls-telehealth-pressure-campaign-misleading",
    },
    {
        "tag": "Federal",
        "tag_color": "#1B4F9B",
        "title": "HR1 Reconciliation Bill Includes Medicaid Work Requirements Starting 2027",
        "source": "KFF Health News",
        "date": "Mar 10, 2026",
        "summary": "House budget reconciliation proposes 80 hrs/month community engagement requirements for Medicaid expansion enrollees, potentially reducing the addressable Medicaid population for behavioral health providers.",
        "url": "https://ccf.georgetown.edu/2025/11/10/the-future-of-acas-medicaid-expansion-what-do-changes-in-hr1-mean/",
    },
    {
        "tag": "Connecticut",
        "tag_color": "#7f8c8d",
        "title": "Connecticut Out-of-State Telehealth Registration Expired With No Replacement",
        "source": "CCHP",
        "date": "Jan 2026",
        "summary": "CT's temporary out-of-state telehealth provider registration expired June 30, 2025. No replacement legislation has been introduced, creating a significant licensing barrier for virtual-only providers like Charlie Health.",
        "url": "https://www.cchpca.org/resources/state-telehealth-laws-and-reimbursement-policies-report-fall-2025/",
    },
    {
        "tag": "Federal",
        "tag_color": "#1B4F9B",
        "title": "Only 23 States Have Full Medicaid Telehealth Payment Parity as of Fall 2025",
        "source": "CCHP State Telehealth Report",
        "date": "Nov 2025",
        "summary": "CCHP's Fall 2025 report finds 23 states have implemented telehealth payment parity, 5 have parity with caveats, and 22 states have no parity requirement — directly affecting IOP reimbursement rates in key markets.",
        "url": "https://www.cchpca.org/resources/state-telehealth-laws-and-reimbursement-policies-report-fall-2025/",
    },
]


def render_newsfeed():
    st.markdown("#### 📰 Live Newsfeed")
    st.caption("Behavioral health & virtual IOP policy news · Static placeholder — production version pulls live from RSS")
    for article in NEWS_FEED:
        with st.container(border=True):
            col_tag, col_meta = st.columns([1, 4])
            col_tag.markdown(
                f'<span style="background:{article["tag_color"]};color:white;'
                f'padding:2px 8px;border-radius:4px;font-size:0.75rem;font-weight:600;">'
                f'{article["tag"]}</span>',
                unsafe_allow_html=True,
            )
            col_meta.caption(f"{article['source']}  ·  {article['date']}")
            st.markdown(f"**[{article['title']}]({article['url']})**")
            st.caption(article["summary"])


# ── Stakeholder tracker ───────────────────────────────────────────────────────

_STAKEHOLDERS_DEFAULT = pd.DataFrame([
    {
        "Name": "Dr. Sarah Mitchell",
        "Title": "Medical Director, Behavioral Health",
        "Organization": "Oregon Health Authority",
        "State": "OR",
        "Last Contact": date(2025, 1, 14),
        "Notes": "Discussed CH licensing concerns re: out-of-state providers. Follow up on OHA operating agreement review status and timeline.",
    },
    {
        "Name": "James Kowalski",
        "Title": "Director, Office of MaineCare Services",
        "Organization": "Maine DHHS",
        "State": "ME",
        "Last Contact": date(2026, 2, 3),
        "Notes": "Expressed strong interest in virtual IOP for rural populations. Requested CH capability deck and Medicaid credentialing timeline.",
    },
    {
        "Name": "Rachel Torres",
        "Title": "VP, Behavioral Health Strategy",
        "Organization": "Blue Cross Blue Shield of Massachusetts",
        "State": "MA",
        "Last Contact": date(2026, 1, 15),
        "Notes": "Contract renewal discussion in progress. Flagged interest in expanded adolescent IOP slots for Q3 2026.",
    },
    {
        "Name": "Dr. Marcus Webb",
        "Title": "Chief Medical Officer",
        "Organization": "OhioRISE / Aetna Better Health of Ohio",
        "State": "OH",
        "Last Contact": date(2025, 12, 8),
        "Notes": "OhioRISE expansion creating new referral opportunities for youth IOP. Follow up on updated billing codes effective Jan 2026.",
    },
    {
        "Name": "Linda Chen",
        "Title": "Director, Telehealth Policy",
        "Organization": "California DHCS",
        "State": "CA",
        "Last Contact": date(2025, 10, 22),
        "Notes": "CalAIM carve-in implementation update. Discussed prior auth requirements for virtual IOP under new managed care contracts.",
    },
    {
        "Name": "Tom Harrington",
        "Title": "Executive Director",
        "Organization": "Kansas Behavioral Health Coalition",
        "State": "KS",
        "Last Contact": date(2024, 11, 14),
        "Notes": "KanCare expansion still maturing. Tom is key connector to KS Medicaid MCOs. Schedule follow-up once CH evaluates KS entry timeline.",
    },
    {
        "Name": "Dr. Priya Nair",
        "Title": "Medical Director, Behavioral Health",
        "Organization": "AHCCCS (Arizona Medicaid)",
        "State": "AZ",
        "Last Contact": date(2025, 4, 30),
        "Notes": "Positive relationship. Discussed IOP reimbursement rate increases. Intro to AHCCCS network adequacy team pending.",
    },
    {
        "Name": "Senator Michael Brooks",
        "Title": "Chair, Senate Health Committee",
        "Organization": "West Virginia Legislature",
        "State": "WV",
        "Last Contact": date(2024, 8, 22),
        "Notes": "Supportive of virtual BH access given WV SUD crisis. CH not yet active in WV — follow up on entry feasibility and legislative support.",
    },
    {
        "Name": "Jennifer Walsh",
        "Title": "VP, Network Development",
        "Organization": "ConnectiCare (CT Medicaid MCO)",
        "State": "CT",
        "Last Contact": date(2024, 9, 5),
        "Notes": "CT out-of-state telehealth registration expired June 2025. Confirm current licensing pathway before re-engaging on network contracting.",
    },
    {
        "Name": "Dr. Carlos Mendez",
        "Title": "Associate Commissioner, Behavioral Health",
        "Organization": "Texas Health & Human Services",
        "State": "TX",
        "Last Contact": date(2024, 6, 18),
        "Notes": "TX commercial market remains primary opportunity given no Medicaid expansion. Discussed STAR Health youth BH contracts as potential entry point.",
    },
])


def render_stakeholder_tracker():
    st.markdown("#### 👥 Key Stakeholder Follow-ups")
    st.caption("Last contact dates editable inline · 🔴 = no contact in 12+ months · Notes auto-save during session")

    if "stakeholders" not in st.session_state:
        st.session_state["stakeholders"] = _STAKEHOLDERS_DEFAULT.copy()

    today = date.today()

    def status(last_contact):
        if pd.isna(last_contact):
            return "⚪ Unknown"
        days = (today - last_contact).days
        if days > 365:
            return f"🔴 {days // 30}mo ago"
        if days > 180:
            return f"🟡 {days // 30}mo ago"
        return f"🟢 {days}d ago"

    display = st.session_state["stakeholders"].copy()
    display.insert(0, "Status", display["Last Contact"].apply(status))

    edited = st.data_editor(
        display,
        column_config={
            "Status":       st.column_config.TextColumn("Status",       disabled=True, width=130),
            "Name":         st.column_config.TextColumn("Name",         disabled=True, width=170),
            "Title":        st.column_config.TextColumn("Title",        disabled=True, width=220),
            "Organization": st.column_config.TextColumn("Organization", disabled=True, width=220),
            "State":        st.column_config.TextColumn("State",        disabled=True, width=60),
            "Last Contact": st.column_config.DateColumn("Last Contact", format="MMM D, YYYY", width=130),
            "Notes":        st.column_config.TextColumn("Notes",        width=320),
        },
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
        key="stakeholder_editor",
    )

    # Persist edits (drop computed Status so it's recalculated fresh next render)
    st.session_state["stakeholders"] = edited.drop(columns=["Status"])


# ─────────────────────────────────────────────────────────────────────────────

def build_map(df: pd.DataFrame, selected_abbr: str) -> go.Figure:
    fig = px.choropleth(
        df,
        locations="abbr",
        locationmode="USA-states",
        color="score",
        scope="usa",
        color_continuous_scale="RdYlGn",
        range_color=[1, 10],
        hover_name="name",
        hover_data={
            "abbr": False,
            "score": True,
            "medicaid": True,
            "ch_active": True,
            "medicaid_covered": True,
        },
        labels={
            "score": "Favorability",
            "medicaid": "Medicaid",
            "ch_active": "CH Status",
            "medicaid_covered": "CH Medicaid",
        },
    )
    fig.add_trace(go.Choropleth(
        locations=[selected_abbr],
        z=[1],
        locationmode="USA-states",
        colorscale=[[0, "rgba(0,0,0,0)"], [1, "rgba(0,0,0,0)"]],
        showscale=False,
        marker_line_color="white",
        marker_line_width=3,
    ))
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar=dict(title="Score", thickness=12, len=0.6),
        geo=dict(bgcolor="rgba(0,0,0,0)", lakecolor="#e8f4f8"),
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# ── LLM brief ────────────────────────────────────────────────────────────────

def build_prompt(state_name: str, d: dict, opp: dict) -> str:
    return f"""You are a strategic analyst for Charlie Health, a virtual behavioral health company
specializing in Intensive Outpatient Programs (IOP). Generate a concise state expansion brief
for {state_name}.

STATE PROFILE
-------------
Favorability Score: {d['favorability_score']}/10
Medicaid Expansion: {d['medicaid_status']}
Charlie Health Currently Active: {'Yes' if d['charlie_health_active'] else 'No'}
CH Has Medicaid Reimbursement: {'Yes' if d['medicaid_covered'] else 'No'}
Telehealth Policy: {d['telehealth_policy']}
Regulatory Context: {d['key_regulatory_notes']}
Recent Developments: {d['recent_developments']}

OPPORTUNITY ESTIMATES (internal model)
---------------------------------------
Addressable IOP Patients: {opp['addressable']:,}
  - Medicaid-eligible: {opp['medicaid_pop']:,} (~${opp['medicaid_rev']/1e6:.1f}M revenue potential)
  - Commercial: {opp['commercial_pop']:,} (~${opp['commercial_rev']/1e6:.1f}M revenue potential)
Total Estimated Revenue Opportunity: ~${opp['total_rev']/1e6:.1f}M

Generate a brief using EXACTLY these section headers (use markdown bold):

**Executive Summary**
2–3 sentences on the overall opportunity.

**Regulatory Posture**
Label: Favorable / Neutral / Unfavorable — then 2 sentences explaining why.

**Medicaid Landscape**
Reimbursement potential, key barriers, and what CH would need to navigate.

**Expansion Recommendation**
One of: Pursue Now / Monitor & Prepare / Deprioritize — with a single sentence rationale.

**Next Steps**
Three specific, actionable items (numbered list).

**Meeting Agenda Starters**
Two conversation hooks Charlie Health should raise in state-level stakeholder meetings.

Be direct and strategic. Write for a VP of Operations or Chief Growth Officer.
Do not add any sections beyond those listed."""


def generate_brief(state_abbr: str) -> str:
    d = STATE_DATA[state_abbr]
    opp = compute_opportunity(state_abbr)
    client = get_client()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=900,
        messages=[{"role": "user", "content": build_prompt(d["name"], d, opp)}],
    )
    return response.content[0].text


# ── Helpers ───────────────────────────────────────────────────────────────────

def fmt_pop(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.0f}K"
    return str(n)

def fmt_rev(n: int) -> str:
    if n >= 1_000_000_000:
        return f"${n/1_000_000_000:.1f}B"
    return f"${n/1_000_000:.0f}M"


# ── UI ────────────────────────────────────────────────────────────────────────

def main():
    with st.sidebar:
        st.header("Settings")
        key_input = st.text_input("Anthropic API Key", type="password",
                                  placeholder="sk-ant-...")
        if key_input:
            st.session_state["api_key"] = key_input
        st.caption("Key stored in session only.")

    st.title("Charlie Health — State Expansion Intelligence")
    st.caption("AI-powered regulatory briefs for virtual IOP market expansion planning.")

    df = build_dataframe()

    # ── Metrics ──────────────────────────────────────────────────────────────
    # States covered = ch_active
    states_covered   = int(df["ch_active"].eq("Active").sum())
    # States w/ Medicaid = CH has active Medicaid reimbursement
    states_medicaid  = int(df["medicaid_covered"].eq("Yes").sum())
    # High opportunity = score 7+
    high_opp         = int(df["score"].ge(7).sum())
    # Unexplored high opp = score 7+ AND not active
    unexplored       = int((df["score"].ge(7) & df["ch_active"].eq("Not active")).sum())
    # Uncovered patient population = sum of IOP-addressable patients in inactive states
    uncovered_pop = sum(
        round(STATE_DATA[abbr]["adult_population"] * STATE_DATA[abbr]["smi_rate"] * 0.15)
        for abbr, d in STATE_DATA.items()
        if not d["charlie_health_active"]
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("States Covered",          states_covered)
    c2.metric("States w/ Medicaid",      states_medicaid)
    c3.metric("High Opportunity (7+)",   high_opp)
    c4.metric("Unexplored High Opp",     unexplored)
    c5.metric("Uncovered IOP Patients",  fmt_pop(uncovered_pop),
              help="Sum of IOP-addressable patients (SMI × 15%) in states where CH is not present")

    st.divider()

    # ── Session state ─────────────────────────────────────────────────────────
    if "selected_abbr" not in st.session_state:
        st.session_state["selected_abbr"] = "CO"
    if "brief_cache" not in st.session_state:
        st.session_state.brief_cache = {}

    # ── Layout ───────────────────────────────────────────────────────────────
    col_map, col_panel = st.columns([1.5, 1], gap="large")

    with col_map:
        state_names  = sorted(df["name"].tolist())
        current_name = STATE_DATA[st.session_state["selected_abbr"]]["name"]

        selected_name = st.selectbox("State", state_names,
                                     index=state_names.index(current_name),
                                     label_visibility="collapsed")
        selected_abbr = df.loc[df["name"] == selected_name, "abbr"].values[0]
        st.session_state["selected_abbr"] = selected_abbr

        fig = build_map(df, selected_abbr)
        event = st.plotly_chart(fig, use_container_width=True,
                                on_select="rerun", key="choropleth_map")

        if event and event.selection and event.selection.get("points"):
            clicked = event.selection["points"][0].get("location")
            if clicked and clicked in STATE_DATA and clicked != selected_abbr:
                st.session_state["selected_abbr"] = clicked
                st.rerun()

        st.caption("Click a state or use the dropdown  |  Green = High (7–10)  |  Yellow = Moderate (4–6)  |  Red = Low (1–3)")
        st.divider()
        render_newsfeed()
        st.divider()
        render_stakeholder_tracker()

    with col_panel:
        d     = STATE_DATA[selected_abbr]
        score = d["favorability_score"]
        score_icon = "🟢" if score >= 7 else "🟡" if score >= 4 else "🔴"
        opp   = compute_opportunity(selected_abbr)

        st.subheader(f"{selected_name}  {score_icon}")

        st.markdown(f"""
**Favorability Score:** {score}/10
**Medicaid:** {d['medicaid_status']}
**CH Active:** {'Yes' if d['charlie_health_active'] else 'No'}
**CH Medicaid Reimbursement:** {'Yes' if d['medicaid_covered'] else 'No'}
**Telehealth Policy:** {d['telehealth_policy']}
""")

        # ── Opportunity size ──────────────────────────────────────────────────
        st.markdown("**Estimated Market Opportunity**")
        o1, o2, o3 = st.columns(3)
        o1.metric("Medicaid Patients",  fmt_pop(opp["medicaid_pop"]),
                  delta=fmt_rev(opp["medicaid_rev"]), delta_color="off")
        o2.metric("Commercial Patients", fmt_pop(opp["commercial_pop"]),
                  delta=fmt_rev(opp["commercial_rev"]), delta_color="off")
        o3.metric("Total Revenue Opp",   fmt_rev(opp["total_rev"]))
        st.caption(
            "Model: adult pop × state SMI rate (SAMHSA 2023) × 15% IOP-eligible. "
            "Revenue: $12K/Medicaid · $18K/commercial patient."
        )

        st.divider()

        # ── Follow-ups / To-dos ───────────────────────────────────────────────
        st.markdown("**Follow-ups / To-dos**")
        st.text_area(
            label="todos",
            key=f"todo_{selected_abbr}",
            placeholder="Add meeting notes, follow-up items, or action items for this state…",
            height=100,
            label_visibility="collapsed",
        )

        st.divider()

        # ── Brief generation ──────────────────────────────────────────────────
        col_btn, col_clear = st.columns([2, 1])
        generate = col_btn.button("Generate Expansion Brief", type="primary",
                                  use_container_width=True)
        if col_clear.button("Clear", use_container_width=True):
            st.session_state.brief_cache.pop(selected_abbr, None)
            st.rerun()

        if generate:
            with st.spinner(f"Generating brief for {selected_name}…"):
                st.session_state.brief_cache[selected_abbr] = generate_brief(selected_abbr)

        if selected_abbr in st.session_state.brief_cache:
            st.markdown(st.session_state.brief_cache[selected_abbr])
        else:
            st.info("Click **Generate Expansion Brief** for a strategic analysis of this state.")

        st.caption("Regulatory context is research-based but should be verified before use.")


if __name__ == "__main__":
    main()
