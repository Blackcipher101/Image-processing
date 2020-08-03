import numpy as np
import cv2



c=1
r=3
cap = cv2.VideoCapture('output.avi')
cap.set(cv2.CAP_PROP_FPS, 10)
def onChange(trackbarValue):
    global cap
    cap.set(1,trackbarValue)



length=int(cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT))
print(length)
cv2.namedWindow('frame')
cv2.createTrackbar( 'trackbar', 'frame', 0, length, onChange )
while True:
    #ret,frame=cap.read()
    if c!=0 or r==2:
        ret,frame=cap.read()
        set=int(cap.get(1))
        cv2.setTrackbarPos('trackbar', 'frame', set)
        cv2.imshow("frame",frame)
        c=1
        r=3
    k=cv2.waitKey(10)
    if k==ord('s'):
        c=0
    if k==ord('r'):
        r=2




cap.release()
cv2.destroyAllWindows()
