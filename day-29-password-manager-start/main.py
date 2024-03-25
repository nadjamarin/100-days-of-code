from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # password_list = []

    # Change these lines to use list comprehension instead
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0, password)
    # print(f"Your password is: {password}")

    # Copy password to user's clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Check for blank entries
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Show popup to user to confirm their entry
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered: \nUsername: {username} \nPassword: {password} \nIs this okay to save?")

        if is_okay:  # Boolean
            # Save user's data into txt file, appending each new entry on a new line
            data = f"{website} | {username} | {password}\n"
            with open("data.txt", "a") as file:
                file.write(data)

            # Clear all entry fields
            website_entry.delete(0, "end")
            # username_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Can have widgets go across more than one column: use columnspan in grid()

# Create labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create entries
website_entry = Entry(width=35)
# Start with cursor in website entry
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
# Put default email in username entry at first character (0)
username_entry.insert(0, "nadjamarin99@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Create buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
