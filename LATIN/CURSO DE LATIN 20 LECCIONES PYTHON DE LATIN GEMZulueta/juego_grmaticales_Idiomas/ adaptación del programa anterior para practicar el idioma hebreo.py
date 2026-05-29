import random

def hebrew_word_guess(points):
    print("\n🇮🇱 Hebrew Word Guess")
    words = {"שלום": "Hello", "תודה": "Thank you", "להתראות": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def hebrew_letter_fill(points):
    print("\n🔠 Hebrew Letter Fill")
    words = {"ש_לום": "שלום", "ת_דה": "תודה", "להת_אות": "להתראות"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def nikud_identification(points):
    print("\n🎵 Nikud (Vowel) Identification")
    words = {"שָלוֹם": "Shalom", "תּוֹדָה": "Toda", "לְהִתְרָאוֹת": "Lehitraot"}
    word, pronunciation = random.choice(list(words.items()))
    answer = input(f"How is '{word}' pronounced? ")
    if answer.lower() == pronunciation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {pronunciation}")
    return points

def sentence_translation(points):
    print("\n📜 Sentence Translation")
    sentences = {"אני אוהב ללמוד עברית.": "I love studying Hebrew."}
    sentence, translation = random.choice(list(sentences.items()))
    answer = input(f"Translate this sentence: '{sentence}' ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def menu():
    points = 0
    while True:
        print("\n🇮🇱 HEBREW LANGUAGE PRACTICE MENU")
        print("1. Hebrew Word Guess")
        print("2. Hebrew Letter Fill")
        print("3. Nikud Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = hebrew_word_guess(points)
        elif option == "2":
            points = hebrew_letter_fill(points)
        elif option == "3":
            points = nikud_identification(points)
        elif option == "4":
            points = sentence_translation(points)
        elif option == "5":
            print(f"\n🎯 Your current progress: {points} points")
        elif option == "6":
            print("👋 Thanks for playing! See you next time.")
            break
        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    menu()
