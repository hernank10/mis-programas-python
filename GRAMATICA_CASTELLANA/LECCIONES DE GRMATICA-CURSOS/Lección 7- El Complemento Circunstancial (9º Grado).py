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
    """Muestra la sección de teoría sobre el Complemento Circunstancial."""
    show_header("Teoría: El Complemento Circunstancial (CC)")
    print("¡Hola! Ya hemos aprendido sobre el Sujeto, el Predicado, y los Objetos Directo e Indirecto.")
    print("Ahora, vamos a conocer otro compañero del verbo: ¡el Complemento Circunstancial!\n")
    
    print("⭐ COMPLEMENTO CIRCUNSTANCIAL (CC):")
    print("   Es la parte de la oración que nos da información sobre las **CIRCUNSTANCIAS** en las que ocurre la acción del verbo.")
    print("   Nos dice: ¿CÓMO?, ¿CUÁNDO?, ¿DÓNDE?, ¿CON QUÉ?, ¿POR QUÉ?, ¿CUÁNTO?, etc.\n")
    print("   Se puede quitar de la oración sin que esta pierda su sentido principal (no siempre, pero es una pista).\n")
    
    print("Tipos de Complemento Circunstancial más comunes:")
    print("  🔹 CC. de LUGAR: Indica dónde ocurre la acción. Pregunta: ¿DÓNDE?")
    print("     Ejemplo: 'Comimos en el restaurante.' -> CC. de LUGAR: EN EL RESTAURANTE\n")
    
    print("  🔹 CC. de TIEMPO: Indica cuándo ocurre la acción. Pregunta: ¿CUÁNDO?")
    print("     Ejemplo: 'Llegaremos mañana.' -> CC. de TIEMPO: MAÑANA\n")
    
    print("  🔹 CC. de MODO: Indica cómo ocurre la acción. Pregunta: ¿CÓMO?")
    print("     Ejemplo: 'Escribe rápidamente.' -> CC. de MODO: RÁPIDAMENTE\n")
    
    print("  🔹 CC. de CANTIDAD: Indica cuánto ocurre la acción. Pregunta: ¿CUÁNTO?")
    print("     Ejemplo: 'Estudió mucho.' -> CC. de CANTIDAD: MUCHO\n")
    
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de oraciones identificando CC de Lugar, Tiempo, Modo y Cantidad."""
    show_header("Ejemplos: Tipos de Complementos Circunstanciales")
    
    examples = [
        ("Mis amigos juegan en el parque.", "en el parque", "LUGAR"),
        ("Saldremos de viaje el viernes.", "el viernes", "TIEMPO"),
        ("Ella canta muy bien.", "muy bien", "MODO"),
        ("Mi hermano comió demasiado.", "demasiado", "CANTIDAD"),
        ("Estudiamos en la biblioteca por la tarde.", "en la biblioteca", "LUGAR"),
        ("Estudiamos en la biblioteca por la tarde.", "por la tarde", "TIEMPO"),
        ("Habla en voz baja.", "en voz baja", "MODO")
    ]

    print("Analicemos estas oraciones e identifiquemos sus Complementos Circunstanciales:\n")
    print(f"{'ORACIÓN':<40} {'COMPLEMENTO CIRCUNSTANCIAL':<30} {'TIPO':<10}")
    print("-" * 80)
    for sentence, cc_phrase, cc_type in examples:
        print(f"{sentence:<40} {cc_phrase.upper():<30} {cc_type.upper():<10}")
        print(f"  (Pregunta: ¿{cc_type} {sentence.split(cc_phrase)[0].strip()}?)\n")
        time.sleep(2) # Pausa para que el estudiante procese

    print("\n¡Los CC nos dan muchos detalles sobre la acción!\n")
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
    show_header("¡A Practicar! El Complemento Circunstancial")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "En 'El niño corre RÁPIDAMENTE', ¿qué tipo de CC es 'RÁPIDAMENTE'?",
            "opt": ["Lugar", "Tiempo", "Modo", "Cantidad"],
            "ans": 2, # Index 2 = "Modo"
            "fb_c": "¡Muy bien! Indica CÓMO corre.",
            "fb_i": "¡Casi! Pregunta: ¿CÓMO corre el niño?"
        },
        {
            "q": "En 'Estudiamos EN CASA', ¿cuál es el CC. de LUGAR?",
            "opt": ["Estudiamos", "EN CASA", "casa"],
            "ans": 1, # Index 1 = "EN CASA"
            "fb_c": "¡Así es! Indica DÓNDE estudiamos.",
            "fb_i": "No. Pregunta: ¿DÓNDE estudiamos?"
        },
        {
            "q": "En 'Llegamos AYER', ¿qué tipo de CC es 'AYER'?",
            "opt": ["Lugar", "Tiempo", "Modo"],
            "ans": 1, # Index 1 = "Tiempo"
            "fb_c": "¡Correcto! Indica CUÁNDO llegamos.",
            "fb_i": "Piénsalo bien. 'Ayer' se refiere a...?"
        },
        {
            "q": "En 'Mi hermana comió MUCHO', ¿qué tipo de CC es 'MUCHO'?",
            "opt": ["Lugar", "Modo", "Cantidad"],
            "ans": 2, # Index 2 = "Cantidad"
            "fb_c": "¡Excelente! Indica CUÁNTO comió.",
            "fb_i": "Inténtalo de nuevo. ¿Qué pregunta le harías al verbo?"
        },
        {
            "q": "En 'Conduce con cuidado', 'con cuidado' es un CC. de...",
            "opt": ["Lugar", "Tiempo", "Modo"],
            "ans": 2, # Index 2 = "Modo"
            "fb_c": "¡Genial! Indica CÓMO conduce.",
            "fb_i": "Fíjate en la pregunta: ¿CÓMO conduce?"
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
    """Permite al usuario escribir 10 oraciones propias, usando CC."""
    show_header("✍️ ¡Escribe Oraciones con Complementos Circunstanciales! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones completas.\n")
    print("¡Intenta agregar Complementos Circunstanciales (de lugar, tiempo, modo o cantidad) a tus oraciones!\n")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
            print("¡Muy bien! Piensa: ¿Tu oración dice cuándo, dónde, cómo o cuánto ocurrió la acción?")
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Excelente! Has practicado escribiendo y añadiendo detalles a tus oraciones.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: El Complemento Circunstancial (9º Grado)")
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
