from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # this will be a list of question Objects

# Iterate all the questions in data.py.Separate the questions and the answers,initialize the Object new_question by
# passing in the questions and answers into the __init__ constructor and store every object inside question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# In the above code we do this to convert the data coming from data.py to Objects which will have the data as fail
# proof, easy to access and will have the autofill thing among other benefits.

# We create the quiz Object from QuizBrain Class
quiz = QuizBrain(question_bank)
# print(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
