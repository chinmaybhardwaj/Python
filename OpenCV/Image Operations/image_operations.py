
import cv2
import numpy as np


img = cv2.imread('ball.jpg', cv2.IMREAD_COLOR)

# Get Pixel
#px = img[55,55]
#print('pixel value:', px)

# Change Pixel Value
#img[55,55] = [255,255,255]
#px = img[55,55]
#print('pixel value:', px)

# ROI
#roi = img[10:150, 10:150]
#print('Region of Image:', roi)

# Add a white block
img[10:50, 10:50] = [255, 255, 255]

ball_face = img[37:111, 107:194]

img[0:74, 0:87] = ball_face

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()