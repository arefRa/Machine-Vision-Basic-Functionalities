import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("./images/Lenna.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_Prewitt_hor = 1/3 * np.array([[-1, 0, 1],
                                    [-1, 0, 1],
                                    [-1, 0, 1]])

kernel_Prewitt_ver = 1/3 * np.array([[-1, -1, -1],
                                    [0, 0, 0],
                                    [1, 1, 1]])

kernel_Sobel_hor = 1/4 * np.array([[-1, 0, 1],
                                    [-2, 0, 2],
                                    [-1, 0, 1]])

kernel_Sobel_ver = 1/4 * np.array([[-1, -2, -1],
                                    [0, 0, 0],
                                    [1, 2, 1]])

kernel_Lap = 1/4 *  np.array([[0, 1, 0],
                              [1, -4, 1],
                              [0, 1, 0]])

image_edge_Prewitt_hor = cv2.filter2D(image, -1, kernel_Prewitt_hor)
image_edge_Prewitt_ver = cv2.filter2D(image, -1, kernel_Prewitt_ver)
image_edge_Prewitt = image_edge_Prewitt_hor + image_edge_Prewitt_ver

image_edge_Sobel_hor = cv2.filter2D(image, -1, kernel_Sobel_hor)
image_edge_Sobel_ver = cv2.filter2D(image, -1, kernel_Sobel_ver)
image_edge_Sobel = image_edge_Sobel_hor + image_edge_Sobel_ver

image_edge_Lap = cv2.filter2D(image, -1, kernel_Lap)


plt.subplot(3, 4, 1),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 2), plt.imshow(image_edge_Prewitt_hor, cmap = 'jet')
plt.title('Prewitt Horizontal'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 3),plt.imshow(image_edge_Prewitt_ver, cmap = 'jet')
plt.title('Prewitt Vertical'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 4),plt.imshow(image_edge_Prewitt, cmap = 'jet')
plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 5),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 6), plt.imshow(image_edge_Sobel_hor, cmap = 'jet')
plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 7),plt.imshow(image_edge_Sobel_ver, cmap = 'jet')
plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 8),plt.imshow(image_edge_Sobel, cmap = 'jet')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 9),plt.imshow(image, cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 10),plt.imshow(image_edge_Lap, cmap = 'bone')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()