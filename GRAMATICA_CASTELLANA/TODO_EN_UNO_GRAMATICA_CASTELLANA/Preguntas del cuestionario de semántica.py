import random

# Preguntas del cuestionario de semántica
questions_semantics = [
    {"type": "multiple_choice", "question": "🌟📜✏️🕵🏛¿Qué estudia la semántica?", 
     "options": ["A) El significado de las palabras", "B) La estructura gramatical", "C) El origen de los sonidos", "D) La entonación del habla"], "answer": "A"},
    {"type": "true_false", "question": "La semántica analiza tanto palabras como oraciones completas.", "answer": "T"},
    {"type": "open", "question": "¿🌟📜✏️🕵🏛Cómo se llama el fenómeno de que una palabra tenga varios significados?", "answer": "Polisemia"},
    {"type": "multiple_choice", "question": "¿Qué es un sinónimo?", 
     "options": ["A) Una palabra con significado opuesto", "B) Una palabra con significado similar", "C) Una palabra con múltiples significados", "D) Una palabra nueva"], "answer": "B"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵🏛¿Qué es un antónimo?", 
     "options": ["A) Una palabra con significado opuesto", "B) Una palabra con significado similar", "C) Una palabra antigua", "D) Una palabra con origen extranjero"], "answer": "A"},
    {"type": "true_false", "question": "📜✏️🕵🏛La homonimia ocurre cuando dos palabras tienen la misma forma pero significados diferentes.", "answer": "T"},
    {"type": "open", "question": "¿🌟📜✏️🕵🏛Cómo se llama la relación entre palabras que comparten un mismo campo de significado?", "answer": "Hiponimia"},
    {"type": "multiple_choice", "question": "¿Qué tipo de relación semántica existe entre 'perro' y 'animal'?", 
     "options": ["A) Hiponimia", "B) Homonimia", "C) Polisemia", "D) Sinonimia"], "answer": "A"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵🏛¿Qué estudia la pragmática en relación con la semántica?", 
     "options": ["A) Los significados literales", "B) Los significados en contexto", "C) La estructura de las oraciones", "D) Los sonidos del habla"], "answer": "B"},
    {"type": "true_false", "question": "El contexto no afecta el significado de una palabra o frase.", "answer": "F"},
    # Añadir más preguntas aquí (hasta completar 50)
]

# Función para mostrar las preguntas
def show_question(question):
    print("\n" + question["question"])
    if question["type"] == "multiple_choice":
        for option in question["options"]:
            print(option)
    response = input("🌟📜✏️🕵🏛 Tu respuesta: ").strip()
    return response

# Función para validar las respuestas
def validate_answer(question, response):
    if question["type"] == "open":
        return response.lower() == question["answer"].lower()
    return response.upper() == question["answer"].upper()

# Función para ejecutar el cuestionario
def run_quiz(questions, title):
    print(f"\n--- {title} ---")
    score = 0
    random.shuffle(questions)  # Mezclar preguntas
    for i, question in enumerate(questions[:20]):  # Limitar a 20 preguntas
        print(f"\nPregunta {i + 1}:")
        response = show_question(question)
        if validate_answer(question, response):
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            score += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {question['answer']}")
    print(f"\n¡Completaste el cuestionario! Tu puntaje final es {score}/{len(questions[:20])}.")

# Menú interactivo
def main_menu():
    while True:
        print("\n---🌟📜✏️🕵🏛️  Menú de Cuestionarios 🌟📜✏️🕵🏛️ ---")
        print("️1️⃣ Cuestionario de Semántica")
        print("2️⃣ Salir")
        
        choice = input("🌟📜✏️🕵🏛 Selecciona una opción (1-2): ").strip()
        
        if choice == "1":
            run_quiz(questions_semantics, "Semántica de la Lengua Castellana")
        elif choice == "2":
            print("🌟📜✏️🕵🏛¡Gracias por practicar!✅ ¡Hasta la próxima!")
            break
        else:
            print("🌟📜✏️🕵🏛Opción no válida. Intenta de nuevo.")
 
# Ejecutar el programa
main_menu()
