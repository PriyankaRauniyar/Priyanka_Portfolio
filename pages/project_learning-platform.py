"""Dedicated case study: online learning platform MySQL system."""

import streamlit as st

from portfolio import load_portfolio, render_project_detail


project = next(item for item in load_portfolio()["projects"] if item["id"] == "learning-platform")
st.markdown('<p class="eyebrow">MySQL · relational workflow design</p>', unsafe_allow_html=True)
st.caption("The ER diagram is the published repository artifact; no production learner outcomes are claimed.")
render_project_detail(project["id"])
