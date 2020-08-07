import cv2
import numpy as np

img = cv2.imread('download.png',1)
G = img.copy()
gpA = [G]
str='hey'
for i in xrange(6):
    G = cv2.pyrDown(G)
    str=str+'a'
    cv2.imshow(str,G)
cv2.waitKey(0)
cv2.destroyAllWindows()
