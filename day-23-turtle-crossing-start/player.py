from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""Create a turtle player that starts at the bottom of the screen and listen for the
 "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough
  in Step 3."""


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

