from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_sleep)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    # Detect when ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
