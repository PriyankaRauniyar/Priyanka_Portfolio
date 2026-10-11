"""Bank research portfolio case study: completed institution-matching phase."""

import streamlit as st

from portfolio import project_by_id, render_footer, render_project_visual


project = project_by_id("bank-research")
st.page_link("pages/home.py", label="Back to portfolio", icon=":material/arrow_back:")
st.markdown('<p class="eyebrow">Research internship · Financial data analytics · Summer 2026</p>', unsafe_allow_html=True)
st.title(project["title"])
st.markdown(
    '<p class="quiet-copy">A reproducible data-integration workflow for studying employee industry expertise and bank lending.</p>',
    unsafe_allow_html=True,
)
st.caption("Completed phase: institution matching and accepted identifier bridge. Downstream employee and lending analysis is pending.")

st.header("Research internship overview")
st.write(
    "The research asks how employees’ prior industry-specific work experience relates to banks’ lending decisions "
    "and performance across loan categories. This completed phase addressed the data-integration foundation: "
    "connecting bank identities in large-scale employment records with FDIC institution identifiers."
)
st.write(
    "I developed and validated an entity-resolution workflow using institution names and historical identities, "
    "geography, employment timelines, structured matching rules, quality checks, and manual verification. "
    "The resulting identifier bridge supports later employee-level linkage and industry-expertise measurement."
)

st.header("Results & outputs")
render_project_visual(project)
st.caption(
    "These are integration and QA milestones. They are not predictive-model scores or findings about lending outcomes."
)

question, scope = st.columns(2)
with question:
    st.subheader("Research question & motivation")
    st.markdown("**Question:** How does employees’ prior industry experience relate to bank lending behavior and performance?")
    st.write(
        "Banks employ people with different industry backgrounds. Testing whether that expertise relates to lending "
        "requires reliable bank identities first. Name changes, mergers, acquisitions, restructuring, and similar names "
        "make employment-to-FDIC linkage a substantial research challenge."
    )
with scope:
    st.subheader("Data & scope")
    st.write(
        "The broader source contains more than 69.8 million LinkedIn/BankFirm employment records. Institution names, "
        "employment timelines, FDIC historical identity information, and FDIC Summary of Deposits geographic evidence "
        "informed the matching and review process. The completed phase produced institution-identifier mappings, "
        "not a merged employee-level dataset."
    )

st.header("Institution-matching work")
st.markdown(
    """- Developed and refined a reproducible workflow for matching employment-source bank identities to FDIC identifiers.
- Evaluated historical names, geographic evidence, and employment timelines for candidate relationships.
- Designed QA checks and manual-review procedures for ambiguous or conflicting mappings.
- Used FDIC Summary of Deposits evidence during institution verification.
- Consolidated a final accepted bridge of **5,156 unique RCIDs**, including **12 professor-approved additions** to the previous 5,144-record version; verified **zero duplicate RCIDs**."""
)
st.markdown("**Tools and methods:** Python · data preparation · entity resolution · historical and geographic matching · QA · manual verification")

st.header("Matching methodology")
workflow = [
    ("01", "Prepare", "Organize institution-identification fields from employment and FDIC sources for comparison."),
    ("02", "Normalize", "Standardize names and account for historical and legal naming variations."),
    ("03", "Match", "Evaluate candidate institutions using name, historical, geographic, and temporal evidence."),
    ("04", "Validate", "Apply quality checks to identify uncertain or conflicting candidate mappings."),
    ("05", "Review", "Manually verify ambiguous cases with historical records and geographic evidence, including FDIC Summary of Deposits."),
    ("06", "Finalize", "Consolidate approved mappings and check RCID uniqueness in the final accepted bridge."),
]
for index in range(0, len(workflow), 2):
    columns = st.columns(2)
    for column, (number, title, detail) in zip(columns, workflow[index:index + 2]):
        with column, st.container(border=True):
            st.markdown(f"**{number} · {title}**")
            st.write(detail)

significance, next_steps = st.columns(2)
with significance:
    st.subheader("Research significance")
    st.write(
        "The accepted identifier bridge provides a traceable foundation for later longitudinal employment histories, "
        "industry classification, and bank-level employee-expertise measures. Separating accepted matches from uncertain "
        "candidates makes downstream integration more reliable."
    )
with next_steps:
    st.subheader("Scope & next steps")
    st.write(
        "Employee-level merging, expertise-measure construction, and statistical analysis of lending outcomes were not "
        "completed in this phase. Next stages would integrate employee histories, classify prior industry experience, "
        "create bank-level expertise measures, and analyze lending relationships. The bridge alone does not establish "
        "an effect on lending."
    )

st.divider()
st.caption(
    "Disclosure: This portfolio shows aggregate metrics and a methodological overview only. Source employment records, "
    "institution-level mappings, restricted code, and unpublished lending findings are not publicly distributed. "
    "The additional methodology and aggregate metrics should be reviewed with the supervising professor before publication."
)
render_footer()
