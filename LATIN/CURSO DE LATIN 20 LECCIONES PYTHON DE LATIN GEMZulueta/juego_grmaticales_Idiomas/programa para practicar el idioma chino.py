import random

def chinese_character_guess(points):
    print("\n🀄 Chinese Character Guess")
    characters = {"你好": "Hello", "谢谢": "Thank you", "再见": "Goodbye"}
    character, meaning = random.choice(list(characters.items()))
    answer = input(f"What is the meaning of '{character}'? ")
    if answer.lower() == meaning.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {meaning}")
    return points

def pinyin_fill(points):
    print("\n🔡 Pinyin Fill")
    words = {"n_h_": "nihao", "xi_xie": "xiexie", "z_ijian": "zaijian"}
    incomplete, complete = random.choice(list(words.items()))
    answer = input(f"Complete the Pinyin word: {incomplete}: ")
    if answer.lower() == complete:
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {complete}")
    return points

def radical_match(points):
    print("\n🎭 Radical Match")
    radicals = {"亻": "Person", "木": "Tree", "火": "Fire"}
    radical, meaning = random.choice(list(radicals.items()))
    answer = input(f"What does the radical '{radical}' mean? ")
    if answer.lower() == meaning.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {meaning}")
    return points

def tone_identification(points):
    print("\n🎵 Tone Identification")
    tones = {"mā": "1st tone", "má": "2nd tone", "mǎ": "3rd tone", "mà": "4th tone"}
    syllable, tone = random.choice(list(tones.items()))
    answer = input(f"Which tone is '{syllable}'? ")
    if answer.lower() == tone.lower():
        print("✅ Correct!")
        points += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {tone}")
    return points

def sentence_translation(points):
    print("\n📜 Sentence Translation")
    sentences = {"我喜欢学习汉语。": "I like studying Chinese."}
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
        print("\n🀄 CHINESE LANGUAGE PRACTICE MENU")
        print("1. Chinese Character Guess")
        print("2. Pinyin Fill")
        print("3. Radical Match")
        print("4. Tone Identification")
        print("5. Sentence Translation")
        print("6. View Progress")
        print("7. Exit")
        option = input("Choose a game: ")
        
        if option == "1":
            points = chinese_character_guess(points)
        elif option == "2":
            points = pinyin_fill(points)
        elif option == "3":
            points = radical_match(points)
        elif option == "4":
            points = tone_identification(points)
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
