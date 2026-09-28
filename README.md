# 🛡️ AI-Powered DeepFake Detection Using Digital Media Fingerprinting

An AI-powered prototype for detecting potentially manipulated audio and video using machine learning and digital media fingerprinting.


## 🚀 Live Demo
[🔗 Click Here to Open the DeepFake Detector](https://deep-fake-detector-ai.streamlit.app/)

## ✨ Features

- 🎵 Audio DeepFake Detection
- 🎬 Video DeepFake Detection
- 🤖 Random Forest Machine Learning
- 🔐 SHA-256 Digital Fingerprinting
- 📊 Confidence-based Prediction
- 🌐 Streamlit Web Interface
- 🔬 Audio and Video Feature Analysis

## 🧰 Technology Stack

- Python
- Streamlit
- Scikit-learn
- Librosa
- OpenCV
- NumPy
- Pandas
- Joblib
- SHA-256

## ⚙️ How It Works

1. User uploads an audio or video file.
2. Relevant audio or visual features are extracted.
3. The extracted features are analyzed using a trained Random Forest model.
4. A SHA-256 digital fingerprint is generated for the uploaded file.
5. The system displays the prediction and confidence score.

## 🎵 Audio Detection

The audio detector extracts:

- MFCC
- Spectral Centroid
- Spectral Bandwidth
- Zero Crossing Rate

These features are analyzed using a trained Random Forest classifier.

## 🎬 Video Detection

The video detector analyzes:

- Mean Intensity
- Standard Deviation
- Edge Density

These features are passed to a trained Random Forest classifier.

## 🔐 Digital Media Fingerprinting

SHA-256 hashing is used to generate a unique digital fingerprint for the uploaded media file.

The fingerprint can help verify whether the exact uploaded file has changed.

## 📂 Project Structure

```text
DeepFakeDetector/
│
├── app.py
├── home.py
├── audio_detector.py
├── video_detector.py
├── fingerprint.py
├── requirements.txt
│
├── .streamlit/
│   └── config.toml
│
├── models/
│   ├── audio_model.pkl
│   └── video_model.pkl
│
└── pages/
    ├── 2_Detection.py
    └── 3_About.py
