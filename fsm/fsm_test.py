from pickle import TRUE


INIT = 'INIT'
TAKEOFF = 'TAKEOFF'
LAND = 'LAND'
IDLE = 'IDLE'
MOVE_LEFT = 'MOVE_LEFT'
MOVE_RIGHT = 'MOVE_RIGHT'
MOVE_DOWN = 'MOVE_DOWN'
MOVE_UP = 'MOVE_UP'
MOVE_FORWARD = 'MOVE_FORWARD'
MOVE_BACKWARD = 'MOVE_BACKWARD'
X = 100
PrevX = 0
Y = 0
PrevY = 0
ROI = 0
PrevROI = 0
next_state = 1


def INIT():
    print("INIT STATE")
    global next_state
    next_state = 2 # move to TAKEOFF STATE
    pass

def TAKEOFF():
    print("TAKEOFF_STATE")
    global next_state
    next_state = 4 # move to idle state
    
    pass

def LAND():
    print("LAND_STATE")
    #state_switch(next_state)
    pass

def IDLE():
    print("IDLE_STATE")
    global next_state
    if X < PrevX:
        next_state = 5 #MOVE_LEFT #5
    elif X > PrevX:
        next_state = 6 #MOVE_RIGHT #6
    elif ROI > PrevROI:
        next_state = 10 # MOVE_BACKWARD #10
    elif ROI < PrevROI:
        next_state = 9 #MOVE_FORWARD #9
    elif Y < PrevY:
        next_state = 8 #MOVE_UP #8
    elif Y > PrevY:
        next_state = 7 #MOVE_DOWN #7
    else:
        next_state = 4
        
	#elif(battery < battery_shutoff):
	#	next_state = FINAL
    
    pass

def MOVE_LEFT():
    print("MOVE_LEFT_STATE")
    global next_state
    next_state = 4
    
    pass

def MOVE_RIGHT():
    print("MOVE_RIGHT_STATE")
    global next_state
    next_state = 4
    
    pass

def MOVE_DOWN():
    print("MOVE_DOWN_STATE")
    global next_state
    next_state = 4
    
    pass

def MOVE_UP():
    print("MOVE_UP_STATE")
    global next_state
    next_state = 4
    
    pass

def MOVE_FORWARD():
    print("MOVE_FORWARD_STATE")
    global next_state
    next_state = 4
    
    pass

def MOVE_BACKWARD():
    print("MOVE_BACKWARD_STATE")
    global next_state
    next_state = 4
    
    pass  

states = {
    1: INIT, 
    2: TAKEOFF, 
    3: LAND, 
    4: IDLE, 
    5: MOVE_LEFT, 
    6: MOVE_RIGHT,
    7: MOVE_DOWN, 
    8: MOVE_UP, 
    9: MOVE_FORWARD, 
    10: MOVE_BACKWARD
    }

def FSM_TICK(state): #FSM call probably
    states.get(state)()


def MAIN():
    global X, PrevX, Y, PrevY, ROI, PrevROI,next_state
    count = 0
    while count < 100:
        X = X - 1
        PrevX = PrevX + 1
        print("Count: " + str(count))
        FSM_TICK(next_state)
        count = count + 1

MAIN()

