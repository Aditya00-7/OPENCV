import cv2 as cv

img = cv.imread('image/dog.jpeg')
cv.imshow('dog', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)



cv.waitKey(0)