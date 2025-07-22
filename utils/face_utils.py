import cv2
import numpy as np
from PIL import Image

def detect_faces(img_file):
    img = np.array(Image.open(img_file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces.tolist()
