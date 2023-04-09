import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import time
import math
from utils.pose_utils import find_xyz, calculate_angle3D, calculate_angle2D, calculate_angle, get_distance

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


def estimate_pose(image):
    # Define initial state and count as list
    temp = ['up']
    count = [0]
    results = pose.process(image)

    if results.pose_landmarks is not None:
        # Get the coordinates of landmark 26, 15, and 25
        landmark_left_knee = [results.pose_landmarks.landmark[26].x, results.pose_landmarks.landmark[26].y]
        landmark_left_wrist = [results.pose_landmarks.landmark[15].x, results.pose_landmarks.landmark[15].y]
        landmark_right_knee = [results.pose_landmarks.landmark[25].x, results.pose_landmarks.landmark[25].y]

        # Calculate the angle between landmark 26, 15, and 25
        angle = calculate_angle(landmark_left_knee, landmark_left_wrist, landmark_right_knee)

        # Check if the angle is less than 90 degrees
        if angle < 90:
            temp.append('up')

        # Check if the angle is greater than 105 degrees
        elif angle > 105:
            temp.append('down')

            # If the state of 'temp' changed from 'up' to 'down', increment 'count'
            if temp[-2] == 'up':
                count.append(count[-1] + 1)

        # If the angle is between 90 and 105 degrees
        else:
            # Remove the 'Please pressure more' text if it is visible
            if len(temp) > 1 and temp[-2] == 'down':
                cv2.putText(image, "", (int(image.shape[1]/2), int(image.shape[0]/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            temp.append('up')

        # Display the 'Please pressure more' text if the state of 'temp' is 'up'
        if temp[-1] == 'up':
            cv2.putText(image, "Please pressure more", (int(image.shape[1]/2), int(image.shape[0]/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Display the count in the top left corner of the video
        cv2.putText(image, f"Count: {count[-1]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return image