import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
import urllib3
 
url='http://192.168.10.106/cam-hi.jpg'  # can change the URL type based on the resolution that you want
im=None


def run1():
    '''
    to display live transmission through the camera
    '''
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)   # display window
    #j = 0
    while True:
        img_resp=urllib.request.urlopen(url)  # opening the url 
        #print("1")
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)   # converting image in bits
        im = cv2.imdecode(imgnp,-1)    # reading the bits image
        #print("2")

        cv2.imshow('live transmission',im)   # displaying the image
        key=cv2.waitKey(5)   # to avoid your kernel from crashing
        if key==ord('q'):
            break
    cv2.destroyAllWindows()

        
def run2():
    '''
    to detect object using using the pretrained model 
    '''
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    #print("After opening the named Window")
    #i = 0
    while True:
        #print("inside the while loop")
        img_resp = urllib.request.urlopen(url)
        #print("opened the image using the URL....")
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        #print("4")

        bbox, label, conf = cv.detect_common_objects(im)   # running the model, yolov3
        #print("5")
        im = draw_bbox(im, bbox, label, conf)  # to draw the bounding box depending on the object that is detected
        #print("Did draw the box")

        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
        #print("Running the live transmission - run1")
        f1= executer.submit(run1)   # to have the live transmission running
        print("Running the object detection - run2")
        f2= executer.submit(run2)   # to have the object detection running