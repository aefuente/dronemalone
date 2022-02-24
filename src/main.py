from djitellopy import Tello
import cv2 as cv
import numpy as np
import pygame as pg
import time

#Width and height of image window
w,h = 360,240
S = 60
FPS = 120
send_rc_control = False

#Creates a drone object
def intitialize():
    drone = Tello()
    drone.connect()

    #Creates pg object
    pg.init()

    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 10
    
    pg.time.set_timer(pg.USEREVENT + 1, 1000 // FPS)
    #print("Battery:",drone.get_battery())
    drone.set_speed(drone.speed)
    drone.streamoff()
    drone.streamon()
    return drone

#Builds the frame from the drone camera
def getFrame(drone,w,h):
    #myFrame = drone.get_frame_read()
    #myFrame = myFrame.frame
    #img = cv.resize(myFrame,(w,h))
    return img

def keydown(drone,key):
       
    if key == pg.K_UP:  # set forward velocity
        drone.for_back_velocity = S
    elif key == pg.K_DOWN:  # set backward velocity
        drone.for_back_velocity = -S
    elif key == pg.K_LEFT:  # set left velocity
        drone.left_right_velocity = -S
    elif key == pg.K_RIGHT:  # set right velocity
        drone.left_right_velocity = S
    elif key == pg.K_w:  # set up velocity
        drone.up_down_velocity = S
    elif key == pg.K_s:  # set down velocity
        drone.up_down_velocity = -S
    elif key == pg.K_a:  # set yaw counter clockwise velocity
        drone.yaw_velocity = -S
    elif key == pg.K_d:  # set yaw clockwise velocity
        drone.yaw_velocity = S

def keyup(drone, key):
        
    if key == pg.K_UP or key == pg.K_DOWN:  # set zero forward/backward velocity
        drone.for_back_velocity = 0
    elif key == pg.K_LEFT or key == pg.K_RIGHT:  # set zero left/right velocity
        drone.left_right_velocity = 0
    elif key == pg.K_w or key == pg.K_s:  # set zero up/down velocity
        drone.up_down_velocity = 0
    elif key == pg.K_a or key == pg.K_d:  # set zero yaw velocity
        drone.yaw_velocity = 0
    elif key == pg.K_t:  # takeoff
        drone.takeoff()
        send_rc_control = True
    elif key == pg.K_l:  # land
        not drone.land()
        send_rc_control = False

def update(drone):
    if send_rc_control:
        drone.send_rc_control(drone.left_right_velocity, drone.for_back_velocity,drone.up_down_velocity, drone.yaw_velocity)


#Invokes drone initialization
drone = intitialize()
myFrame = drone.get_frame_read()

pg.display.set_caption("Video")
screen = pg.display.set_mode([960,720])

#Main loop
loop = True
while loop:

    for event in pg.event.get():
        if event.type == pg.USEREVENT + 1:
            update(drone)
        elif event.type == pg.QUIT:
            should_stop = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                loop = True
            else:
                keydown(drone,event.key)
        elif event.type == pg.KEYUP:
            keyup(drone, event.key)

        # if frame_read.stopped:
        #     break

    myFrame = myFrame.frame
    screen.fill([0,0,0])

    
    text = "Battery: {}%".format(drone.get_battery())
    cv.putText(myFrame, text, (5, 720 - 5),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    myFrame = cv.cvtColor(myFrame, cv.COLOR_BGR2RGB)
    myFrame = np.rot90(myFrame)
    myFrame = np.flipud(myFrame)

    myFrame = pg.surfarray.make_surface(myFrame)
    screen.blit(myFrame, (0, 0))
    pg.display.update()
    #Invokes frame method to create an image
    #img = getFrame(drone,w,h)

    #Show image in window
    #cv.imshow('Frame',img)

    #cv.waitKey(1)
    #Exit the program by pressing 'q'
    # if keyboard.is_pressed('q'):
    #     print("Battery:",drone.get_battery())
    #     drone.land()
    #     break

    time.sleep(1 / FPS)



