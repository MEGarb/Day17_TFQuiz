from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    question_bank.append(Question(entry.get("question"), entry.get("correct_answer")))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have reached the end of the quiz.")
print(f"Out of {len(quiz.questions_list)} questions you have answered {quiz.score} correctly.")
