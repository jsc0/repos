from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # this will be a list of question Objects

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# In the above code we do this to convert the data coming from data.py to Objects which will have the data in a fail
# proof and will have an easy way to work by the autofill thing.

quiz = QuizBrain(question_bank)
quiz.next_question()

print(question_bank[2].text)









#new_q = Question("Pollas", "En vinagre")
#print(new_q.text, new_q.answer)