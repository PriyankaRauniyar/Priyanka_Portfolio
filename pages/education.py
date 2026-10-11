"""Education details grounded in the current resume and portfolio."""

import streamlit as st

from portfolio import render_footer


st.markdown('<p class="eyebrow">Academic background</p>', unsafe_allow_html=True)
st.title("Education")
st.markdown(
    '<p class="quiet-copy">Formal training across business analytics, management, and information technology.</p>',
    unsafe_allow_html=True,
)

degrees = [
    {
        "degree": "Master of Science, Business Analytics & AI",
        "institution": "The University of Texas at Dallas",
        "when": "Expected May 2027",
        "place": "Dallas, Texas",
        "detail": "Graduate study focused on analytics and artificial intelligence.",
    },
    {
        "degree": "International Master of Business Administration",
        "institution": "University of Wolverhampton",
        "when": "October 2023",
        "place": "Wolverhampton, England",
        "detail": "GPA 3.64",
    },
    {
        "degree": "Bachelor of Technology, Information Technology",
        "institution": "RK University",
        "when": "May 2020",
        "place": "Rajkot, India",
        "detail": "GPA 3.45",
    },
]

for index, degree in enumerate(degrees, start=1):
    with st.container(key=f"education_{index}"):
        number, details = st.columns([.16, 1])
        number.markdown(f'<p class="education-number">0{index}</p>', unsafe_allow_html=True)
        details.markdown(f"### {degree['degree']}")
        details.markdown(f"**{degree['institution']}** · {degree['place']}")
        details.caption(f"{degree['when']} · {degree['detail']}")

st.info("The current resume does not list a GPA for the UTD master's program, so none is shown here.")
render_footer()
