"""Streamlit entry point for Priyanka Rauniyar's analytics portfolio."""

import streamlit as st

from portfolio import add_global_styles


st.set_page_config(
    page_title="Priyanka Rauniyar | Analytics Portfolio",
    page_icon="PR",
    layout="wide",
    initial_sidebar_state="collapsed",
)

add_global_styles()

pages = [
    st.Page("pages/home.py", title="Home", icon=":material/home:", default=True, url_path="home"),
    st.Page("pages/projects.py", title="Projects", icon=":material/analytics:", url_path="projects"),
    st.Page("pages/experience.py", title="Experience", icon=":material/work:", url_path="experience"),
    st.Page("pages/education.py", title="Education", icon=":material/school:", url_path="education"),
    st.Page("pages/certifications.py", title="Achievements", icon=":material/verified:", url_path="achievements"),
    st.Page("pages/skills.py", title="Skills", icon=":material/psychology:", url_path="skills"),
    st.Page("pages/contact.py", title="Contact", icon=":material/mail:", url_path="contact"),
    st.Page("pages/resume.py", title="Resume", icon=":material/download:", url_path="resume"),
]

project_pages = [
    st.Page(f"pages/project_{project_id}.py", title=f"{title} case study", url_path=f"project-{project_id}")
    for project_id, title in [
        ("readmission", "Readmission"),
        ("pantrypulse", "PantryPulse"),
        ("health-risk", "Health Risk Classification"),
        ("learning-platform", "Online Learning Platform"),
        ("emergency-room", "Emergency Room Database"),
    ]
]

research_page = st.Page(
    "pages/project_bank-research.py", title="Research Internship", icon=":material/science:",
    url_path="project-bank-research",
)

navigation = st.navigation({"Portfolio": pages, "Research": [research_page], "Project details": project_pages}, position="hidden")

with st.sidebar:
    with st.container(key="mobile_menu"):
        st.markdown("### Menu")
        for page in [pages[0], research_page, *pages[1:]]:
            st.page_link(page, use_container_width=True)
        with st.expander("Project details"):
            for page in project_pages:
                st.page_link(page, use_container_width=True)
    st.divider()
    st.link_button("Email Priyanka", "mailto:priyanka.rauniyar@utdallas.edu", use_container_width=True)
    st.link_button("GitHub profile", "https://github.com/PriyankaRauniyar", use_container_width=True)

# Native page links preserve the Streamlit session and respect deployment base paths.
with st.container(key="header_menu"):
    menu = st.columns(11, gap="small")
    menu[0].markdown("**PR · Priyanka**")
    for column, page in zip(menu[1:9], [pages[0], research_page, *pages[1:7]]):
        with column:
            with st.container(key=f"menu_{'selected' if navigation.url_path == page.url_path else 'item'}_{page.url_path or 'home'}"):
                st.page_link(page, use_container_width=True)
    with menu[9]:
        with st.container(key="menu_selected_details" if navigation in project_pages else "menu_item_details"):
            with st.popover("Project details", use_container_width=True):
                for page in project_pages:
                    st.page_link(page, use_container_width=True)
    with menu[10]:
        with st.container(key="menu_selected_resume" if navigation.url_path == pages[7].url_path else "menu_item_resume"):
            st.page_link(pages[7], use_container_width=True)

navigation.run()
