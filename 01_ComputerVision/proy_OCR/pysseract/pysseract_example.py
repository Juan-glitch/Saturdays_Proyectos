import pytesseract
import cv2
import numpy as np


# In windows, needed to add the .exe file
# https://stackoverflow.com/questions/46004859/winerror-5access-denied-pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\u404878\\Tesseract\\tesseract.exe'




img = cv2.imread('logo_2.jpg')

# Convert 2 binary
# convert to binary
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
imagem = cv2.bitwise_not(thresh)
imgcopy = imagem.copy()
cv2.imwrite('logo_2_binary.jpg', imagem)
d = pytesseract.image_to_data(imgcopy, output_type=pytesseract.Output.DICT)
print(d)

for i in range(len(d['level'])):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(imgcopy, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', imgcopy)
cv2.waitKey(0)