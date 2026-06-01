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
    print(f"🕵️‍♀️ {title.upper()} 🕵️‍♀️")
    print("=" * 75)
    print()

def show_introduction():
    """Introduce los conceptos de secuencia detallada e idea principal vs. detalles de apoyo."""
    show_header("Introducción: ¡Maestros de la Comprensión!")
    print("¡Hola, futuros escritores y lectores expertos! 📚")
    print("Hoy vamos a subir de nivel en cómo entendemos y organizamos la información.")
    print("Aprenderemos a seguir el hilo de las historias con todos sus detalles y a encontrar la 'joya' de cada párrafo: ¡su idea principal!\n")
    
    print("Con esta lección, podrás:")
    print("   ✅ Reconstruir cualquier historia o proceso paso a paso.")
    print("   ✅ Saber qué es lo más importante en lo que lees.")
    print("   ✅ Escribir tus propias ideas de forma súper clara y organizada.\n")
    
    print("¡Prepárense para desentrañar el significado de las palabras!\n")
    input("Presiona ENTER para comenzar nuestra aventura...")

def show_detailed_sequence_concept():
    """Explica el concepto de secuencia detallada de eventos."""
    show_header("Secuencia Detallada: ¡El Orden de los Sucesos!")
    print("Ya sabemos que las cosas pasan en un orden. Pero a veces, ¡hay muchos pasos y detalles!\n")
    print("Para entender bien una historia o un proceso, necesitamos identificar cada paso y el orden en que ocurre.")
    print("Piensa en una receta de cocina: si cambias el orden, ¡el pastel no sale bien!\n")
    
    print("Palabras que nos ayudan a seguir el orden:")
    print("  ➡️ **Primero, al principio, para empezar...**")
    print("  ➡️ **Luego, después, a continuación, entonces...**")
    print("  ➡️ **Finalmente, al final, por último...**\n")
    
    print("**Ejemplo: Cómo hacer un jugo de naranja 🍊**")
    print("  1. **Primero**, toma las naranjas del frutero.")
    print("  2. **Luego**, córtalas por la mitad con cuidado.")
    print("  3. **Después**, exprime cada mitad para sacar el jugo.")
    print("  4. **Finalmente**, vierte el jugo en un vaso y a disfrutar.\n")
    
    print("¡Cada detalle cuenta para entender la secuencia!\n")
    input("Presiona ENTER para el juego de la secuencia detallada...")

def game_detailed_sequence():
    """Juego de ordenar una secuencia de eventos con más detalles."""
    show_header("Juego 1: ¡El Director de Cine de Historias!")
    print("Te daré 4 oraciones de una pequeña historia o proceso, ¡pero están desordenadas!")
    print("Tu misión es ponerlas en el orden correcto usando los números '1', '2', '3' y '4'.\n")

    scenarios = [
        {"name": "Un día en la playa 🏖️",
         "steps": ["Construimos un gran castillo de arena con torres y un foso.", "Llegamos a la playa y buscamos un buen lugar para poner la toalla.", "Nadamos en el mar y jugamos con las olas hasta que nos cansamos.", "Al final del día, recogimos nuestras cosas y regresamos a casa."],
         "correct_order_text": ["Llegamos a la playa y buscamos un buen lugar para poner la toalla.", "Nadamos en el mar y jugamos con las olas hasta que nos cansamos.", "Construimos un gran castillo de arena con torres y un foso.", "Al final del día, recogimos nuestras cosas y regresamos a casa."]},
        
        {"name": "Cómo cuidar a tu mascota 🐶",
         "steps": ["Le damos de comer su comida favorita a la hora indicada.", "Lo sacamos a pasear para que haga ejercicio y juegue.", "Le damos mucho cariño y lo peinamos para que esté bonito.", "Primero, nos aseguramos de que tenga agua fresca en su recipiente."],
         "correct_order_text": ["Primero, nos aseguramos de que tenga agua fresca en su recipiente.", "Le damos de comer su comida favorita a la hora indicada.", "Lo sacamos a pasear para que haga ejercicio y juegue.", "Le damos mucho cariño y lo peinamos para que esté bonito."]},
        
        {"name": "Preparar una ensalada de frutas 🍓🥝",
         "steps": ["Cortamos las frutas en trozos pequeños y las ponemos en un tazón grande.", "Lavamos bien todas las frutas bajo el grifo.", "Mezclamos las frutas con un poco de jugo de limón.", "Servimos la ensalada fría para disfrutarla."],
         "correct_order_text": ["Lavamos bien todas las frutas bajo el grifo.", "Cortamos las frutas en trozos pequeños y las ponemos en un tazón grande.", "Mezclamos las frutas con un poco de jugo de limón.", "Servimos la ensalada fría para disfrutarla."]},
    ]
    
    random.shuffle(scenarios)
    score = 0
    num_scenarios = 2 # Limitamos a 2 escenarios

    for i in range(num_scenarios):
        s = scenarios[i]
        print(f"\n--- Escenario {i+1} de {num_scenarios}: {s['name']} ---")
        print("Estas son las oraciones (desordenadas):")
        for j, step in enumerate(s['steps']):
            print(f"  {j+1}. {step}")
        
        user_order_nums = []
        user_order_text = []
        print("\n¡Escribe el número de la oración para cada posición en el orden correcto!")
        keywords = ["Primero", "Segundo", "Tercero", "Cuarto"]
        for k in range(4):
            while True:
                try:
                    choice_num = int(input(f"{keywords[k]}: "))
                    if 1 <= choice_num <= 4 and choice_num not in user_order_nums:
                        user_order_nums.append(choice_num)
                        user_order_text.append(s['steps'][choice_num-1])
                        break
                    else:
                        print("Ese número no es válido o ya lo usaste. Intenta de nuevo.")
                except ValueError:
                    print("Por favor, escribe un número (1, 2, 3 o 4).")
        
        print("\nTu orden es:")
        for k, step_text in enumerate(user_order_text):
            print(f"  {keywords[k]}: {step_text}")
        
        correct = True
        for k in range(4):
            if user_order_text[k] != s['correct_order_text'][k]:
                correct = False
                break
        
        if correct:
            print("¡Fantástico! 🎉 Has ordenado la historia perfectamente. ¡Eres un gran director de cine!")
            score += 1
        else:
            print("¡Uhm, casi lo logras! 🤔 El orden correcto era:")
            for k, step_text in enumerate(s['correct_order_text']):
                print(f"  {keywords[k]}: {step_text}")
        time.sleep(7)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_scenarios} escenarios correctos. ¡Muy bien hecho! 👏")
    input("Presiona ENTER para el siguiente paso...")

def show_main_idea_details_concept():
    """Explica el concepto de idea principal vs. detalles de apoyo."""
    show_header("Idea Principal y Detalles: ¡Lo Importante y lo que lo Explica!")
    print("Ya sabemos que la **idea principal** es lo más importante de un párrafo. Es como el 'gran mensaje'.")
    print("Pero, ¿qué son los **detalles de apoyo**? 🤔\n")
    
    print("Los **detalles de apoyo** son las oraciones que:")
    print("  ✨ Explican la idea principal.")
    print("  ✨ Dan ejemplos de la idea principal.")
    print("  ✨ Añaden más información sobre la idea principal.\n")
    
    print("**Ejemplo:**")
    print("  'Los delfines son animales muy inteligentes. Pueden aprender trucos complejos y comunicarse entre sí con sonidos especiales. También son muy amigables con los humanos y les gusta jugar.'")
    print("\n  **Idea Principal:** 'Los delfines son animales muy inteligentes.'")
    print("  **Detalles de Apoyo:**")
    print("    - 'Pueden aprender trucos complejos y comunicarse entre sí con sonidos especiales.'")
    print("    - 'También son muy amigables con los humanos y les gusta jugar.'\n")
    
    print("¡La idea principal es la cabeza, y los detalles son el cuerpo que la sostiene!\n")
    input("Presiona ENTER para el juego de la idea principal y los detalles...")

def game_main_idea_details():
    """Juego de identificar la idea principal y los detalles de apoyo."""
    show_header("Juego 2: ¡El Separador de Ideas!")
    print("Te daré un párrafo. Primero, elige la **idea principal**. Luego, identifica un **detalle de apoyo**.\n")
    
    paragraphs = [
        {"text": "Los árboles son muy importantes para nuestro planeta. Nos dan el oxígeno que respiramos y son el hogar de muchos animales. Sus raíces ayudan a mantener la tierra en su lugar y sus hojas nos dan sombra en días soleados.", 
         "main_idea_options": ["A) Los árboles dan sombra.", "B) Los árboles son importantes para el planeta.", "C) Los árboles son hogar de animales."], 
         "correct_main_idea": "B", 
         "details_options": ["1) Nos dan oxígeno.", "2) Sus raíces mantienen la tierra.", "3) Sus hojas dan sombra."],
         "correct_details": ["1", "2", "3"],
         "explanation": "La idea principal es la importancia general de los árboles. Los detalles explican por qué son importantes."},
        
        {"text": "El deporte es bueno para la salud. Ayuda a nuestros músculos a crecer fuertes y a nuestro corazón a latir mejor. También nos ayuda a tener más energía y a dormir bien por la noche. Hacer ejercicio nos mantiene felices.", 
         "main_idea_options": ["A) El deporte nos da energía.", "B) El deporte es bueno para la salud.", "C) El deporte nos ayuda a dormir."], 
         "correct_main_idea": "B", 
         "details_options": ["1) Ayuda a los músculos y al corazón.", "2) Nos da energía y ayuda a dormir.", "3) Nos mantiene felices."],
         "correct_details": ["1", "2", "3"],
         "explanation": "La idea principal es que el deporte es bueno para la salud. Los detalles explican los beneficios específicos."},
    ]
    
    random.shuffle(paragraphs)
    score = 0
    num_paragraphs = 2 # Limitamos a 2 párrafos

    for i in range(num_paragraphs):
        p = paragraphs[i]
        print(f"\n--- Párrafo {i+1} de {num_paragraphs} ---")
        print(f"Párrafo: '{p['text']}'")
        
        # Pregunta 1: Idea Principal
        print("\n1. ¿Cuál es la IDEA PRINCIPAL?")
        for j, option in enumerate(p['main_idea_options']):
            print(f"  {option}")
        
        while True:
            user_main_idea = input("Tu respuesta (A, B o C): ").upper().strip()
            if user_main_idea in ['A', 'B', 'C']:
                break
            else:
                print("Por favor, escribe 'A', 'B' o 'C'.")
        
        if user_main_idea == p['correct_main_idea']:
            print("¡Muy bien! 🎉 Esa es la idea principal.")
            score += 0.5 # Media puntuación por esta parte
        else:
            print(f"¡Uhm, no! 🤔 La idea principal era la opción **{p['correct_main_idea']}**.")
        
        # Pregunta 2: Detalles de Apoyo
        print("\n2. Ahora, ¿cuál de estas opciones es un DETALLE DE APOYO para la idea principal?")
        for j, option in enumerate(p['details_options']):
            print(f"  {option}")
        
        while True:
            user_detail = input("Tu respuesta (1, 2 o 3): ").strip()
            if user_detail in ['1', '2', '3']:
                break
            else:
                print("Por favor, escribe '1', '2' o '3'.")
        
        if user_detail in p['correct_details']: # Aceptamos cualquier detalle correcto
            print("¡Excelente! 🎉 Ese es un buen detalle de apoyo.")
            score += 0.5 # Media puntuación por esta parte
        else:
            print("¡No es ese! 🤔 Esa no es un detalle de apoyo para la idea principal.")
        
        print(f"Explicación general: {p['explanation']}")
        time.sleep(8)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_paragraphs} puntos. ¡Eres un separador de ideas genial! 🏆")
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: ¡Desentraña la Historia y Sus Detalles! (4º Grado)")
        print("1. Introducción: ¡Maestros de la Comprensión!")
        print("2. Secuencia Detallada: ¡El Orden de los Sucesos!")
        print("3. Jugar: ¡El Director de Cine de Historias!")
        print("4. Idea Principal y Detalles: ¡Lo Importante y lo que lo Explica!")
        print("5. Jugar: ¡El Separador de Ideas!")
        print("6. Salir de la Lección")
        print("=" * 75)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_detailed_sequence_concept()
        elif choice == '3':
            game_detailed_sequence()
        elif choice == '4':
            show_main_idea_details_concept()
        elif choice == '5':
            game_main_idea_details()
        elif choice == '6':
            print("¡Adiós, lectores y escritores! ¡Sigan desentrañando el mundo con sus mentes organizadas! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
