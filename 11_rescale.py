import cv2 as cv


# Function to rescale standalone Videos/Images
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[0]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA);



# Function to rescale or change resolution of live videos
def changeRes(width, height):
    capture.set(3, width);
    capture.set(4, height);



# Resizing Video
capture = cv.VideoCapture(0);
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame);
    cv.imshow('Video', resized_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break;


# Resizing Image
img = cv.imread('Images/_happy_jumping_on_beach-40815.jpg')
resized_image = rescaleFrame(img)
cv.imshow('Happy Face', resized_image);


capture.release();
capture.destroyAllWindows();
cv.waitKey(0)