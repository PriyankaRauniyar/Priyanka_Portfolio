"""Resume access from the top navigation."""

import streamlit as st

from portfolio import ROOT, render_footer


st.markdown('<p class="eyebrow">Professional profile</p>', unsafe_allow_html=True)
st.title("Resume")
st.write("Download my resume or open the PDF in your browser.")

resume = ROOT / "PriyankaRauniyar_Resume.pdf"
if resume.is_file():
    download, preview = st.columns(2)
    download.download_button(
        "Download resume",
        data=resume.read_bytes(),
        file_name=resume.name,
        mime="application/pdf",
        icon=":material/download:",
        use_container_width=True,
    )
    preview.link_button(
        "View resume in browser",
        "/app/static/PriyankaRauniyar_Resume.pdf",
        icon=":material/open_in_new:",
        use_container_width=True,
    )
else:
    st.error("Resume PDF is unavailable.")

render_footer()
