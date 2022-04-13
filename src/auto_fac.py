from djitellopy import Tello
import cv2 
import pygame
import numpy as np
import time
import expertFSM


'''

This program provides instructions to a DJI Tello Drone that enables it to
automatically track a human face.

'''

DRONE_SPEED = 10

FPS = 120

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
WINDOW_DISPLAY_CAPTION = "Automatic Drone Tracking"

FACE_CASCADE = cv2.CascadeClassifier('./src/cascades/haarcascade_frontalface_default.xml')

CENTER_FRAME = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

class FrontEnd(object):

    def __init__(self):
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = DRONE_SPEED

        self.send_rc_control = False

        self.pygame.init()
        self.pygame.time.set_timer(self.pygame.USERVENT + 1, 1000//FPS)

        self.drone = Tello()


    
    def display_window(self):
        self.pygame.display.set_caption(WINDOW_DISPLAY_CAPTION)

        self.screen = self.pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
