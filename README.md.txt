This project provides 3 files:

1) Arduino_code --> To program the ESP 32 camera. You can use an FTDI module or an Arduino Uno to program the ESP 32 camera. Make sure to have installed the ESP 32 camera board before running the code. Set the board to ESP 32 Wrover module. Set the baud rate and the COM port values accordingly.
   You would need to change the SSID and password depending upon the Wifi that you have connected to.

2) object_detection.py --> Uses a pretrained model (YOLOv3) on COCO dataset that is used to detect object

3) face_recognition.py --> Uses Haarcascades to detect eyes and face of people

In order to get your code running on the ESP 32 camera, you have to make sure that your device and the camera module is connected to the same network. In the object and face recognition code, you simply have to replace the IP address in the URL with the one that was displayed through your Arduino's serial monitor.