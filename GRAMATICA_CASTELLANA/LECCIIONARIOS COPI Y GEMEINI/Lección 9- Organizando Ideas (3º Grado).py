import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    clear_screen()
    print("=" * 80)
    print(f"🌟 {title.upper()} 🌟")
    print("=" * 80)
    print()

def show_introduction_l3():
    show_header("Introducción: ¡Detectives de Ideas!")
    print("¡Hola, pequeños detectives de ideas! 🕵️‍♀️")
    print("Hoy aprenderemos a encontrar la 'idea más importante' en lo que leemos o escribimos, ¡como si fuera un tesoro!")
    print("También veremos cómo una cosa causa otra, ¡como las piezas de un dominó!")
    print("Esto nos ayudará a entender mejor las historias y lo que nos cuentan.\n")
    input("Presiona ENTER para empezar nuestra aventura...")

def show_main_idea_concept_l3():
    show_header("La Idea Principal: ¡El Corazón del Párrafo!")
    print("Cada párrafo tiene una **idea principal**. Es como el 'corazón' o el mensaje más importante de ese párrafo.")
    print("Las otras oraciones son **detalles** que explican o dan más información sobre esa idea principal.\n")
    print("Para encontrarla, pregúntate: '¿De qué se trata esto principalmente?'\n")
    print("Ejemplo:")
    print("  'Los perros son mascotas maravillosas. Son leales, juguetones y nos hacen compañía. Además, nos protegen.'")
    print("  **Idea Principal:** 'Los perros son mascotas maravillosas.'")
    print("  **Detalles:** 'Son leales, juguetones y nos hacen compañía. Además, nos protegen.'\n")
    input("Presiona ENTER para descubrir la Causa y Efecto...")

def show_cause_effect_concept_l3():
    show_header("Causa y Efecto: ¡El Juego del Porqué!")
    print("En la vida, y en las historias, una cosa puede hacer que otra suceda. ¡Eso es Causa y Efecto!")
    print("La **causa** es lo que hace que algo pase (el 'porqué').")
    print("El **efecto** es lo que sucede (el 'qué pasó').\n")
    print("Ejemplo:")
    print("  **Causa:** Llovió muy fuerte.")
    print("  **Efecto:** Las calles se mojaron.")
    print("  **Palabras clave:** porque, por eso, debido a, así que.\n")
    input("Presiona ENTER para jugar a los detectives...")

def game_main_idea_cause_effect_l3():
    show_header("Juego: ¡Detectives de Ideas y Causa/Efecto!")
    print("Primera parte: ¡Encuentra la Idea Principal!")
    questions_mi = [
        {"text": "Mi perro Fido es muy divertido. Le gusta correr en el parque, perseguir la pelota y saltar sobre mí cuando llego a casa.", "main_idea_hint": "Mi perro Fido es muy divertido."},
        {"text": "El agua es muy importante para la vida. La bebemos para mantenernos sanos, las plantas la necesitan para crecer y los animales para vivir.", "main_idea_hint": "El agua es muy importante para la vida."},
    ]
    random.shuffle(questions_mi)
    
    for i, q in enumerate(questions_mi[:2]): # Limit to 2 questions
        print(f"\n--- Pregunta {i+1} de 2 (Idea Principal) ---")
        print(f"Lee este párrafo: '{q['text']}'")
        user_answer = input("¿Cuál crees que es la idea más importante de este párrafo? ").strip()
        
        if q['main_idea_hint'].lower() in user_answer.lower():
            print("¡Bingo! 🎉 ¡Lo encontraste! Esa es la idea principal.")
        else:
            print("¡Casi! 🤔 La idea principal es la que te dice de qué se trata todo el párrafo.")
            print(f"La idea principal es: '{q['main_idea_hint']}'")
        time.sleep(5)

    print("\nSegunda parte: ¡Encuentra la Causa y el Efecto!")
    questions_ce = [
        {"text": "El niño comió muchos dulces, por eso le dolió la barriga.", "cause_hint": "El niño comió muchos dulces", "effect_hint": "le dolió la barriga."},
        {"text": "Como llovió, las plantas crecieron mucho.", "cause_hint": "llovió", "effect_hint": "las plantas crecieron mucho."},
    ]
    random.shuffle(questions_ce)

    for i, q in enumerate(questions_ce[:2]): # Limit to 2 questions
        print(f"\n--- Pregunta {i+1} de 2 (Causa/Efecto) ---")
        print(f"Lee esta oración: '{q['text']}'")
        user_cause = input("¿Cuál es la CAUSA (qué hizo que pasara)? ").strip()
        user_effect = input("¿Cuál es el EFECTO (qué pasó)? ").strip()

        if q['cause_hint'].lower() in user_cause.lower() and q['effect_hint'].lower() in user_effect.lower():
            print("¡Excelente! 🎉 ¡Identificaste la causa y el efecto correctamente!")
        else:
            print("¡Sigue practicando! 🤔")
            print(f"Causa: '{q['cause_hint']}' | Efecto: '{q['effect_hint']}'")
        time.sleep(5)

    print("\n¡Juego terminado! ¡Eres un gran detective de ideas y acciones! 🕵️‍♀️")
    input("Presiona ENTER para la siguiente actividad...")

# --- NUEVO EJERCICIO PARA LECCIÓN 3 ---
def exercise_write_and_identify_main_idea_l3():
    show_header("Ejercicio: ¡Escribe y Encuentra tu Idea Principal!")
    print("Ahora, ¡es tu turno de ser el escritor!")
    print("Piensa en tu comida favorita. Escribe un párrafo muy corto (2 o 3 oraciones) sobre por qué te gusta.")
    print("Recuerda que tu párrafo debe tener una idea principal clara y algunos detalles que la expliquen.\n")
    
    user_paragraph = input("Escribe tu párrafo aquí: \n> ").strip()
    print("\n¡Muy bien! Has escrito tu párrafo. Ahora, piensa...")
    print(f"Tu párrafo: '{user_paragraph}'\n")
    
    print("De las oraciones que escribiste (o creando una nueva si lo prefieres), ¿cuál es la **idea más importante** de tu párrafo?")
    user_main_idea = input("Escribe la idea principal de TU párrafo: \n> ").strip()
    
    print("\n--- Reflexión ---")
    print(f"Tu párrafo: '{user_paragraph}'")
    print(f"Tu idea principal identificada: '{user_main_idea}'\n")
    
    print("Considera: ¿Esta idea principal que elegiste es una oración general que engloba todo lo que dijiste?")
    print("¿O es muy específica, como un detalle?")
    print("¡Sigue practicando! La clave es que tu idea principal sea el 'paraguas' de todo lo demás.")
    input("\nPresiona ENTER para continuar...")


def show_main_menu_l3():
    while True:
        show_header("Lección 9: Organizando Ideas (3º Grado)")
        print("1. Introducción: ¡Detectives de Ideas!")
        print("2. La Idea Principal: ¡El Corazón del Párrafo!")
        print("3. Causa y Efecto: ¡El Juego del Porqué!")
        print("4. Jugar: ¡Detectives de Ideas y Causa/Efecto!")
        print("5. **NUEVO:** Ejercicio: ¡Escribe y Encuentra tu Idea Principal!")
        print("6. Salir de la Lección")
        print("=" * 80)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction_l3()
        elif choice == '2':
            show_main_idea_concept_l3()
        elif choice == '3':
            show_cause_effect_concept_l3()
        elif choice == '4':
            game_main_idea_cause_effect_l3()
        elif choice == '5':
            exercise_write_and_identify_main_idea_l3()
        elif choice == '6':
            print("¡Adiós, pequeños detectives! ¡Sigan organizando el mundo! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# Comentado para no ejecutar automáticamente
# if __name__ == "__main__":
#     show_main_menu_l3()
