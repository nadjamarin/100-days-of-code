import tkinter


# Create a function to determine what happens when button is clicked
def button_clicked():
    print("I got clicked")
    # Change label to say "I got clicked" when button is clicked
    my_label["text"] = "I got clicked"
    # Put text input from user into label when button is clicked
    my_label["text"] = input.get()


# Create window
window = tkinter.Tk()

# Change window attributes
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# Pack the label onto the screen
# pack() has many more options than Turtle.write(), due to **kw
# my_label.pack()
# my_label.pack(side="left")
# my_label.pack(expand=True)

# Changing label attributes: two methods
# one attribute at a time
my_label["text"] = "New text"
# config() allows multiple attributes at a time
my_label.config(text="New Text")
my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Creating a Button object
# command argument lets you put name of function that executes when button is clicked
button = tkinter.Button(text="Click Me", command=button_clicked)
new_button = tkinter.Button(text="New Button")
# Display the button
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
# Reminder: you can use "from tkinter import *" to import all functions

# Entry
input = tkinter.Entry(width=15)
# input.pack()
input.grid(column=3, row=2)
print(input.get())



# import turtle
# tim = turtle.Turtle()
# # Can call write() with only arg as an argument since all other arguments are optional
# tim.write("Some text")
# tim.write("Some text", font=("Times New Roman", 80, "bold"))

# Keep the window on the screen and listen for user input
# This line has to be at the very end of the program
window.mainloop()
