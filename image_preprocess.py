from config import RED_WAVELENGTH, GREEN_WAVELENGTH, BLUE_WAVELENGTH
import cv2

#load test image
img = cv2.imread('image_test.png')
#extract channels
red_channel = img[:,:,0]
green_channel = img[:,:,1]
blue_channel = img[:,:,2]
#display channels
cv2.imshow('Red Channel', red_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Blue Channel', blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

# c-matrix (of the book)

