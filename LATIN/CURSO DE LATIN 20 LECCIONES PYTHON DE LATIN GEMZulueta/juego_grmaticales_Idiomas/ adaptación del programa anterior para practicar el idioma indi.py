import random

def hindi_word_guess(points):
    print("\n🇮🇳 Hindi Word Guess")
    words = {"नमस्ते": "Hello", "धन्यवाद": "Thank you", "अलविदा": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def devanagari_fill(points):
    print("\n🔠 Devanagari Fill")
    words = {"न_मस्ते": "नमस्ते", "ध_न्यवाद": "धन्यवाद", "अ_विदा": "अलविदा"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def hindi_phrase_identification(points):
    print("\n🎌 Hindi Phrase Identification")
    phrases = {"भारत": "India", "विद्यालय": "School", "शिक्षक": "Teacher"}
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
    sentences = {"मैं हिंदी सीख रहा हूँ।": "I am learning Hindi."}
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
        print("\n🇮🇳 HINDI LANGUAGE PRACTICE MENU")
        print("1. Hindi Word Guess")
        print("2. Devanagari Fill")
        print("3. Hindi Phrase Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = hindi_word_guess(points)
        elif option == "2":
            points = devanagari_fill(points)
        elif option == "3":
            points = hindi_phrase_identification(points)
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
