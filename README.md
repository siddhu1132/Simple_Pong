# Creating Simple_Pong game Using Python

It is a simple yet thrilling and exciting game of all the time.

Each player controls a paddle in the game by dragging it vertically across the screen’s left or right side. Players use their paddles to strike back and forth on the ball.

Turtle is an inbuilt graphic module in Python. It uses a panel and pen to depict illustrations. 

STEPS :

import turtle and create a window.

Step 1) Create two paddles A and B on the left and right side of the screen.

Create Paddle A and adjust shape, size, color, position, and speed using turtle module. Position of Paddle A is left Side of Window.
Create Paddle B same as above. Position of Paddle B is right Side of Window.

Step 2) Create a ball.

Create Ball and adjust size, color, speed and shape. Ball is at center of  window.

Step 3) Create an event to move the paddles up and down on pressing a certain keys.

For Paddle A, the adjustment aof movements are given by keyboard buttons ( W : Up, S : Down )
For Paddle B, (UP_Arrow : Up,  Down_Arrow : Down)

Bind these Keyboard buttons to Window using win.listen() and win.onkeypress()

Step 4) Create the function to update the score after each player misses a collision.
