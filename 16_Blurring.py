import cv2 as cv

img = cv.imread('Images/yoga.jpg')
cv.imshow('Image', img);



# Averaging Blur
averaging =  cv.blur(img, (3,3))
cv.imshow("Avrage Blur", averaging);


# Gaussian Blur 
gausBlur = cv.GaussianBlur(img, (3,3), 0);
cv.imshow("Gaussian Blur", gausBlur);


# Median Blur
median = cv.medianBlur(img, 3);
cv.imshow('Median Blur', median);


# Bilateral Blur
bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow('Bilateral', bilateral)











cv.waitKey(0)