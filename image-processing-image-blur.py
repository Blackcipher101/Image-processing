import cv2
import numpy as np

img = cv2.imread('testobstu.png')

kernel = np.ones((6,6),np.float32)/36
dst = cv2.filter2D(img,-1,kernel)
med=cv2.medianBlur(img,5)
Nblur = cv2.blur(img,(5,5))
Gblur = cv2.GaussianBlur(img,(5,5),0)
Bblur = cv2.bilateralFilter(img,15,75,75)
cv2.imshow('ori',img)
cv2.imshow('reduced',dst)
cv2.imshow('median',med)
cv2.imshow('Nblu',Nblur)
cv2.imshow('Gauss',Gblur)
cv2.imshow('Bilateral',Bblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
