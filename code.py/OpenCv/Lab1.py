import sys
import cv2 as cv

img = cv.imread("/Applications/opencv-4.8.0/samples/data/baboon.jpg");
if img is None : 
    sys.exit("Cannot open image.")

print("Size: {}x{}".format(img.shape[0],img.shape[1]))
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey()
