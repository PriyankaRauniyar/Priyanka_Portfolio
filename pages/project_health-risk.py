"""Dedicated case study: R health-risk model comparison."""

import streamlit as st

from portfolio import load_portfolio, render_project_detail


project = next(item for item in load_portfolio()["projects"] if item["id"] == "health-risk")
st.markdown('<p class="eyebrow">R · interpretable model comparison</p>', unsafe_allow_html=True)
st.caption("The accuracy comparison and plots are taken from the public repository README and figures folder. Selected model metrics, the decision tree, and the BMI risk curve are displayed below.")
render_project_detail(project["id"])
