import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("./images/black_white_01.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = np.abs(fshift) #np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'jet')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'jet')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()