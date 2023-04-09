import cv2
import mediapipe as mp

image = cv2.imread("image.jpg")

pose = mp.solutions.pose.Pose()

result = pose.process(image)

if result.pose_landmarks:
    for landmark in result.pose_landmarks.landmark:
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
