import cv2
import numpy as np
import pytesseract
from PIL import Image

from pytesseract import image_to_string

result=pytesseract.image_to_string(Image.open("a.png"))

print('-----START----')
print(result)
print('-------DONE--------')
