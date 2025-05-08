from pypylon import pylon
import cv2

#create a continuous stream
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
camera.StartGrabbingMax(5000)
converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

#show continuous stream

while True:
    # Retrieve the image
    grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grab_result.GrabSucceeded():
        # Convert image to OpenCV format
        image = converter.Convert(grab_result)
        img_array = image.GetArray()

        # Display the image using OpenCV
        cv2.imshow('Basler Image', img_array)
        cv2.waitKey(1)
    else:
        print("Image grab failed")

    # Release the resource
    grab_result.Release()