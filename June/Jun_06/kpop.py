import random

# Define the questions and answers
questions = [
    {"question": "Which K-pop group is known for the hit song 'Dynamite'?", "answer": "BTS"},
    {"question": "Which K-pop girl group released the song 'DDU-DU DDU-DU'?", "answer": "BLACKPINK"},
    {"question": "Who is the leader of the girl group Twice?", "answer": "Jihyo"},
    {"question": "Which K-pop group is known as the 'Nation's Girl Group'?", "answer": "Girls' Generation"},
    {"question": "Which K-pop boy group debuted with the song 'No More Dream'?", "answer": "BTS"},
    {"question": "Who is the main dancer of EXO?", "answer": "Kai"},
    {"question": "Which K-pop girl group has a member named Lisa?", "answer": "BLACKPINK"},
    {"question": "What year did the girl group Red Velvet debut?", "answer": "2014"},
    {"question": "Which K-pop group is known for the song 'Fantastic Baby'?", "answer": "BIGBANG"},
    {"question": "Who is the maknae (youngest member) of the boy group SHINee?", "answer": "Taemin"},
]

def kpop_quiz():
    random.shuffle(questions)
    score = 0

    print("Welcome to the K-pop Trivia Quiz!")
    print("You will be asked 5 questions. Let's see how much you know about K-pop!\n")

    for i in range(5):
        question = questions[i]
        user_answer = input(f"Question {i+1}: {question['question']} ")

        if user_answer.strip().lower() == question['answer'].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.\n")

    print(f"You got {score} out of 5 questions correct!")
    if score == 5:
        print("Amazing! You're a true K-pop fan!")
    elif 3 <= score < 5:
        print("Great job! You know your K-pop well!")
    else:
        print("Better luck next time! Keep enjoying K-pop!")

if __name__ == "__main__":
    kpop_quiz()
