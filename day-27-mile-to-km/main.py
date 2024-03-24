import tkinter


def button_pressed():
    # Convert user input from miles to km
    num_miles = float(user_input.get()) * 1.609

    # Display the answer
    num_km["text"] = num_miles


# Create window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=125)

# Create and place labels
font_size = 14
is_equal_to = tkinter.Label(text="is equal to", font=("Arial", font_size, "normal"))
kilometers = tkinter.Label(text="Km", font=("Arial", font_size, "normal"))
miles = tkinter.Label(text="Miles", font=("Arial", font_size, "normal"))
num_km = tkinter.Label(text="0", font=("Arial", font_size, "normal"))

is_equal_to.grid(column=0, row=1)
kilometers.grid(column=2, row=1)
miles.grid(column=2, row=0)
num_km.grid(column=1, row=1)

# Create and place button
calc_button = tkinter.Button(text="Calculate", command=button_pressed)
calc_button.grid(column=1, row=2)

# Create and place entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

# Add padding to each widget
pad_x = 5
pad_y = 5
is_equal_to.config(padx=pad_x, pady=pad_y)
kilometers.config(padx=pad_x, pady=pad_y)
miles.config(padx=pad_x, pady=pad_y)
num_km.config(padx=pad_x, pady=pad_y)
calc_button.config(padx=pad_x, pady=pad_y)

window.mainloop()
