from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface # We import the class from the module ui

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface() # We declare the object quiz_ui from the class QuizInterface

# while quiz.still_has_questions():  --> We comment this out because we are using the self.window.mainloop() in ui.py
#     quiz.next_question()               which acts like a while loop and both would colide, we can only have one.

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
