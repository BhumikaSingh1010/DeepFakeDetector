import os
import joblib
import streamlit as st

from fingerprint import generate_fingerprint
from audio_detector import extract_audio_features
from video_detector import extract_video_features

st.set_page_config(
    page_title="Detection",
    page_icon="🔍",
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

.upload-card,
.result-card,
.info-card {
    background: white;
    border: 1px solid #FFE0A3;
    border-radius: 20px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 4px 15px #F57C0012;
}

.upload-card {
    border: 2px dashed #FFB300;
}

.info-card {
    background: #FFF8E7;
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
    st.markdown("### 🔍 Detection")
    st.write("Analyze audio and video media.")

# Title
st.markdown("""
<div class="title">
🔍 Media <span class="orange">Detection</span>
</div>

<p style="color:#667085;font-size:17px;">
Upload your media file and analyze it using
machine learning and digital fingerprinting.
</p>
""", unsafe_allow_html=True)

st.divider()

# Upload
st.markdown("""
<div class="upload-card">
<h2>📁 Upload Media</h2>
<p style="color:#777">
Supported formats: WAV, MP3, MP4, AVI, MOV
</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["wav", "mp3", "mp4", "avi", "mov"],
    label_visibility="collapsed"
)

if uploaded_file:

    st.success("✅ File uploaded successfully!")

    # File information
    st.subheader("📄 File Information")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("File Name", uploaded_file.name)

    with c2:
        st.metric("File Type", uploaded_file.type)

    with c3:
        st.metric(
            "Size",
            f"{uploaded_file.size / 1024:.2f} KB"
        )

    # Fingerprint
    fingerprint = generate_fingerprint(uploaded_file)

    st.subheader("🔐 SHA-256 Digital Fingerprint")
    st.code(fingerprint)

    # Save uploaded file
    os.makedirs("uploads", exist_ok=True)

    temp_file = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # AUDIO
    if uploaded_file.type.startswith("audio"):

        st.subheader("🎵 Audio Analysis")

        try:
            features = extract_audio_features(temp_file)

            model = joblib.load(
                "models/audio_model.pkl"
            )

            prediction = model.predict([features])[0]

            probabilities = model.predict_proba(
                [features]
            )[0]

            confidence = max(probabilities) * 100

            if prediction == 0:
                st.success("✅ MEDIA APPEARS REAL")
            else:
                st.error("⚠️ POTENTIAL DEEPFAKE DETECTED")

            st.subheader("📊 Detection Results")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

            with c2:
                st.metric(
                    "Features",
                    len(features)
                )

            with c3:
                st.metric(
                    "Media Type",
                    "Audio"
                )

            st.markdown("""
            <div class="info-card">
            <b>🤖 Model:</b> Random Forest<br><br>
            <b>🔬 Features:</b> MFCC, Spectral Centroid,
            Spectral Bandwidth, Zero Crossing Rate<br><br>
            <b>🔐 Verification:</b> SHA-256
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🔬 View Extracted Features"):

                for i, value in enumerate(features):
                    st.write(
                        f"Feature {i + 1}: {value:.4f}"
                    )

        except Exception as e:
            st.error(
                f"❌ Audio analysis failed: {e}"
            )

    # VIDEO
    elif uploaded_file.type.startswith("video"):

        st.subheader("🎬 Video Analysis")

        try:
            features = extract_video_features(
                temp_file
            )

            model = joblib.load(
                "models/video_model.pkl"
            )

            prediction = model.predict([features])[0]

            probabilities = model.predict_proba(
                [features]
            )[0]

            confidence = max(probabilities) * 100

            if prediction == 0:
                st.success("✅ MEDIA APPEARS REAL")
            else:
                st.error("⚠️ POTENTIAL DEEPFAKE DETECTED")

            st.subheader("📊 Detection Results")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

            with c2:
                st.metric(
                    "Features",
                    len(features)
                )

            with c3:
                st.metric(
                    "Media Type",
                    "Video"
                )

            st.markdown("""
            <div class="info-card">
            <b>🤖 Model:</b> Random Forest<br><br>
            <b>🔬 Features:</b> Mean Intensity,
            Standard Deviation, Edge Density<br><br>
            <b>🔐 Verification:</b> SHA-256
            </div>
            """, unsafe_allow_html=True)

            st.subheader("🔬 Video Feature Values")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Mean Intensity",
                    f"{features[0]:.3f}"
                )

            with c2:
                st.metric(
                    "Std Deviation",
                    f"{features[1]:.3f}"
                )

            with c3:
                st.metric(
                    "Edge Density",
                    f"{features[2]:.3f}"
                )

        except Exception as e:
            st.error(
                f"❌ Video analysis failed: {e}"
            )

st.divider()

st.caption(
    "🛡️ DeepFake Detector | "
    "Machine Learning + Digital Fingerprinting"
)
