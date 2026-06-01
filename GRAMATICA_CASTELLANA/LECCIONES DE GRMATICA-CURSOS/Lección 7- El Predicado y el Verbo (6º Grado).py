import random
import os
import time

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("-" * 60)
    print(f"📚 {title.upper()} 📚")
    print("-" * 60)
    print()

def show_theory():
    """Muestra la sección de teoría sobre el predicado y el verbo."""
    show_header("Teoría: El Predicado y el Verbo")
    print("¡Hola! Ya somos expertos encontrando el Sujeto en una oración.")
    print("Hoy vamos a conocer la otra parte muy importante de la oración: ¡EL PREDICADO!\n")
    
    print("Recordemos:")
    print("  ⭐ EL SUJETO: Es quién o qué hace la acción (o de quién o qué se habla).\n")
    
    print("⭐ EL PREDICADO:")
    print("   Es lo que se dice del sujeto, la acción que el sujeto realiza o el estado en que se encuentra.")
    print("   La palabra más importante del predicado es siempre un **VERBO**.")
    print("   Para encontrar el predicado, una vez que sabes el sujeto, todo lo demás es el predicado.\n")
    
    print("⭐ EL VERBO:")
    print("   Es la palabra que indica una **ACCIÓN** (correr, saltar), un **ESTADO** (ser, estar), o un **PROCESO** (crecer, llover).")
    print("   ¡El verbo es el 'corazón' del predicado!\n")
    
    print("Ejemplos:")
    print("  - 'El perro corre rápido.'")
    print("    Sujeto: El perro")
    print("    Predicado: corre rápido. (Verbo: corre)\n")
    print("  - 'La niña lee un libro.'")
    print("    Sujeto: La niña")
    print("    Predicado: lee un libro. (Verbo: lee)\n")
    
    input("Presiona ENTER para ver más ejemplos...")

def show_examples():
    """Muestra ejemplos de oraciones identificando sujeto, predicado y verbo."""
    show_header("Ejemplos: Sujeto, Predicado y Verbo")
    
    examples = [
        ("Los niños juegan en el parque.", "Los niños", "juegan en el parque", "juegan"),
        ("Mi mamá prepara la cena.", "Mi mamá", "prepara la cena", "prepara"),
        ("El sol brilla en el cielo.", "El sol", "brilla en el cielo", "brilla"),
        ("Las flores crecen en el jardín.", "Las flores", "crecen en el jardín", "crecen"),
        ("Juan está feliz hoy.", "Juan", "está feliz hoy", "está")
    ]

    print("Analicemos estas oraciones:\n")
    for sentence, subject, predicate, verb in examples:
        print(f"Oración: '{sentence}'")
        print(f"  Sujeto: {subject.upper()}")
        print(f"  Predicado: {predicate.upper()} (Verbo: {verb.upper()})")
        print("-" * 30)
        time.sleep(1.5) # Pausa para que el estudiante procese

    print("\n¡Ahora sabes encontrar las dos partes principales de la oración y su corazón, el verbo!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def run_exercise(question, options, correct_answer_index, feedback_correct, feedback_incorrect):
    """Ejecuta un solo ejercicio de opción múltiple."""
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"  {i+1}. {option}")
    
    while True:
        try:
            choice = int(input("Elige el número de tu respuesta: "))
            if 1 <= choice <= len(options):
                if choice - 1 == correct_answer_index:
                    print(f"¡Correcto! ✅ {feedback_correct}")
                    return True
                else:
                    print(f"¡Incorrecto! ❌ {feedback_incorrect}")
                    return False
            else:
                print("Número no válido. Elige un número de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, escribe un número.")
    print("-" * 30)
    time.sleep(2) # Pausa para que el usuario lea el feedback

def start_exercises():
    """Inicia la sección de ejercicios."""
    show_header("¡A Practicar! Sujeto, Predicado y Verbo")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "En 'El pájaro vuela alto', ¿cuál es el PREDICADO?",
            "opt": ["El pájaro", "vuela alto", "pájaro"],
            "ans": 1, # Index 1 = "vuela alto"
            "fb_c": "¡Muy bien! 'Vuela alto' es lo que hace el pájaro.",
            "fb_i": "¡Casi! Recuerda, el predicado es lo que se dice del sujeto."
        },
        {
            "q": "En 'Mi hermana canta bien', ¿cuál palabra es el VERBO?",
            "opt": ["Mi", "hermana", "canta", "bien"],
            "ans": 2, # Index 2 = "canta"
            "fb_c": "¡Así es! 'Canta' es la acción.",
            "fb_i": "No. Busca la palabra que indica una acción."
        },
        {
            "q": "En 'Las flores huelen rico', ¿cuál es el PREDICADO?",
            "opt": ["Las flores", "huelen rico", "huelen"],
            "ans": 1, # Index 1 = "huelen rico"
            "fb_c": "¡Correcto! 'Huelen rico' es lo que hacen las flores.",
            "fb_i": "Piénsalo bien. Es todo lo que se dice de las flores."
        },
        {
            "q": "La palabra 'comer' es un...",
            "opt": ["Sujeto", "Predicado", "Verbo"],
            "ans": 2, # Index 2 = "Verbo"
            "fb_c": "¡Excelente! 'Comer' es una acción, es un verbo.",
            "fb_i": "Recuerda, es una palabra que indica una acción."
        },
        {
            "q": "En 'El profesor explica la lección', ¿cuál es el VERBO?",
            "opt": ["El", "profesor", "explica", "lección"],
            "ans": 2, # Index 2 = "explica"
            "fb_c": "¡Genial! 'Explica' es la acción que hace el profesor.",
            "fb_i": "Busca la palabra que dice qué hace el profesor."
        },
    ]

    for i, ex in enumerate(exercises):
        total_questions += 1
        print(f"\n--- Pregunta {i+1} de {len(exercises)} ---")
        if run_exercise(ex["q"], ex["opt"], ex["ans"], ex["fb_c"], ex["fb_i"]):
            score += 1
    
    print("\n" * 2)
    print("-" * 60)
    print("¡EJERCICIOS TERMINADOS!")
    print(f"Tu puntuación final es: {score} de {total_questions} preguntas correctas. 🎉")
    print("-" * 60)
    print("¡Sigue practicando!\n")
    input("Presiona ENTER para volver al menú principal...")

def write_sentences():
    """Permite al usuario escribir 10 oraciones propias, identificando sujeto y predicado."""
    show_header("✍️ ¡Escribe Tus Propias Oraciones! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones completas.\n")
    print("Para cada oración, piensa: ¿cuál es el SUJETO? y ¿cuál es el PREDICADO?")
    print("¡Y no olvides usar un VERBO en cada predicado!\n")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
            print("¡Bien! Ahora piensa: ¿quién/qué hace la acción (Sujeto)? Y ¿qué se dice del sujeto (Predicado)?")
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Excelente trabajo! Has practicado escribiendo y analizando oraciones.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: El Predicado y el Verbo (6º Grado)")
        print("1. Aprender la Teoría")
        print("2. Ver Ejemplos")
        print("3. Hacer Ejercicios")
        print("4. Escribir Mis Propias Oraciones")
        print("5. Salir de la Lección")
        print("-" * 60)

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            show_theory()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            start_exercises()
        elif choice == '4':
            write_sentences()
        elif choice == '5':
            print("¡Hasta pronto! Sigue aprendiendo. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
