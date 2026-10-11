"""Project index with direct links to complete case studies."""

import streamlit as st

from portfolio import load_portfolio, render_footer, render_project_card


project_order = ["readmission", "pantrypulse", "health-risk", "learning-platform", "emergency-room"]
projects_by_id = {project["id"]: project for project in load_portfolio()["projects"]}
projects = [projects_by_id[project_id] for project_id in project_order]
st.markdown('<p class="eyebrow">Selected work · documented evidence</p>', unsafe_allow_html=True)
st.title("Projects")
st.markdown(
    '<p class="quiet-copy page-intro">Explore each project’s problem, methods, results, and limitations. '
    'Open any project for the full story, results, and links to the published work.</p>',
    unsafe_allow_html=True,
)

for project in projects:
    render_project_card(project, featured=project.get("featured", False))

render_footer()
