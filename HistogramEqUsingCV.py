import cv2 as cv
import numpy as np

img = cv.imread("imgs/puppy.jpg")

# creating a Histograms Equalization
# of a image using cv.equalizeHist()
equ = cv.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv.imshow('Hist',res)
cv.waitKey(0)
cv.destroyAllWindows()