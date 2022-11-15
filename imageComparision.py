import cv2
import numpy as np
orignal =cv2.imread("1.jpg")
duplicate= cv2.imread("1.jpg")
if orignal.shape==duplicate.shape:
    print("The images have same size")
    diffrence=cv2.subtract(orignal,duplicate)
    b,g,r=cv2.split(diffrence)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r)==0:
        print("The images are compeletly same")
    else:
        print("not same")
else:
    print("Diffrent shape & Sizze")
cv2.imshow("Orignal",orignal)
cv2.imshow("Duplicate",duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
