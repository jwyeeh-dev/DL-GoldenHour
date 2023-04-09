import cv2
import mediapipe as mp
import numpy as np

def load_model():
    # Load the Mediapipe instance segmentation model
    model = mp.solutions.SemanticSegmentation(model_selection=1)
    return model

def segment(image, model):
    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform instant segmentation
    results = model.process(image)
    mask = np.stack([results.segmentation_mask]*3, axis=-1)

    # Convert the mask to binary format
    mask = np.where(mask > 0.5, 255, 0).astype('uint8')

    return mask
