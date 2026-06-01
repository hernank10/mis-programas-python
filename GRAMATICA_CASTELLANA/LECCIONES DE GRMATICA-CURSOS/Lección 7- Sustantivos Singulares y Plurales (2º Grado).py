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
    """Muestra la sección de teoría sobre sustantivos singulares y plurales."""
    show_header("Teoría: Sustantivos Singulares y Plurales")
    print("¡Hola de nuevo! Ya sabemos que los sustantivos son palabras que nombran.\n")
    print("Ahora vamos a aprender algo nuevo sobre ellos: ¡si nombran a UNO o a MUCHOS!\n")
    
    print("⭐ SUSTANTIVO SINGULAR:")
    print("   Es la palabra que nombra a UNA SOLA cosa, persona o animal.")
    print("   Ejemplos: un gato, una flor, un niño.\n")
    
    print("⭐ SUSTANTIVO PLURAL:")
    print("   Es la palabra que nombra a MUCHAS cosas, personas o animales.")
    print("   Para hacer un sustantivo plural, casi siempre le agregamos una 'S' o 'ES' al final.")
    print("   Ejemplos: muchos gatos (gato + s), muchas flores (flor + es), muchos niños (niño + s).\n")
    
    print("¡Es fácil! Singular es UNO, Plural es MUCHOS.\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de sustantivos singulares y plurales."""
    show_header("Ejemplos: Uno y Muchos")
    
    examples = [
        ("árbol", "árboles"),
        ("casa", "casas"),
        ("flor", "flores"),
        ("perro", "perros"),
        ("niño", "niños"),
        ("pez", "peces"),
        ("lápiz", "lápices"),
        ("mesa", "mesas"),
        ("cama", "camas"),
        ("pájaro", "pájaros")
    ]

    print("Mira cómo cambian las palabras cuando nombran a uno o a muchos:\n")
    print(f"{'SINGULAR (UNO)':<20} {'PLURAL (MUCHOS)':<20}")
    print("-" * 40)
    for singular, plural in examples:
        print(f"{singular:<20} {plural:<20}")
        time.sleep(0.5) # Pequeña pausa para que el niño pueda leer

    print("\n¡Fíjate bien en cómo terminan las palabras en plural!\n")
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
    show_header("¡A Practicar! Ejercicios de Singular y Plural")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "¿Cuál palabra está en SINGULAR?",
            "opt": ["perros", "gato", "flores"],
            "ans": 1, # Index 1 = "gato"
            "fb_c": "¡Muy bien! 'Gato' es uno solo.",
            "fb_i": "¡Casi! Recuerda, singular es UNO."
        },
        {
            "q": "¿Cuál palabra está en PLURAL?",
            "opt": ["libro", "sillas", "mesa"],
            "ans": 1, # Index 1 = "sillas"
            "fb_c": "¡Así es! 'Sillas' son muchas.",
            "fb_i": "No. Plural significa MUCHOS."
        },
        {
            "q": "Si tengo un 'pájaro', ¿cómo digo si tengo MUCHOS?",
            "opt": ["pájaros", "pájaroes", "pájara"],
            "ans": 0, # Index 0 = "pájaros"
            "fb_c": "¡Correcto! Le agregamos una 's'.",
            "fb_i": "Piensa en la regla para hacer plural."
        },
        {
            "q": "Si tengo una 'flor', ¿cómo digo si tengo MUCHAS?",
            "opt": ["flor", "floras", "flores"],
            "ans": 2, # Index 2 = "flores"
            "fb_c": "¡Excelente! 'Flores' es el plural.",
            "fb_i": "Recuerda, a veces agregamos 'es'."
        },
        {
            "q": "En la frase 'Los niños juegan', ¿cuál palabra es PLURAL?",
            "opt": ["Los", "niños", "juegan"],
            "ans": 1, # Index 1 = "niños"
            "fb_c": "¡Genial! 'Niños' son muchos.",
            "fb_i": "Esa no es. Busca la palabra que nombra a muchos."
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
    """Permite al usuario escribir 10 oraciones propias, enfocándose en singular/plural."""
    show_header("✍️ ¡Escribe Oraciones con Singular y Plural! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones.\n")
    print("¡Intenta usar sustantivos en SINGULAR y en PLURAL en tus oraciones!\n")
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
            # i -= 1 # No decrementamos 'i' para que el contador siga avanzando incluso si la oración es vacía.

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
        show_header("Lección 7: Sustantivos Singulares y Plurales (2º Grado)")
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
