import numpy as np
import cv2
im=cv2.imread('testobstu.png',0)

blur = cv2.GaussianBlur(im,(5,5),0)



h, g = np.histogram(im.ravel(), 256, [0, 256])
h = h.astype(np.float)
g = g.astype(np.float)[:-1]
c = np.cumsum(h)
m = np.cumsum(h * g)
s = np.cumsum(h * g**2)
cb = c[-1] - c
mb = m[-1] - m
sb = s[-1] - s
with np.errstate(invalid='ignore', divide='ignore'):
    sigma_f = np.sqrt(s/c - (m/c)**2)
    sigma_b = np.sqrt(sb/cb - (mb/cb)**2)
    p = c / c[-1]
    v = p * np.log(sigma_f) + (1-p)*np.log(sigma_b) - p*np.log(p) - (1-p)*np.log(1-p)
v[~np.isfinite(v)] = np.inf
idx = np.argmin(v)
t = g[idx]
thresh = im.copy()
thresh[thresh > t] = 255
thresh[thresh < t]  = 0
cv2.imshow("Otsu", thresh)
cv2.imshow("orignal", im)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
