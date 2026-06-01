import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 95)
    print(f"🗺️ {title.upper()} 🗺️")
    print("=" * 95)
    print()

def show_introduction():
    """Introduce los conceptos de elaboración de esquemas, relevancia y síntesis."""
    show_header("Introducción: ¡Arquitectos de Ideas Complejas!")
    print("¡Hola, jóvenes pensadores y futuros investigadores! 💡")
    print("En esta lección, vamos a aprender a construir argumentos y textos muy sólidos, como si fueran edificios.")
    print("Para ello, usaremos planos llamados **esquemas** y aprenderemos a elegir solo la información que realmente importa, incluso si viene de muchos lugares.\n")
    
    print("Con las habilidades de hoy, podrán:")
    print("   ✅ Planificar sus trabajos y ensayos antes de escribirlos.")
    print("   ✅ Elegir la mejor información para apoyar sus ideas.")
    print("   ✅ Combinar lo que aprenden de diferentes lugares para crear algo nuevo y fuerte.\n")
    
    print("¡Prepárense para ser los maestros en la organización y la construcción de conocimiento!\n")
    input("Presiona ENTER para comenzar a diseñar...")

def show_outlining_concept():
    """Explica el concepto de elaboración de esquemas."""
    show_header("Elaboración de Esquemas: ¡Los Planos de tu Argumento!")
    print("Un **esquema** es como un mapa o un plano de tu texto o argumento. Te ayuda a organizar tus ideas antes de empezar a escribir.\n")
    print("Tiene diferentes niveles:")
    print("  ⭐ **Tesis o Idea Principal:** Es la idea central de todo tu trabajo, lo que quieres demostrar o explicar. ¡Va al principio!")
    print("  ⭐ **Puntos Principales:** Son las ideas grandes que apoyan tu tesis. Cada una puede ser un párrafo.")
    print("  ⭐ **Evidencia/Detalles:** Son los datos, ejemplos, hechos o explicaciones que prueban tus puntos principales.\n")
    
    print("**Ejemplo de un Esquema Simple:**")
    print("  **Tema:** Por qué la lectura es importante para los estudiantes.")
    print("  **Tesis:** La lectura mejora muchas habilidades clave en los estudiantes.")
    print("    I. Punto Principal 1: La lectura mejora el vocabulario.")
    print("      A. Detalle/Evidencia: Al leer, encontramos palabras nuevas.")
    print("      B. Detalle/Evidencia: Usar un diccionario ayuda a aprender su significado.")
    print("    II. Punto Principal 2: La lectura fomenta la imaginación.")
    print("      A. Detalle/Evidencia: Las historias nos transportan a otros mundos.")
    print("      B. Detalle/Evidencia: Permite crear imágenes mentales de personajes y lugares.\n")
    
    print("¡Un buen esquema te ahorra tiempo y hace tu escritura mucho más clara!\n")
    input("Presiona ENTER para practicar con esquemas...")

def game_build_simple_outline():
    """Juego de construir un esquema simple para un tema dado."""
    show_header("Juego 1: ¡El Arquitecto de Esquemas!")
    print("Te daré un tema y una tesis. Tu misión es organizar los puntos principales y los detalles en un esquema.\n")

    scenarios = [
        {"topic": "La importancia del reciclaje",
         "thesis": "El reciclaje es crucial para proteger nuestro planeta y sus recursos.",
         "items": {
             "Punto Principal 1": "Reduce la contaminación.",
             "Detalle A (para P1)": "Menos basura en vertederos.",
             "Detalle B (para P1)": "Menos químicos en el aire y el agua.",
             "Punto Principal 2": "Ahorra recursos naturales.",
             "Detalle A (para P2)": "Reutiliza materiales como papel y plástico.",
             "Detalle B (para P2)": "Disminuye la necesidad de extraer nuevas materias primas."
         },
         "correct_order_keys": ["Punto Principal 1", "Detalle A (para P1)", "Detalle B (para P1)", "Punto Principal 2", "Detalle A (para P2)", "Detalle B (para P2)"]},
        
        {"topic": "Beneficios de hacer ejercicio",
         "thesis": "Hacer ejercicio regularmente trae muchos beneficios para nuestra salud física y mental.",
         "items": {
             "Punto Principal 1": "Mejora la salud del cuerpo.",
             "Detalle A (para P1)": "Fortalece músculos y huesos.",
             "Detalle B (para P1)": "Ayuda al corazón y pulmones.",
             "Punto Principal 2": "Beneficia la mente.",
             "Detalle A (para P2)": "Reduce el estrés y la ansiedad.",
             "Detalle B (para P2)": "Mejora el estado de ánimo y la concentración."
         },
         "correct_order_keys": ["Punto Principal 1", "Detalle A (para P1)", "Detalle B (para P1)", "Punto Principal 2", "Detalle A (para P2)", "Detalle B (para P2)"]},
    ]
    
    random.shuffle(scenarios)
    num_scenarios = 1 # Para enfocarse en la profundidad

    for i in range(num_scenarios):
        s = scenarios[i]
        print(f"\n--- Desafío {i+1} de {num_scenarios} ---")
        print(f"**Tema:** {s['topic']}")
        print(f"**Tesis:** {s['thesis']}\n")
        
        print("Ahora, vamos a construir el esquema. Tienes estas ideas:")
        numbered_items = list(s['items'].values())
        random.shuffle(numbered_items) # Mezcla las ideas para que el estudiante las ordene
        for j, item_text in enumerate(numbered_items):
            print(f"  {j+1}. {item_text}")
        
        user_outline = []
        print("\n¡Organiza las ideas en el esquema! Escribe el NÚMERO de la idea en el orden que va.")
        print("Usa 'P1' para Punto Principal 1, 'D1A' para Detalle 1A, etc.")
        
        key_mapping = {
            "Punto Principal 1": "I. Punto Principal 1",
            "Detalle A (para P1)": "  A. Detalle/Evidencia",
            "Detalle B (para P1)": "  B. Detalle/Evidencia",
            "Punto Principal 2": "II. Punto Principal 2",
            "Detalle A (para P2)": "  A. Detalle/Evidencia",
            "Detalle B (para P2)": "  B. Detalle/Evidencia"
        }

        # Simula la creación del esquema paso a paso
        print("\nIngresa los números de las ideas en el orden correcto para tu esquema:")
        
        # Mapping item_text to original key for later comparison
        text_to_key = {v: k for k, v in s['items'].items()}

        for k in range(len(s['correct_order_keys'])):
            while True:
                try:
                    choice_num = int(input(f"Qué va en el paso {k+1}?: "))
                    if 1 <= choice_num <= len(numbered_items) and numbered_items[choice_num-1] not in [item[1] for item in user_outline]:
                        # Add original key and text to user_outline
                        original_key = text_to_key[numbered_items[choice_num-1]]
                        user_outline.append((original_key, numbered_items[choice_num-1]))
                        break
                    else:
                        print("Ese número no es válido o ya lo usaste. Intenta de nuevo.")
                except ValueError:
                    print("Por favor, escribe un número.")
        
        print("\n¡Tu esquema propuesto es el siguiente!")
        print(f"**Tesis:** {s['thesis']}")
        for original_key, item_text in user_outline:
            # Check if it's a main point or a detail for printing
            if "Punto Principal" in original_key:
                print(f"  {key_mapping[original_key]}: {item_text}")
            else:
                # Find which main point this detail belongs to based on correct order
                # This is a simplification; in a real app, outline structure would be more robust
                if s['correct_order_keys'].index(original_key) < s['correct_order_keys'].index("Punto Principal 2"):
                     print(f"    {key_mapping[original_key]}: {item_text}")
                else:
                    # This logic assumes only two main points for simplicity
                    print(f"    {key_mapping[original_key]}: {item_text}")

        # Basic check for correctness (simplified for console)
        correct_count = 0
        for k in range(len(s['correct_order_keys'])):
            if s['items'][s['correct_order_keys'][k]] == user_outline[k][1]:
                correct_count += 1

        if correct_count == len(s['correct_order_keys']):
            print("\n¡Fabuloso! 🎉 Has construido el esquema perfectamente. ¡Eres un gran arquitecto de ideas!")
        else:
            print("\n¡Casi! 🤔 Repasa el orden y la relación entre los puntos principales y los detalles.")
            print("\n**El esquema correcto sería:**")
            print(f"**Tesis:** {s['thesis']}")
            for correct_key in s['correct_order_keys']:
                if "Punto Principal" in correct_key:
                    print(f"  {key_mapping[correct_key]}: {s['items'][correct_key]}")
                else:
                    print(f"    {key_mapping[correct_key]}: {s['items'][correct_key]}")
        
        time.sleep(12)
    
    print(f"\nJuego terminado. ¡Sigue practicando la construcción de esquemas! 📐")
    input("Presiona ENTER para el siguiente paso...")

def show_relevance_synthesis_concept():
    """Explica la relevancia de la información y la síntesis de múltiples fuentes."""
    show_header("Relevancia y Síntesis: ¡Juntando lo Más Importante!")
    print("Cuando investigas un tema, encuentras mucha información. ¡Pero no toda es igual de útil!\n")
    
    print("--- **Relevancia de la Información:** ¿Importa para mi punto? 🤔")
    print("  Una información es **relevante** si te ayuda DIRECTAMENTE a probar tu tesis o a explicar tus puntos principales.")
    print("  Si no está relacionada con tu tema o no ayuda a tu argumento, ¡es irrelevante y debes dejarla de lado!\n")
    print("  **Ejemplo:** Si tu tesis es 'Los perros son buenas mascotas', un dato sobre 'el tipo de comida favorita de los gatos' no es relevante.")

    print("\n--- **Síntesis de Múltiples Fuentes:** ¡Crea algo nuevo con lo que aprendes! 🧪")
    print("  **Sintetizar** es tomar ideas de diferentes textos o fuentes y combinarlas para formar un nuevo entendimiento o un argumento más fuerte.")
    print("  No es solo copiar y pegar, ¡es procesar y unir para crear tu propia visión!")
    print("  **Piensa en esto:**")
    print("    - Fuente 1 dice 'A es bueno porque B'.")
    print("    - Fuente 2 dice 'A también es bueno por C'.")
    print("    - **Tu síntesis:** 'A es bueno por B y C, lo cual demuestran ambas fuentes'.\n")
    
    print("¡Sintetizar y elegir la información relevante te hace un investigador muy poderoso!\n")
    input("Presiona ENTER para el desafío de relevancia y síntesis...")

def game_relevance_synthesis():
    """Juego de identificar información relevante y sintetizar de fuentes."""
    show_header("Juego 2: ¡El Investigador Experto!")
    print("Lee el tema de investigación. Luego, identifica la información más relevante y piensa cómo la sintetizarías.\n")
    
    challenges = [
        {"topic": "La importancia de las abejas para el medio ambiente.",
         "thesis": "Las abejas son fundamentales para la salud del ecosistema global.",
         "info_options": [
             "1. Las abejas viven en colmenas y son insectos pequeños.",
             "2. Las abejas polinizan las plantas, lo que es vital para la producción de alimentos y flores.",
             "3. Las abejas tienen aguijones para defenderse de los depredadores.",
             "4. Las abejas producen miel, que es un alimento dulce y natural.",
             "5. Sin la polinización de las abejas, muchas plantas no podrían reproducirse, afectando a otros animales."
         ],
         "relevant_nums": ["2", "4", "5"], # 4 can be argued as relevant for "salud del ecosistema" (food source)
         "synthesis_hint": "Combina la polinización con la producción de alimentos/flores y la conexión con la cadena alimenticia de otros animales. También puedes mencionar la miel como un producto valioso que aportan al ecosistema."
        },
        
        {"topic": "Por qué es importante proteger los océanos.",
         "thesis": "Los océanos son vitales para la vida en la Tierra y necesitan nuestra protección.",
         "info_options": [
             "1. Los océanos cubren la mayor parte de la superficie terrestre.",
             "2. Los océanos producen gran parte del oxígeno que respiramos.",
             "3. Muchos animales marinos están en peligro por la contaminación plástica.",
             "4. El agua del océano es salada y no se puede beber directamente.",
             "5. Los arrecifes de coral son ecosistemas marinos muy diversos y frágiles."
         ],
         "relevant_nums": ["2", "3", "5"],
         "synthesis_hint": "Conecta la producción de oxígeno con la vida en la Tierra, la amenaza de la contaminación a los animales y la importancia de los ecosistemas como los arrecifes."
        },
    ]
    
    random.shuffle(challenges)
    num_challenges = 1 # Para profundidad

    for i in range(num_challenges):
        c = challenges[i]
        print(f"\n--- Desafío {i+1} de {num_challenges} ---")
        print(f"**Tema de Investigación:** '{c['topic']}'")
        print(f"**Tu Tesis/Idea Central:** '{c['thesis']}'\n")
        
        print("Aquí tienes información que encontraste. ¿Qué números de la lista son **más relevantes** para tu tesis? (Separados por comas, ej. 1,3)")
        for j, info in enumerate(c['info_options']):
            print(f"  {j+1}. {info}")
        
        user_relevant_input = input("Números de la información más relevante: ").strip()
        user_relevant_nums = [n.strip() for n in user_relevant_input.split(',')]
        
        # Check relevance (simplified)
        if all(item in c['relevant_nums'] for item in user_relevant_nums) and len(user_relevant_nums) == len(c['relevant_relevant_nums']):
             print("¡Excelente! Has elegido la información más relevante. 🎉")
        else:
            print(f"¡Revisa! 🤔 La información más relevante para tu tesis sería: {', '.join(c['relevant_nums'])}. Recuerda que solo aquello que apoya directamente tu punto es relevante.")

        input("\nPresiona ENTER para la parte de Síntesis...")
        
        print(f"\n**Parte 2: ¡Sintetiza la Información!**")
        print("Ahora, con la información más relevante, ¿cómo combinarías las ideas para formar un párrafo coherente y apoyar tu tesis?")
        print(f"Pista para tu síntesis: {c['synthesis_hint']}")
        
        user_synthesis = input("Escribe tu síntesis de 2-3 oraciones: ").strip()
        print(f"\nTu síntesis: '{user_synthesis}'")
        print("\n¡Muy bien! Sintetizar es un paso clave para hacer tus argumentos fuertes y claros.")
        
        print("\n¡Has demostrado ser un investigador y organizador de información de alto nivel! 🏆")
        time.sleep(10)
    
    print(f"\nDesafío terminado. ¡Sigue practicando la relevancia y la síntesis! 🧪")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: Diseñando Argumentos y Sintetizando Fuentes (7º Grado)")
        print("1. Introducción: ¡Arquitectos de Ideas Complejas!")
        print("2. Elaboración de Esquemas: ¡Los Planos de tu Argumento!")
        print("3. Jugar: ¡El Arquitecto de Esquemas!")
        print("4. Relevancia y Síntesis: ¡Juntando lo Más Importante!")
        print("5. Jugar: ¡El Investigador Experto!")
        print("6. Salir de la Lección")
        print("=" * 95)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_outlining_concept()
        elif choice == '3':
            game_build_simple_outline()
        elif choice == '4':
            show_relevance_synthesis_concept()
        elif choice == '5':
            game_relevance_synthesis()
        elif choice == '6':
            print("¡Adiós, futuros expertos en la investigación y la argumentación! ¡El mundo necesita sus mentes organizadas! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
