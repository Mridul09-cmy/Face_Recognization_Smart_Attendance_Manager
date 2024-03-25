import cv2
import os
import numpy as np
from PIL import Image

# Path for face image database
path = 'datasets'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImageID(path):
    imagePath = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imagePaths in imagePath:
        try:
            faceImage = Image.open(imagePaths).convert('L')
            faceNP = np.array(faceImage, 'uint8')  # Ensure data type is uint8
            Id = int(os.path.split(imagePaths)[-1].split(".")[1])
            faces.append(faceNP)
            ids.append(Id)
            cv2.imshow("Training", faceNP)
            cv2.waitKey(1)
        except Exception as e:
            print(f"Error processing image {imagePaths}: {e}")
            continue

    return ids, faces

try:
    IDs, facedata = getImageID(path)
    recognizer.train(facedata, np.array(IDs))
    recognizer.save("Trainer.yml")
    cv2.destroyAllWindows()
    print("Training Completed............")
except Exception as e:
    print(f"An error occurred during training: {e}")
