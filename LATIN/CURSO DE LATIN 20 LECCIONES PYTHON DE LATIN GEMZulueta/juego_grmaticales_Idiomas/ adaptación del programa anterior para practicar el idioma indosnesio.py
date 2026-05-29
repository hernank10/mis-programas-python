import random

def indonesian_word_guess(points):
    print("\n🇮🇩 Indonesian Word Guess")
    words = {"Halo": "Hello", "Terima kasih": "Thank you", "Selamat tinggal": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def indonesian_fill(points):
    print("\n🔠 Indonesian Fill")
    words = {"Ha_o": "Halo", "Te_ima kasih": "Terima kasih", "S_lamat tinggal": "Selamat tinggal"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def indonesian_phrase_identification(points):
    print("\n🎌 Indonesian Phrase Identification")
    phrases = {"Indonesia": "Indonesia", "Sekolah": "School", "Guru": "Teacher"}
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
    sentences = {"Saya sedang belajar bahasa Indonesia.": "I am learning Indonesian."}
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
        print("\n🇮🇩 INDONESIAN LANGUAGE PRACTICE MENU")
        print("1. Indonesian Word Guess")
        print("2. Indonesian Fill")
        print("3. Indonesian Phrase Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = indonesian_word_guess(points)
        elif option == "2":
            points = indonesian_fill(points)
        elif option == "3":
            points = indonesian_phrase_identification(points)
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
