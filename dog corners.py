# Need to reset the images since we drew on them
doggo = cv2.imread('../DATA/sammy.jpg')
doggo = cv2.cvtColor(doggo,cv2.COLOR_BGR2RGB)
gray_doggo = cv2.cvtColor(doggo,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_doggo,10000,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(doggo,(x,y),3,255,-1)

plt.imshow(doggo)