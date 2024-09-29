import cv2 as cv

img = cv.imread('image/dog.jpeg')
cv.imshow('dog', img)


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
cv.imshow('Blur', cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT))
cv.imshow('Blur', cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT))

# Edge Cascade
canney = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', cv.Canny(img, 125, 175))

# Dilating the image
dilated = cv.dilate(canney, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)