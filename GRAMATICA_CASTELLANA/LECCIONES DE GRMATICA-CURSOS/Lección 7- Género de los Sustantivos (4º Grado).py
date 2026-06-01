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
    """Muestra la sección de teoría sobre el género de los sustantivos."""
    show_header("Teoría: Género de los Sustantivos")
    print("¡Hola! Ya sabemos que los sustantivos nombran y que pueden ser uno o muchos.")
    print("Hoy aprenderemos que los sustantivos también tienen GÉNERO: ¡pueden ser MASCULINOS o FEMENINOS!\n")
    
    print("⭐ SUSTANTIVOS MASCULINOS:")
    print("   Son los sustantivos a los que les podemos poner 'EL' o 'UN' delante.")
    print("   Muchos de ellos terminan en la letra 'O'.")
    print("   Ejemplos: EL libro, UN perro, EL niño.\n")
    
    print("⭐ SUSTANTIVOS FEMENINOS:")
    print("   Son los sustantivos a los que les podemos poner 'LA' o 'UNA' delante.")
    print("   Muchas de ellas terminan en la letra 'A'.")
    print("   Ejemplos: LA mesa, UNA flor, LA niña.\n")
    
    print("¡Recuerda! Podemos usar 'EL' o 'LA' para saber si un sustantivo es masculino o femenino.\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de sustantivos masculinos y femeninos."""
    show_header("Ejemplos: Masculino y Femenino")
    
    examples = [
        ("libro", "masculino"),
        ("mesa", "femenino"),
        ("perro", "masculino"),
        ("flor", "femenino"),
        ("niño", "masculino"),
        ("niña", "femenino"),
        ("sol", "masculino"),
        ("luna", "femenino"),
        ("árbol", "masculino"),
        ("casa", "femenino")
    ]

    print("Mira estos ejemplos y cómo usamos 'el' o 'la' para saber su género:\n")
    print(f"{'SUSTANTIVO':<15} {'ARTÍCULO':<10} {'GÉNERO':<15}")
    print("-" * 40)
    for word, gender in examples:
        article = "EL" if gender == "masculino" else "LA"
        print(f"{word:<15} {article:<10} {gender.upper():<15}")
        time.sleep(0.5) # Pequeña pausa para que el niño pueda leer

    print("\n¡Practica diciendo 'el' o 'la' antes de cada palabra!\n")
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
    show_header("¡A Practicar! Ejercicios de Género")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "¿Cuál de estas palabras es un sustantivo FEMENINO?",
            "opt": ["libro", "silla", "globo"],
            "ans": 1, # Index 1 = "silla"
            "fb_c": "¡Muy bien! Decimos 'LA silla'.",
            "fb_i": "¡Casi! Prueba a decir 'el' o 'la' antes de cada palabra."
        },
        {
            "q": "¿Cuál de estas palabras es un sustantivo MASCULINO?",
            "opt": ["ventana", "computadora", "teléfono"],
            "ans": 2, # Index 2 = "teléfono"
            "fb_c": "¡Así es! Decimos 'EL teléfono'.",
            "fb_i": "No. Piensa en qué artículo (el/la) usas."
        },
        {
            "q": "La palabra 'mesa' es...",
            "opt": ["Masculino", "Femenino"],
            "ans": 1, # Index 1 = "Femenino"
            "fb_c": "¡Correcto! Decimos 'LA mesa'.",
            "fb_i": "¿Decimos 'el mesa' o 'la mesa'?"
        },
        {
            "q": "La palabra 'sol' es...",
            "opt": ["Masculino", "Femenino"],
            "ans": 0, # Index 0 = "Masculino"
            "fb_c": "¡Excelente! Decimos 'EL sol'.",
            "fb_i": "Inténtalo de nuevo. Piensa en el artículo."
        },
        {
            "q": "En 'LA ciudad es grande', ¿cuál es el GÉNERO de 'ciudad'?",
            "opt": ["Masculino", "Femenino"],
            "ans": 1, # Index 1 = "Femenino"
            "fb_c": "¡Genial! 'La ciudad' nos dice que es femenino.",
            "fb_i": "Fíjate en la palabra pequeña que va antes de 'ciudad'."
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
    """Permite al usuario escribir 10 oraciones propias, usando sustantivos masculinos y femeninos."""
    show_header("✍️ ¡Escribe Oraciones con Sustantivos Masculinos y Femeninos! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones.\n")
    print("¡Intenta usar sustantivos MASCULINOS (con 'el' o 'un') y FEMENINOS (con 'la' o 'una')!\n")
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
        show_header("Lección 7: Género de los Sustantivos (4º Grado)")
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
