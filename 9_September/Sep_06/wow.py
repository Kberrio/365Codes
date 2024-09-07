import random

wow_lore = [
    {
        "question": "Who was the Lich King before Arthas?",
        "answer": "Ner'zhul",
        "explanation": "Ner'zhul, an orc shaman, was transformed into the Lich King by Kil'jaeden."
    },
    {
        "question": "What is the name of the Titan who stabbed Azeroth with his sword?",
        "answer": "Sargeras",
        "explanation": "Sargeras, the fallen Titan, stabbed Azeroth with his sword at the end of the Legion expansion."
    },
    {
        "question": "Who is known as the 'Aspect of Death'?",
        "answer": "Deathwing",
        "explanation": "Deathwing, formerly known as Neltharion, became corrupted and is now known as the Aspect of Death."
    },
    {
        "question": "What is the name of the first Guardian of Tirisfal?",
        "answer": "Alodi",
        "explanation": "Alodi was the first Guardian of Tirisfal, a powerful mage empowered to fight the Burning Legion."
    },
    {
        "question": "Who was the orc who first drank the blood of Mannoroth?",
        "answer": "Grom Hellscream",
        "explanation": "Grommash 'Grom' Hellscream was the first to drink Mannoroth's blood, leading to the corruption of the orcs."
    }
]

def run_quiz():
    score = 0
    total_questions = len(wow_lore)
    
    print("Welcome to the World of Warcraft Lore Quiz!")
    print(f"There are {total_questions} questions. Let's begin!\n")
    
    random.shuffle(wow_lore)
    
    for i, lore_item in enumerate(wow_lore, 1):
        print(f"Question {i}: {lore_item['question']}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == lore_item['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {lore_item['answer']}.")
        
        print(f"Explanation: {lore_item['explanation']}\n")
    
    print(f"Quiz complete! You scored {score} out of {total_questions}.")
    print(f"Your lore knowledge is {score/total_questions*100:.2f}% strong!")

if __name__ == "__main__":
    run_quiz()