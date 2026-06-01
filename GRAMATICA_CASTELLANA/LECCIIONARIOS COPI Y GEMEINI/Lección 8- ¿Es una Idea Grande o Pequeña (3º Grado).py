import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("+" * 65)
    print(f"🌟 {title.upper()} 🌟")
    print("+" * 65)
    print()

def show_introduction():
    """Introduce el concepto de ideas grandes y apelación a sentimientos."""
    show_header("Introducción: Ideas Grandes y Sentimientos")
    print("¡Hola, pequeños pensadores! 👋")
    print("Ya sabemos si una idea 'tiene sentido' o 'no tiene sentido'.")
    print("Hoy vamos a aprender a reconocer dos tipos de ideas que a veces nos confunden:\n")
    
    print("1. 🎈 **IDEAS MUY GRANDES (o Exageradas):**")
    print("   A veces, alguien dice algo como: '¡Este es el MEJOR juguete del MUNDO ENTERO!'")
    print("   O: '¡TODOS los niños aman el chocolate!'")
    print("   Son ideas muy, muy grandes. ¿Pero es verdad? ¿De verdad es el MEJOR de TODO el mundo?")
    print("   A veces, estas ideas no tienen pruebas o son solo una opinión muy grande.\n")
    
    print("2. ❤️ **IDEAS QUE TOCAN TUS SENTIMIENTOS:**")
    print("   Otras veces, alguien quiere que hagas algo y te dice: 'Si no me prestas tu juguete, me pondré MUY triste y no seré tu amigo.'")
    print("   O: '¡Compra este dulce! ¡Te hará el niño MÁS feliz del mundo!'")
    print("   Estas ideas intentan que decidas algo por cómo te sientes (triste, feliz, asustado), no porque sea una buena razón.\n")
    
    print("Vamos a aprender a identificarlas para pensar mejor y tomar buenas decisiones.")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de ideas grandes y apelación a sentimientos."""
    show_header("Ejemplos: ¿Idea Grande o Toca Sentimientos?")
    
    examples = [
        {"text": "¡Mi dibujo es el más bonito de toda la clase!", "type": "GRANDE", "explanation": "Es una idea muy grande. ¿Es verdad que es el más bonito de TODOS? Quizás solo es bonito para ti."},
        {"text": "Si no comes tus verduras, la planta del jardín se pondrá triste.", "type": "SENTIMIENTOS", "explanation": "Intenta que comas usando la tristeza de la planta, no porque las verduras sean buenas para ti."},
        {"text": "¡Todos los gatos odian el agua!", "type": "GRANDE", "explanation": "Es una idea muy grande. ¿TODOS? Quizás a algunos sí les gusta o no les importa."},
        {"text": "Por favor, ayúdame a recoger. Si no, me sentiré muy solo.", "type": "SENTIMIENTOS", "explanation": "Intenta que ayudes usando el sentimiento de soledad, no porque sea bueno ayudar."},
        {"text": "¡Este es el mejor día de mi vida!", "type": "GRANDE", "explanation": "Es una idea muy grande. ¿De verdad el MEJOR de TODA tu vida? Quizás solo es un día muy bueno."},
        {"text": "Si no compartes tu galleta, el monstruo de las galletas vendrá por ti.", "type": "SENTIMIENTOS", "explanation": "Intenta asustarte para que compartas, no porque compartir sea bueno."},
    ]

    print("Lee cada frase y piensa si es una 'idea muy grande' o si 'toca tus sentimientos'.\n")
    for i, ex in enumerate(examples):
        print(f"--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "GRANDE":
            print(f"¡Es una IDEA MUY GRANDE! 🎈 {ex['explanation']}\n")
        else:
            print(f"¡Toca tus SENTIMIENTOS! ❤️ {ex['explanation']}\n")
        time.sleep(2)
        print("-" * 30)

    print("\n¡Ahora es tu turno de ser un detective de ideas y sentimientos!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_idea_type():
    """Juego de identificar si una frase es una idea grande o toca sentimientos."""
    show_header("Juego 1: ¡Detective de Ideas y Sentimientos!")
    print("Te daré una frase. Tienes que decir si es una 'IDEA GRANDE' (G) o si 'TOCA SENTIMIENTOS' (S).\n")
    print("Escribe 'G' para Idea Grande o 'S' para Toca Sentimientos.\n")

    questions = [
        {"text": "¡Mi papá es el más fuerte de todo el universo!", "answer": "G", "explanation": "Es una exageración, ¿el más fuerte de TODO el universo?"},
        {"text": "Si no me das tu juguete, voy a llorar mucho.", "answer": "S", "explanation": "Intenta convencerte usando la tristeza."},
        {"text": "¡Todas las niñas aman las muñecas!", "answer": "G", "explanation": "¿TODAS? No es cierto, a algunas les gustan otras cosas."},
        {"text": "Este chocolate te hará el niño más feliz del mundo.", "answer": "S", "explanation": "Intenta convencerte usando la felicidad."},
        {"text": "¡Nunca nadie me escucha!", "answer": "G", "explanation": "¿NUNCA NADIE? Es una idea muy grande, quizás a veces sí te escuchan."},
        {"text": "Si no vienes a mi fiesta, me sentiré muy solo y triste.", "answer": "S", "explanation": "Usa tus sentimientos para que vayas a la fiesta."},
        {"text": "Mi mamá hace la mejor comida de la historia.", "answer": "G", "explanation": "¿La MEJOR de TODA la historia? Es una opinión muy grande."},
        {"text": "Si no ayudas a tu hermano, Papá Noel no te traerá regalos.", "answer": "S", "explanation": "Intenta que ayudes usando el miedo a no recibir regalos."},
        {"text": "¡Siempre llueve cuando quiero salir a jugar!", "answer": "G", "explanation": "¿SIEMPRE? Es una exageración, a veces hace sol."},
        {"text": "Si me das un abrazo, me sentiré mucho mejor.", "answer": "S", "explanation": "Usa tus sentimientos para pedir un abrazo (aunque un abrazo siempre es bueno)."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 5 # Limitamos a 5 para no alargar demasiado

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿Es 'Idea Grande' (G) o 'Toca Sentimientos' (S)?: ").upper().strip()
            if user_input in ['G', 'S']:
                break
            else:
                print("Por favor, escribe 'G' o 'S'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(2)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detective! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_make_it_fair():
    """Juego de transformar ideas grandes o que tocan sentimientos en ideas justas."""
    show_header("Juego 2: ¡Hazlo Justo y Verdadero!")
    print("Te daré una frase que es una 'idea grande' o que 'toca sentimientos'.")
    print("Tu misión es escribirla de una forma más JUSTA y VERDADERA, sin exagerar o usar solo los sentimientos.\n")

    transformations = [
        {"original": "¡Mi mamá es la mejor mamá del mundo entero!", 
         "fair": "Mi mamá es una mamá muy buena y la quiero mucho.",
         "hint": "Piensa: ¿De verdad la mejor de TODO el mundo? ¿O es la mejor para ti?"},
        {"original": "Si no me prestas tu juguete, no seré tu amigo nunca más.", 
         "fair": "Me gustaría mucho que me prestaras tu juguete.",
         "hint": "Piensa: ¿Es justo decir que no serás su amigo? ¿Cómo lo pedirías con respeto?"},
        {"original": "¡Todos los niños de mi clase son muy altos!", 
         "fair": "Algunos niños de mi clase son altos.",
         "hint": "Piensa: ¿TODOS? ¿O solo algunos?"},
        {"original": "Si no me compras ese dulce, me sentiré muy triste.", 
         "fair": "Me gustaría mucho ese dulce.",
         "hint": "Piensa: ¿Es justo usar la tristeza para conseguir algo? ¿Cómo lo pedirías sin manipular?"},
        {"original": "¡Siempre gano en todos los juegos!", 
         "fair": "A veces gano en los juegos.",
         "hint": "Piensa: ¿SIEMPRE? ¿De verdad en TODOS los juegos?"},
    ]
    
    random.shuffle(transformations)
    num_questions = 3 # Limitamos a 3

    for i in range(num_questions):
        t = transformations[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase original: '{t['original']}'")
        print(f"Pista: {t['hint']}")
        
        user_input = input("Escribe la frase de forma más JUSTA y VERDADERA: ").strip()
        
        print(f"\nTu respuesta: '{user_input}'")
        print(f"Idea de cómo hacerla justa: '{t['fair']}'")
        print("\n¡Muy bien! Has pensado en cómo hacer las ideas más justas y verdaderas. 🎉")
        time.sleep(3)
    
    print(f"\nJuego terminado. ¡Has aprendido a hacer las ideas más justas y verdaderas!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_unfair_example():
    """Permite al usuario crear su propio ejemplo de frase injusta y luego transformarla."""
    show_header("✍️ ¡Crea Tus Propios Ejemplos Injustos! ✍️")
    print("Vamos a crear una frase que sea una 'idea grande' o que 'toque sentimientos'.")
    print("Luego, la transformaremos para que sea justa y verdadera.\n")

    while True:
        original_phrase = input("1. Escribe una frase que sea una 'idea muy grande' o que 'toque sentimientos' (Ej: 'Mi equipo siempre gana'): ").strip()
        if original_phrase:
            break
        else:
            print("Por favor, escribe una frase.")

    print(f"\nTu frase original: '{original_phrase}'")
    
    while True:
        transformed_phrase = input("2. Ahora, escribe la misma frase, pero de forma más JUSTA y VERDADERA (Ej: 'Mi equipo a veces gana'): ").strip()
        if transformed_phrase:
            break
        else:
            print("Por favor, escribe la frase transformada.")

    print("\n--- ¡Tu Ejemplo Creado! ---")
    print(f"Tu frase original (grande/sentimientos): '{original_phrase}' 🎈❤️")
    print(f"Tu frase justa y verdadera: '{transformed_phrase}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a transformar las ideas para que sean más justas! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Es una Idea Grande o Pequeña? (3º Grado)")
        print("1. Introducción: Ideas Grandes y Sentimientos")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡Detective de Ideas y Sentimientos!")
        print("4. Jugar: ¡Hazlo Justo y Verdadero!")
        print("5. ✍️ ¡Crea Tus Propios Ejemplos Injustos! ✍️")
        print("6. Salir de la Lección")
        print("+" * 65)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_idea_type()
        elif choice == '4':
            game_make_it_fair()
        elif choice == '5':
            create_own_unfair_example()
        elif choice == '6':
            print("¡Adiós! Sigue pensando: ¿Es una idea grande? ¿Toca mis sentimientos? 🤔👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
