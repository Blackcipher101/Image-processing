import cv2
import numpy as np

img = cv2.imread('thunder.png',0)
img1 = cv2.imread('thunder.png',1)
ret,thresh = cv2.threshold(img,200,255,0)
thresh=cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img1 = cv2.drawContours(img1,[box],0,(0,0,255),2)
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img1 = cv2.circle(img1,center,radius,(0,255,0),2)
ellipse = cv2.fitEllipse(cnt)
img1 = cv2.ellipse(img1,ellipse,(255,255,0),2)
x,y,w,h = cv2.boundingRect(cnt)
print x,y,w,h
img1 = cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,255),2)
cv2.imshow('center',img1)
cv2.imshow('cente',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
