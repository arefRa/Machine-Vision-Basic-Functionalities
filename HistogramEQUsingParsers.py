import cv2 as cv
from __future__ import print_function
import cv2 as cv
import argparse

# Sir this code is totally from the internet and is just a demonstration of a better version of the histogram equation
# Please read the other Code as my student assignment


parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='lena.jpg')

args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
cv.waitKey()