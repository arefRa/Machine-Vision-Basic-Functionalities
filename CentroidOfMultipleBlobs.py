import cv2 as cv

# note if you have an error about args not found
# or any errors about cX line
# please input images manually and dicomment the if statement i commented
# sorry master i dont really know why this error happened
# I just found a solution for it online :(

# read image through command line
#img = cv.imread(args["ipimage"])
img = cv.imread('./Input/Lenna.jpg')

# convert the image to grayscale
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv.threshold(gray_image,127,255,0)

# find contours in the binary image
im2, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    M = cv.moments(c)

# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv.circle(img, (cX, cY), 5, (255, 255, 255), -1)
cv.putText(img, "centroid", (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#
#if M["m00"] != 0:
#    cX = int(M["m10"] / M["m00"])
#    cY = int(M["m01"] / M["m00"])
#else:
#    cX, cY = 0, 0

# display the image
cv.imshow("Image", img)
cv.waitKey(0)