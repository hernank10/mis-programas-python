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
    print(f"🌟 {title.upper()} 🌟")
    print("-" * 60)
    print()

def show_theory():
    """Muestra la sección de teoría sobre sustantivos."""
    show_header("Teoría: ¿Qué son los Sustantivos?")
    print("¡Hola! Hoy vamos a aprender sobre unas palabras muy especiales: ¡los NOMBRES!\n")
    print("En español, a los NOMBRES les decimos SU-STAN-TI-VOS.")
    print("Un SUSTANTIVO es una palabra que usamos para nombrar:")
    print("  👧 PERSONAS (como tú, mamá, el maestro)")
    print("  🐶 ANIMALES (como perro, gato, pájaro)")
    print("  🏠 COSAS (como casa, pelota, libro, el sol)\n")
    print("¡Todo lo que tiene un nombre es un SUSTANTIVO!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de sustantivos."""
    show_header("Ejemplos de Sustantivos")
    
    examples = {
        "PERSONAS": ["niña", "papá", "maestra", "doctor", "abuela"],
        "ANIMALES": ["elefante", "pato", "conejo", "pez", "león"],
        "COSAS": ["silla", "manzana", "lápiz", "cama", "árbol"]
    }

    for category, words in examples.items():
        print(f"\n--- {category.upper()} ---")
        for word in words:
            print(f"  - {word}")
            time.sleep(0.5) # Pequeña pausa para que el niño pueda leer

    print("\n¿Ves? ¡Muchas palabras son sustantivos!\n")
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
    show_header("¡A Practicar! Ejercicios de Sustantivos")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "¿Cuál de estas palabras es un nombre de ANIMAL?",
            "opt": ["correr", "perro", "azul"],
            "ans": 1, # Index 1 = "perro"
            "fb_c": "¡Sí, 'perro' es un animal!",
            "fb_i": "¡Casi! Piensa en qué palabra nombra a un animal."
        },
        {
            "q": "¿Cuál de estas palabras nombra una COSA?",
            "opt": ["cantar", "rápido", "mesa"],
            "ans": 2, # Index 2 = "mesa"
            "fb_c": "¡Así es! 'Mesa' es una cosa.",
            "fb_i": "No. ¿Cuál de esas nombra algo que puedes tocar?"
        },
        {
            "q": "¿Cuál de estas palabras es el nombre de una PERSONA?",
            "opt": ["dormir", "mamá", "grande"],
            "ans": 1, # Index 1 = "mamá"
            "fb_c": "¡Correcto! 'Mamá' es una persona.",
            "fb_i": "Esa no es. Recuerda los nombres de personas."
        },
        {
            "q": "En la frase 'El GATO salta', ¿cuál palabra es un sustantivo?",
            "opt": ["El", "GATO", "salta"],
            "ans": 1, # Index 1 = "GATO"
            "fb_c": "¡Muy bien! 'Gato' es el nombre de un animal.",
            "fb_i": "No es esa. Un sustantivo es un nombre."
        },
        {
            "q": "En 'La niña come una MANZANA', ¿cuál es un sustantivo?",
            "opt": ["La", "niña", "come", "MANZANA"],
            "ans": 3, # Index 3 = "MANZANA"
            "fb_c": "¡Excelente! 'Manzana' es el nombre de una cosa.",
            "fb_i": "Inténtalo de nuevo. Busca la palabra que nombra algo."
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
    """Permite al usuario escribir 10 oraciones propias."""
    show_header("✍️ ¡Escribe Tus Propias Oraciones! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones usando sustantivos (nombres).\n")
    print("Recuerda: Los sustantivos nombran PERSONAS, ANIMALES o COSAS.")
    print("¡Intenta usar al menos un sustantivo en cada oración!\n")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")
            i -= 1 # Para que no cuente la oración vacía

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Muy bien! Has practicado escribiendo tus propias ideas.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Los Sustantivos (1º Grado)")
        print("1. Aprender la Teoría de los Sustantivos")
        print("2. Ver Ejemplos de Sustantivos")
        print("3. Hacer Ejercicios")
        print("4. Escribir Mis Propias Oraciones") # Nueva opción
        print("5. Salir de la Lección")
        print("-" * 60)

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            show_theory()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            start_exercises()
        elif choice == '4': # Nueva función
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
