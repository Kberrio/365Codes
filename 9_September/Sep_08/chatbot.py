import re
import random

def simple_chatbot():
    # Define patterns and responses
    patterns = {
        r'\b(hi|hello|hey)\b': ['Hello!', 'Hi there!', 'Hey!'],
        r'how are you': ['I'm doing well, thanks!', 'I'm great, how about you?'],
        r'what\'s your name': ['I'm a simple chatbot.', 'You can call me ChatBot.'],
        r'bye': ['Goodbye!', 'See you later!', 'Bye!'],
        r'': ['I'm not sure I understand. Can you rephrase that?', 'Could you please elaborate?']
    }

    print("ChatBot: Hello! How can I help you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break

        for pattern, responses in patterns.items():
            if re.search(pattern, user_input):
                print("ChatBot:", random.choice(responses))
                break
        else:
            print("ChatBot: I'm not sure how to respond to that. Can you try asking something else?")

if __name__ == "__main__":
    simple_chatbot()