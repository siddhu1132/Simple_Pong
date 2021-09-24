# Simple Pong in Python 3
# By Siddhartha
# 1. Getting Started (creating a Window)
# 2. Paddles and Ball
# 3. Moving the paddles and ball
# 4. Border Checking
# 5. Paddle and Ball Collisions
# 6. Score
# 7. Sound

import winsound
import turtle       # It is a module for building the basic graphics for games.

win = turtle.Screen()    # Create a window

win.title('Pong by Siddhartha')

win.bgcolor('black')

win.setup(width=800, height=600)

win.tracer(0)     # It stops windows from updating. It speedup our games

# Score

score_a = 0
score_b = 0

# Sound

file = "bounce.wav"

# Paddle A


paddle_a = turtle.Turtle()  # It is an object of turtle. Turtle is a class name
paddle_a.speed(0)  # Speed of the animation
paddle_a.shape('square')  # default shape is 20*20 pixels
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # It draws the line
paddle_a.goto(-350, 0)  # Paddle starts at -350

# Paddle B

paddle_b = turtle.Turtle()  # It is an object of turtle. Turtle is a class name
paddle_b.speed(0)  # Speed of the animation
paddle_b.shape('square')  # default shape is 20*20 pixels
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # It draws the line
paddle_b.goto(+350, 0)  # Paddle starts at +350

# Ball

ball = turtle.Turtle()  # It is an object of turtle. Turtle is a class name
ball.speed(0)  # Speed of the animation
ball.shape('square')  # default shape is 20*20 pixels
ball.color('white')
ball.penup()  # It draws the line
ball.goto(0, 0)  # Ball is at middle

ball.dx = 0.2  # everytime our ball  moves it moves 2 pixels to right
ball.dy = 0.2  # everytime our ball  moves it moves 2 pixels to up


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A : 0 Player B : 0', align='center', font=('Courier', 24, 'normal'))


# Function

def paddle_a_up():
    y = paddle_a.ycor()   # To move Paddle A up, we need to know Y coordinates of Paddle
    y += 20   # it adds 20 pixels to y coordinate
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()   # To move Paddle A up, we need to know Y coordinates of Paddle
    y -= 20   # it decreases 20 pixels down to y coordinate
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()   # To move Paddle A up, we need to know Y coordinates of Paddle
    y += 20   # it adds 20 pixels to y coordinate
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()   # To move Paddle A up, we need to know Y coordinates of Paddle
    y -= 20   # it decreases 20 pixels down to y coordinate
    paddle_b.sety(y)

# Keyboard binding


win.listen()  # It tells us to listen to keyboard input
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main Game loop
while True:

    win.update()  # It updates the screen when the loop runs

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking, What happens if Paddles, Ball hits the border

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A : {} Player B : {}'.format(score_a, score_b), align='center',
                  font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A : {} Player B : {}'.format(score_a, score_b), align='center',
                  font=('Courier', 24, 'normal'))

    # Paddle and Ball collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
