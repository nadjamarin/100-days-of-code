from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 260)
        self.score = 1
        self.write(f"Level {self.score}", move=False, align="Left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", move=False, align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="Center", font=FONT)