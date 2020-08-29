import cv2
import pytesseract

from ocr_functions import *

# main 
img = cv2.imread('/Users/bjornar/Documents/lucidtech/data/text_image.jpg')

show_img(img)

# convert to grayscale
gray = get_grayscale(img)

show_img(gray, 'OCR Gray')

# remove noise
canny = canny(gray)
show_img(canny, 'OCR Canny')

# deskew
deskew = deskew(img)
show_img(deskew, 'OCR Deskew')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

#closing all open windows  
cv2.destroyAllWindows()  