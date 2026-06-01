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
    """Muestra la sección de teoría sobre el sujeto."""
    show_header("Teoría: El Sujeto en la Oración")
    print("¡Hola! Ya sabemos mucho de los sustantivos. Ahora, vamos a ver cómo los usamos en las oraciones.\n")
    
    print("Cada oración tiene dos partes muy importantes:")
    print("1. ⭐ EL SUJETO:")
    print("   Es la persona, animal o cosa de quien se habla en la oración.")
    print("   También es quien realiza la acción que dice el verbo.")
    print("   Para encontrar el sujeto, podemos preguntar: '¿QUIÉN?' o '¿QUÉ?' hace la acción.\n")
    
    print("2. ⭐ EL PREDICADO:")
    print("   Es lo que se dice del sujeto, o la acción que el sujeto realiza.")
    print("   (¡Lo veremos con más detalle en otra lección!)\n")
    
    print("Hoy nos concentraremos en encontrar el SUJETO. ¡Es casi siempre un sustantivo!\n")
    print("Ejemplos:")
    print("  - 'El perro corre rápido.'  -> ¿QUIÉN corre? EL PERRO. (Sujeto)")
    print("  - 'La niña lee un libro.' -> ¿QUIÉN lee? LA NIÑA. (Sujeto)")
    print("  - 'Las flores son bonitas.' -> ¿QUÉ son bonitas? LAS FLORES. (Sujeto)\n")
    
    input("Presiona ENTER para ver más ejemplos...")

def show_examples():
    """Muestra ejemplos de oraciones identificando el sujeto."""
    show_header("Ejemplos: Encontrando el Sujeto")
    
    examples = [
        ("El sol brilla mucho.", "El sol"),
        ("Mi mamá cocina delicioso.", "Mi mamá"),
        ("Los pájaros cantan en el árbol.", "Los pájaros"),
        ("La pelota es redonda.", "La pelota"),
        ("Juan juega fútbol.", "Juan"),
        ("Las estrellas aparecen de noche.", "Las estrellas"),
        ("El gato duerme en el sofá.", "El gato")
    ]

    print("En cada oración, el SUJETO es la parte que está en MAYÚSCULAS:\n")
    for sentence, subject in examples:
        highlighted_sentence = sentence.replace(subject, subject.upper())
        print(f"  - {highlighted_sentence}")
        print(f"    Pregunta: ¿QUIÉN/QUÉ {sentence.split(subject)[1].strip()}? -> {subject.upper()}")
        time.sleep(1) # Pequeña pausa para que el niño pueda leer

    print("\n¡Recuerda preguntar '¿Quién?' o '¿Qué?' para encontrar el sujeto!\n")
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
    show_header("¡A Practicar! Encontrando el Sujeto")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "En la oración 'El pájaro vuela alto', ¿cuál es el SUJETO?",
            "opt": ["El", "pájaro", "vuela alto"],
            "ans": 1, # Index 1 = "pájaro"
            "fb_c": "¡Muy bien! 'El pájaro' es quien vuela.",
            "fb_i": "¡Casi! Pregunta: ¿QUIÉN vuela alto?"
        },
        {
            "q": "En la oración 'Mi hermana canta bien', ¿cuál es el SUJETO?",
            "opt": ["Mi hermana", "canta bien", "bien"],
            "ans": 0, # Index 0 = "Mi hermana"
            "fb_c": "¡Así es! 'Mi hermana' es quien canta.",
            "fb_i": "No. ¿QUIÉN canta bien?"
        },
        {
            "q": "En la oración 'Las flores huelen rico', ¿cuál es el SUJETO?",
            "opt": ["Las flores", "huelen rico", "rico"],
            "ans": 0, # Index 0 = "Las flores"
            "fb_c": "¡Correcto! 'Las flores' son las que huelen rico.",
            "fb_i": "¿QUÉ huelen rico?"
        },
        {
            "q": "En 'El carro rojo es nuevo', ¿cuál es el SUJETO?",
            "opt": ["El carro rojo", "es nuevo", "nuevo"],
            "ans": 0, # Index 0 = "El carro rojo"
            "fb_c": "¡Excelente! 'El carro rojo' es de quien se habla.",
            "fb_i": "Piensa: ¿QUÉ es nuevo?"
        },
        {
            "q": "En 'Los niños juegan en el parque', ¿cuál es el SUJETO?",
            "opt": ["Los niños", "juegan", "en el parque"],
            "ans": 0, # Index 0 = "Los niños"
            "fb_c": "¡Genial! 'Los niños' son quienes juegan.",
            "fb_i": "Busca quién realiza la acción de jugar."
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
    """Permite al usuario escribir 10 oraciones propias, identificando el sujeto."""
    show_header("✍️ ¡Escribe Tus Propias Oraciones y Encuentra el Sujeto! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones completas.\n")
    print("Después de cada oración, intenta pensar: ¿cuál es el SUJETO en lo que escribiste?\n")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
            # Aquí podríamos añadir una pequeña interacción para que el niño intente identificar el sujeto
            # Pero para mantener la simplicidad de la consola, solo le pedimos que "piense" en ello.
            print("¡Muy bien! Ahora piensa: ¿quién o qué hace la acción en esta oración?")
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Excelente trabajo! Has practicado escribiendo y pensando en el sujeto.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: El Sujeto en la Oración (5º Grado)")
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
