import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 90)
    print(f"🎭 {title.upper()} 🎭")
    print("=" * 90)
    print()

def show_introduction():
    """Introduce los conceptos de apelación a la emoción, apelación a la ignorancia y hombre de paja."""
    show_header("Introducción: Analizando la Persuasión y los Argumentos Distorsionados")
    print("¡Hola, analistas de la comunicación! 🧐")
    print("Hemos avanzado mucho en el pensamiento crítico. Hoy descubriremos cómo se intenta influir en nosotros de formas más complejas:\n")
    
    print("1. ❤️‍🩹 **'Jugar con tus Sentimientos' (Apelación a la Emoción):**")
    print("   Imagina un anuncio de un perrito triste en la calle, pidiendo que dones dinero.")
    print("   ¿Te están dando razones lógicas o están usando la tristeza para que dones?")
    print("   Se busca que actúes por cómo te sientes, no por la lógica de la situación.\n")
    
    print("2. ❓ **'Porque No se Ha Probado' (Apelación a la Ignorancia):**")
    print("   Alguien dice: 'Nadie ha podido probar que los extraterrestres no existen, así que deben existir.'")
    print("   ¿Es eso una prueba real? ¡No! Que no se haya probado lo contrario, no lo hace verdad.")
    print("   La falta de pruebas no es una prueba en sí misma.\n")

    print("3. 👻 **'El Hombre de Paja' (Distorsionar el Argumento):**")
    print("   Tú dices: 'Creo que deberíamos tener menos tarea para poder hacer más actividades extracurriculares.'")
    print("   Y alguien responde: '¡Ah, así que quieres que no tengamos NADA de tarea y que no aprendamos NUNCA nada!'")
    print("   ¿Dijiste eso? ¡No! Tu idea fue exagerada o cambiada para que fuera más fácil de atacar.")
    print("   Es como crear un muñeco de paja (un argumento falso y débil) para derribarlo en lugar de tu argumento real.\n")
    
    print("¡Aprendamos a pensar con la cabeza y a defender nuestras ideas reales!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de apelación a la emoción, apelación a la ignorancia y hombre de paja."""
    show_header("Ejemplos: ¿Emoción, Ignorancia o Hombre de Paja?")
    
    examples = [
        {"text": "Por favor, dame un poco más de tiempo para el proyecto, mi perro está enfermo y estoy muy triste.", 
         "type": "EMOCION", "explanation": "Usa la tristeza para obtener más tiempo, no una razón académica."},
        {"text": "Nadie ha demostrado que el monstruo del lago Ness no existe, por lo tanto, debe existir.", 
         "type": "IGNORANCIA", "explanation": "La falta de prueba de no-existencia no es prueba de existencia."},
        {"text": "Tú dices: 'Deberíamos comer menos dulces.' Respuesta: '¡Así que quieres que vivamos sin ninguna alegría y solo comamos lechuga!'", 
         "type": "HOMBRE_PAJA", "explanation": "Tu argumento de 'menos dulces' fue exagerado a 'ninguna alegría' y 'solo lechuga'."},
        {"text": "Si no compras este juguete para tu hijo, será el único que no lo tenga y se sentirá muy solo y excluido.", 
         "type": "EMOCION", "explanation": "Usa el miedo a la soledad y exclusión para persuadir a la compra."},
        {"text": "No hay pruebas de que las hadas no existan, así que son reales.", 
         "type": "IGNORANCIA", "explanation": "La ausencia de prueba en contra no es prueba a favor."},
        {"text": "Propuesta: 'Sugiero que usemos menos agua para cuidar el planeta.' Oposición: '¡Entonces quieres que no nos duchemos y que la gente viva sucia!'", 
         "type": "HOMBRE_PAJA", "explanation": "La sugerencia de 'menos agua' fue distorsionada a 'no ducharse' y 'vivir sucio'."},
    ]

    print("Lee cada frase y piensa si apela a la 'emoción', a la 'ignorancia' o es un 'hombre de paja'.\n")
    for i, ex in enumerate(examples):
        print(f"\n--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "EMOCION":
            print(f"¡Es APELACIÓN A LA EMOCIÓN! ❤️‍🩹 {ex['explanation']}\n")
        elif ex['type'] == "IGNORANCIA":
            print(f"¡Es APELACIÓN A LA IGNORANCIA! ❓ {ex['explanation']}\n")
        else: # HOMBRE_PAJA
            print(f"¡Es un HOMBRE DE PAJA! 👻 {ex['explanation']}\n")
        time.sleep(5)
        print("=" * 55)

    print("\n¡Ahora es tu turno de desenmascarar estas tácticas!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_tactic():
    """Juego de identificar el tipo de error lógico."""
    show_header("Juego 1: ¡El Detector de Manipulaciones!")
    print("Te daré una situación. Dime si es 'EMOCIÓN' (E), 'IGNORANCIA' (I) o 'HOMBRE DE PAJA' (H).\n")
    print("Escribe 'E', 'I' o 'H'.\n")

    questions = [
        {"text": "Si no me das el permiso para ir a la fiesta, seré el único que no vaya y me sentiré muy mal y triste por ti.", 
         "answer": "E", "explanation": "Usa la culpa y la tristeza para conseguir el permiso."},
        {"text": "No se ha demostrado que los fantasmas no existan, así que es posible que haya uno en esta casa.", 
         "answer": "I", "explanation": "La falta de prueba de no-existencia no es prueba de existencia."},
        {"text": "Tú dices: 'Deberíamos ahorrar dinero para un viaje.' Respuesta: '¡Así que quieres que nunca compremos nada y vivamos como pobres!'", 
         "answer": "H", "explanation": "La idea de 'ahorrar para un viaje' fue distorsionada a 'nunca comprar nada' y 'vivir como pobres'."},
        {"text": "Por favor, compra mi limonada. La hice con mucho esfuerzo y si no la compras, mis sueños se romperán.", 
         "answer": "E", "explanation": "Usa la lástima y la presión emocional para vender la limonada."},
        {"text": "No hay pruebas de que la vida en otros planetas exista, por lo tanto, no existe.", 
         "answer": "I", "explanation": "La falta de prueba a favor no es prueba en contra."},
        {"text": "Propuesta: 'Creo que deberíamos tener un poco más de tiempo para el almuerzo.' Oposición: '¡Quieren que pasemos todo el día comiendo y no haciendo nada productivo!'", 
         "answer": "H", "explanation": "La idea de 'un poco más de tiempo' fue exagerada a 'todo el día comiendo y no haciendo nada'."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿'EMOCIÓN' (E), 'IGNORANCIA' (I) o 'HOMBRE DE PAJA' (H)?: ").upper().strip()
            if user_input in ['E', 'I', 'H']:
                break
            else:
                print("Por favor, escribe 'E', 'I' o 'H'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(5)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detector de manipulaciones! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_respond_logically():
    """Juego de responder lógicamente a una falacia."""
    show_header("Juego 2: ¡Responde con Lógica!")
    print("Te daré una frase que usa una de las tácticas que aprendimos.")
    print("Tu misión es responder de una forma que **ignore la táctica y se centre en la lógica o la realidad**.\n")

    corrections = [
        {"original": "Por favor, no me castigues, me sentiré muy mal y mi corazón se romperá.", 
         "type": "EMOCION", "corrected_hint": "Entiendo cómo te sientes, pero el castigo es por tus acciones y para que aprendas.",
         "explanation": "No te dejes llevar por la emoción. Enfócate en la razón del castigo."},
        {"original": "Como nadie ha demostrado que los unicornios no existen, deben ser reales.", 
         "type": "IGNORANCIA", "corrected_hint": "Que no se haya probado su no-existencia no significa que existan. Necesitamos pruebas reales para creer en algo.",
         "explanation": "La falta de pruebas no es una prueba."},
        {"original": "Tú dices: 'Deberíamos usar menos plástico.' Respuesta: '¡Así que quieres que volvamos a la Edad de Piedra y no usemos nada moderno!'", 
         "type": "HOMBRE_PAJA", "corrected_hint": "No, mi idea es usar menos plástico, no dejar de usar todo lo moderno. Hay muchas alternativas.",
         "explanation": "Corrige la distorsión y vuelve a tu argumento real."},
        {"original": "Si no votas por mi idea, la clase será un desastre y todos seremos infelices.", 
         "type": "EMOCION", "corrected_hint": "Entiendo que crees en tu idea, pero necesito razones lógicas para votarla, no solo por miedo al desastre.",
         "explanation": "Pide razones lógicas, no te dejes influenciar por el miedo."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase con táctica: '{c['original']}'")
        print(f"Tipo de táctica: {'Emoción' if c['type'] == 'EMOCION' else ('Ignorancia' if c['type'] == 'IGNORANCIA' else 'Hombre de Paja')}")
        print(f"Pista para pensar: {c['explanation']}")
        
        user_response = input("Escribe cómo responderías con lógica o para aclarar: ").strip()
        
        print(f"\nTu respuesta: '{user_response}'")
        print(f"Una forma de responder: '{c['corrected_hint']}'")
        print("\n¡Genial! ¡Has aprendido a responder con lógica y a no caer en las trampas! 🎉")
        time.sleep(6)
    
    print(f"\nJuego terminado. ¡Eres un maestro respondiendo con argumentos sólidos!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_fallacy_example():
    """Permite al usuario crear su propio ejemplo de falacia y corregirlo."""
    show_header("✍️ ¡Crea y Corrige Tus Propias Tácticas! ✍️")
    print("Vamos a crear una frase que use 'emoción', 'ignorancia' o sea un 'hombre de paja'.")
    print("Luego, tú la corregirás o responderás con una lógica fuerte.\n")

    while True:
        original_sentence = input("1. Escribe una frase con una táctica (Ej: 'Si no me dejas jugar, me pondré a llorar y seré tu enemigo para siempre'): ").strip()
        if original_sentence:
            break
        else:
            print("Por favor, escribe una frase.")
    
    print(f"\nTu frase original con táctica: '{original_sentence}'")

    while True:
        fixed_sentence = input("2. Ahora, escribe cómo la corregirías o cómo responderías con lógica (Ej: 'No, si no me dejas jugar, no seremos enemigos. Podemos buscar otra cosa que hacer juntos.'): ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe la respuesta lógica.")

    print("\n--- ¡Tu Ejemplo Creado y Corregido! ---")
    print(f"Tu frase con táctica: '{original_sentence}' ❤️‍🩹❓👻")
    print(f"Tu respuesta lógica: '{fixed_sentence}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a construir ideas con una lógica fuerte y a defenderte de las manipulaciones! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Juegan con tus Sentimientos? (8º Grado)")
        print("1. Introducción: Analizando la Persuasión y los Argumentos Distorsionados")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡El Detector de Manipulaciones!")
        print("4. Jugar: ¡Responde con Lógica!")
        print("5. ✍️ ¡Crea y Corrige Tus Propias Tácticas! ✍️")
        print("6. Salir de la Lección")
        print("=" * 90)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_tactic()
        elif choice == '4':
            game_respond_logically()
        elif choice == '5':
            create_own_fallacy_example()
        elif choice == '6':
            print("¡Adiós! Sigue pensando con la cabeza fría y defendiendo la verdad. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
