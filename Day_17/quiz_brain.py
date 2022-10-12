class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 1
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number - 1]
        ui = input(f"Q.{self.question_number}: {question.text} type(true/false)? : ")
        self.check_answer(ui, question.answer)
        self.print_score()
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)

    def check_answer(self, u_ans, c_ans):
        if u_ans.lower() == c_ans.lower():
            print("That's correct. you get a point.")
            self.score += 1
        else:
            print("That's wrong. :( ")

    def print_score(self):
        print(f"Your current score is : {self.score}/{self.question_number} \n")

    def print_end_result(self):
        print("\nThe Quiz has ended")
        print(f"Your final score is {self.score}/12")
