"""Dedicated case study: PantryPulse food-insecurity planning prototype."""

import streamlit as st

from portfolio import load_portfolio, render_project_detail


project = next(item for item in load_portfolio()["projects"] if item["id"] == "pantrypulse")
st.markdown('<p class="eyebrow">Food insecurity · forecasting & planning</p>', unsafe_allow_html=True)
st.caption("Repository-only link: no public live deployment URL was found in the project materials reviewed.")
render_project_detail(project["id"])
