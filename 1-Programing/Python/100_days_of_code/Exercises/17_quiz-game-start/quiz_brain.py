class QuizBrain:

    def __init__(self, q_list): # q_list is receiving the question_bank (all the questions and answers).
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self): #Check if you reached the end of the questions, if so return True
        return self.question_number < len(self.question_list)

    def next_question(self): # We select one question from the whole question_list.
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer): #Check if the answer is correct or not and print proper info
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You are wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")