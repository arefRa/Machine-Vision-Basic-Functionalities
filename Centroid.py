import cv2 as cv

# this first step is to turn img into grayscale
# for binarization purposes

simpleImage = cv.imread('./Input/lena_color.jpg')
grayImage = cv.cvtColor(simpleImage,cv.COLOR_BGR2GRAY)

# feel free to use already graied image:
# grayImage = cv.imread("./Input/Lenna.jpg")

# now converting grayImg to binaryImg and finding the moments
# all discribed in EX06 PDF file

ret,thresh = cv.threshold(grayImage,127,255,0)
M = cv.moments(thresh)

# calculating the coordinates of the center:

cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# this part is for highlighting the center:

cv.circle(simpleImage, (cX, cY), 5, (255, 255, 255), -1)
cv.putText(simpleImage, "centroid", (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv.imshow("Image", simpleImage)
cv.waitKey(0)