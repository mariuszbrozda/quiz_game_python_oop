from data import question_data
from question_model import Question
from quiz_game import QuizBrain

quiz_is_on = True

question_bank = []

for question in question_data:
    question_text = question['question']
    answer_text = question['correct_answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)