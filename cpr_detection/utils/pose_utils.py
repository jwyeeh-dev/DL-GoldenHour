import numpy as np
import math

def find_xyz(ind_list, landmark):
    a = landmark[ind_list[0]]
    b = landmark[ind_list[1]]
    c = landmark[ind_list[2]]

    first = [a.x,a.y,a.z]
    mid = [b.x,b.y,b.z]
    end = [c.x,c.y,c.z]
    return first, mid, end

def calculate_angle3D(a, b, c, direction):

    """
    calculate_angle3D is divided by left and right side because this function uses external product
    input : a,b,c -> landmarks with shape [x,y,z,visibility]
        direction -> int -1 or 1
                    -1 means Video(photo) for a person's left side and 1 means Video(photo) for a person's right side
    output : angle between vector ba and bc with range 0~360
    """

    # external product's z value
    external_z = (b[0] - a[0]) * (b[1] - c[1]) - (b[1] - a[1]) * (b[0] - c[0])

    a = np.array(a) # first
    b = np.array(b) # mid
    c = np.array(c) # end

    ba = b - a
    bc = b - c
    dot_result = np.dot(ba, bc)


    ba_size = np.linalg.norm(ba)
    bc_size = np.linalg.norm(bc)
    radi = np.arccos(dot_result / (ba_size * bc_size))
    angle = np.abs(radi * 180.0 / np.pi)

    # left side
    if external_z * direction > 0:
        angle = 360 - angle

    return angle

def calculate_angle2D(a, b, c, direction):

    """
    calculate_angle2D is divided by left and right side because this function uses external product
    input : a,b,c -> landmarks with shape [x,y,z,visibility]
            direction -> int -1 or 1
                        -1 means Video(photo) for a person's left side and 1 means Video(photo) for a person's right side
    output : angle between vector ba and bc with range 0~360
    """

    # external product's z value
    external_z = (b[0] - a[0]) * (b[1] - c[1]) - (b[1] - a[1]) * (b[0] - c[0])

    a = np.array(a[:2]) # first
    b = np.array(b[:2]) # mid
    c = np.array(c[:2]) # end

    ba = b - a
    bc = b - c
    dot_result = np.dot(ba, bc)


    ba_size = np.linalg.norm(ba)
    bc_size = np.linalg.norm(bc)
    radi = np.arccos(dot_result / (ba_size * bc_size))
    angle = np.abs(radi * 180.0 / np.pi)

    if external_z * direction > 0:
        angle = 360 - angle

    return angle

# Define function to calculate angle between landmarks
def calculate_angle(a, b, c):
    a = np.array(a) # landmark 26
    b = np.array(b) # landmark 15
    c = np.array(c) # landmark 25
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def get_distance(lm_from, lm_to):
    x2 = (lm_from.x - lm_to.x) ** 2
    y2 = (lm_from.y-lm_to.y) ** 2
    return (x2+y2) ** 0.5
