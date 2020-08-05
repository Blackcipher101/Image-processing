import cv2
import numpy as np

img = cv2.imread('img.jpg',0)
cv2.namedWindow('binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('binaryinv', cv2.WINDOW_NORMAL)
cv2.namedWindow('trunc', cv2.WINDOW_NORMAL)
cv2.namedWindow('tozen', cv2.WINDOW_NORMAL)
cv2.namedWindow('in_tozen', cv2.WINDOW_NORMAL)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('binary',thresh1)
cv2.imshow('binaryinv',thresh2)
cv2.imshow('trunc',thresh3)
cv2.imshow('tozen',thresh4)
cv2.imshow('in_tozen',thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()
