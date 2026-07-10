import streamlit as st

from components.sidebar import sidebar
from components.hero import hero
from components.video_card import video_card
from components.statistics_card import statistics
from components.transcript_viewer import transcript_viewer
from components.downloads import downloads
from components.footer import footer

from transcript import (
    fetch_transcript,
    transcript_to_text,
    get_available_languages
)

from youtube import get_video_title

from utils import (
    extract_video_id,
    clean_filename
)

from statistics import transcript_statistics

from file_handler import (
    save_as_text,
    save_as_json
)

from pdf_exporter import save_as_pdf


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="YouTube Transcript Fetcher Pro",
    page_icon="🎥",
    layout="wide"
)
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------
# Sidebar
# -------------------------------------------------

sidebar()

# -------------------------------------------------
# Hero
# -------------------------------------------------

hero()

# -------------------------------------------------
# URL Input
# -------------------------------------------------

url = st.text_input(
    "🔗 YouTube URL",
    placeholder="https://youtu.be/xxxxxxxx"
)

fetch = st.button(
    "🚀 Fetch Transcript",
    use_container_width=True
)

# -------------------------------------------------
# Variables
# -------------------------------------------------

title = None
video_id = None
selected = None
stats = None
text = None
filename = None

# -------------------------------------------------
# Fetch Transcript
# -------------------------------------------------

if fetch:

    try:

        with st.spinner("🎥 Fetching transcript..."):

            video_id = extract_video_id(url)

            if not video_id:
                st.error("Invalid YouTube URL")
                st.stop()

            title = get_video_title(url)

            languages = get_available_languages(video_id)

            language_names = [
                f"{lang['name']} ({lang['code']})"
                for lang in languages
            ]

            selected = st.selectbox(
                "🌍 Select Language",
                language_names
            )

            code = selected.split("(")[-1].replace(")", "")

            transcript = fetch_transcript(
                video_id,
                code
            )

            text = transcript_to_text(transcript)

            stats = transcript_statistics(text)

            filename = clean_filename(title)

            save_as_text(text, filename)

            save_as_json(transcript, filename)

            save_as_pdf(text, filename)

        st.success("🎉 Transcript Downloaded Successfully!")

    except Exception as e:

        st.error(e)

# -------------------------------------------------
# Video Card
# -------------------------------------------------

st.divider()

if title:

    video_card(
        title=title,
        video_id=video_id,
        language=selected
    )

else:

    video_card(
        title="Waiting for video...",
        video_id="",
        language="-"
    )

# -------------------------------------------------
# Statistics
# -------------------------------------------------

st.divider()

if stats:

    statistics(stats)

else:

    statistics({
        "words": 0,
        "lines": 0,
        "characters": 0,
        "reading_time": 0
    })

# -------------------------------------------------
# Transcript Viewer
# -------------------------------------------------

st.divider()

if text:

    transcript_viewer(text)

else:

    transcript_viewer(
        "Transcript will appear here..."
    )

# -------------------------------------------------
# Downloads
# -------------------------------------------------

st.divider()

if filename:

    downloads(filename)

# -------------------------------------------------
# Footer
# -------------------------------------------------

footer()