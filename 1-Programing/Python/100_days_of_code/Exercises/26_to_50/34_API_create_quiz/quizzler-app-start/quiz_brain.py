import html

class QuizBrain:

    def __init__(self, q_list): # You receive the question_bank (list of objects)
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self): # Check if the the question number is lower than the number of questions
        return self.question_number < len(self.question_list) # in the question_list

    def next_question(self): # Select next question, unescape it's format and print question number and question into the app
        self.current_question = self.question_list[self.question_number]# Select the question within the list of objects
        self.question_number += 1
        q_text = html.unescape(self.current_question.text) # Unescape special characters (don't show strange codes)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer): # This comes from ui.py, true_pressed() or false_pressed(). Is triggered when we press the buttons of the app.
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False