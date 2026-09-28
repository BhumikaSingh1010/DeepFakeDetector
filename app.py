import streamlit as st

st.set_page_config(
    page_title="DeepFake Detector",
    page_icon="🛡️",
    layout="wide"
)

home = st.Page("home.py", title="Home", icon="🏠")
detection = st.Page("pages/2_Detection.py", title="Detection", icon="🔍")
about = st.Page("pages/3_About.py", title="About", icon="ℹ️")

pg = st.navigation([home, detection, about], position="sidebar")
pg.run()