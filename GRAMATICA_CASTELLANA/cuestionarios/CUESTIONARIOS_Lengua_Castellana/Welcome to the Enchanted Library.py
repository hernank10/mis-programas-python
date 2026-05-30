import time

def welcome():
    print("\n🌟 Welcome to the Enchanted Library 🌟")
    print("Here, the rules of language are trapped in magical books.")
    print("Your mission is to solve grammatical challenges and release this knowledge.")
    print("Get ready to learn, solve, and succeed. Good luck!\n")

def main_menu():
    print("\n📚 Main Menu:")
    print("1. Explore the library")
    print("2. Solve grammar riddles")
    print("3. View achievements")
    print("4. Exit the game")
    return input("Choose an option (1-4): ")

def explore_library():
    print("\n✨ You are in a room filled with magical books. Some are sealed by riddles.")
    print("Each book contains a fragment of grammatical knowledge.")
    print("Discover the secrets by answering the challenges correctly.\n")

def solve_riddles(achievements):
    print("\n🧐 Solve the following riddles to release the books:")
    questions = [
        {
            "question": "What is the subject in the sentence: 'The cat chases the mouse'?",
            "options": ["1. The cat", "2. Chases", "3. The mouse"],
            "answer": "1"
        },
        {
            "question": "What type of word is 'quickly'?",
            "options": ["1. Noun", "2. Adverb", "3. Verb"],
            "answer": "2"
        },
        {
            "question": "What is the plural of 'light'?",
            "options": ["1. Lights", "2. Lightes", "3. Lights"],
            "answer": "1"
        }
    ]

    for i, q in enumerate(questions):
        print(f"\n📖 Book {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter the number of the correct answer: ")
        if answer == q["answer"]:
            print("✅ Correct! The book has been released.")
            achievements.append(f"Book {i+1}: {q['question']}")
        else:
            print("❌ Incorrect. Moving on to the next book.")
    return achievements

def view_achievements(achievements):
    if achievements:
        print("\n🏆 Achievements unlocked:")
        for achievement in achievements:
            print(f"- {achievement}")
    else:
        print("\n⚠️ You don't have any achievements yet. Solve riddles to unlock books.")

def farewell():
    print("\n📚 Thanks for visiting the Enchanted Library. See you next time!")

def game():
    welcome()
    achievements = []
    while True:
        option = main_menu()
        if option == "1":
            explore_library()
        elif option == "2":
            achievements = solve_riddles(achievements)
        elif option == "3":
            view_achievements(achievements)
        elif option == "4":
            farewell()
            break
        else:
            print("⚠️ Invalid option. Please try again.")
        time.sleep(1)

# Start the game
game()
