import turtle
import random

timmy = turtle.Turtle()


timmy.shape("turtle")
# timmy_the_turtle.color("DarkSeaGreen")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# # Turtle Challenge 1: Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# # Turtle Challenge 2: Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# Turtle Challenge 3: Drawing different shapes
colors = ["light steel blue", "light sky blue", "dark turquoise", "light green", "forest green",
          "lemon chiffon", "coral", "dark orchid", "steel blue"]
num_sides = 3
while num_sides <= 10:
    timmy.color(random.choice(colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
    num_sides += 1


# # Turtle Challenge 4: Draw a random walk
# colors = ["light sky blue", "dark turquoise", "light green", "forest green",
#           "wheat", "coral", "dark orchid", "steel blue", "crimson"]
# headings = [0, 90, 180, 270]
# timmy.width(10)
# timmy.speed(0)
#
# for _ in range(200):
#     timmy.setheading(random.choice(headings))
#     timmy.color(random.choice(colors))
#     timmy.forward(20)


# # Generating random colors using RGB instead of a list of color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
#
# turtle.colormode(255)  # defines type of RGB definition
# headings = [0, 90, 180, 270]
# timmy.width(10)
# timmy.speed(0)
#
# for _ in range(200):
#     timmy.setheading(random.choice(headings))
#     timmy.color(random_color())
#     timmy.forward(20)


# # Turtle Challenge 5: Draw a spirograph
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
#
# turtle.colormode(255)
# deg_per_turn = 4
# timmy.speed(0)
#
# for _ in range(int(360/deg_per_turn)):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.right(deg_per_turn)


screen = turtle.Screen()  # these lines have to be at the end of the code
screen.exitonclick()
