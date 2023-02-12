import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math

from Convolution_Manual import do_convolution

def get_box_kernel(size=3, verbose=False):
    kernel = np.ones((size,size)) / 9
          
    if verbose:
        plt.imshow(kernel, interpolation='none', cmap='gray')
        plt.title("Kernel ( {}X{} )".format(size, size))
        plt.show()
        
    return kernel

# run from here
image = cv2.imread("./images/cat.jpg")
kernel_size = 3

kerenl = get_box_kernel(kernel_size, verbose=False)
do_convolution(image, kerenl, False, True)