#from expertFSM import INIT, TAKEOFF, LAND, IDLE, MOVE_LEFT, MOVE_RIGHT, MOVE_DOWN, MOVE_UP, MOVE_FORWARD, MOVE_BACKWARD, FSM_TICK, work, states
#from expertFSM import *
from random import randint
import expertFSM
# TO-Do: test cythonized version
#from setup import ext_modules
# Global variables for FSM drone operation
#state = 1   #TO-DO: Remove state stuff from this. It should all be contained in expertFSM.pyx
#next_state = 1

# X = 100
# Y = 0
# ROI = 0


#command = "back 5" # arbitrary command to test if variable is updated correctly

# Function to test cythonized FSM   # equivalent to loop that calls FSM
def droneCommand(X, Y, ROI): # may need to store PrevROI, PrevX, etc in this file if Cython loses the information after running
    print ('in dronecommand \n')
    command = str(expertFSM.FSM_TICK(X, Y, ROI))
    if (command == 'null'): # check to see what is returned w/o assigning val to IDLE state
        print (str(command) + 'rip\n')
        pass # do nothing
    else:
        return command

# Function to test dronecommand. Equivalent to using the value returned from loop in AI python file
def testDroneCommand(X, Y, ROI):
    ('in testdronecommand \n')
    #expertFSM.state = 0
    #expertFSM.startup()
    i = 0
    while(i < 100):
        rand1 = randint(0,100)
        X = rand1
        rand2 = randint(0,100)
        Y = rand2
        print ("X: " + str(X))
        print ("Y: " + str(Y))

        print (droneCommand(X, Y, ROI))
        i = i + 1

# Calling to test
print ('Starting... \n')
X = 0
Y = 0
ROI = 0
testDroneCommand(X, Y, ROI)

#print(work())
#TO-Do: loop dronecommand to test FSM


