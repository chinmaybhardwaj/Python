
import cv2
import numpy as np


img = cv2.imread('ball.jpg', cv2.IMREAD_COLOR)

#STRAIGHT LINE
#cv2.line(img, (0,0), (150,150), (255, 255, 255), 5)

# RECTANGLE
#cv2.rectangle(img, (5, 5), (80,100), (255, 255, 255), 5)

# CIRCLE
#cv2.circle(img, (40, 50), 40, (255, 255, 255), 5)  #  width = -1 = fill whole circle

# POLYGON
pts = np.array([[10,5], [20,30], [50,20], [30,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)   # True = connect last & first point


# TEXT WITH FONT
font = cv2.FONT_HERSHEY_SIMPLEX
# (IMAGE, POSITION, FONT, FONT_SIZE, COLOR, FONT_LETTER_WIDTH, ?)
cv2.putText(img,  'OpenCV', (0,120), font, 0.6, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()