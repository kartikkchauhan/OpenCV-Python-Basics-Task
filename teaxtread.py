#from pytesseract import image_to_string
#from PIL import Image
#img=Image.open("2.png")
#text=image_to_string(img)
#print(text)

import pytesseract
from PIL import Image

img = Image.open('a.png')
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
print( pytesseract.image_to_string(img) )

   
