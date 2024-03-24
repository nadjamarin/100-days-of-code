# import another_module
# print(another_module.another_variable)
#
# # documentation of turtle module is in course resources
# from turtle import Turtle, Screen
#
# # timmy is an object, Turtle is the class
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen")
# timmy.forward(100)
#
# # Attributes
# my_screen = Screen() # create a screen
# print(my_screen.canvheight) # canvas height is an attribute
# my_screen.exitonclick()


# Load packages into PyCharm
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
