import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 60)
    print(f"🧩 {title.upper()} 🧩")
    print("=" * 60)
    print()

def show_introduction():
    """Introduce los conceptos de secuencia simple y agrupar ideas."""
    show_header("Introducción: ¡Ordenando Nuestros Pensamientos!")
    print("¡Hola, pequeños organizadores! 🧒👧")
    print("Hoy vamos a aprender un juego muy divertido: ¡poner nuestras ideas en orden!\n")
    
    print("Imagina que quieres contarle a alguien lo que hiciste hoy. ¿Empiezas por el final o por el principio?")
    print("Para que te entiendan bien, ¡tus ideas tienen que ir en orden!\n")
    
    print("También aprenderemos a juntar las cosas que se parecen. Como las frutas van con las frutas, y los juguetes con los juguetes.\n")
    
    print("¡Ordenar nos ayuda a pensar mejor y a explicar todo súper claro!\n")
    input("Presiona ENTER para empezar a ordenar...")

def show_sequence_concept():
    """Explica y ejemplifica el concepto de secuencia."""
    show_header("Ordenando Historias: Primero, Después, Al final")
    print("Las historias tienen un principio, un medio y un final. ¡Como tu día!\n")
    
    print("Mira este ejemplo:")
    print("  1. Primero, me levanto de la cama. ☀️")
    print("  2. Después, desayuno mi cereal favorito. 🥣")
    print("  3. Al final, me cepillo los dientes. 🦷\n")
    
    print("¿Ves? Si lo cuentas en orden, ¡todo tiene mucho sentido!\n")
    input("Presiona ENTER para el juego de secuencia...")

def game_simple_sequence():
    """Juego de ordenar eventos simples."""
    show_header("Juego 1: ¡El Orden Mágico!")
    print("Te daré unas acciones. Dime cuál va **primero**, cuál **después** y cuál **al final**.\n")

    scenarios = [
        {"name": "Preparar un sandwich 🥪",
         "steps": ["Comer el sandwich.", "Untar la crema de cacahuete en el pan.", "Poner otro pan encima."],
         "correct_order_text": ["Untar la crema de cacahuete en el pan.", "Poner otro pan encima.", "Comer el sandwich."],
         "keywords": ["Primero", "Después", "Al final"]},
        
        {"name": "Plantar una flor 🌸",
         "steps": ["La flor crece y da una hermosa flor.", "Poner la semilla en la tierra.", "Regar la semilla con agua."],
         "correct_order_text": ["Poner la semilla en la tierra.", "Regar la semilla con agua.", "La flor crece y da una hermosa flor."],
         "keywords": ["Primero", "Luego", "Finalmente"]},
        
        {"name": "Pintar un dibujo 🎨",
         "steps": ["Colorear el dibujo.", "Dibujar las líneas con lápiz.", "Mostrar mi obra de arte."],
         "correct_order_text": ["Dibujar las líneas con lápiz.", "Colorear el dibujo.", "Mostrar mi obra de arte."],
         "keywords": ["Inicio", "Siguiente", "Fin"]},
    ]
    
    random.shuffle(scenarios)
    score = 0
    num_scenarios = 2 # Limitamos a 2 escenarios

    for i in range(num_scenarios):
        s = scenarios[i]
        print(f"\n--- Escenario {i+1} de {num_scenarios}: {s['name']} ---")
        print("Estas son las acciones (desordenadas):")
        for j, step in enumerate(s['steps']):
            print(f"  {j+1}. {step}")
        
        user_order = []
        print("\n¡Ahora, ordena las acciones usando '1', '2' y '3'!")
        for k in range(3):
            while True:
                try:
                    choice_num = int(input(f"{s['keywords'][k]} va la acción número: "))
                    if 1 <= choice_num <= 3 and s['steps'][choice_num-1] not in user_order:
                        user_order.append(s['steps'][choice_num-1])
                        break
                    else:
                        print("Ese número no es válido o ya lo usaste. Intenta de nuevo.")
                except ValueError:
                    print("Por favor, escribe un número (1, 2 o 3).")
        
        print("\nTu orden:")
        for k, step_text in enumerate(user_order):
            print(f"  {s['keywords'][k]}: {step_text}")
        
        correct = True
        for k in range(3):
            if user_order[k] != s['correct_order_text'][k]:
                correct = False
                break
        
        if correct:
            print("¡Fabuloso! 🎉 Tu orden es perfecta.")
            score += 1
        else:
            print("¡Casi! 🤔 El orden correcto era:")
            for k, step_text in enumerate(s['correct_order_text']):
                print(f"  {s['keywords'][k]}: {step_text}")
        time.sleep(5)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_scenarios} escenarios correctos. ¡Eres un gran organizador de historias! 📖")
    input("Presiona ENTER para el siguiente paso...")

def show_grouping_concept():
    """Explica y ejemplifica el concepto de agrupar ideas."""
    show_header("Agrupando Ideas: ¿Qué Va Junto?")
    print("Algunas cosas se parecen y van juntas. ¡Como tus juguetes!\n")
    print("Si tienes pelotas y carros, los pones en diferentes cajas, ¿verdad?\n")
    
    print("Mira:")
    print("  - Las manzanas y las bananas son **Frutas**.")
    print("  - Los perros y los gatos son **Animales**.\n")
    
    print("Agrupar nos ayuda a entender mejor el mundo y las ideas.\n")
    input("Presiona ENTER para el juego de agrupar...")

def game_simple_grouping():
    """Juego de agrupar objetos o ideas simples."""
    show_header("Juego 2: ¡El Gran Clasificador!")
    print("Te daré unas palabras. Dime si van en el grupo de 'Comida' 🍎 o 'Juguetes' 🧸.\n")
    
    items = [
        {"word": "galleta", "group": "COMIDA", "emoji": "🍪"},
        {"word": "oso de peluche", "group": "JUGUETES", "emoji": "🧸"},
        {"word": "brócoli", "group": "COMIDA", "emoji": "🥦"},
        {"word": "bloques", "group": "JUGUETES", "emoji": "🧱"},
        {"word": "manzana", "group": "COMIDA", "emoji": "🍎"},
        {"word": "muñeca", "group": "JUGUETES", "emoji": "👧"},
    ]
    
    random.shuffle(items)
    score = 0
    num_items = 4 # Limitamos a 4 items

    print("Escribe 'C' para COMIDA o 'J' para JUGUETES.\n")
    for i in range(num_items):
        item = items[i]
        print(f"\n--- Pregunta {i+1} de {num_items} ---")
        print(f"¿'{item['word']}' es COMIDA o JUGUETES? {item['emoji']}")
        
        while True:
            user_input = input("Tu respuesta (C/J): ").upper().strip()
            if user_input in ['C', 'J']:
                break
            else:
                print("Por favor, escribe 'C' o 'J'.")
        
        if (user_input == 'C' and item['group'] == 'COMIDA') or \
           (user_input == 'J' and item['group'] == 'JUGUETES'):
            print(f"¡Correcto! ¡'{item['word']}' es {item['group']}! 🎉")
            score += 1
        else:
            print(f"¡Oops! No es correcto. 🤔 '{item['word']}' es {item['group']}.")
        time.sleep(3)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_items} items correctos. ¡Eres un clasificador brillante! 📦")
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: ¡Pon tus Ideas en Orden! (1º Grado)")
        print("1. Introducción: ¡Ordenando Nuestros Pensamientos!")
        print("2. Ordenando Historias: Primero, Después, Al final")
        print("3. Jugar: ¡El Orden Mágico!")
        print("4. Agrupando Ideas: ¿Qué Va Junto?")
        print("5. Jugar: ¡El Gran Clasificador!")
        print("6. Salir de la Lección")
        print("=" * 60)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_sequence_concept()
        elif choice == '3':
            game_simple_sequence()
        elif choice == '4':
            show_grouping_concept()
        elif choice == '5':
            game_simple_grouping()
        elif choice == '6':
            print("¡Adiós! ¡Sigue ordenando tus ideas y el mundo! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
