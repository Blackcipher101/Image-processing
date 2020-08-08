import cv2
import numpy as np

img = cv2.imread('thunder.png',0)
img1 = cv2.imread('thunder.png',1)
ret,thresh = cv2.threshold(img,200,255,0)
thresh=cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
equi_diameter = np.sqrt(4*area/np.pi)
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print "area:",area
print "extent:",extent
print "as:",aspect_ratio
print "equi_diameter:",equi_diameter
print "angle:",angle
