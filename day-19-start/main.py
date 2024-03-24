import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    timmy.forward(25)


def move_backward():
    timmy.backward(25)


def rotate_ccw():
    timmy.left(20)


def rotate_cw():
    timmy.right(20)


def clear_screen():
    turtle.resetscreen()
    # # or can do this
    # timmy.clear() # clears the turtle's drawings
    # timmy.penup()
    # timmy.home()
    # timmy.pendown()


# def draw_arc_cw():
#     timmy.circle(-50, 30)
#
#
# def draw_arc_ccw():
#     timmy.circle(50, 30)


screen.listen()
# when passing function into another function, no () at the end
# screen.onkey(key="space", fun=move_forward)

# Challenge: make an etch-a-sketch app
# def etch_a_sketch():
# still_running = True
# while still_running:
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_ccw)
screen.onkey(key="d", fun=rotate_cw)
screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="e", fun=draw_arc_cw)
# screen.onkey(key="q", fun=draw_arc_ccw)

screen.exitonclick()
