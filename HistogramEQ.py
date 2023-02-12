import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image

# what ever we execute will come inline instead of a new window
# similar to what master said
# matplotlib inline also can be used with a % sign in ipynb formats
# use at your own will

img1 = cv.imread("/imgs/puppy.jpg")

grayImg1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

# in order to know the size of the image:
(ro,co) = (grayImg1.shape)

indexPixel = 0

# a zeros mat for histogram to find intensity vs frequency

Hist = np.zeros((256), dtype=int)
print(Hist)

while indexPixel < 256:
    Hist[indexPixel] = np.count_nonzero(grayImg1 = indexPixel)
    indexPixel = indexPixel + 1

Intensity = np.arange(0,256,1)

print(Intensity)
print(Hist)

plt.bar(Intensity,Hist,color = 'maroon',width=0.5)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram Eq")

plt.show()
