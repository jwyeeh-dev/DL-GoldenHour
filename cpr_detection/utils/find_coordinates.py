import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import time
import math

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def find_xyz(ind_list, landmark):
  a = landmark[ind_list[0]]
  b = landmark[ind_list[1]]
  c = landmark[ind_list[2]]

  first = [a.x,a.y,a.z]
  mid = [b.x,b.y,b.z]
  end = [c.x,c.y,c.z]
  return first, mid, end