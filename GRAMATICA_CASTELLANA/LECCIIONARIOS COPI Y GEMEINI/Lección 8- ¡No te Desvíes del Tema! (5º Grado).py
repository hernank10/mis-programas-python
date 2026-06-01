import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 75)
    print(f"🎯 {title.upper()} 🎯")
    print("=" * 75)
    print()

def show_introduction():
    """Introduce los conceptos de desviar el tema y atacar a la persona."""
    show_header("Introducción: Habla de la IDEA, No te Desvíes")
    print("¡Hola, futuros argumentadores! 🚀")
    print("Hemos aprendido a pensar con claridad y a buscar razones reales.")
    print("Hoy vamos a aprender a no caer en dos trucos que a veces usan las personas para evitar hablar claro:\n")
    
    print("1. 🚩 **'Cambiar el Tema' (Pista Falsa):**")
    print("   Imagina que le preguntas a tu amigo: '¿Por qué no hiciste tu tarea?'")
    print("   Y él responde: '¡Pero mira qué bonito día hace! ¿Vamos a jugar fútbol?'")
    print("   ¿Te respondió la pregunta? ¡No! Cambió el tema para no hablar de la tarea.")
    print("   Es como una **pista falsa** que nos lleva a otro lugar.\n")
    
    print("2. 😠 **'Atacar a la Persona, No a la IDEA':**")
    print("   Imagina que dices: 'Creo que deberíamos pintar el mural de la escuela de color azul.'")
    print("   Y alguien responde: '¡Tú siempre dices cosas raras! No sabes nada de pintar.'")
    print("   ¿Está hablando de la idea (pintar de azul) o está hablando mal de ti? ¡De ti!")
    print("   Esto no ayuda a decidir el color del mural. Siempre debemos hablar de las IDEAS.\n")
    
    print("¡Aprenderemos a no desviarnos y a hablar de lo que importa!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de desviar el tema y atacar a la persona."""
    show_header("Ejemplos: ¿Desvío o Ataque a la Persona?")
    
    examples = [
        {"text": "Maestra, ¿por qué la tarea de matemáticas fue tan difícil? Alumno: '¡Pero el recreo estuvo muy divertido hoy!'", 
         "type": "DESVIO", "explanation": "El alumno cambió el tema para no hablar de la tarea difícil."},
        {"text": "Juan dice: 'Deberíamos organizar una limpieza del parque.' Pedro: 'Juan siempre anda con esas ideas aburridas, ¡él es un aburrido!'", 
         "type": "ATAQUE", "explanation": "Pedro no habló de la idea de limpiar el parque, habló mal de Juan."},
        {"text": "Mamá: '¿Ya te lavaste las manos?' Hijo: '¡Mira qué grande está el perro del vecino!'", 
         "type": "DESVIO", "explanation": "El hijo desvió la atención al perro para no responder sobre las manos."},
        {"text": "Ana: 'Creo que el personaje principal del cuento no fue muy valiente.' Carlos: 'Tú no sabes de cuentos, ¡siempre te duermes cuando leen!'", 
         "type": "ATAQUE", "explanation": "Carlos no habló de la opinión de Ana sobre el personaje, la atacó a ella."},
        {"text": "Amigo 1: '¿Por qué llegaste tarde al partido?' Amigo 2: '¡Qué buen gol metimos al final del juego!'", 
         "type": "DESVIO", "explanation": "El Amigo 2 cambió el tema al gol para no explicar por qué llegó tarde."},
        {"text": "Sofía: 'Este camino es más corto para llegar a casa.' Leo: '¿Qué sabes tú? ¡Si eres el más despistado de todos!'", 
         "type": "ATAQUE", "explanation": "Leo no discutió si el camino era corto, atacó a Sofía por ser despistada."},
    ]

    print("Lee cada diálogo y piensa si alguien 'desvió el tema' o 'atacó a la persona'.\n")
    for i, ex in enumerate(examples):
        print(f"\n--- Diálogo {i+1} ---")
        print(f"'{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "DESVIO":
            print(f"¡Es un DESVÍO DE TEMA! 🚩 {ex['explanation']}\n")
        else: # ATAQUE
            print(f"¡Es un ATAQUE A LA PERSONA! 😠 {ex['explanation']}\n")
        time.sleep(3)
        print("=" * 40)

    print("\n¡Ahora es tu turno de descubrir estos trucos!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_tactic():
    """Juego de identificar si se desvía el tema o se ataca a la persona."""
    show_header("Juego 1: ¡El Detector de Trucos!")
    print("Te mostraré una conversación. Dime si alguien 'DESVIÓ EL TEMA' (D) o 'ATACÓ A LA PERSONA' (A).\n")
    print("Escribe 'D' para Desvío o 'A' para Ataque a la Persona.\n")

    questions = [
        {"text": "Carlos: 'Creo que el perro necesita más paseos.' Sofía: '¡Pero si tú siempre llegas tarde a todo!'", 
         "answer": "A", "explanation": "Sofía atacó a Carlos por sus tardanzas, no habló de los paseos del perro."},
        {"text": "Papá: '¿Ya terminaste de organizar tu cuarto?' Hija: '¡Papá, mira el video divertido que encontré en internet!'", 
         "answer": "D", "explanation": "La hija desvió la conversación al video para evitar el tema del cuarto."},
        {"text": "Maestra: '¿Por qué no entregaste tu proyecto?' Alumno: '¡Qué bonita camisa tiene puesta hoy, maestra!'", 
         "answer": "D", "explanation": "El alumno cambió el tema para no hablar del proyecto no entregado."},
        {"text": "Hermana: 'No deberías comer tantas galletas, son malas para los dientes.' Hermano: '¡Tú siempre das consejos, y no sabes nada!'", 
         "answer": "A", "explanation": "El hermano atacó a su hermana en lugar de discutir si las galletas eran malas."},
        {"text": "Entrenador: 'Necesitamos practicar más para el partido.' Jugador: '¿Viste el partido de ayer? ¡Fue increíble!'", 
         "answer": "D", "explanation": "El jugador desvió la atención al partido de ayer en lugar de la práctica."},
        {"text": "Amiga 1: 'Ese juego es difícil.' Amiga 2: '¡Tú eres muy lenta para los juegos, por eso te parece difícil!'", 
         "answer": "A", "explanation": "Amiga 2 atacó la habilidad de Amiga 1, no la dificultad del juego."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Diálogo: '{q['text']}'")
        
        while True:
            user_input = input("¿'DESVÍO' (D) o 'ATAQUE' (A)?: ").upper().strip()
            if user_input in ['D', 'A']:
                break
            else:
                print("Por favor, escribe 'D' o 'A'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(3)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detector de trucos! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_stay_on_topic():
    """Juego de mantenerse en el tema o defender la idea, no atacar."""
    show_header("Juego 2: ¡Mantente en la Idea!")
    print("Te daré una situación donde alguien usa un 'truco'.")
    print("Tu misión es responder de una forma que **vuelva al tema** o **hable de la idea, no de la persona**.\n")

    situations = [
        {"original": "Maestra: '¿Por qué no has terminado tu lectura?' Alumno: '¡La ventana está abierta y hace mucho ruido!'", 
         "correct_response": "Entiendo, pero ¿me puedes decir por qué no terminaste la lectura?", 
         "hint": "El alumno desvió. ¿Cómo le pides que vuelva al tema de la lectura?"},
        {"original": "Amigo A: 'No me gustó mucho la película.' Amigo B: '¡Tú siempre criticas todo, nunca te gusta nada!'", 
         "correct_response": "¿Por qué no te gustó la película? Hablemos de eso, no de mí.", 
         "hint": "Amigo B atacó a la persona. ¿Cómo le pides que hable de la película?"},
        {"original": "Mamá: '¿Dónde pusiste tus zapatos?' Hijo: '¡Mamá, mira mi dibujo nuevo!'", 
         "correct_response": "Qué bonito dibujo, pero ¿dónde están tus zapatos?", 
         "hint": "El hijo desvió. ¿Cómo le recuerdas los zapatos sin ignorar su dibujo?"},
        {"original": "Compañero: 'No creo que esa sea la mejor idea para el proyecto.' Tú: '¡Tú nunca tienes buenas ideas para nada!'", 
         "correct_response": "Explícame por qué crees que no es la mejor idea, así lo podemos mejorar.", 
         "hint": "Tú atacaste al compañero. ¿Cómo vuelves a hablar de la idea del proyecto?"},
    ]
    
    random.shuffle(situations)
    num_questions = 3 # Limitamos a 3

    for i in range(num_questions):
        s = situations[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Situación: '{s['original']}'")
        print(f"Pista: {s['hint']}")
        
        user_response = input("Escribe cómo responderías para mantener el tema o hablar de la idea: ").strip()
        
        print(f"\nTu respuesta: '{user_response}'")
        print(f"Una forma de hacerlo: '{s['correct_response']}'")
        print("\n¡Excelente! ¡Has aprendido a mantener el tema y a hablar de las ideas! 🎉")
        time.sleep(4)
    
    print(f"\nJuego terminado. ¡Has aprendido a no desviarte y a hablar de lo que importa!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_trick_example():
    """Permite al usuario crear su propio ejemplo de desvío o ataque y cómo resolverlo."""
    show_header("✍️ ¡Crea Tus Propios Trucos y Soluciones! ✍️")
    print("Vamos a crear una conversación donde alguien 'desvíe el tema' o 'ataque a la persona'.")
    print("Luego, tú dirás cómo responderías para arreglarlo y mantener la conversación justa.\n")

    while True:
        original_dialogue = input("1. Escribe un diálogo corto con un 'truco' (desvío o ataque): ").strip()
        if original_dialogue:
            break
        else:
            print("Por favor, escribe un diálogo.")
    
    print(f"\nTu diálogo con el 'truco': '{original_dialogue}'")

    while True:
        your_solution = input("2. Ahora, ¿cómo responderías para volver al tema o hablar de la idea (no de la persona)?: ").strip()
        if your_solution:
            break
        else:
            print("Por favor, escribe tu solución.")

    print("\n--- ¡Tu Ejemplo Creado! ---")
    print(f"Situación con truco: '{original_dialogue}' 🚩😠")
    print(f"Tu solución para una conversación justa: '{your_solution}' ✅")
    print("\n¡Qué buen trabajo! ¡Eres muy listo para detectar y corregir los trucos de la conversación! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¡No te Desvíes del Tema! (5º Grado)")
        print("1. Introducción: Habla de la IDEA, No te Desvíes")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡El Detector de Trucos!")
        print("4. Jugar: ¡Mantente en la Idea!")
        print("5. ✍️ ¡Crea Tus Propios Trucos y Soluciones! ✍️")
        print("6. Salir de la Lección")
        print("=" * 75)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_tactic()
        elif choice == '4':
            game_stay_on_topic()
        elif choice == '5':
            create_own_trick_example()
        elif choice == '6':
            print("¡Adiós! Recuerda siempre hablar de la idea y no desviarte. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
