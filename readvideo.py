import cv2
cap = cv2.VideoCapture(0) #default video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #capture property
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# windows dvix and macos or linux xvid codec
writer = cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,width,height)#20fps to be safe?

while True:
    ret,frame = cap.read()
    # comment out gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    writer.write(frame)
    
    # feed just frame for color below
    cv2.imshow('frame',gray)
    #mac linux need a sep script 4 this
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break #wait till q is pressed to break
        
cap.release()
writer.release()
cv2.destroyAllWindows()