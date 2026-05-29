import random

def arabic_word_guess(points):
    print("\n🇸🇦 Arabic Word Guess")
    words = {"مرحبا": "Hello", "شكرا": "Thank you", "وداعا": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def arabic_letter_fill(points):
    print("\n🔠 Arabic Letter Fill")
    words = {"م_رحبا": "مرحبا", "ش_كرا": "شكرا", "و_داعا": "وداعا"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def harakat_identification(points):
    print("\n🎵 Harakat (Vowel) Identification")
    words = {"مَرْحَبًا": "Marhaban", "شُكْرًا": "Shukran", "وَدَاعًا": "Wada'an"}
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
    sentences = {"أنا أحب تعلم العربية.": "I love studying Arabic."}
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
        print("\n🇸🇦 ARABIC LANGUAGE PRACTICE MENU")
        print("1. Arabic Word Guess")
        print("2. Arabic Letter Fill")
        print("3. Harakat Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = arabic_word_guess(points)
        elif option == "2":
            points = arabic_letter_fill(points)
        elif option == "3":
            points = harakat_identification(points)
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
