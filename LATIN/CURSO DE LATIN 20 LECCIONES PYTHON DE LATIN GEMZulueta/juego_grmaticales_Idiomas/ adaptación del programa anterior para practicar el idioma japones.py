import random

def japanese_word_guess(points):
    print("\n🇯🇵 Japanese Word Guess")
    words = {"こんにちは": "Hello", "ありがとう": "Thank you", "さようなら": "Goodbye"}
    word, translation = random.choice(list(words.items()))
    answer = input(f"What is the meaning of '{word}'? ")
    if answer.lower() == translation.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {translation}")
    return points

def hiragana_fill(points):
    print("\n🔠 Hiragana Fill")
    words = {"こ_にちは": "こんにちは", "あ_がとう": "ありがとう", "さ_うなら": "さようなら"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the word: {incomplete}: ")
    if answer == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def kanji_identification(points):
    print("\n🎌 Kanji Identification")
    words = {"日本": "Japan", "学校": "School", "先生": "Teacher"}
    word, meaning = random.choice(list(words.items()))
    answer = input(f"What does '{word}' mean? ")
    if answer.lower() == meaning.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {meaning}")
    return points

def sentence_translation(points):
    print("\n📜 Sentence Translation")
    sentences = {"私は日本語を勉強しています。": "I am studying Japanese."}
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
        print("\n🇯🇵 JAPANESE LANGUAGE PRACTICE MENU")
        print("1. Japanese Word Guess")
        print("2. Hiragana Fill")
        print("3. Kanji Identification")
        print("4. Sentence Translation")
        print("5. View Progress")
        print("6. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = japanese_word_guess(points)
        elif option == "2":
            points = hiragana_fill(points)
        elif option == "3":
            points = kanji_identification(points)
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
