import cv2
cap=cv2.VideoCapture("3.mp4")
rt,img=cap.read()

cv2.imshow("Video", img)
