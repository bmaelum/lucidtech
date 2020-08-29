import cv2
import pytesseract
from pytesseract import Output
from ocr_functions import *


img = cv2.imread('OCR-tesseract/receipt_image.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

# -- Get words from image --
words_from_image(img)