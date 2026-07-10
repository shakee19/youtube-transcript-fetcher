import streamlit as st

def downloads(filename):

    st.subheader("⬇️ Downloads")

    c1, c2, c3 = st.columns(3)

    with open(f"transcripts/{filename}.txt", "rb") as f:
        c1.download_button(
            "📄 TXT",
            f,
            file_name=f"{filename}.txt"
        )

    with open(f"transcripts/{filename}.json", "rb") as f:
        c2.download_button(
            "📦 JSON",
            f,
            file_name=f"{filename}.json"
        )

    with open(f"transcripts/{filename}.pdf", "rb") as f:
        c3.download_button(
            "📕 PDF",
            f,
            file_name=f"{filename}.pdf"
        )