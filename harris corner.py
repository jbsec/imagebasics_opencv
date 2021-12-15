#### imports ####

import cv2 
import numpy as np  

import matplotlib.pyplot as plt
%matplotlib inline


### Image Reads & Converts ###

flat_chess = cv2.imread('../DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
#plt.imshow(gray_flat_chess,cmap='gray')
gray = np.float32(gray_flat_chess) # Make sure flt is int

### Harris Corner Detection ###

dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

## Result ##

dst = cv2.dilate(dst,None)

## Thresh ###

flat_chess[dst>0.01*dst.max()] = [255,0,0] #rgb chan for red.
