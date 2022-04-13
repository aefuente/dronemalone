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



'''

Class for interfacing with the drone.

'''

class Drone:

    def __init__(self):
       self.drone = Tello()

    def connect(self):
        self.drone.connect()

    def set_speed(self, speed):
        self.drone.set_speed(speed)

    def refresh_stream(self):
        self.drone.streamoff()
        self.drone.streamon()

    def get_frame(self):
        return self.drone.get_frame_read()

     


''' 

Class for controlling the drone

'''
class Controller:

    def __init__(self):

        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0

        self.speed = DRONE_SPEED
        self.send_rc_control = False

        self.drone = Drone()



    ''' Initializes drone connection ''' 
    def initialize_drone(self):
        self.drone.connect()

        self.drone.set_speed(DRONE_SPEED)

        self.drone.refresh_stream()



    ''' Sets all velocities to 0 '''
    def reset_velocity(self):
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0



    ''' User event quit '''
    def test_quit(self, event):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            return True
        return False


    ''' User event update '''
    def user_event(self, event,flag=False):

        self.update()

        if flag is True:
            pygame.time.wait(500)

        self.reset_velocity()
        self.update()



    ''' Loop to continously control drone '''
    def run(self):
        should_stop = False
        flag = False

        while not should_stop:
            for event in pygame.event.get():

                if event.type == pygame.USEREVENT + 1:
                    self.user_event(event,flag)
                    flag=False

                elif event.type == pygame.KEYUP:
                    self.keyup(event.key)

                should_stop = self.test_quit(event)

            if frame_read.stopped:
                break
            




    ''' Update drone movement'''
    def update(self):
        if self.send_rc_control:
            self.drone.send_rc_control(self.left_right_velocity, \
                                  self.for_back_velocity,   \
                                  self.up_down_velocity,    \
                                  self.yaw_velocity)



    ''' Take of and land function'''
    def keyup(self, key):
        if key == pygame.K_t:  # takeoff
            self.drone.takeoff()
            self.send_rc_control = True
        elif key == pygame.K_l:  # land
            self.drone.land()
            self.send_rc_control = False

    



''' Function for initializing Pygame '''
def intialize_pygame():
    pygame.init()
    pygame.time.set_timer(pygame.USERVENT + 1, 1000//FPS)



''' Function for displaying pygame window '''
def display_window():
    pygame.display.set_caption(WINDOW_DISPLAY_CAPTION)
    return pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])




if __name__ == '__main__':


    controller = Controller()
    controller.initialize_drone()

    frame = controller.drone.get_frame()

 
