from pypylon import pylon

#query camera type
cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()
print(cam_list)
if not cam_list:
    print("No camera found")
else:
    for device in cam_list:
        #print(f"Camera {i}:")
        print(f"  Model Name     : {device.GetModelName()}")
        print(f"  Serial Number  : {device.GetSerialNumber()}")
        print(f"  Device Class   : {device.GetDeviceClass()}")
        print(f"  Full Name      : {device.GetFullName()}")