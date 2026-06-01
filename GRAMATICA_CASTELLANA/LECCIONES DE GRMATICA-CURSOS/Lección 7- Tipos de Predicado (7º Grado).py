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
    """Muestra la sección de teoría sobre los tipos de predicado."""
    show_header("Teoría: Predicado Nominal y Predicado Verbal")
    print("¡Hola! Ya sabemos que la oración tiene Sujeto y Predicado, y que el verbo es clave.")
    print("Ahora, veremos que no todos los predicados son iguales. ¡Hay dos tipos principales!\n")
    
    print("⭐ 1. PREDICADO VERBAL (PV):")
    print("   Es el tipo de predicado más común.")
    print("   Su núcleo (la palabra más importante) es un VERBO que indica una ACCIÓN.")
    print("   Estos verbos no son 'ser', 'estar' o 'parecer'.")
    print("   Ejemplos de verbos en PV: correr, saltar, comer, escribir, dormir.\n")
    print("   Oración: 'El niño JUEGA en el parque.'")
    print("     Sujeto: El niño")
    print("     Predicado Verbal: JUEGA en el parque (Núcleo: JUEGA - acción)\n")
    
    print("⭐ 2. PREDICADO NOMINAL (PN):")
    print("   Su núcleo NO es una acción, sino un verbo que indica un ESTADO o una CUALIDAD del sujeto.")
    print("   Los verbos del predicado nominal son siempre: **SER, ESTAR o PARECER** (verbos copulativos).")
    print("   Después de estos verbos, generalmente hay una palabra que describe al sujeto (un adjetivo o sustantivo).\n")
    print("   Oración: 'La casa ES grande.'")
    print("     Sujeto: La casa")
    print("     Predicado Nominal: ES grande (Núcleo: ES - estado)\n")
    
    print("   Oración: 'Mi hermana ESTÁ feliz.'")
    print("     Sujeto: Mi hermana")
    print("     Predicado Nominal: ESTÁ feliz (Núcleo: ESTÁ - estado)\n")
    
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de oraciones clasificando los predicados."""
    show_header("Ejemplos: Predicado Verbal vs. Nominal")
    
    examples = [
        ("El perro ladra fuerte.", "ladra fuerte", "verbal", "ladra"),
        ("Mi abuela es muy amable.", "es muy amable", "nominal", "es"),
        ("Los estudiantes escriben un cuento.", "escriben un cuento", "verbal", "escriben"),
        ("Ella está cansada.", "está cansada", "nominal", "está"),
        ("El cielo parece gris.", "parece gris", "nominal", "parece"),
        ("Nosotros viajamos a la costa.", "viajamos a la costa", "verbal", "viajamos")
    ]

    print("Observa cómo se clasifican estos predicados:\n")
    print(f"{'ORACIÓN':<35} {'PREDICADO':<25} {'TIPO':<10} {'VERBO':<10}")
    print("-" * 80)
    for sentence, predicate, p_type, verb in examples:
        print(f"{sentence:<35} {predicate.upper():<25} {p_type.upper():<10} {verb.upper():<10}")
        time.sleep(1.5) # Pausa para que el estudiante procese

    print("\n¡Recuerda los verbos SER, ESTAR, PARECER para el predicado nominal!\n")
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
    show_header("¡A Practicar! Tipos de Predicado")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "En 'Mi primo JUEGA baloncesto', ¿qué tipo de predicado es?",
            "opt": ["Predicado Verbal", "Predicado Nominal"],
            "ans": 0, # Index 0 = "Predicado Verbal"
            "fb_c": "¡Muy bien! 'Juega' es un verbo de acción.",
            "fb_i": "¡Casi! ¿'Juega' es SER, ESTAR o PARECER?"
        },
        {
            "q": "En 'El cielo ESTÁ nublado', ¿qué tipo de predicado es?",
            "opt": ["Predicado Verbal", "Predicado Nominal"],
            "ans": 1, # Index 1 = "Predicado Nominal"
            "fb_c": "¡Así es! 'Está' es un verbo copulativo.",
            "fb_i": "No. Recuerda los verbos SER, ESTAR, PARECER."
        },
        {
            "q": "La oración 'Mi papá ES doctor' tiene un predicado...",
            "opt": ["Verbal", "Nominal"],
            "ans": 1, # Index 1 = "Nominal"
            "fb_c": "¡Correcto! 'Es' es un verbo copulativo.",
            "fb_i": "Piénsalo bien. El verbo es 'es'."
        },
        {
            "q": "En 'Los pájaros VUELAN', el predicado es...",
            "opt": ["Verbal", "Nominal"],
            "ans": 0, # Index 0 = "Verbal"
            "fb_c": "¡Excelente! 'Vuelan' es una acción.",
            "fb_i": "Inténtalo de nuevo. ¿'Vuelan' es SER, ESTAR o PARECER?"
        },
        {
            "q": "En 'El libro PARECE interesante', ¿qué tipo de predicado es?",
            "opt": ["Predicado Verbal", "Predicado Nominal"],
            "ans": 1, # Index 1 = "Predicado Nominal"
            "fb_c": "¡Genial! 'Parece' es un verbo copulativo.",
            "fb_i": "Fíjate en el verbo. ¿Es una acción o un estado?"
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
    """Permite al usuario escribir 10 oraciones propias, clasificando sus predicados."""
    show_header("✍️ ¡Escribe Oraciones y Clasifica Sus Predicados! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones completas.\n")
    print("Para cada oración, piensa: ¿su predicado es VERBAL o NOMINAL?\n")
    print("Recuerda: PREDICADO NOMINAL usa SER, ESTAR o PARECER.")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
            print("¡Muy bien! Piensa: ¿Tu predicado tiene un verbo de acción (Verbal) o SER/ESTAR/PARECER (Nominal)?")
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Excelente! Has practicado escribiendo y analizando los tipos de predicado.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Tipos de Predicado (7º Grado)")
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
