from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y_coord = -100

# generate all 6 turtles
for idx in range(0, 6):
    current_turtle = Turtle("turtle")
    current_turtle.penup()
    current_turtle.color(colors[idx])
    current_turtle.goto(x=-230, y=y_coord)
    y_coord += 40
    turtle_list.append(current_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230: # turtle is 40 by 40 pixels, so 230 brings it to right edge
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
