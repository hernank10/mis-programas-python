import random

def russian_word_guess(points):
    print("\n🇷🇺 Russian Word Guess")
    words = {"Привет": "Hello", "Спасибо": "Thank you", "До свидания": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def cyrillic_fill(points):
    print("\n🔠 Cyrillic Fill")
    words = {"Пр_вет": "Привет", "Спа_ибо": "Спасибо", "До св_дания": "До свидания"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer.lower() == complete.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def case_match(points):
    print("\n📏 Case Matching")
    cases = {"Я иду в школу (Accusative)": "Accusative", "Я горжусь тобой (Instrumental)": "Instrumental"}
    sentence, case = random.choice(list(cases.items()))
    answer = input(f"Identify the case used in this sentence: '{sentence}' ")
    if answer.lower() == case.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {case}")
    return points

def stress_identification(points):
    print("\n🎵 Stress Identification")
    words = {"молокО": "mo-lo-KO", "гОрода": "GO-ro-da", "телефОн": "te-le-FON"}
    word, pronunciation = random.choice(list(words.items()))
    answer = input(f"Where is the stress in '{word}'? (Write the syllables separated by hyphens) ")
    if answer.lower() == pronunciation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {pronunciation}")
    return points

def sentence_translation(points):
    print("\n📜 Sentence Translation")
    sentences = {"Я люблю изучать русский язык.": "I love studying Russian."}
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
        print("\n🇷🇺 RUSSIAN LANGUAGE PRACTICE MENU")
        print("1. Russian Word Guess")
        print("2. Cyrillic Fill")
        print("3. Case Match")
        print("4. Stress Identification")
        print("5. Sentence Translation")
        print("6. View Progress")
        print("7. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = russian_word_guess(points)
        elif option == "2":
            points = cyrillic_fill(points)
        elif option == "3":
            points = case_match(points)
        elif option == "4":
            points = stress_identification(points)
        elif option == "5":
            points = sentence_translation(points)
        elif option == "6":
            print(f"\n🎯 Your current progress: {points} points")
        elif option == "7":
            print("👋 Thanks for playing! See you next time.")
            break
        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    menu()
