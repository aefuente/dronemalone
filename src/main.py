from djitellopy import Tello
import cv2 as cv
import numpy as np

w,h = 360,240

def intitialize():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print("Battery:",myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def getFrame(myDrone,w,h):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv.resize(myFrame,(w,h))
    return img


myDrone = intitialize()

while True:
    #print("Battery:",myDrone.get_battery())
    #Frame reading
    #img = getFrame(myDrone,w,h)

    #Show frame in window
    #cv.imshow('Frame',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Battery:",myDrone.get_battery())
        myDrone.land()
        break




