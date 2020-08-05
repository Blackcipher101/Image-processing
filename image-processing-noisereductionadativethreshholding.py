import cv2
import numpy as np

img = cv2.imread('testobstu.png',0)
#img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('orginal',img)
cv2.imshow('binary',th1)
cv2.imshow('mean',th2)
cv2.imshow('guass',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
