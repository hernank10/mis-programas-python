import random

def identify_meaning():
    words = {"correr": "To move quickly with long strides", "brillante": "Reflecting a lot of light"}
    word, meaning = random.choice(list(words.items()))
    options = [meaning, "Incorrect option 1", "Incorrect option 2"]
    random.shuffle(options)
    print(f"What is the meaning of '{word}'?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = int(input("Choose the correct option: "))
    print("Correct!" if options[answer - 1] == meaning else "Incorrect")

def synonyms_antonyms():
    synonyms = {"feliz": "alegre", "rápido": "veloz"}
    antonyms = {"feliz": "triste", "rápido": "lento"}
    word = random.choice(list(synonyms.keys()))
    print(f"Write a synonym or antonym of '{word}':")
    answer = input().strip()
    if answer in (synonyms[word], antonyms[word]):
        print("Correct!")
    else:
        print(f"Incorrect. A synonym would be '{synonyms[word]}' and an antonym '{antonyms[word]}'")

def complete_sentence():
    sentences = {"brillante": "The sun is very ______ today."}
    word, sentence = random.choice(list(sentences.items()))
    print(sentence)
    answer = input("Complete the sentence: ").strip()
    if answer == word:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{word}'")

def classify_words():
    word_context = {"científico": "technical", "pintoresco": "literary"}
    word, category = random.choice(list(word_context.items()))
    print(f"In what context is the word '{word}' used?")
    answer = input("Respond: technical, colloquial, literary: ").strip().lower()
    if answer == category:
        print("Correct!")
    else:
        print(f"Incorrect. The correct category is '{category}'")

def define_word():
    word = "correr"
    print(f"Write a definition for the word '{word}':")
    answer = input()
    print("Thank you for your response! Here is the correct definition: To move quickly with long strides.")

def menu():
    while True:
        print("\nWord Practice Menu")
        print("1. Meaning Identification")
        print("2. Synonym and Antonym Relationship")
        print("3. Sentence Completion")
        print("4. Word Classification by Context")
        print("5. Definition Construction")
        print("6. Exit")
        option = input("Choose an option: ")
        if option == "1":
            identify_meaning()
        elif option == "2":
            synonyms_antonyms()
        elif option == "3":
            complete_sentence()
        elif option == "4":
            classify_words()
        elif option == "5":
            define_word()
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

menu()
