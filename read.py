import cv2  as cv

img = cv.imread('image/dog.jpeg')
 
cv.imshow('Dog', img)
cv.imshow('Dog Gray', cv.cvtColor(img, cv.COLOR_BGR2GRAY))

def  rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
  # reading video
capture = cv.VideoCapture('video/video11.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0) 