import streamlit as st

st.set_page_config(
    page_title="DeepFake Detector",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp{background:#FFFDF8}
[data-testid="stSidebar"]{background:#FFF8E7}
.orange{color:#F57C00}
.hero,.card,.step{
    background:white;
    border:1px solid #FFE0A3;
    border-radius:20px;
    padding:25px;
    margin:12px 0;
    box-shadow:0 4px 15px #F57C0012
}
.hero{background:linear-gradient(135deg,#FFF4D6,#FFF)}
.title{font-size:46px;font-weight:800}
.sub{color:#667085;font-size:18px}
.badge{
    background:#FFF0C2;
    color:#D96B00;
    padding:7px 14px;
    border-radius:20px
}
.step{background:#FFF9ED}
.footer{text-align:center;color:#777;padding:25px}
</style>
""", unsafe_allow_html=True)

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
    st.info("AI-powered media analysis with digital fingerprinting.")

st.markdown("""
<div class="hero">
<span class="badge">🛡️ AI MEDIA SECURITY</span>

<div class="title">
Welcome to <span class="orange">DeepFake</span> Detector
</div>

<p class="sub">
Detect potential AI-generated or manipulated audio and video
using machine learning, feature analysis and SHA-256
digital fingerprinting.
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("✨ What Our System Does")

cols = st.columns(3)

features = [
    ("🎵 Audio Detection",
     "Analyzes MFCC and spectral features using a Random Forest model."),
    ("🎬 Video Detection",
     "Analyzes mean intensity, standard deviation and edge density."),
    ("🔐 Digital Fingerprint",
     "Generates a SHA-256 fingerprint for media integrity verification.")
]

for col, (title, description) in zip(cols, features):
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

st.subheader("⚙️ How It Works")

steps = [
    ("1️⃣", "Upload Media", "Upload an audio or video file."),
    ("2️⃣", "Extract Features", "Extract important audio or visual characteristics."),
    ("3️⃣", "AI Prediction", "Random Forest analyzes the extracted features."),
    ("4️⃣", "Verify Integrity", "Generate a SHA-256 digital fingerprint.")
]

for icon, title, description in steps:
    st.markdown(
        f"""
        <div class="step">
        <b>{icon} {title}</b><br>
        <span style="color:#777">{description}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.subheader("🧰 Technology Stack")

cols = st.columns(5)

tech = [
    ("Language", "Python"),
    ("Interface", "Streamlit"),
    ("Model", "Random Forest"),
    ("Fingerprint", "SHA-256"),
    ("Analysis", "Audio + Video")
]

for col, (name, value) in zip(cols, tech):
    col.metric(name, value)

st.markdown("""
<div class="card">
<h3>💡 Project Highlight</h3>

<p>
Machine learning analyzes media characteristics while SHA-256
creates a unique fingerprint for the uploaded file.
Together, the system provides both
<b>media analysis</b> and <b>file integrity verification</b>.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
🛡️ <b>DeepFake Detector</b><br>
Verify • Detect • Stay Safe<br><br>
Built with Python • Streamlit • Machine Learning
</div>
""", unsafe_allow_html=True)