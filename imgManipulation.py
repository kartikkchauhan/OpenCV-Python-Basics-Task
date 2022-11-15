import cv2
img=cv2.imread("1.jpg")
print(img)
cv2.imshow("My image",img)
cv2.imwrite("2.jpg",img)
