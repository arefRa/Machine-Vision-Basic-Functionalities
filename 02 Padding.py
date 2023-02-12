import cv2
import numpy as np

def addPadding(image, size = 1):
    width, height, channel = image.shape
    new_width = width + 2 * size
    new_height = height + 2 * size

    color = (0, 0, 0)
    new_image = np.full((new_width, new_height, channel), color, dtype=np.uint8)

    # compute center offset
    xx = (new_width - width) // 2
    yy = (new_height - height) // 2

    # copy img image into center of result image
    new_image[0:width, 0:height] = image

    return new_image

image_path = "./images/lenna.jpg"

# load image
image = cv2.imread(image_path)

# check if the image loaded
assert image is not None, "Cannot load image!"

padding_size = 50
padded_image = addPadding(image, padding_size)

# show the result
cv2.imshow("Original Image", image)
cv2.imshow("Padded image", padded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()