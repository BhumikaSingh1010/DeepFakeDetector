# 🛡️ AI-Powered DeepFake Detection Using Digital Media Fingerprinting

An AI-powered prototype for detecting potentially manipulated audio and video using machine learning and digital media fingerprinting.

## Features

- 🎵 Audio DeepFake Detection
- 🎬 Video DeepFake Detection
- 🤖 Random Forest Machine Learning
- 🔐 SHA-256 Digital Fingerprinting
- 📊 Confidence-based prediction
- 🌐 Streamlit Web Interface

## Technology Stack

- Python
- Streamlit
- Scikit-learn
- Librosa
- OpenCV
- NumPy
- Pandas
- SHA-256

## How It Works

1. Upload an audio or video file.
2. Extract relevant media features.
3. Analyze the features using a trained Random Forest model.
4. Generate a SHA-256 digital fingerprint.
5. Display the detection result and confidence.

## Project Structure

```text
DeepFakeDetector/
├── app.py
├── home.py
├── audio_detector.py
├── video_detector.py
├── fingerprint.py
├── requirements.txt
├── .streamlit/
├── models/
└── pages/

🚀 **[Live Demo](https://deep-fake-detector-ai.streamlit.app)**


## ⚠️ Prototype Limitation

This project is a research and demonstration prototype. The current video detector uses basic visual features such as mean intensity, standard deviation, and edge density. Detection results should not be treated as definitive proof of whether media is authentic or manipulated.

## 🔮 Future Scope

- Advanced CNN and Transformer-based detection
- Face-level manipulation detection
- Temporal frame analysis
- Lip-sync and audio-video consistency checking
- Larger and more diverse datasets
- Explainable AI visualizations
- Database-based detection history

## 👩‍💻 Project

**AI-Powered DeepFake Detection Using Digital Media Fingerprinting**

Built using Python, Streamlit, Machine Learning, and SHA-256 Digital Fingerprinting.
