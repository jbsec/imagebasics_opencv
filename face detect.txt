#face detection (not recogn)
# imports
import numpy as np
import cv2 
import matplotlib.pyplot as plt
%matplotlib inline

# read in images
# change dir to your own resources
nadia = cv2.imread('../DATA/Nadia_Murad.jpg',0)
denis = cv2.imread('../DATA/Denis_Mukwege.jpg',0)
solay = cv2.imread('../DATA/solvay_conference.jpg',0)

# pass in classifier
# classify features of faces
face_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img
result = detect_face(solay)
plt.imshow(result,cmap='gray')