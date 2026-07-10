import streamlit as st

def statistics(stats):

    st.subheader("📊 Transcript Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Words", stats["words"])
    c2.metric("Lines", stats["lines"])
    c3.metric("Characters", stats["characters"])
    c4.metric("Reading Time", f"{stats['reading_time']} min")