import streamlit as st

def transcript_viewer(text):

    st.subheader("📄 Transcript")

    st.text_area(
        "",
        value=text,
        height=350
    )