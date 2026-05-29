import json

# Función para guardar el progreso
def guardar_progreso(progreso):
    with open("english_progress.json", "w") as archivo:
        json.dump(progreso, archivo)
    print("Progress saved successfully.")

# Función para cargar el progreso
def cargar_progreso():
    try:
        with open("english_progress.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Lista inicial de ejercicios básicos
english_exercises = [
    {"type": "translation", "question": "Translate to English: 'Hola, ¿cómo estás?'", "answer": "Hello, how are you?"},
    {"type": "fill_in_blank", "question": "Complete the sentence: I ___ (be) happy today.", "answer": "am"},
    {"type": "multiple_choice", "question": "Choose the correct word: She ___ (likes/like) to read books.", "options": ["likes", "like"], "answer": "likes"},
    {"type": "true_false", "question": "The sentence 'I has a car' is correct.", "answer": "false"},
    {"type": "word_order", "question": "Rearrange the words: 'is name my John'", "answer": "My name is John."}
]

# Introducción
def introduccion_ingles():
    print("""
Welcome to the Enhanced English Learning Program!
Features:
- Vocabulary and grammar exercises.
- Sentence formation and multiple-choice questions.
- Personalized exercise creation.
- Progress tracking.
Enjoy your learning journey!
""")

# Ejercicios dinámicos
def practicar_ingles():
    print("Let's practice English!")
    progreso = cargar_progreso()
    correct_answers = 0

    for i, exercise in enumerate(english_exercises, 1):
        print(f"\nExercise {i}: {exercise['question']}")
        if exercise["type"] == "multiple_choice":
            print("Options:", ", ".join(exercise["options"]))

        respuesta = input("Your answer: ").strip().lower()

        if respuesta == exercise["answer"].lower():
            print("Correct!")
            progreso[f"Exercise {i}"] = "Correct"
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {exercise['answer
