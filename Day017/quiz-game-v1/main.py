question_bank = []

for question in question_data:
    new_question = Question(
        question["category"],
        question["difficulty"],
        question["question"],
        question["correct_answer"],
        question["incorrect_answers"]
    )
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_game()
