import colorgram
import turtle
import random

# # use colorgram to extract colors from Hirst ref image
# # image.jpeg has to be on same level as main.py in the project tree
# colors = colorgram.extract("image.jpeg",20)
# # print(colors)
# color_list = []
#
# for item in colors:
#     # get the rgb color from current item in colors
#     color = item.rgb
#     # # or can do this
#     # r = color.rgb.r
#     # g = color.rgb.g
#     # b = color.rgb.b
#     # add color to color list in tuple form
#     color_list.append((color[0], color[1], color[2]))

# print(color)
# print(color[0])
# print(color_list)

# remove white colors from color_list by hand
color_list = [(204, 165, 107), (151, 73, 47), (52, 93, 125), (223, 202, 135), (170, 153, 40), (136, 32, 21),
              (133, 163, 185), (200, 91, 70), (48, 122, 88), (67, 47, 40), (14, 100, 73), (146, 178, 146),
              (162, 143, 157), (234, 176, 165), (111, 74, 77), (20, 84, 89)]

# goal: 20 wide spots, 50 in between, 10 by 10 grid of spots
timmy = turtle.Turtle()
timmy.speed(0)
turtle.colormode(255)
timmy.hideturtle()
# set initial position
timmy.penup()
timmy.setheading(225)
timmy.forward(200)
timmy.setheading(0)

for row in range(10):
    # draw a row of dots
    for column in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        # timmy.pendown()
    # move up to the next row
    timmy.left(90)
    # timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()