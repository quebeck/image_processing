# main
from pypylon import pylon
import cv2
import numpy as np

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
camera.StartGrabbingMax(1)
converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

# Retrieve the image
grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

if grab_result.GrabSucceeded():
    # Convert image to OpenCV format
    image = converter.Convert(grab_result)
    img_array = image.GetArray()

    # Display the image using OpenCV
    cv2.imshow('Basler Image', img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save image to file
    cv2.imwrite('image.png', img_array)
else:
    print("Image grab failed")

# Release the resource
grab_result.Release()
camera.Close()