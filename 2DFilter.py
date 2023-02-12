import cv2
import numpy as np
from matplotlib import pyplot as plt


# In this example we are going to show how we may use "pyplot" library as well as opencv to show an image!
# We are also going to show how a custom kernel could be defined and used

# Run script
if __name__ == '__main__':
    input_image = cv2.imread("./images/lenna.jpg")

    # define a custom kernel
    kernel = np.zeros((5,5), np.float32)

    # fill it with 1s (a box filter)
    kernel[0][0] = 1
    kernel[0][1] = 1
    kernel[0][2] = 1
    kernel[0][3] = 1
    kernel[0][4] = 1

    kernel[1][0] = 1
    kernel[1][1] = 1
    kernel[1][2] = 1
    kernel[1][3] = 1
    kernel[1][4] = 1

    kernel[2][0] = 1
    kernel[2][1] = 1
    kernel[2][2] = 1
    kernel[2][3] = 1
    kernel[2][4] = 1
    
    kernel[3][0] = 1
    kernel[3][1] = 1
    kernel[3][2] = 1
    kernel[3][3] = 1
    kernel[3][4] = 1
    
    kernel[4][0] = 1
    kernel[4][1] = 1
    kernel[4][2] = 1
    kernel[4][3] = 1
    kernel[4][4] = 1

    # we need this to make the box filter works fine!
    kernel *= 1.0/25.0

    filtered_image = cv2.filter2D(input_image, -1, kernel)

    # Note: OpenCv loads images with BGR channel order where pylpot uses RGB order
    # so, we need to convert both images (input and filtered) from BRG to RGB 

    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)    

    # Now, take your time to discover whats going on here ;-)
    plt.subplot(121)
    plt.imshow(input_image)
    plt.title("Input image")    
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(122)
    plt.imshow(filtered_image)
    plt.title("Box-filtered image")    
    plt.xticks([])
    plt.yticks([])
    
    plt.show()