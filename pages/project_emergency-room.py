"""Dedicated case study: emergency-room MySQL database model."""

import streamlit as st

from portfolio import load_portfolio, render_project_detail


project = next(item for item in load_portfolio()["projects"] if item["id"] == "emergency-room")
st.markdown('<p class="eyebrow">Healthcare data systems · MySQL</p>', unsafe_allow_html=True)
st.caption("The case study models clinical operations; the published schema does not contain real patient records.")
render_project_detail(project["id"])
