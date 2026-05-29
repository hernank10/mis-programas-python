import random

def korean_word_guess(points):
    print("\n🇰🇷 Korean Word Guess")
    words = {"안녕하세요": "Hello", "감사합니다": "Thank you", "안녕": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def hangul_fill(points):
    print("\n🔠 Hangul Fill")
    words = {"안_하세요": "안녕하세요", "감_합니다": "감사합니다", "안_": "안녕"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def korean_phrase_identification(points):
    print("\n🎌 Korean Phrase Identification")
    phrases = {"한국": "Korea", "학교": "School", "선생님": "Teacher"}
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
    sentences = {"저는 한국어를 배우고 있어요.": "I am learning Korean."}
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
        print("\n🇰🇷 KOREAN LANGUAGE PRACTICE MENU")
        print("1. Korean Word Guess")
        print("2. Hangul Fill")
        print("3. Korean Phrase Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = korean_word_guess(points)
        elif option == "2":
            points = hangul_fill(points)
        elif option == "3":
            points = korean_phrase_identification(points)
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
