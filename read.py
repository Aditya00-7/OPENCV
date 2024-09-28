import cv2 as cv

img = cv.imread('image/dog.jpeg')
 
cv.imshow('Dog', img)
cv.imshow('Dog Gray', cv.cvtColor(img, cv.COLOR_BGR2GRAY))

def  rescaleFrame(frame, scale=0.75):
    # work for image, video and live
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeres(width, height):
    # only work for live video
    capture.set(3, width)
    capture.set(4, height)


  # reading video
capture = cv.VideoCapture('video/video11.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()

cv.destroyAllWindows()

cv.waitKey(0) 