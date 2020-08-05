import cv2
import numpy as np

img = cv2.imread('testobstu.png',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('ori',img)
cv2.imshow('bin',th1)
cv2.imshow('just otsu',th2)
cv2.imshow('gauss and Otsu',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
