import cv2
import numpy as np

img = cv2.imread('testobstu.png')
rows,cols,ch = img.shape
img = cv2.circle(img,(100,50), 1, (0,0,255), -1)
img = cv2.circle(img,(150,50), 1, (0,0,255), -1)
img = cv2.circle(img,(50,250), 1, (0,0,255), -1)
img = cv2.circle(img,(250,250), 1, (0,0,255), -1)

pts1 = np.float32([[100,50],[150,50],[50,250],[250,250]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('change',dst)
cv2.imshow('ori',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
