"""Dedicated case study: retrospective hospital readmission research dashboard."""

import streamlit as st

from portfolio import load_portfolio, render_project_detail


project = next(item for item in load_portfolio()["projects"] if item["id"] == "readmission")
st.markdown('<p class="eyebrow">Frozen model · retrospective evaluation</p>', unsafe_allow_html=True)
st.caption("This report separates untouched held-out test results from the larger historical precomputed prediction export.")
render_project_detail(project["id"])
