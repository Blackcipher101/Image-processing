import cv2
import numpy as np

img = cv2.imread('circle.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,' ',cy)
img = cv2.circle(img,(cx,cy), 2, (255,255,255), -1)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)
print "area:",area
print "peri:",perimeter
cv2.imshow('center',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
