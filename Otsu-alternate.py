import numpy as np
import mahotas
import cv2

image = cv2.imread('testobstu.png',0)
blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

T = mahotas.thresholding.otsu(blurred)
thresh = blurred.copy()
thresh[thresh > T] = 255
thresh[thresh < T]  = 0
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
