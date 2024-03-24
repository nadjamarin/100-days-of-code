from turtle import Turtle
import math


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.y_direction = 1
        # self.x_direction = 1
        self.x_move = 10
        self.y_move = 10
        self.speed_sleep = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # if self.x_direction > 0:
        #     new_x = self.xcor() + 10
        # else:
        #     new_x = self.xcor() - 10
        # if self.y_direction > 0:
        #     new_y = self.ycor() + 10
        # else:
        #     new_y = self.ycor() - 10

    def bounce_wall(self):
        self.y_move *= -1
        # if self.x_direction > 0:
        #     new_x = self.xcor() + 10
        # else:
        #     new_x = self.xcor() + 10
        # if self.y_direction > 0:
        #     new_y = self.ycor() - 10
        # else:
        #     new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
        # self.y_direction = self.y_direction * -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.speed_sleep *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.speed_sleep = 0.1
