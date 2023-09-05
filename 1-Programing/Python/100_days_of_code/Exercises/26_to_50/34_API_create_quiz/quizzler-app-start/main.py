from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface # We import the class from the module ui

question_bank = [] # Here we will store the 10 questions and answers. Will be stored as a list of 10 objects, like this:
# [<question_model.Question object at 0x106099390>, <question_model.Question object at 0x104a7d390>, ...

# This loop will get each question and answer comming from the API
for question in question_data: # We iterate the list question_data, which contains 10 questions from the API
    question_text = question["question"] # We get the question, like: Socrates wrote The Linux Bible
    question_answer = question["correct_answer"] # we get the answer, like: True
    new_question = Question(question_text, question_answer) # We store the question and the answer
    question_bank.append(new_question) # And we append it to the list question_bank

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz) # We declare the object quiz_ui from the class QuizInterface

# while quiz.still_has_questions():  --> We comment this out because we are using the self.window.mainloop() in ui.py
#     quiz.next_question()               which acts like a while loop and both would colide, we can only have one.
