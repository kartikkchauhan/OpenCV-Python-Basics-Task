
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import sys


img = cv2.imread('product.jpeg',cv2.IMREAD_COLOR)

img = cv2.resize(img, (620,480) )


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noiseAs in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF) etc. LPF helps in removing noises, blurring the images etc. HPF filters helps in finding edges in the images.
##cv2.imshow("cnt",gray)

edged = cv2.Canny(gray, 30, 200) #Perform Edge detection

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contourContours can be explained simply as a
#curve joining all the continuous points (along the boundary), having same
#color or intensity.
#The contours are a useful tool for shape analysis and object detection and recognition.

#For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
#findContours function modifies the source image. So if you want source image even after finding contours, already store it to some other variables.
#In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
# loop over our contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break



if screenCnt is None:
	detected = 0
	print ("No contour detected")
	sys.exit()
else:
	detected = 1



if detected == 1:
	cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

# Masking the part other than the number plate
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)

# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]



#Read the number plate
text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("Detected Number is:",text)

cv2.imshow('image',img)
cv2.imshow('Cropped',Cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()


