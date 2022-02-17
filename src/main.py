from djitellopy import Tello
import cv2 as cv
import numpy as np
import keyboard

#Width and height of image window
w,h = 360,240

#For tv
#w,h = 930, 500

#Creates a drone object
def intitialize():
    drone = Tello()
    drone.connect()
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0
    print("Battery:",drone.get_battery())
    drone.streamoff()
    drone.streamon()
    return drone

#Builds the frame from the drone camera
def getFrame(drone,w,h):
    myFrame = drone.get_frame_read()
    myFrame = myFrame.frame
    img = cv.resize(myFrame,(w,h))
    return img

#Invokes drone initialization
drone = intitialize()

#Main loop
while True:

    #Invokes frame method to create an image
    img = getFrame(drone,w,h)

    #Show image in window
    cv.imshow('Frame', img)

    if cv.waitKey(100) == ord('q'):
        break

    #Exit the program by pressing 'q'
    if keyboard.is_pressed('q'):
        print("Battery:",drone.get_battery())
        drone.land()
        break
    



