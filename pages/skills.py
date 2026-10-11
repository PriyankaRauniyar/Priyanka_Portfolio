"""Skills organized by practical capability and supported examples."""

import streamlit as st


st.markdown('<p class="eyebrow">Tools & methods</p>', unsafe_allow_html=True)
st.title("Skills")
st.markdown(
    '<p class="quiet-copy">A practical view of the tools and methods documented in the resume, connected to work shown in this portfolio.</p>',
    unsafe_allow_html=True,
)

skill_sets = [
    {
        "number": "01",
        "title": "Python & machine learning",
        "skills": ["Python", "R", "Machine learning", "Predictive modeling", "Data cleaning & preprocessing", "Exploratory data analysis", "Statistical analysis"],
        "evidence": "R health-risk model comparison · Python readmission research dashboard · PantryPulse forecast prototype",
    },
    {
        "number": "02",
        "title": "SQL & data systems",
        "skills": ["MySQL", "MongoDB", "Relational database design", "SQL reporting", "Data modeling"],
        "evidence": "Online learning platform schema · Emergency room relational case study",
    },
    {
        "number": "03",
        "title": "BI & visualization",
        "skills": ["Power BI", "Tableau", "Microsoft Excel", "Data visualization", "Presentation"],
        "evidence": "Dashboard communication, model figures, ER diagrams, and research reporting documented across portfolio projects.",
    },
    {
        "number": "04",
        "title": "Research & communication",
        "skills": ["Large-scale institution matching", "Data quality assurance", "Market & user analysis", "IoT applications", "Social media marketing", "SEO", "Communication"],
        "evidence": "Ongoing bank employee-expertise matching summary · campaign analytics · IoT robotics internship",
    },
]

for skill_set in skill_sets:
    with st.container(key=f"skills_{skill_set['number']}"):
        left, right = st.columns([.9, 1.4])
        with left:
            st.markdown(f'<p class="eyebrow">Capability {skill_set["number"]}</p>', unsafe_allow_html=True)
            st.subheader(skill_set["title"])
        with right:
            st.markdown("".join(f'<span class="tool-chip">{skill}</span>' for skill in skill_set["skills"]), unsafe_allow_html=True)
            st.caption(skill_set["evidence"])

st.caption("Skill list is based on the current resume and documented portfolio work; it does not imply certification or proficiency level.")
