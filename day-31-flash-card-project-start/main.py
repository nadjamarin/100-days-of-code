from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = "Arial 40 italic"
WORD_FONT = "Arial 60 bold"
current_card = {}


# ---------------------------- RANDOM WORD GENERATOR ------------------------------- #
def next_card(result):
    global current_card, flip_timer, words_to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    current_french_word = current_card["French"]
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(word_text, text=current_french_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")

    # If user guessed correctly, remove that word from the list of words to learn
    if result == "right":
        words_to_learn.remove(current_card)

    # Save current words to learn in a CSV file
    words_to_learn_df = pandas.DataFrame(words_to_learn)
    words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)

    # Have delay of 3 sec before flipping card
    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Create canvas for flashcard image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
title_text = canvas.create_text(400, 150, text="French", font=TITLE_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=lambda: next_card("wrong"))
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=lambda: next_card("right"))
right_button.grid(column=1, row=1)

# Read in list of words to learn
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Start from full list if words_to_learn.csv does not exist
    data = pandas.read_csv("data/french_words.csv")
    words_to_learn = data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

# Call next_card() so program starts with random card
next_card("wrong")

window.mainloop()
