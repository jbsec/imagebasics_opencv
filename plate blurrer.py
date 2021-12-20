import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img = cv2.imread('../DATA/car_plate.jpg')

#scale and color
def display(img):
    fig = plt.figure(figsize=(10,8))
    ax = fix.subplot(111)
    new_img = cv2.cvtColor(img,cv2.COLORBGR2RGB)
    ax.imshow(new_img)
    display(img)

#load classifer
plate_cascade = cv2.CascadeClassifier('../DATA/haarcascade_russian_plate_number.xl')

def detect_plate(img):
    plate_img = img.copy()
    
    plate_rects = plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)
    
    for (x,y,w,h) in plate_rects:
        cv2.rectangle(plate_img,(x,y),(x+w,y+h),(0,0,255),4)
        
    return plate_img

    display(result)
    
def detect_and_blur_plate(img):
    plate_img.copy()
    roi = img.copy()
    
    plate_rects = plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)
    
    for (x,y,w,h) in plate_rects:
        roi = roi[y:y+h,x:x+w]
        blurred_roi = cv2.medianBlue(roi,7)
        plate_img[y:y,x:x+w] = blurred_roi
        
    return plate_img