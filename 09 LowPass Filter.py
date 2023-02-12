import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("./images/cat.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

f = np.fft.fft2(img)            # to Fourier  
fshift = np.fft.fftshift(f)     # shift to center (N/2)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# masking with a rectangular window of size nxn.
n = 150

fshift[0:crow-n//2, :] = 0 
fshift[crow+n//2:rows, :] = 0

fshift[:, 0:ccol-n//2] = 0
fshift[:, ccol+n//2:cols] = 0

f_ishift = np.fft.ifftshift(fshift) # inverse the shift
img_back = np.fft.ifft2(f_ishift)   # inverse the Fourier 
img_back = np.abs(img_back)         # find absolute value

plt.subplot(1, 3, 1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3),plt.imshow(img_back, cmap = 'jet')
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()