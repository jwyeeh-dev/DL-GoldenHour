import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import time
import math
from pose_utils import find_xyz, calculate_angle3D, calculate_angle2D, calculate_angle, get_distance

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def find_pressing_point(image, pose):
    image_height, image_width, _ = image.shape
    results = pose.process(image)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Calculate the middle point between landmarks 11 and 12
        x1, y1 = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
        x2, y2 = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
        x_mid_1, y_mid_1 = (x1 + x2) / 2 * image_width, (y1 + y2) / 2 * image_height
        

        # Calculate the middle point between landmarks 23 and 24
        x1, y1 = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
        x2, y2 = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
        x_mid_2, y_mid_2 = (x1 + x2) / 2 * image_width, (y1 + y2) / 2 * image_height
        

        # Calculate the 2/3 point between the two middle points
        x, y = (2 * x_mid_1 + x_mid_2) / 3, (2 * y_mid_1 + y_mid_2) / 3

        # Fit the 1/3 point coordinate to the video size
        x, y = int(max(min(x, image_width), 0)), int(max(min(y, image_height), 0))

        # Draw a green circle on the 1/3 point
        cv2.circle(image, (x, y), 10, (0, 255, 0), -1)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    return image