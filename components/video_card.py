import streamlit as st

def video_card(title, video_id, language):

    left, right = st.columns([1, 2])

    with left:

        thumbnail = (
            f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        )

        st.image(
            thumbnail,
            use_container_width=True
        )

    with right:

        st.subheader("🎬 Video Details")

        st.success("Video Loaded Successfully")

        st.markdown(f"### {title}")

        st.write("**Video ID:**", video_id)

        st.write("**Language:**", language)