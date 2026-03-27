import os
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

@st.cache_data
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
