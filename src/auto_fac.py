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

