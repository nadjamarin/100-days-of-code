from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# make question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
# print(question_bank)
# print(question_bank[0].answer)


quiz = QuizBrain(question_bank)
# print(len(question_bank))

more_questions = True
while more_questions:
    quiz.next_question()
    more_questions = quiz.still_has_questions()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")