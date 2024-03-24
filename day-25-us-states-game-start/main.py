import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add US map image to window
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Make Turtle object for writing state names on the map
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()


# Extract data from 50_states.csv
state_data = pandas.read_csv("50_states.csv")
states_list = state_data["state"].to_list()

num_correct = 0
correct_guesses_list = []
game_is_on = True

while game_is_on:
    # Ask user to input a guess
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state's name?").title()

    # Check if user's answer matches any of the states and has not already been guessed
    if answer_state in states_list and answer_state not in correct_guesses_list:
        num_correct += 1
        correct_guesses_list.append(answer_state)

        # Find x and y coordinates for the corresponding state
        state_row = state_data[state_data.state == answer_state]
        x_coor = int(state_row.x)
        y_coor = int(state_row.y)

        # Move to the x and y coordinates of corresponding state and write state name
        state_name.goto(x_coor, y_coor)
        state_name.write(answer_state, move=False, align='center', font=('Arial', 8, 'normal'))
        # This is a way to get the actual item in the state position
        # state_name.write(state_row.state.item())

    elif answer_state == "Exit":
        # Create a list of the states the user missed
        # states_to_learn = []
        # for state in states_list:
        #     if state not in correct_guesses_list:
        #         states_to_learn.append(state)
        
        # Adapting the code to use list comprehension instead
        states_to_learn = [state for state in states_list if state not in correct_guesses_list]

        # Save missed states to a CSV file
        states_to_learn_df = pandas.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("States_to_Learn.csv")
        game_is_on = False

    # If user wins, exit loop and display a win message
    if num_correct == 50:
        state_name.goto(0, 0)
        state_name.color("green")
        state_name.write("You win!", align="center", font=('Arial', 20, 'normal'))
        game_is_on = False


# def get_mouse_click_coor(x, y):
#     print(x, y)
# Can use this to find the coordinates of each state
# turtle.onscreenclick(get_mouse_click_coor)

# Keep screen open
turtle.mainloop()
