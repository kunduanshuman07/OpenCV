# Importing cv2
import cv2 as cv;

 # Reading Images
img = cv.imread('Images/_happy_jumping_on_beach-40815.jpg')
cv.imshow('Happy Face', img);

# Reading Videos
capture = cv.VideoCapture(0);
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break;

capture.release();
capture.destroyAllWindows();



# Waitkey for viewing the image/video
cv.waitKey(0)
