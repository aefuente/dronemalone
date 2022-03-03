from djitellopy import Tello
import cv2 as cv
import numpy as np

SCREEN_WIDTH=720
SCREEN_HEIGHT=480

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

def getFrame(myDrone,w=SCREEN_WIDTH,h=SCREEN_HEIGHT):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv.resize(myFrame,(w,h))
    return img


face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
myDrone = intitialize()

while True:

    #Frame reading
    img = getFrame(myDrone)


    cap = myDrone.get_video_capture()


    # Calculate center of frame
    center_x = int(SCREEN_WIDTH/2)
    center_y = int(SCREEN_HEIGHT/2)

    # Draw circle at center of the frame
    cv.circle(img, (center_x, center_y), 10, (0, 255, 0))



    # Convert frame to grayscale in order to apply the haar cascade for face identification
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, minNeighbors=5)

    # If a face is recognized, draw a rectangle over it and add it to the face list
    face_center_x = center_x
    face_center_y = center_y
    z_area = 0
    for face in faces:
        (x, y, w, h) = face
        cv.rectangle(img,(x, y),(x + w, y + h),(255, 255, 0), 2)

        face_center_x = x + int(h/2)
        face_center_y = y + int(w/2)
        z_area = w * h
        cv.circle(img, (face_center_x, face_center_y), 10, (0, 0, 255))

    # Calculate recognized face offset from center
    offset_x = face_center_x - center_x
    offset_y = face_center_y - center_y

    cv.putText(img, f'[{offset_x}, {offset_y}, {z_area}]', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)

    #Show frame in window
    cv.imshow('Frame',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Battery:",myDrone.get_battery())
        myDrone.land()
        break




