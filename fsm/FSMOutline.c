/*
   FSM Code Outline
   Parker Weber + Zachery Gansz
   Last Updated: 2/15/2022
*/

// Includes
#include <stdio.h>


// Declare Variables
//char command[] = "TEST";	// command to send to Python
char *command = "TEST";	// command to send to Python

int PrevX = 0;
int PrevY = 0;
int PrevROI = 0;
int X = 0;
int Y = 0;
int ROI = 0;
int battery = 100; // assumed charged

int battery_shutoff = 15;	// land drone once battery falls below this percent


// Declare Functions



// Create FSM State Variable Definition
typedef enum {INIT, LAND, TAKEOFF, IDLE, MOVE_LEFT, MOVE_RIGHT, MOVE_DOWN, MOVE_UP, MOVE_FORWARD, MOVE_BACKWARD, FINAL} State;

// Create state variables
State state, next_state;

// FSM Model
void FSM_tick()
{
	printf("%s","Inside of FSM_tick....\n");
	fflush(stdout);

	switch(state)
	{
		case INIT:
			// code for INIT state & logic for next_state
			printf("%s","In INIT\n");

			next_state = TAKEOFF;  // next state after initializing
			fflush(stdout);

			break;
		case TAKEOFF:
			// Code for TAKEOFF State
			printf("%s","In TAKEOFF\n");

			command = "takeoff";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case LAND:
			// Code for LAND State
			printf("%s","In LAND\n");

			command = "land";
			printf("%s", command);
			fflush(stdout);

			break;
		case IDLE:
			// Code for IDLE State
			printf("%s","In IDLE\n");

			// TO:DO Grab inputs from Python File

			// Choose state to move to
			if (X < PrevX) {
				next_state = MOVE_LEFT;
			}
			else if (X > PrevX) {
				next_state = MOVE_RIGHT;
			}
			else if (ROI > PrevROI) {
				next_state = MOVE_BACKWARD;
			}
			else if (ROI < PrevROI) {
				next_state = MOVE_FORWARD;
			}
			else if (Y < PrevY) {
				next_state = MOVE_UP;
			}
			else if (Y > PrevY) {
				next_state = MOVE_DOWN;
			}
			else if (battery < battery_shutoff) {
				next_state = FINAL;
			}

			break;
		case MOVE_LEFT:
			// Code for MOVE_LEFT State
			printf("%s","In MOVE_LEFT\n");

			command = "left 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case MOVE_RIGHT:
			// Code for MOVE_RIGHT State
			printf("%s","In MOVE_RIGHT\n");

			command = "right 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case MOVE_DOWN:
			// Code for MOVE_DOWN State
			printf("%s","In MOVE_DOWN\n");

			command = "down 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case MOVE_UP:
			// Code for MOVE_UP State
			printf("%s","In MOVE_UP\n");

			command = "up 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case MOVE_FORWARD:
			// Code for MOVE_FORWARD State
			printf("%s","In MOVE_FORWARD\n");

			command = "forward 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case MOVE_BACKWARD:
			// Code for MOVE_BACKWARD State
			printf("%s","In MOVE_BACKWARD\n");

			command = "back 20";
			printf("%s", command);
			fflush(stdout);
			next_state = IDLE;

			break;
		case FINAL:
			printf("%s","In FINAL\n");
			printf("%s","Program Ending\n"); // Check if done


			break;
		default:
			next_state = LAND;	// End if error
	}

	state = next_state;  // update to next state
}

int main(void)  // add args or reference args?
{

	printf("%s","In Main....\n");
	fflush(stdout);
	//printf("%s",command);
    // Initialize variables

    state = INIT;

    // Infinitely loop
    //print("Beginning infinite loop:\r\n");

    while(state != FINAL) {
		printf("%s","In Infinite Loop....\n");
		fflush(stdout);

		//                                                      	//
        // Determined by how information is received from Python    //
        //                                                      	//

		printf("%s","Grabbing Inputs from Python....\n");
		fflush(stdout);
        // PrevX = X
        // PrevY = Y
        // PrevROI = ROI
        // X = CameraX (assuming this is where we pass in value from AI program)
        // Y = CameraY
        // ROI = CameraROI
        // next_state = CheckForNextState(PrevX,PrevY,PrevROI,X,Y,ROI)


		printf("%s","Ticking FSM....\n");
		fflush(stdout);
		FSM_tick();




    }

    return 0;

}

