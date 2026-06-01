import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 70)
    print(f"🔍 {title.upper()} 🔍")
    print("=" * 70)
    print()

def show_introduction():
    """Introduce los conceptos de causa y efecto e idea principal."""
    show_header("Introducción: ¡Detectives de Ideas y Sucesos!")
    print("¡Hola, jóvenes detectives del pensamiento! 🕵️‍♂️")
    print("Hoy vamos a ser como Sherlock Holmes, buscando pistas para entender por qué pasan las cosas y cuál es la idea más importante de lo que leemos o escuchamos.\n")
    
    print("Aprenderemos a responder dos preguntas clave:")
    print("   ✅ **¿Por qué pasó eso?** (Causa y Efecto)")
    print("   ✅ **¿De qué se trata esto?** (Idea Principal)\n")
    
    print("¡Esto nos ayudará a comprender todo mucho mejor y a explicar nuestras ideas con más claridad!\n")
    input("Presiona ENTER para empezar nuestra investigación...")

def show_cause_effect_concept():
    """Explica el concepto de causa y efecto."""
    show_header("Causa y Efecto: ¿Por Qué Pasó Esto?")
    print("Todo lo que pasa tiene una **causa** (la razón por la que algo sucede) y un **efecto** (lo que sucede como resultado).\n")
    print("Es como un dominó: una pieza cae (causa) y hace que la siguiente caiga (efecto).")
    
    print("\n**Ejemplo 1:**")
    print("  **Causa:** Llovió muy fuerte. 🌧️")
    print("  **Efecto:** La calle se mojó. ☔")
    
    print("\n**Ejemplo 2:**")
    print("  **Causa:** Me lavé las manos con jabón. 🧼")
    print("  **Efecto:** Mis manos quedaron limpias. ✨")
    
    print("\n¡Las causas y los efectos van de la mano!\n")
    input("Presiona ENTER para jugar al detective de causas y efectos...")

def game_cause_effect():
    """Juego de identificar causa o efecto en escenarios simples."""
    show_header("Juego 1: ¡El Detective de Causas y Efectos!")
    print("Te daré una frase. Dime si lo que te pido es la **CAUSA** o el **EFECTO**.\n")
    print("Escribe 'C' para Causa o 'E' para Efecto.\n")

    questions = [
        {"scenario": "El niño estudió mucho para el examen. Sacó una buena nota.", 
         "ask": "¿Por qué sacó una buena nota? ('El niño estudió mucho')", 
         "answer": "C", "explanation": "Estudiar mucho es la causa de la buena nota."},
        
        {"scenario": "La planta no recibió agua. Se secó.", 
         "ask": "¿Qué pasó porque la planta no recibió agua? ('Se secó')", 
         "answer": "E", "explanation": "Secarse es el efecto de no recibir agua."},
        
        {"scenario": "Pusimos la basura en el bote. La calle se ve limpia.", 
         "ask": "¿Qué causó que la calle se vea limpia? ('Pusimos la basura en el bote')", 
         "answer": "C", "explanation": "Poner la basura es la causa de una calle limpia."},
        
        {"scenario": "El semáforo se puso en rojo. Los carros se detuvieron.", 
         "ask": "¿Qué efecto tuvo el semáforo en rojo? ('Los carros se detuvieron')", 
         "answer": "E", "explanation": "Los carros se detuvieron es el efecto del semáforo rojo."},
        
        {"scenario": "Ana corrió muy rápido. Ganó la carrera.", 
         "ask": "¿Qué fue la causa de que Ana ganara la carrera? ('Ana corrió muy rápido')", 
         "answer": "C", "explanation": "Correr rápido fue la causa de ganar."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 3 # Limitamos a 3 preguntas

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Situación: '{q['scenario']}'")
        print(f"Pregunta: {q['ask']}")
        
        while True:
            user_input = input("¿CAUSA (C) o EFECTO (E)?: ").upper().strip()
            if user_input in ['C', 'E']:
                break
            else:
                print("Por favor, escribe 'C' o 'E'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(5)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detective de causas y efectos! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente paso...")

def show_main_idea_concept():
    """Explica el concepto de idea principal."""
    show_header("La Idea Principal: ¿De Qué Trata?")
    print("Cuando leemos un párrafo o una historia, hay una **idea principal**, que es lo más importante de lo que nos habla.\n")
    print("Piensa en la idea principal como el 'gran tema' o el 'punto clave'. Es como el título más importante para ese pedacito de texto.\n")
    
    print("**Ejemplo:**")
    print("  'Los perros son mascotas muy populares. Les encanta jugar, son leales y pueden aprender muchos trucos. Necesitan ejercicio y mucho amor.'")
    print("\n  ¿De qué trata este párrafo principalmente?")
    print("  La **idea principal** es: 'Los perros son mascotas populares y necesitan cuidado'.\n")
    
    print("¡Presta atención a las palabras que se repiten o a lo que es más importante!\n")
    input("Presiona ENTER para el juego de la idea principal...")

def game_main_idea():
    """Juego de identificar la idea principal en párrafos cortos."""
    show_header("Juego 2: ¡El Cazador de Ideas Principales!")
    print("Te daré un párrafo corto. Lee con atención y dime cuál es la **idea principal**.\n")
    
    paragraphs = [
        {"text": "Las abejas son insectos muy ocupados. Vuelan de flor en flor recolectando néctar. Con el néctar, hacen miel deliciosa que guardan en sus colmenas. Las abejas son muy importantes para las plantas.", 
         "main_idea_options": ["A) Las abejas vuelan.", "B) Las abejas hacen miel.", "C) Las abejas son insectos muy ocupados e importantes que hacen miel."], 
         "correct_answer": "C", "explanation": "La opción C resume lo más importante del párrafo sobre las abejas."},
        
        {"text": "El agua es muy importante para la vida. La necesitamos para beber, para bañarnos y para regar las plantas. Los animales y las personas no podríamos vivir sin agua. Debemos cuidarla mucho.", 
         "main_idea_options": ["A) El agua es para bañarse.", "B) El agua es muy importante para la vida y debemos cuidarla.", "C) Los animales necesitan agua."], 
         "correct_answer": "B", "explanation": "La opción B abarca el punto principal: la importancia del agua y la necesidad de cuidarla."},
        
        {"text": "Los planetas giran alrededor del sol. Nuestro planeta se llama Tierra. Marte es rojo y Júpiter es el más grande. Cada planeta es diferente y viaja por el espacio.", 
         "main_idea_options": ["A) La Tierra es un planeta.", "B) Cada planeta es diferente y gira alrededor del sol.", "C) Júpiter es grande."], 
         "correct_answer": "B", "explanation": "La opción B resume que los planetas son diferentes y giran alrededor del sol."},
    ]
    
    random.shuffle(paragraphs)
    score = 0
    num_paragraphs = 2 # Limitamos a 2 párrafos

    for i in range(num_paragraphs):
        p = paragraphs[i]
        print(f"\n--- Párrafo {i+1} de {num_paragraphs} ---")
        print(f"Párrafo: '{p['text']}'")
        print("\n¿Cuál es la idea principal?")
        for j, option in enumerate(p['main_idea_options']):
            print(f"  {option}")
        
        while True:
            user_input = input("Tu respuesta (A, B o C): ").upper().strip()
            if user_input in ['A', 'B', 'C']:
                break
            else:
                print("Por favor, escribe 'A', 'B' o 'C'.")
        
        if user_input == p['correct_answer']:
            print("¡Bingo! 🎉 ¡Lo lograste! Esa es la idea principal.")
            print(f"Explicación: {p['explanation']}")
            score += 1
        else:
            print("¡Casi! 🤔 La idea principal era la opción **{}**. {}".format(p['correct_answer'], p['explanation']))
        time.sleep(6)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_paragraphs} ideas principales. ¡Eres un cazador de ideas increíble! 🏆")
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: ¿Por Qué Pasó? ¡Descubre la Idea Más Grande! (3º Grado)")
        print("1. Introducción: ¡Detectives de Ideas y Sucesos!")
        print("2. Causa y Efecto: ¿Por Qué Pasó Esto?")
        print("3. Jugar: ¡El Detective de Causas y Efectos!")
        print("4. La Idea Principal: ¿De Qué Trata?")
        print("5. Jugar: ¡El Cazador de Ideas Principales!")
        print("6. Salir de la Lección")
        print("=" * 70)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_cause_effect_concept()
        elif choice == '3':
            game_cause_effect()
        elif choice == '4':
            show_main_idea_concept()
        elif choice == '5':
            game_main_idea()
        elif choice == '6':
            print("¡Adiós, pequeños pensadores! ¡Sigan investigando y descubriendo ideas! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
