import cv2
import numpy as np

img = cv2.imread('circle.png',0)
img1 = cv2.imread('circle.png',1)
ret,thresh = cv2.threshold(img,200,255,0)
thresh=cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
img1 = cv2.circle(img1,leftmost, 2, (0,0,255), -1)
img1 = cv2.circle(img1,rightmost, 2, (0,0,255), -1)
img1 = cv2.circle(img1,topmost, 2, (0,0,255), -1)
img1 = cv2.circle(img1,bottommost, 2, (0,0,255), -1)
cv2.imshow("image06",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
