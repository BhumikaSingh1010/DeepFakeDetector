import cv2
import numpy as np


def extract_video_features(file_path, max_frames=20):

    video = cv2.VideoCapture(file_path)

    if not video.isOpened():
        raise ValueError("Unable to open video file.")

    features = []

    frame_count = 0

    while frame_count < max_frames:

        success, frame = video.read()

        if not success:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize frame
        gray = cv2.resize(gray, (128, 128))

        # Calculate basic visual statistics
        mean_intensity = np.mean(gray)
        std_intensity = np.std(gray)

        # Edge detection
        edges = cv2.Canny(gray, 100, 200)

        edge_density = np.mean(edges > 0)

        # Store frame-level features
        features.append([
            mean_intensity,
            std_intensity,
            edge_density
        ])

        frame_count += 1

    video.release()

    if len(features) == 0:
        raise ValueError("No frames could be extracted from the video.")

    # Convert to NumPy array
    features = np.array(features)

    # Average features across frames
    final_features = np.mean(features, axis=0)

    return final_features