
import cv2
import numpy as np
import matplotlib.pyplot as plt


# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

img = cv2.imread('ball.jpg', cv2.IMREAD_GRAYSCALE)


# Using CV2
#cv2.imshow('Image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Using Matplotlib
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()

# Saving Image
cv2.imwrite('ball_gray.png', img)