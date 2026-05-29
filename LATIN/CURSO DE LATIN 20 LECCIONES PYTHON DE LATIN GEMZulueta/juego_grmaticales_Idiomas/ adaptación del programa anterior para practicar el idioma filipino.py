import random

def filipino_word_guess(points):
    print("\n🇵🇭 Filipino Word Guess")
    words = {"Kumusta": "Hello", "Salamat": "Thank you", "Paalam": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def filipino_fill(points):
    print("\n🔠 Filipino Fill")
    words = {"Ku_usta": "Kumusta", "Sa_amat": "Salamat", "P_alam": "Paalam"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def filipino_phrase_identification(points):
    print("\n🎌 Filipino Phrase Identification")
    phrases = {"Aso": "Dog", "Pusa": "Cat", "Guro": "Teacher"}
    phrase, meaning = random.choice(list(phrases.items()))
    answer = input(f"What does '{phrase}' mean? ")
    if answer.lower() == meaning.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {meaning}")
    return points

def sentence_translation(points):
    print("\n📜 Sentence Translation")
    sentences = {"Nag-aaral ako ng wikang Filipino.": "I am learning Filipino."}
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
        print("\n🇵🇭 FILIPINO LANGUAGE PRACTICE MENU")
        print("1. Filipino Word Guess")
        print("2. Filipino Fill")
        print("3. Filipino Phrase Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = filipino_word_guess(points)
        elif option == "2":
            points = filipino_fill(points)
        elif option == "3":
            points = filipino_phrase_identification(points)
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
