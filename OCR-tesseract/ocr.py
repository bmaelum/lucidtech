import cv2
import pytesseract

from ocr_functions import *

## Import image
img = cv2.imread('OCR-tesseract/text_image.jpg')

show_img(img)

#  /// PREPROCESSING ///
## Convert to grayscale 
gray = get_grayscale(img)

show_img(gray, 'OCR Gray')

## Remove noise
canny = canny(gray)
show_img(canny, 'OCR Canny')

# Deskew
deskew = deskew(img)
show_img(deskew, 'OCR Deskew')

show_images(images, 3, ["gray","rnoise","dilate","erode","thresh","deskew","opening","canny"])


#closing all open windows  receipt
cv2.destroyAllWindows()  


# /// PYTESSERACT ///
# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)
