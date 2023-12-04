import cv2
import segmentation
import landmarks

def main():
    # Load the segmentation model
    segmentation_model = segmentation.load_model()
    
    # Load the landmarks model
    landmarks_model = landmarks.load_model()
    
    # Capture an image from a camera
    cap = cv2.VideoCapture(0)
    ret, image = cap.read()
    
    # Perform instant segmentation
    mask = segmentation.segment(image, segmentation_model)
    
    # Detect landmarks on the body
    body_landmarks = landmarks.detect(image, landmarks_model)
    
    # Calculate the distance between the sternum landmark and the other landmarks
    sternum = body_landmarks[12] # index 12 is the landmark for the sternum
    distances = []
    for landmark in body_landmarks:
        distance = calculate_distance(landmark, sternum)
        distances.append(distance)
    
    # Find the landmark closest to the heart
    heart_landmark_index = distances.index(min(distances))
    
    # Visualize the result
    image = visualize_body(image, body_landmarks)
    image = visualize_heart(image, body_landmarks[heart_landmark_index])
    cv2.imshow('result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
