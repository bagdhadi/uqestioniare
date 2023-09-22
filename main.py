from data import question_data
from questionaire import Question
from quiz_brave import Quiz
question_bank = []
for q in question_data:
    question_text =q["question"]
    question_answer =q["answer"]
    new_question =  Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz ")  
print(f"your final score was: {quiz.score}/{quiz.question_number} ")  

