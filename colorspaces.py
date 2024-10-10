import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image/dog.jpeg')
cv.imshow('dog', img)

plt.imshow(img)
plt.show()

#bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)    
cv.imshow('LAB', lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

#lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB_BGR', lab_bgr)

cv.waitKey(0)