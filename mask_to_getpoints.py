import cv2
import numpy as np

img = cv2.imread('thunder.png',0)
img1 = cv2.imread('thunder.png',1)
ret,thresh = cv2.threshold(img,200,255,0)
thresh=cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
mask = np.zeros(img.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
#pixelpoints = np.transpose(np.nonzero(mask))
pixelpoints = cv2.findNonZero(mask)
print pixelpoints
