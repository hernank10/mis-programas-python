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
    """Muestra la sección de teoría sobre OD y OI."""
    show_header("Teoría: Objeto Directo y Objeto Indirecto")
    print("¡Hola! Ya sabemos que el predicado verbal tiene un verbo de acción.")
    print("Ahora, veremos cómo los verbos se conectan con otras palabras: ¡los COMPLEMENTOS!\n")
    
    print("⭐ 1. OBJETO DIRECTO (OD):")
    print("   Es la persona, animal o cosa que RECIBE DIRECTAMENTE la acción del verbo.")
    print("   Para encontrarlo, puedes preguntar al verbo: '¿QUÉ?' o '¿A QUIÉN?'")
    print("   Se puede sustituir por los pronombres 'LO', 'LA', 'LOS', 'LAS'.\n")
    print("   Ejemplo: 'María come UNA MANZANA.'")
    print("     Pregunta: ¿QUÉ come María? -> UNA MANZANA (OD)")
    print("     Sustitución: María LA come.\n")
    
    print("   Ejemplo: 'Yo veo A PEDRO.'")
    print("     Pregunta: ¿A QUIÉN veo yo? -> A PEDRO (OD)")
    print("     Sustitución: Yo LO veo.\n")
    
    print("⭐ 2. OBJETO INDIRECTO (OI):")
    print("   Es la persona, animal o cosa que RECIBE EL BENEFICIO o DAÑO de la acción del verbo.")
    print("   Para encontrarlo, puedes preguntar al verbo: '¿A QUIÉN?' o '¿PARA QUIÉN?'")
    print("   Se puede sustituir por los pronombres 'LE', 'LES'.")
    print("   ¡Ojo! A veces el OD y OI pueden usar 'a quién', pero el OI siempre es quien 'recibe' el efecto indirecto.\n")
    print("   Ejemplo: 'Ella da un regalo A SU MADRE.'")
    print("     Pregunta: ¿A QUIÉN da un regalo? -> A SU MADRE (OI)")
    print("     Sustitución: Ella LE da un regalo.\n")
    
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de oraciones identificando OD y OI."""
    show_header("Ejemplos: Encontrando OD y OI")
    
    examples = [
        ("Mi hermano lee un libro.", "un libro", None),                  # OD
        ("Compré flores para mi abuela.", None, "para mi abuela"),       # OI
        ("El niño patea la pelota.", "la pelota", None),                # OD
        ("Escribí una carta a mi amigo.", "una carta", "a mi amigo"),    # OD y OI
        ("Vimos a Juan en el parque.", "a Juan", None),                 # OD
        ("Dio dulces a los niños.", "dulces", "a los niños")            # OD y OI
    ]

    print("Analicemos estas oraciones e identifiquemos sus complementos:\n")
    for sentence, od, oi in examples:
        print(f"Oración: '{sentence}'")
        if od:
            print(f"  Objeto Directo (OD): {od.upper()} (¿Qué/A quién {sentence.split(od)[0].strip().split()[-1]}?)") # Simplificado para consola
        if oi:
            print(f"  Objeto Indirecto (OI): {oi.upper()} (¿A quién/Para quién {sentence.split(oi)[0].strip().split()[-1]}?)") # Simplificado
        if not od and not oi:
            print("  No hay OD ni OI claros en este ejemplo.")
        print("-" * 30)
        time.sleep(2) # Pausa para que el estudiante procese

    print("\n¡Practica haciendo las preguntas '¿Qué?', '¿A quién?', '¿Para quién?'!\n")
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
    show_header("¡A Practicar! Objeto Directo y Objeto Indirecto")
    score = 0
    total_questions = 0

    exercises = [
        {
            "q": "En 'Mi primo lee UN LIBRO', ¿cuál es el Objeto Directo?",
            "opt": ["Mi primo", "lee", "UN LIBRO"],
            "ans": 2, # Index 2 = "UN LIBRO"
            "fb_c": "¡Muy bien! 'Un libro' es lo que lee.",
            "fb_i": "¡Casi! Pregunta: ¿QUÉ lee mi primo?"
        },
        {
            "q": "En 'Le doy dulces A MI HERMANA', ¿cuál es el Objeto Indirecto?",
            "opt": ["dulces", "A MI HERMANA", "doy"],
            "ans": 1, # Index 1 = "A MI HERMANA"
            "fb_c": "¡Así es! 'A mi hermana' recibe el beneficio.",
            "fb_i": "No. Pregunta: ¿A QUIÉN le doy dulces?"
        },
        {
            "q": "En 'Compré un regalo PARA MI PAPÁ', 'un regalo' es...",
            "opt": ["Objeto Indirecto", "Objeto Directo", "Sujeto"],
            "ans": 1, # Index 1 = "Objeto Directo"
            "fb_c": "¡Correcto! 'Un regalo' es lo que compré.",
            "fb_i": "¿QUÉ compré?"
        },
        {
            "q": "En 'El profesor explica la lección A LOS ESTUDIANTES', 'A LOS ESTUDIANTES' es...",
            "opt": ["Objeto Directo", "Objeto Indirecto"],
            "ans": 1, # Index 1 = "Objeto Indirecto"
            "fb_c": "¡Excelente! 'A los estudiantes' reciben el beneficio de la explicación.",
            "fb_i": "Piensa: ¿A QUIÉN explica la lección?"
        },
        {
            "q": "La oración 'Ella canta UNA CANCIÓN' tiene Objeto Directo. ¿Cuál es?",
            "opt": ["Ella", "canta", "UNA CANCIÓN"],
            "ans": 2, # Index 2 = "UNA CANCIÓN"
            "fb_c": "¡Genial! 'Una canción' es lo que ella canta.",
            "fb_i": "Busca lo que ella canta."
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
    """Permite al usuario escribir 10 oraciones propias, usando OD y OI."""
    show_header("✍️ ¡Escribe Oraciones con Objeto Directo e Indirecto! ✍️")
    print("Ahora es tu turno. Escribe 10 oraciones completas.\n")
    print("¡Intenta usar un Objeto Directo (OD) o un Objeto Indirecto (OI) en cada una!")
    print("OD: ¿Qué? o ¿A quién? - OI: ¿A quién? o ¿Para quién? (recibe el beneficio)\n")
    print("Cuando termines una oración, presiona ENTER. Si quieres terminar antes, escribe 'listo'.\n")

    sentences = []
    for i in range(1, 11):
        sentence = input(f"Oración {i}: ").strip()
        if sentence.lower() == 'listo':
            break
        if sentence: # Solo guarda si no está vacía
            sentences.append(sentence)
            print("¡Muy bien! Piensa: ¿Qué o a quién recibe la acción directamente? (OD)")
            print("¿A quién o para quién es el beneficio? (OI)")
        else:
            print("Oración vacía. Intenta de nuevo o escribe 'listo'.")

    print("\n--- Tus Oraciones ---")
    if sentences:
        for i, s in enumerate(sentences):
            print(f"{i+1}. {s}")
        print("\n¡Excelente! Has practicado escribiendo y pensando en los objetos directo e indirecto.\n")
    else:
        print("No escribiste ninguna oración esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Objeto Directo y Objeto Indirecto (8º Grado)")
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
