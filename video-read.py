import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    k=cv2.waitKey(60)
    if k== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
