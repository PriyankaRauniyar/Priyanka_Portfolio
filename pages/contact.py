"""Direct contact links with no backend form."""

import streamlit as st

from portfolio import render_footer


st.markdown('<p class="eyebrow">Start a conversation</p>', unsafe_allow_html=True)
st.title("Contact")
st.markdown(
    '<p class="quiet-copy">For analytics, business intelligence, data science, healthcare analytics, and research collaborations.</p>',
    unsafe_allow_html=True,
)

with st.container(key="contact_card"):
    email, profiles = st.columns([1.15, 1])
    with email:
        st.markdown('<p class="eyebrow">Preferred contact</p>', unsafe_allow_html=True)
        st.subheader("Email")
        st.write("For opportunities and professional inquiries.")
        st.link_button(
            "priyanka.rauniyar@utdallas.edu",
            "mailto:priyanka.rauniyar@utdallas.edu",
            use_container_width=True,
            help="Compose an email to Priyanka's university address.",
        )
        with st.expander("Personal email"):
            st.link_button("rauniyar.priyanka@gmail.com", "mailto:rauniyar.priyanka@gmail.com", use_container_width=True)
    with profiles:
        st.markdown('<p class="eyebrow">Professional profiles</p>', unsafe_allow_html=True)
        st.subheader("Connect")
        st.link_button("LinkedIn", "https://www.linkedin.com/in/priyanka-rauniyar/", use_container_width=True, help="Open Priyanka's LinkedIn profile.")
        st.link_button("GitHub", "https://github.com/PriyankaRauniyar", use_container_width=True, help="Browse Priyanka's public project repositories.")

st.caption("No message form, tracking endpoint, or backend service is used.")

render_footer()
