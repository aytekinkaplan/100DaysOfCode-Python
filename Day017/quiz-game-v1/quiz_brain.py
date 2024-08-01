class QuizBrain:

    def __init__(self, q_list,q_category, q_difficulty, q_question, q_correct_answer, q_incorrect_answers):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.category = q_category
        self.difficulty = q_difficulty
        self.question = q_question
        self.correct_answer = q_correct_answer
        self.incorrect_answers = q_incorrect_answers

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def question_category(self):
        print(f"Category: {self.category}")

    def question_difficulty(self):
        print(f"Difficulty: {self.difficulty}")

    def question_text(self):
        print(f"Question: {self.question}")


    def end_game(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")




