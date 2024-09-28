import cv2 as cv
import numpy as np

img = cv.imread('image/dog.jpeg')
cv.imshow('Dog', img)


blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)           


img =cv.imread('image/dog.jpeg')
cv.imshow('Dog', img)

# 1. Paint the image a certain color

blank[:] = 0, 255, 0
cv.imshow('Green', blank)

#2 Painting certain part of the image

blank[200:300, 300:400] = 0, 0, 254
cv.imshow('Red', blank)

# 3. Draw a rectangle
cv.rectangle(blank, (0,0), (500,500), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# draw a filled rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle', blank)

# 4. Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=2)
cv.imshow('Circle', blank)  

#draw a filled circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=cv.FILLED)
cv.imshow('Filled Circle', blank)

# 5. Draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=2)
cv.imshow('Line', blank)

# 6. Write text
cv.putText(blank, 'Hello, my name is Dog', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) 
cv.imshow('Text', blank)

cv.waitKey(0)