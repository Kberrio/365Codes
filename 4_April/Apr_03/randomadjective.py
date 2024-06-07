import random

adjectives = ["stupid", "ugly", "lazy", "smelly", "obnoxious", "idiotic", "pathetic", "clueless"]
nouns = ["donkey", "blobfish", "slug", "pigeon", "mold", "dunce", "moron", "pickle"]

def generate_insult():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"You {adjective} {noun}!"

def main():
    print("Welcome to the Random Insult Generator!")
    while True:
        input("Press Enter to generate a random insult, or type 'quit' to exit.")
        insult = generate_insult()
        print(insult)

        if input("Generate another insult? (yes/no): ").lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
