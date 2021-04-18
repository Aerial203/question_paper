import random


class Question:

    def __init__(self, five_marks_question_list, ten_marks_question_list):
        self.five_marks_list = five_marks_question_list
        self.ten_marks_list = ten_marks_question_list
        self.total_five_marks = 11
        self.total_ten_marks = 4

    def generate_five_marks_question(self):
        all_questions = []
        five_marks_question = []
        for questions in self.five_marks_list:
            all_questions.append(questions["question"])
        while len(five_marks_question) != self.total_five_marks:
            random_question = random.choice(all_questions)
            if random_question not in five_marks_question:
                five_marks_question.append(random_question)
        return five_marks_question

    def generate_ten_marks_questions(self):
        all_questions = []
        ten_marks_question = []
        for questions in self.ten_marks_list:
            all_questions.append(questions["question"])
        while len(ten_marks_question) != self.total_ten_marks:
            random_question = random.choice(all_questions)
            if random_question not in ten_marks_question:
                ten_marks_question.append(random_question)
        return ten_marks_question
