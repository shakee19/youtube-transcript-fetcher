import streamlit as st

def hero():

    st.markdown(
        """
        <h1 style='text-align:center;'>
        🎥 YouTube Transcript Fetcher Pro
        </h1>

        <h4 style='text-align:center;color:gray'>
        Download transcripts in multiple languages
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.info(
        "✨ Supports TXT • JSON • PDF • Multiple Languages"
    )