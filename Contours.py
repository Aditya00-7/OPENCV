import cv2 as cv

img =cv.imread('image/dog.jpeg')
cv.imshow('dog', img)

# blank = cv.imread('image/blank.jpg')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)           
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
# ret,thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh) 

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)    # cv.RETR_LIST, cv.RETR_EXTERNAL, cv.RETR_TREE


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

print(f'{len(contours)} contour(s found!')


cv.waitKey(0)