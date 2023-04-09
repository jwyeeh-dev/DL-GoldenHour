import cv2
import mediapipe as mp

def load_model():
    # Load the Mediapipe Holistic model
    model = mp.solutions.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    return model

def detect(image, model):
    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the landmarks
    results = model.process(image)
    landmarks = results.pose_landmarks.landmark

    return landmarks
