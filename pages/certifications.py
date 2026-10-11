"""Certificates linked to browser-viewable PDF files."""

import streamlit as st

from portfolio import ROOT, render_footer


st.markdown('<p class="eyebrow">Recognition & academic programs</p>', unsafe_allow_html=True)
st.title("Achievements")
st.markdown(
    '<p class="quiet-copy page-intro">Selected international academic experiences and the certificates documenting my participation.</p>',
    unsafe_allow_html=True,
)

certificates = [
    (
        "72nd Lindau Nobel Laureate Meeting",
        "Lindau, Germany · June 25–30, 2023",
        "Official Certificate of Attendance confirming my participation in the 72nd Lindau Nobel Laureate Meeting, following qualification through a global, multi-step selection process. The meeting brought young researchers together with Nobel Laureates for scientific exchange.",
        "Lindau_Certification.pdf",
    ),
    (
        "2022 LUCS-PACE Summer School",
        "University of Oslo · August 29–September 2, 2022",
        "Participated in the interdisciplinary LUCS-PACE summer school, From Energy Systems to Energy Justice. The program explored sustainability and energy transitions through technical and social perspectives.",
        "Oslo_Summer_School.pdf",
    ),
]

for index, (title, detail, summary, filename) in enumerate(certificates, start=1):
    with st.container(key=f"certificate_{index}"):
        st.markdown(f'<p class="eyebrow">0{index} · Achievement</p>', unsafe_allow_html=True)
        st.subheader(title)
        st.caption(detail)
        st.write(summary)
        if (ROOT / "static" / filename).is_file():
            st.link_button("View certificate in browser ↗", f"/app/static/{filename}")
        else:
            st.warning("The certificate PDF is unavailable.")

render_footer()
