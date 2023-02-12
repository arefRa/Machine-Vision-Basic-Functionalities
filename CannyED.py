import cv2 as cv

img1 = cv.imread('imgs/Lenna.jpg')
img2 = cv.imread('imgs/LightHouse.jpg')

cv.imshow('Lenna',img1)
#cv.imshow('Lighthouse',img2)

# canny edge usign openCv:

canny = cv.Canny(img1,125,175)
cv.imshow('CannyEdges',canny)

#cannyLightHouse = cv.Canny(img2,125,175)
#cv.imshow('CannyEdges',cannyLightHouse)

#cv.imwrite("./output/CannyLenna.jpg",canny)
cv.waitKey(0)
