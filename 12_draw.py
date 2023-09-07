import cv2 as cv
import numpy as np

# Create a blank Image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank Image", blank);

# Painting the Image with a color
blank[:] = 0,255,0
cv.imshow("Green Image", blank);

# Painting a specific portion of the image with color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Red Portion", blank);

# Creating a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0, 0, 255), thickness=2);
cv.imshow('Rectangle', blank)

# Creating a circle
cv.circle(blank, (250,250), 40, (0, 0, 255), thickness=2);
cv.imshow('Circle', blank)

# Creating a Line
cv.line(blank, (0,0), (250,250), (0, 0, 255), thickness=2);
cv.imshow('Line', blank)

# Putting Text
cv.putText(blank, "Hello I am Anshuman Kundu", (255, 255), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (0,0,255), thickness=3)
cv.imshow('Text', blank);


cv.waitKey(0);