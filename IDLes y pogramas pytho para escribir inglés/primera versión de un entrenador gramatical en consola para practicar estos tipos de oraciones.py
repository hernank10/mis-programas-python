import random

# Diccionario con tipos de oraciones y ejemplos
exercises = {
    "Declarative": [
        ("She is reading a book.", "declarative"),
        ("I live in London.", "declarative"),
        ("They like pizza.", "declarative")
    ],
    "Interrogative": [
        ("Are you coming?", "interrogative"),
        ("Where do you live?", "interrogative"),
        ("Is it raining?", "interrogative")
    ],
    "Imperative": [
        ("Close the door.", "imperative"),
        ("Please sit down.", "imperative"),
        ("Turn off the light.", "imperative")
    ],
    "Exclamatory": [
        ("What a beautiful day!", "exclamatory"),
        ("How amazing!", "exclamatory"),
        ("That’s incredible!", "exclamatory")
    ]
}

def practice():
    score = 0
    total = 5
    all_sentences = [s for group in exercises.values() for s in group]
    random.shuffle(all_sentences)

    print("💡 Identify the type of sentence: declarative, interrogative, imperative, exclamatory")
    print("Type your answer in English.\n")

    for i in range(total):
        sentence, correct_type = all_sentences[i]
        print(f"{i+1}. {sentence}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct_type:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. It was: {correct_type}\n")

    print(f"🏆 Final score: {score}/{total}")

if __name__ == "__main__":
    practice()
