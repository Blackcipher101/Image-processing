import cv2
import numpy as np

img = cv2.imread('star.png',0)
img1 = cv2.imread('star.png',1)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print approx
t=[]
for i in xrange(len(approx)):
    t.append(approx[i][0])
print t
pts = np.array(t, np.int32)
pts = pts.reshape((-1,1,2))

img1 = cv2.polylines(img1,[pts],True,(0,0,255),thickness= 4)
cv2.imshow('center',img1)
cv2.imshow('cente',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
