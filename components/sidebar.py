import streamlit as st

def sidebar():

    with st.sidebar:

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
            width=170
        )

        st.title("Transcript Fetcher")

        st.caption("Professional Edition")

        st.divider()

        st.subheader("✨ Features")

        features = [
            "Multiple Languages",
            "TXT Export",
            "JSON Export",
            "PDF Export",
            "Statistics",
            "Transcript Preview",
            "Dark Theme"
        ]

        for feature in features:
            st.success(feature)

        st.divider()

        st.subheader("Project")

        st.write("Version **3.0**")

        st.write("Python **3.9+**")

        st.write("Framework **Streamlit**")

        st.divider()

        st.info("Made with ❤️ by Shakira")