import cv2 as cv
import numpy as np

img = cv.imread('Images/yoga.jpg')
cv.imshow("Image", img);

# Splitting the image into its b,g,r grayscales pixel concentrations : This way splits the image into b,g and r providing the lighter regions being the more concentrations of that porticular color.
b,g,r = cv.split(img);
cv.imshow('Blue', b);
cv.imshow('Green', g);
cv.imshow('Red', r);

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# How can we merge these images back to the original Image;
merged = cv.merge([b,g,r]);
cv.imshow("Merged", merged);


# If we want the actual color scales instead of gray scale splitting
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red);

cv.waitKey(0);