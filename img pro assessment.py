import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# directory may change, this is default
img = cv2.imread('../DATA/giraffes.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
display_img(img)

img = cv2.imread('../DATA/giraffes.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

display_img(thresh1,cmap='gray')

img = cv2.imread('../DATA/giraffes.jpg')

#convert to hsv hue sat value
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
display_img(img)

# just leaving it here, need to move on quick. 
