import cv2
import numpy as np

img = cv2.imread('testobstu.png')

kernel = np.ones((6,6),np.float32)/36
dst = cv2.filter2D(img,-1,kernel)
med=cv2.medianBlur(img,5)
blur = cv2.blur(img,(5,5))
cv2.imshow('reduced',dst)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
