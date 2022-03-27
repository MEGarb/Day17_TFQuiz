class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{(self.question_number + 1)}: {self.questions_list[self.question_number].text} (True/False): ")
        self.check_answer(answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, ans, corr_ans):
        if ans.lower() == corr_ans.lower():
            self.score += 1
            print("\nCorrect!")
        else:
            print("\nBetter luck next time.")
        print(f"The correct answer was : {corr_ans}")
        print(f"You have a score of {self.score} out of a possible {self.question_number + 1}\n")



