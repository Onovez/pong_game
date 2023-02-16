from config import *
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



win = t.Screen()
win.bgcolor("black")
win.title("Pong")
win.setup(S_WIDTH, S_HEIGHT)
win.tracer(0)


l_paddle = Paddle(L_PADDLE_POS)
r_paddle = Paddle(R_PADDLE_POS)

ball = Ball()

score = Scoreboard()

win.listen()


win.onkeypress(r_paddle.up, "Up")
win.onkeypress(r_paddle.down, "Down")
win.onkeypress(l_paddle.up, "w")
win.onkeypress(l_paddle.down, "s")





game_on = True
while game_on:
    time.sleep(ball.move_speed)
    win.update()
    ball.move()
    
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    
    # Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    # Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        
        
    # paddles with the border
    if r_paddle.ycor() > 260:
        r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() - 20)
    if r_paddle.ycor() < -260:
        r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() + 20)
    
    if l_paddle.ycor() > 260:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() - 20)
    if l_paddle.ycor() < -260:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() + 20)
        


win.exitonclick()