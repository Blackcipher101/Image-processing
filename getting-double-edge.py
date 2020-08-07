import cv2
import numpy as np

img = cv2.imread('box.png',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
cv2.imshow('img',img)
cv2.imshow('sobelx8u',sobelx8u)
cv2.imshow('sobel_8u',sobel_8u)
cv2.waitKey(0)
cv2.destroyAllWindows()
