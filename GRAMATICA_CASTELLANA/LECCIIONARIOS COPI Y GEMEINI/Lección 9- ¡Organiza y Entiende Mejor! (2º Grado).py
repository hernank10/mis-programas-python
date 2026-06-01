import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 65)
    print(f"📖 {title.upper()} 📖")
    print("=" * 65)
    print()

def show_introduction():
    """Introduce los conceptos de secuencia y clasificación avanzada para 2.º grado."""
    show_header("Introducción: ¡Somos Expertos en Ordenar!")
    print("¡Hola, súper organizadores! 🌟")
    print("¿Recuerdan cómo ordenamos nuestras ideas? ¡Hoy seremos aún mejores!")
    print("Vamos a usar palabras mágicas para contar historias en el orden correcto y a clasificar cosas como verdaderos detectives. 🕵️‍♀️\n")
    
    print("Esto nos ayudará a:")
    print("   ✅ Contar lo que pasó de forma más clara.")
    print("   ✅ Entender mejor lo que leemos o escuchamos.")
    print("   ✅ Poner todo en su lugar.\n")
    
    print("¡Prepárense para organizar y aprender más!\n")
    input("Presiona ENTER para empezar...")

def show_sequence_concept():
    """Explica el concepto de secuencia con palabras clave."""
    show_header("Contando Pasos: Con Primero, Luego, Después, Al final")
    print("Para que nuestras historias sean súper claras, usamos palabras que nos dicen el orden de lo que pasa.\n")
    print("Mira estas palabras secretas que nos ayudan:")
    print("  ⭐ **Primero...** (Lo que pasó al principio)")
    print("  ⭐ **Luego...** (Lo que vino después del primero)")
    print("  ⭐ **Después...** (Otra cosa que vino más tarde)")
    print("  ⭐ **Al final...** (Lo último que pasó)\n")
    
    print("**Ejemplo:** ¿Cómo me preparo para dormir? 😴")
    print("  **Primero**, me pongo la pijama.")
    print("  **Luego**, me cepillo los dientes.")
    print("  **Después**, leo un cuento.")
    print("  **Al final**, me acuesto y duermo.\n")
    
    print("¡Es como seguir una receta! Cada paso en su lugar.\n")
    input("Presiona ENTER para el juego de ordenar pasos...")

def game_ordered_actions():
    """Juego de ordenar una secuencia de eventos con más pasos."""
    show_header("Juego 1: ¡La Receta Secreta del Orden!")
    print("Te daré 4 acciones de una actividad. ¡Ayúdame a ponerlas en el orden correcto!\n")
    print("Usa los números '1', '2', '3' y '4' para ordenar.\n")

    scenarios = [
        {"name": "Hacer un dibujo 🎨",
         "steps": ["Colorear el dibujo.", "Dibujar las formas con lápiz.", "Guardar el dibujo.", "Pensar qué quiero dibujar."],
         "correct_order_text": ["Pensar qué quiero dibujar.", "Dibujar las formas con lápiz.", "Colorear el dibujo.", "Guardar el dibujo."]},
        
        {"name": "Preparar la mochila para la escuela 🎒",
         "steps": ["Poner los cuadernos.", "Revisar la lista de la escuela.", "Poner la lonchera.", "Cerrar la mochila."],
         "correct_order_text": ["Revisar la lista de la escuela.", "Poner los cuadernos.", "Poner la lonchera.", "Cerrar la mochila."]},
        
        {"name": "Cuidar una planta 🌱",
         "steps": ["Ver crecer la planta.", "Poner la semilla en la tierra.", "Regar la planta.", "Ponerla al sol."],
         "correct_order_text": ["Poner la semilla en la tierra.", "Ponerla al sol.", "Regar la planta.", "Ver crecer la planta."]},
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
        
        user_order_nums = []
        user_order_text = []
        print("\n¡Dime el número de la acción para: Primero, Luego, Después, Al final!")
        keywords = ["Primero", "Luego", "Después", "Al final"]
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
            print("¡Increíble! 🎉 Tu orden es perfecta. ¡Tienes una mente muy ordenada!")
            score += 1
        else:
            print("¡Uhm, casi lo logras! 🤔 El orden correcto era:")
            for k, step_text in enumerate(s['correct_order_text']):
                print(f"  {keywords[k]}: {step_text}")
        time.sleep(6)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_scenarios} escenarios correctos. ¡Muy bien hecho! 👏")
    input("Presiona ENTER para el siguiente paso...")

def show_grouping_concept():
    """Explica y ejemplifica el concepto de clasificación por atributos."""
    show_header("Clasificando Cosas: Por Color, Tamaño o Qué Hacen")
    print("Recuerdan que las cosas que se parecen van juntas. ¡Ahora vamos a ver **por qué** se parecen!\n")
    print("Podemos clasificar por:")
    print("  🌈 **Color:** Todas las cosas rojas van aquí, todas las azules allá.")
    print("  📏 **Tamaño:** Los objetos grandes en un lado, los pequeños en otro.")
    print("  🛠️ **Función (Qué hacen):** Cosas que usas para comer, cosas que usas para jugar.\n")
    
    print("**Ejemplo:**")
    print("  - Una manzana roja y una cereza roja son rojas. ¡Van juntas por su **COLOR**!")
    print("  - Un elefante y un ratón son animales. ¡Pero uno es **GRANDE** y el otro es **PEQUEÑO**!")
    print("  - Un tenedor y una cuchara sirven para comer. ¡Van juntos por su **FUNCIÓN**!\n")
    
    print("¡Así, entendemos mejor cómo son las cosas!\n")
    input("Presiona ENTER para el juego de clasificar...")

def game_attribute_grouping():
    """Juego de clasificar objetos por atributos específicos."""
    show_header("Juego 2: ¡El Clasificador Inteligente!")
    print("Te daré unas palabras. Dime en qué grupo van, ¡pensando en su atributo principal! (Color, Tamaño, o Función)\n")
    
    items = [
        {"word": "sol", "group_type": "COLOR", "group_name": "AMARILLO", "emoji": "☀️"},
        {"word": "coche", "group_type": "TAMAÑO", "group_name": "GRANDE", "emoji": "🚗"},
        {"word": "lápiz", "group_type": "FUNCIÓN", "group_name": "PARA DIBUJAR/ESCRIBIR", "emoji": "✏️"},
        {"word": "hormiga", "group_type": "TAMAÑO", "group_name": "PEQUEÑO", "emoji": "🐜"},
        {"word": "árbol", "group_type": "COLOR", "group_name": "VERDE/CAFÉ", "emoji": "🌳"},
        {"word": "tijeras", "group_type": "FUNCIÓN", "group_name": "PARA CORTAR", "emoji": "✂️"},
    ]
    
    random.shuffle(items)
    score = 0
    num_items = 4 # Limitamos a 4 items

    print("Responde 'C' para Color, 'T' para Tamaño o 'F' para Función.\n")
    for i in range(num_items):
        item = items[i]
        print(f"\n--- Pregunta {i+1} de {num_items} ---")
        print(f"¿Por qué el/la '{item['word']}' ( {item['emoji']} ) va en el grupo de '{item['group_name']}'? ¿Por su COLOR, TAMAÑO o FUNCIÓN?")
        
        while True:
            user_input = input("Tu respuesta (C/T/F): ").upper().strip()
            if user_input in ['C', 'T', 'F']:
                break
            else:
                print("Por favor, escribe 'C', 'T' o 'F'.")
        
        correct_map = {"C": "COLOR", "T": "TAMAÑO", "F": "FUNCIÓN"}
        
        if correct_map.get(user_input) == item['group_type']:
            print(f"¡Súper! 🎉 Correcto. ¡Es por su **{item['group_type']}**!")
            score += 1
        else:
            print(f"¡Oh, no! 🤔 La razón principal es su **{item['group_type']}**.")
        time.sleep(4)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_items} items correctos. ¡Eres un clasificador de primera! 🏆")
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: ¡Organiza y Entiende Mejor! (2º Grado)")
        print("1. Introducción: ¡Somos Expertos en Ordenar!")
        print("2. Contando Pasos: Con Primero, Luego, Después, Al final")
        print("3. Jugar: ¡La Receta Secreta del Orden!")
        print("4. Clasificando Cosas: Por Color, Tamaño o Qué Hacen")
        print("5. Jugar: ¡El Clasificador Inteligente!")
        print("6. Salir de la Lección")
        print("=" * 65)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_sequence_concept()
        elif choice == '3':
            game_ordered_actions()
        elif choice == '4':
            show_grouping_concept()
        elif choice == '5':
            game_attribute_grouping()
        elif choice == '6':
            print("¡Adiós! ¡Sigue organizando el mundo con tu mente brillante! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
