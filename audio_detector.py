import librosa
import numpy as np


def extract_audio_features(file_path):

    audio, sample_rate = librosa.load(
        file_path,
        sr=None
    )

    # MFCC
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=13
    )

    # Spectral Centroid
    spectral_centroid = librosa.feature.spectral_centroid(
        y=audio,
        sr=sample_rate
    )

    # Spectral Bandwidth
    spectral_bandwidth = librosa.feature.spectral_bandwidth(
        y=audio,
        sr=sample_rate
    )

    # Zero Crossing Rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(
        audio
    )

    features = np.concatenate([
        np.mean(mfcc, axis=1),
        np.mean(spectral_centroid, axis=1),
        np.mean(spectral_bandwidth, axis=1),
        np.mean(zero_crossing_rate, axis=1)
    ])

    return features