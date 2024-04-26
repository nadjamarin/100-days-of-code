from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # Can define data type of quiz_brain using a colon
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Test",
                                                     font="Arial 18 italic",
                                                     fill=THEME_COLOR,
                                                     width=280)
        # Add padding in grid() line
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0,
                                   command=self.check_true_answer)
        self.check_button.grid(row=2, column=0)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0,
                                   command=self.check_false_answer)
        self.cross_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", font=("Arial", 14, "normal"), bg=THEME_COLOR, fg="white", pady=20)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz.")
            self.score_label.config(text=f"Final Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            # Disable the buttons so they can't be pressed
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
