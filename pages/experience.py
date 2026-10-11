"""Professional experience and leadership."""

import streamlit as st

from portfolio import render_footer


st.markdown('<p class="eyebrow">Work & leadership</p>', unsafe_allow_html=True)
st.title("Experience")
st.markdown(
    '<p class="quiet-copy">Roles across campaign analytics, machine-learning research, product development, and community leadership.</p>',
    unsafe_allow_html=True,
)

experiences = [
    {
        "role": "Digital Marketing Executive",
        "organization": "Bitmosys Lab",
        "location": "Kathmandu, Nepal",
        "dates": "Feb 2022 - Aug 2022",
        "summary": "Used market and user analysis to improve campaign decisions and support community outreach.",
        "evidence": [
            "Data-driven marketing strategies improved campaign ROI by 12%.",
            "Presented findings that informed 3+ community outreach initiatives.",
            "Collaborated with a five-member team; promotional work increased customer reach by 18%.",
        ],
    },
    {
        "role": "Research Intern",
        "organization": "Vyobotics",
        "location": "Singapore",
        "dates": "Oct 2020 - Oct 2021",
        "summary": "Applied machine learning in IoT robotics and collaborated with an international team.",
        "evidence": [
            "Implemented a machine-learning model that improved predictive accuracy by 15%.",
            "Delivered technical presentations and mentored peers on IoT applications.",
        ],
    },
    {
        "role": "Intern",
        "organization": "Immobile Design",
        "location": "Ahmedabad, India",
        "dates": "Jan 2020 - May 2020",
        "summary": "Contributed iOS interface design and database work.",
        "evidence": [
            "Designed and developed an iOS app interface for student users.",
            "Optimized database performance and mentored new interns on database structuring.",
        ],
    },
]

for index, experience in enumerate(experiences, start=1):
    with st.container(key=f"experience_{index}"):
        number, details, dates = st.columns([.14, 1.4, .8])
        number.markdown(f'<p class="education-number">0{index}</p>', unsafe_allow_html=True)
        details.subheader(experience["role"])
        details.caption(f"{experience['organization']} · {experience['location']}")
        details.write(experience["summary"])
        details.markdown("**Selected results and responsibilities**")
        for evidence in experience["evidence"]:
            details.markdown(f"- {evidence}")
        dates.caption(experience["dates"])

st.markdown('<p class="eyebrow">Leadership</p>', unsafe_allow_html=True)
st.header("Building participation and teams")
leadership = [
    (
        "Women in Science and Technology Group",
        "Executive member · RK University · Jan 2018 - Dec 2019",
        "Supported 70+ students in STEM through workshops, peer guidance, and awareness campaigns; organized three training sessions and campaigns.",
    ),
    (
        "Techno Planet National Event",
        "Application integration with Smart Bike · Oct 2019",
        "Led a six-member team presenting an IoT model-integration project recognized at a national-level competition for innovation.",
    ),
]
leadership_columns = st.columns(2)
for index, (column, (organization, role, detail)) in enumerate(zip(leadership_columns, leadership)):
    with column, st.container(key=f"leadership_{index}"):
        st.subheader(organization)
        st.caption(role)
        st.write(detail)

render_footer()
