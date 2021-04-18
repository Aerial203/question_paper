from questionbank import question_ten, questions_five
from question_brain import Question

QUESTION_NUMBER = 0
question = Question(questions_five, question_ten)
total_five_marks = question.total_five_marks - 1
total_ten_marks = question.total_ten_marks - 1
five_marks_question = question.generate_five_marks_question()
ten_marks_question = question.generate_ten_marks_questions()

# Generates the random questions.
with open("question.doc", mode="w") as file:
    file.write(f"Attempt any {total_ten_marks}"
               f" Questions:\t\t\t\t\t\t\t [{total_ten_marks}*10={total_ten_marks*10}]\n\n")
    for ten_marks in ten_marks_question:
        QUESTION_NUMBER += 1
        file.write(f"{QUESTION_NUMBER}.\t{ten_marks}\n")

    file.write(f"\n\nAttempt any {total_five_marks} "
               f"Questions:\t\t\t\t\t\t\t [{total_five_marks}*5={total_five_marks*5}]\n\n")
    for five_marks in five_marks_question:
        QUESTION_NUMBER += 1
        file.write(f"{QUESTION_NUMBER}.\t{five_marks}\n")

QUESTION_NUMBER = 0
