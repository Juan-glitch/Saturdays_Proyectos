import cv2
import numpy as np

img = cv2.imread(r'logos\various_03_03_22\logo (2).jpg')
#  ToGray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  ToBinary
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite(r'logo_1_normal.jpg', img)
cv2.imwrite(r'logo_1_thresh.jpg', thresh)
cv2.imwrite(r'logo_1_gray.jpg', gray)
