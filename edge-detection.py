import cv2
import numpy as np

img = cv2.imread('download.png',0)
edges = cv2.Canny(img,100,200)
cv2.namedWindow('edges', cv2.WINDOW_NORMAL)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('edges',edges)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
