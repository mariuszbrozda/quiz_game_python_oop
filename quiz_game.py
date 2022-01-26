

class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.scores = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.q_text} (True/False)?: ').lower()
        self.check_answer(user_answer, current_question.q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Correct answer!')
            self.scores += 1
            print(f'Your current score: {self.scores}/{self.question_number}')
        else:
            print('Wrong answer')
            print(f'The correct answer was: {correct_answer}')
            print(f'Your current score: {self.scores}/{self.question_number}')
            print('\n')


    def if_quiz_still_has_question(self):
        question_number = self.question_number
        return question_number < len(self.question_list)