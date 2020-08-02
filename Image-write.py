import numpy as np
import cv2 as cv

img=cv.imread("test.jpg",0)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()
elif k==ord('s'):
    cv.imwrite("img.jpg",img)
    
