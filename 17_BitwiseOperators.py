import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype='uint8');
rectangle = cv.rectangle(blank.copy(), (30,30), (300,300), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle);

# Bitwise And : Shwws the intersection point
bitwise_and = cv.bitwise_and(rectangle, circle);
cv.imshow('Bitwise And', bitwise_and)

# Bitwise Or: Shows the intersection and non-intersections
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise Or', bitwise_or);

# Bitwise XOR : Shows the non-intersections
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor);

# Bitwise not : Shows the inversion of a particular image
bitwise_not = cv.bitwise_not(rectangle);
cv.imshow('Bitwise Not', bitwise_not);

cv.waitKey(0);