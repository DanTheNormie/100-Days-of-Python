from Day_17.question_model import Question
from Day_17.data import question_data
from Day_17.quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    question = Question(text, answer)

    question_bank.append(question)

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

qb.print_end_result()
