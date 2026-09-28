import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #FFFDF8;
}

[data-testid="stSidebar"] {
    background: #FFF8E7;
}

.title {
    font-size: 42px;
    font-weight: 800;
}

.orange {
    color: #F57C00;
}

.card {
    background: white;
    border: 1px solid #FFE0A3;
    border-radius: 20px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 4px 15px #F57C0012;
}

.highlight {
    background: #FFF5D6;
    border-left: 5px solid #FFB300;
    padding: 18px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:

    st.markdown(
        "<h1 style='text-align:center'>🛡️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center'>DeepFake "
        "<span class='orange'>Detector</span></h2>",
        unsafe_allow_html=True
    )

    st.caption("Verify • Detect • Stay Safe")
    st.divider()
    st.write("ℹ️ About the Project")

# Title
st.markdown("""
<div class="title">
ℹ️ About <span class="orange">The Project</span>
</div>

<p style="color:#667085;font-size:17px;">
AI-powered detection and digital media verification prototype.
</p>
""", unsafe_allow_html=True)

# Objective
st.markdown("""
<div class="card">
<h2>🎯 Project Objective</h2>

<p>
The objective of this project is to develop a prototype
capable of analyzing audio and video media for patterns
that may indicate AI-generated or manipulated content.
</p>
</div>
""", unsafe_allow_html=True)

# Methodology
st.subheader("⚙️ Methodology")

steps = [
    ("📁", "Media Upload",
     "User uploads an audio or video file."),

    ("🔬", "Feature Extraction",
     "Important audio or visual characteristics are extracted."),

    ("🤖", "Machine Learning",
     "Random Forest analyzes the extracted features."),

    ("🔐", "Digital Fingerprinting",
     "SHA-256 creates a unique fingerprint of the media."),

    ("📊", "Result",
     "The system displays prediction and confidence.")
]

for icon, title, description in steps:
    st.markdown(
        f"""
        <div class="card">
        <h3>{icon} {title}</h3>
        <p style="color:#666">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Technology
st.subheader("🧰 Technology Stack")

cols = st.columns(3)

tech = [
    ("🐍 Python", "Core programming language."),
    ("🌐 Streamlit", "Interactive web application."),
    ("🤖 Scikit-learn", "Random Forest machine learning.")
]

for col, (title, description) in zip(cols, tech):
    with col:
        st.markdown(
            f"""
            <div class="card">
            <h3>{title}</h3>
            <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Limitation
st.subheader("⚠️ Prototype Limitation")

st.markdown("""
<div class="highlight">

This is a research and demonstration prototype.
The current video model uses basic visual features
such as mean intensity, standard deviation and edge density.

A production system would require a much larger,
diverse and carefully validated dataset together
with more advanced deepfake detection techniques.

</div>
""", unsafe_allow_html=True)

# Future scope
st.subheader("🚀 Future Scope")

st.markdown("""
- Advanced CNN / Transformer-based video analysis
- Face-level manipulation detection
- Temporal frame analysis
- Lip-sync and audio-video consistency checking
- Larger benchmark datasets
- Database-based analysis history
- Explainable AI visualizations
""")

st.divider()

st.markdown("""
<p style="text-align:center;color:#777">
🛡️ DeepFake Detector • Verify • Detect • Stay Safe
</p>
""", unsafe_allow_html=True)
