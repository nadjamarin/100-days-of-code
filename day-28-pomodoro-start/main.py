from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 0.5
# SHORT_BREAK_MIN = 0.2
# LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 != 0:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_title.config(fg=GREEN, text="Work")
    elif reps % 2 == 0 and reps % 8 != 0:
        # If it's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        timer_title.config(fg=PINK, text="Break")
    else:
        # If it's the 8th rep:
        count_down(long_break_sec)
        timer_title.config(fg=RED, text="Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # first argument is time in ms, second is function, the rest are arguments for the function
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark_text = ""
        if reps % 2 == 0:
            check_marks.config(text=f"{check_mark_text}✔")

        # Her solution
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     check_mark_text += "✔"
        # check_marks.config(text=check_mark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Set up canvas with tomato image and timer
# highlightthickness = 0 removes border of the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

# Add buttons, checkmark, and title to the window
# can find checkmarks online to copy and paste: ✔
start_button = Button(text="Start", command=start_timer)
start_button.config(bg=PINK, fg="white", font=(FONT_NAME, 12, "bold"), relief=GROOVE)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(bg=PINK, fg="white", font=(FONT_NAME, 12, "bold"), relief=GROOVE)
reset_button.grid(column=2, row=2)

timer_title = Label(text="Timer", font=(FONT_NAME, 38, "bold"), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 12, "normal"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
