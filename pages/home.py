"""Executive home page with the complete portfolio overview."""

import base64
from contextlib import nullcontext
from html import escape

import streamlit as st

from portfolio import ROOT, load_portfolio, render_footer, render_project_visual


portfolio = load_portfolio()
projects = portfolio["projects"]
project_by_id = {project["id"]: project for project in projects}
portrait_path = ROOT / "static" / "portrait.jpg"
background_path = ROOT / "static" / "hero-background.jpg"
if background_path.is_file():
    background_data = base64.b64encode(background_path.read_bytes()).decode("ascii")
    st.markdown(
        '<style>'
        '.st-key-home_hero.stVerticalBlock {'
        'background-color: #203f34;'
        'background-image: linear-gradient(110deg, rgba(16, 35, 28, .86), rgba(16, 35, 28, .80)), '
        f'url("data:image/jpeg;base64,{background_data}");'
        'background-size: cover; background-position: center; background-repeat: no-repeat;'
        'background-clip: padding-box;'
        '}'
        '</style>',
        unsafe_allow_html=True,
    )

with st.container(key="home_content"):
    with st.container(key="home_hero"):
        portrait, copy = st.columns([.7, 1.7], gap="large", vertical_alignment="center")
        with portrait:
            if portrait_path.is_file():
                portrait_data = base64.b64encode(portrait_path.read_bytes()).decode("ascii")
                st.markdown(
                    f'<img class="portrait" src="data:image/jpeg;base64,{portrait_data}" width="640" height="800" fetchpriority="high" alt="Portrait of Priyanka Rauniyar">',
                    unsafe_allow_html=True,
                )
                st.markdown('<p class="portrait-note">Dallas, Texas · Business Analytics & AI</p>', unsafe_allow_html=True)
        with copy, st.container(key="home_hero_copy"):
            st.markdown('<p class="eyebrow">Healthcare analytics · Business intelligence · Research</p>', unsafe_allow_html=True)
            st.title("Priyanka Rauniyar")
            st.subheader("Turning complex data into decisions that matter..")
            st.markdown(
                '<div class="hero-intro">'
                '<p>I’m a Business Analytics &amp; AI graduate student at UT Dallas with experience across '
                'healthcare analytics, financial research, and business intelligence. I build predictive models, '
                'dashboards, and reliable data workflows that make complex information useful for decisions. '
                'My work spans hospital readmission risk, food insecurity, and large-scale bank data integration, '
                'with a focus on clear results and honest interpretation.</p>'
                '</div>', unsafe_allow_html=True,
            )
            with st.container(key="home_profile_actions"):
                profile_actions = st.columns(3)
                profile_actions[0].link_button("GitHub", "https://github.com/PriyankaRauniyar", icon=":material/code:", use_container_width=True)
                profile_actions[1].link_button("LinkedIn", "https://www.linkedin.com/in/priyanka-rauniyar/", icon=":material/business_center:", use_container_width=True)
                profile_actions[2].link_button("Email", "mailto:priyanka.rauniyar@utdallas.edu", icon=":material/mail:", use_container_width=True)
    st.markdown('<p class="home-section-label">01 · Research Internship</p>', unsafe_allow_html=True)
    st.header("Summer research · Financial data analytics")
    research = portfolio["research_internships"][0]
    with st.container(key="home_research_internship"):
        summary, metrics = st.columns([1.1, 1], gap="large")
        with summary:
            st.caption("Summer 2026 · Completed institution-matching phase")
            st.subheader(research["title"])
            st.write(research["contribution"])
            st.markdown("".join(f'<span class="tool-chip">{escape(tool)}</span>' for tool in research["methods"]), unsafe_allow_html=True)
            st.caption("Employee-level merging and lending analysis are pending.")
            st.page_link("pages/project_bank-research.py", label="Research internship details", icon=":material/science:", use_container_width=True)
        with metrics:
            render_project_visual(research)

    st.markdown('<p class="home-section-label">02 · Featured Projects</p>', unsafe_allow_html=True)
    st.header("Projects that make evidence usable")
    featured_project = project_by_id["readmission"]
    with st.container(key="home_featured_project"):
        summary, visual = st.columns([1.05, 1])
        with summary:
            st.markdown(f'<p class="project-type">{featured_project["category"]}</p>', unsafe_allow_html=True)
            st.subheader(featured_project["title"])
            st.write(featured_project["problem"])
            st.markdown("**Frozen model:** 60% CatBoost + 40% XGBoost weighted ensemble.")
            st.markdown("**Project implementation**")
            st.write(featured_project["contribution"])
            st.markdown(
                f'<div class="result-band"><strong>19,802 held-out test encounters</strong><br>'
                '52.43% accuracy · 46.15% macro F1 · 39.67% within-30-day recall</div>',
                unsafe_allow_html=True,
            )
            st.caption("99,343 historical precomputed predictions are a separate export and are not used for test results. Retrospective research demonstration, not clinically validated.")
            actions = st.columns(2)
            actions[0].page_link("pages/project_readmission.py", label="View project details", icon=":material/article:", use_container_width=True)
            actions[1].link_button("Live dashboard", "https://hospital-readmission-risk-dashboard-pr.streamlit.app/", icon=":material/open_in_new:", use_container_width=True)
        with visual:
            render_project_visual(featured_project)

    st.markdown("""
    <style>
    [class*="st-key-home_preview_"].stVerticalBlock .preview-category { color: #8bd3ad; font-size: .85rem !important; font-weight: 800; letter-spacing: .075em; text-transform: uppercase; margin: 0 0 .7rem; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-title { color: #f2f5ef; font-family: 'DM Serif Display', Georgia, serif; font-size: clamp(1.4rem, 1.8vw, 1.75rem) !important; line-height: 1.22; margin: 0 0 .85rem; text-align: center; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-description { color: #f2f5ef; font-size: .98rem !important; line-height: 1.55; margin: 0 0 1rem; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-evidence { padding: .7rem .9rem; margin: .1rem 0 .85rem; border-left: 3px solid #f0a18b; background: #101a16; color: #e5efe7; font-size: .98rem; line-height: 1.45; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-caption { color: #c1d1c7; font-size: .9rem !important; line-height: 1.45; margin: 0 0 .9rem; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-spacer { flex: 1; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-tools { display: flex; flex-wrap: wrap; gap: .4rem; margin: 1rem 0 .85rem; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-tool { border: 1px solid #40594b; border-radius: 999px; padding: .3rem .55rem; color: #c1d1c7; font-size: .82rem; font-weight: 700; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-link { display: block; box-sizing: border-box; width: 100%; padding: .7rem 1rem; border: 1px solid #8bd3ad; border-radius: 6px; color: #f2f5ef !important; text-decoration: none; text-align: center; font-weight: 700; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-link:hover, [class*="st-key-home_preview_"].stVerticalBlock .preview-link:focus-visible { background: #8bd3ad; color: #102219 !important; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-metrics { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .55rem; margin: .1rem 0 .8rem; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-metrics div { padding: .6rem .75rem; border: 1px solid #40594b; border-radius: 7px; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-metrics strong { display: block; color: #8bd3ad; font-size: 1.3rem; line-height: 1.2; }
    [class*="st-key-home_preview_"].stVerticalBlock .preview-metrics span { display: block; color: #c1d1c7; font-size: .82rem; line-height: 1.3; }
    </style>
    """, unsafe_allow_html=True)

    preview_ids = ["pantrypulse", "health-risk", "learning-platform", "emergency-room"]
    preview_columns = None
    for project_id in preview_ids:
        project = project_by_id[project_id]
        if project_id == "pantrypulse":
            evidence = (
                '<div class="preview-metrics">'
                '<div><strong>503,440</strong><span>People facing food insecurity</span></div>'
                '<div><strong>19.2%</strong><span>Food insecurity rate</span></div>'
                '<div><strong>45%</strong><span>Above SNAP income limit</span></div>'
                '<div><strong>$3.51</strong><span>Cost per meal</span></div></div>'
                '<p class="preview-caption">Dallas County, 2024 dashboard example. Eight-week forecasts; simulated capacity scenarios.</p>'
            )
        else:
            evidence = f'<div class="preview-evidence">{escape(project["outcome"])}</div>'
        tools = "".join(
            f'<span class="preview-tool">{escape(tool)}</span>' for tool in project["methods"][:4]
        )
        index = preview_ids.index(project_id) - 1
        if project_id == "pantrypulse":
            placement = nullcontext()
        else:
            if index % 2 == 0:
                remaining = len(preview_ids) - 1
                preview_columns = st.columns(1 if index == remaining - 1 else 2)
            placement = preview_columns[index % 2]
        with placement, st.container(key=f"home_preview_{project_id}"):
            if project_id == "pantrypulse":
                description, chart = st.columns([1.05, 1], gap="large")
            else:
                description, chart = nullcontext(), None
            with description:
                st.markdown(
                    f'<p class="preview-category">{escape(project["category"])}</p>'
                    f'<h3 class="preview-title">{escape(project["title"])}</h3>'
                    f'<p class="preview-description">{escape(project["problem"])}</p>'
                    f'{evidence}<div class="preview-tools">{tools}</div>',
                    unsafe_allow_html=True,
                )
                actions = st.columns(2) if project_id == "pantrypulse" else None
                detail_action = actions[0] if actions else st
                detail_action.page_link(f"pages/project_{project_id}.py", label="View project details", use_container_width=True)
                dashboard = next((link for link in project["links"] if "dashboard" in link["label"].lower()), None)
                if dashboard:
                    dashboard_action = actions[1] if actions else st
                    dashboard_action.link_button("Live dashboard", dashboard["url"], icon=":material/open_in_new:", use_container_width=True)
            if chart is not None:
                with chart:
                    render_project_visual(project)

    st.markdown('<p class="home-section-label">03 · Experience</p>', unsafe_allow_html=True)
    st.header("Analytical work across sectors")
    experience_columns = st.columns(3)
    experience_overview = [
        ("Bitmosys Lab", "Digital Marketing Executive · Kathmandu", "12% campaign ROI improvement · 18% customer reach increase"),
        ("Vyobotics", "Research Intern · Singapore", "15% predictive accuracy improvement in IoT robotics"),
        ("Immobile Design", "iOS Intern · Ahmedabad", "iOS interface design and database optimization"),
    ]
    for index, (column, (organization, role, result)) in enumerate(zip(experience_columns, experience_overview)):
        with column, st.container(key=f"home_experience_{index}"):
            st.markdown(f"**{organization}**")
            st.caption(role)
            st.write(result)
    with st.container(key="home_section_link_experience"):
        st.page_link("pages/experience.py", label="Full Experience & leadership", icon=":material/work:")

    st.markdown('<p class="home-section-label">04 · Education</p>', unsafe_allow_html=True)
    st.header("Business, analytics, and technology")
    education_columns = st.columns(3)
    for index, (column, degree, institution, detail) in enumerate(zip(
        education_columns,
        ["M.S. Business Analytics & AI", "International MBA", "B.Tech. Information Technology"],
        ["The University of Texas at Dallas", "University of Wolverhampton", "RK University"],
        ["Expected May 2027", "2023 · GPA 3.64", "May 2020 · GPA 3.45"],
    )):
        with column, st.container(key=f"home_education_{index}"):
            st.markdown(f"**{degree}**")
            st.caption(institution)
            st.caption(detail)
    with st.container(key="home_section_link_education"):
        st.page_link("pages/education.py", label="Education details", icon=":material/school:")

    st.markdown('<p class="home-section-label">05 · Achievements</p>', unsafe_allow_html=True)
    st.header("Selected academic achievements")
    cert_columns = st.columns(2)
    cert_items = [
        ("72nd Lindau Nobel Laureate Meeting", "Lindau, Germany · June 25–30, 2023", "Official Certificate of Attendance confirming participation after qualification through a global, multi-step selection process.", "Lindau_Certification.pdf"),
        ("LUCS-PACE Summer School", "University of Oslo · August 29–September 2, 2022", "Participated in the interdisciplinary summer school From Energy Systems to Energy Justice, exploring sustainability and equitable energy transitions.", "Oslo_Summer_School.pdf"),
    ]
    for index, (column, (name, detail, description, filename)) in enumerate(zip(cert_columns, cert_items)):
        with column, st.container(key=f"home_certificate_{index}"):
            st.subheader(name)
            st.caption(detail)
            st.write(description)
            if (ROOT / "static" / filename).is_file():
                st.link_button("View certificate in browser ↗", f"/app/static/{filename}", use_container_width=True)
            else:
                st.caption("Certificate PDF is unavailable.")
    with st.container(key="home_section_link_certifications"):
        st.page_link("pages/certifications.py", label="All achievements", icon=":material/verified:")

    st.markdown('<p class="home-section-label">06 · Skills</p>', unsafe_allow_html=True)
    st.header("Capabilities across the analytics lifecycle")
    skill_columns = st.columns(4)
    for index, (column, title, detail) in enumerate(zip(
        skill_columns,
        ["Model", "Structure", "Communicate", "Research"],
        ["Python, R, ML, EDA, evaluation", "MySQL, MongoDB, relational design", "Power BI, Tableau, Excel", "Statistical analysis, matching, QA"],
    )):
        with column, st.container(key=f"home_skill_{index}"):
            st.markdown(f"**{title}**")
            st.caption(detail)
    with st.container(key="home_section_link_skills"):
        st.page_link("pages/skills.py", label="Skills & methods", icon=":material/psychology:")

    st.markdown('<p class="home-section-label">07 · Contact</p>', unsafe_allow_html=True)
    st.header("Let’s connect")
    st.markdown("For analytics, business intelligence, data science, healthcare analytics, and research opportunities.")
    contact_actions = st.columns(3)
    contact_actions[0].link_button("Email Priyanka", "mailto:priyanka.rauniyar@utdallas.edu", icon=":material/mail:", use_container_width=True)
    contact_actions[1].link_button("LinkedIn", "https://www.linkedin.com/in/priyanka-rauniyar/", icon=":material/business_center:", use_container_width=True)
    contact_actions[2].link_button("GitHub", "https://github.com/PriyankaRauniyar", icon=":material/code:", use_container_width=True)

    render_footer()
