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
    """Muestra la sección de teoría sobre sustantivos comunes y propios."""
    show_header("Teoría: Sustantivos Comunes y Propios")
    print("¡Hola! Hoy vamos a aprender otra forma de clasificar a los sustantivos (los nombres).\n")
    
    print("⭐ SUSTANTIVOS COMUNES:")
    print("   Son los nombres que usamos para cosas, personas o animales EN GENERAL.")
    print("   No nombran a uno solo en especial, sino a cualquiera de su tipo.")
    print("   Siempre se escriben con LETRA MINÚSCULA al principio (a menos que empiecen una oración).")
    print("   Ejemplos: perro, ciudad, niña, río, montaña.\n")
    
    print("⭐ SUSTANTIVOS PROPIOS:")
    print("   Son los nombres que usamos para nombrar a UNA SOLA persona, animal o lugar ESPECÍFICO.")
    print("   Siempre se escriben con LETRA MAYÚSCULA al principio, ¡no importa dónde estén en la oración!")
    print("   Ejemplos: Fido (nombre de un perro), Bogotá (nombre de una ciudad), Sofía (nombre de una niña), Magdalena (nombre de un río), Everest (nombre de una montaña).\n")
    
    print("¡Recuerda! COMUNES para cosas en general (minúscula), PROPIOS para uno en especial (MAYÚSCULA).\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de sustantivos comunes y propios."""
    show_header("Ejemplos: Comunes y Propios")
    
    examples = [
        ("niña", "Sofía"),
        ("perro", "Max"),
        ("ciudad", "Madrid"),
        ("río", "Amazonas"),
        ("montaña", "Chimborazo"),
        ("país", "Colombia"),
        ("océano", "Pacífico"),
        ("escuela", "Colegio Las Acacias")
    ]

    print("Mira la diferencia entre un sustantivo común y su propio:\n")
    print(f"{'COMÚN (minúscula)':<25} {'PROPIO (MAYÚSCULA)':<30}")
    print("-" * 55)
    for comun, propio in examples:
        print(f"{comun:<25} {propio:<30}")
        time.sleep(0.5) # Pequeña pausa para que el niño pueda leer

    print("\n¡Fíjate bien en la letra grande de los sustantivos propios!\n")
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
    show_header("¡A Practicar! Ejercicios de Comunes y Propios")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "¿Cuál palabra es un sustantivo PROPIO?",
            "opt": ["casa", "perro", "Juan"],
            "ans": 2, # Index 2 = "Juan"
            "fb_c": "¡Muy bien! 'Juan' es el nombre de una persona específica.",
            "fb_i": "¡Casi! Recuerda, los propios nombran a UNO en especial y van con MAYÚSCULA."
        },
        {
            "q": "¿Cuál palabra es un sustantivo COMÚN?",
            "opt": ["María", "colegio", "México"],
            "ans": 1, # Index 1 = "colegio"
            "fb_c": "¡Así es! 'Colegio' es un nombre general.",
            "fb_i": "No. Los comunes nombran cosas en general y van con minúscula."
        },
        {
            "q": "Si hablo de 'la CIUDAD', ¿es un sustantivo común o propio?",
            "opt": ["Común", "Propio"],
            "ans": 0, # Index 0 = "Común"
            "fb_c": "¡Correcto! 'Ciudad' es un nombre general.",
            "fb_i": "Piénsalo bien. ¿Nombra a cualquier ciudad o a una específica?"
        },
        {
            "q": "La palabra 'Colombia' es un sustantivo...",
            "opt": ["común", "propio"],
            "ans": 1, # Index 1 = "propio"
            "fb_c": "¡Excelente! 'Colombia' es el nombre de un país específico.",
            "fb_i": "Recuerda la regla de las mayúsculas."
        },
        {
            "q": "En la frase 'Mi ABUELA se llama Ana', ¿cuál es el sustantivo COMÚN?",
            "opt": ["ABUELA", "Ana"],
            "ans": 0, # Index 0 = "ABUELA"
            "fb_c": "¡Genial! 'Abuela' es un nombre común.",
            "fb_i": "No es esa. Busca el nombre general."
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
    """Permite al usuario escribir 10 oraciones propias, usando comunes y propios."""
    show_header("✍️ ¡Escribe Oraciones con Sustantivos Comunes y Propios! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones.\n")
    print("¡Intenta usar sustantivos COMUNES y PROPIOS en tus oraciones!")
    print("Recuerda: Los PROPIOS siempre empiezan con MAYÚSCULA.\n")
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
        show_header("Lección 7: Sustantivos Comunes y Propios (3º Grado)")
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
