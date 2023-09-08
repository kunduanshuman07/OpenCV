import cv2 as cv
import numpy as np

img = cv.imread('_happy_jumping_on_beach-40815.jpg')

# Grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the canny Image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated);

# Eroding the dilated image back to canny 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized',resized)


cv.waitKey(0)