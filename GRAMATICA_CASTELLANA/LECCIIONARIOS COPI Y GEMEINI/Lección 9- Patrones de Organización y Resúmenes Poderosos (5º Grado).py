import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 80)
    print(f"🗺️ {title.upper()} 🗺️")
    print("=" * 80)
    print()

def show_introduction():
    """Introduce los conceptos de patrones de organización y resúmenes."""
    show_header("Introducción: ¡Navegando por la Información!")
    print("¡Hola, exploradores del conocimiento! 🚀")
    print("Hasta ahora, hemos aprendido a encontrar lo más importante en un texto y a seguir el orden de los sucesos.")
    print("Hoy, vamos a descubrir los 'mapas secretos' que usan los escritores para organizar sus ideas: los **patrones de organización**.\n")
    
    print("También aprenderemos a crear **resúmenes poderosos**, que son como versiones 'mini' de lo que leemos, ¡pero con toda la información clave!\n")
    
    print("Esto les ayudará a:")
    print("   ✅ Entender textos más rápido y mejor.")
    print("   ✅ Recordar lo que leen fácilmente.")
    print("   ✅ Explicar temas complicados de forma sencilla.\n")
    
    input("Presiona ENTER para descifrar estos patrones...")

def show_organizational_patterns_concept():
    """Explica los patrones comunes de organización textual."""
    show_header("Patrones de Organización: ¿Cómo Están Hechas las Ideas?")
    print("Los autores no ponen las ideas de cualquier forma. ¡Usan 'patrones' o 'formas' para que entendamos mejor!\n")
    print("Vamos a ver tres de los más comunes:")
    
    print("\n--- 1. **Secuencia Cronológica (Orden del Tiempo)** ⏳")
    print("   **¿Cómo es?** Las ideas se presentan en el orden en que suceden los eventos, paso a paso, de principio a fin.")
    print("   **Palabras clave:** Primero, luego, después, antes, siguiente, finalmente, fechas (1990, 2005), años después, durante.")
    print("   **Ejemplo:** 'El Imperio Romano **comenzó** en el año 27 a.C. **Luego**, se expandió por gran parte de Europa. **Finalmente**, cayó en el año 476 d.C.'")

    print("\n--- 2. **Causa y Efecto** ➡️")
    print("   **¿Cómo es?** Se explica por qué algo sucede (la causa) y qué resultados tiene (el efecto).")
    print("   **Palabras clave:** Porque, debido a, a causa de, por eso, por consiguiente, el resultado fue, si... entonces.")
    print("   **Ejemplo:** '**Debido a** la sequía prolongada, los cultivos no crecieron bien, **por eso** hubo escasez de alimentos.'")

    print("\n--- 3. **Comparación y Contraste** ⚖️")
    print("   **¿Cómo es?** Se muestran las similitudes (comparación) y las diferencias (contraste) entre dos o más cosas.")
    print("   **Palabras clave:** Similar a, también, ambos, igual que, a diferencia de, en contraste con, pero, mientras que, por otro lado.")
    print("   **Ejemplo:** 'Los perros son **similares** a los lobos en su linaje. **Sin embargo**, los perros han sido domesticados, **mientras que** los lobos siguen siendo salvajes.'\n")
    
    print("¡Identificar estos patrones es como tener un mapa para leer!\n")
    input("Presiona ENTER para el juego de patrones...")

def game_identify_pattern():
    """Juego de identificar el patrón de organización en textos cortos."""
    show_header("Juego 1: ¡El Detective de Patrones!")
    print("Te daré un texto corto. Lee con atención y dime qué **patrón de organización** usa.\n")
    print("Elige 'S' para Secuencia, 'CE' para Causa y Efecto, o 'CC' para Comparación y Contraste.\n")

    questions = [
        {"text": "Primero, se calienta el agua en una olla. Después, se añade la pasta y se cocina por diez minutos. Finalmente, se escurre el agua y se sirve con salsa.", 
         "answer": "S", "pattern_name": "Secuencia Cronológica", "explanation": "Describe los pasos en orden de tiempo."},
        
        {"text": "Debido a que el glaciar se derritió, el nivel del mar en esa zona ha subido considerablemente, causando inundaciones en la costa.", 
         "answer": "CE", "pattern_name": "Causa y Efecto", "explanation": "El derretimiento (causa) llevó a la subida del mar e inundaciones (efecto)."},
        
        {"text": "Las manzanas son rojas y crujientes, mientras que las bananas son amarillas y suaves. Ambas son frutas, pero su sabor y textura son muy diferentes.", 
         "answer": "CC", "pattern_name": "Comparación y Contraste", "explanation": "Muestra similitudes (frutas) y diferencias (color, textura)."},
        
        {"text": "En 1492, Cristóbal Colón llegó a América. Luego, se establecieron las primeras colonias europeas. Más tarde, los nuevos países declararon su independencia.", 
         "answer": "S", "pattern_name": "Secuencia Cronológica", "explanation": "Eventos históricos presentados en orden temporal."},
        
        {"text": "Si una persona no duerme lo suficiente, su concentración disminuye y puede sentirse muy cansada durante el día. Por eso, es importante descansar bien.", 
         "answer": "CE", "pattern_name": "Causa y Efecto", "explanation": "La falta de sueño (causa) lleva a la disminución de la concentración y cansancio (efecto)."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 3 # Limitamos a 3 preguntas

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Texto: '{q['text']}'")
        
        while True:
            user_input = input("¿Qué patrón usa? (S/CE/CC): ").upper().strip()
            if user_input in ['S', 'CE', 'CC']:
                break
            else:
                print("Por favor, escribe 'S', 'CE' o 'CC'.")
        
        if user_input == q['answer']:
            print(f"¡Correcto! 🎉 Es un patrón de **{q['pattern_name']}**.")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print(f"¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}' ({q['pattern_name']}). Explicación: {q['explanation']}")
        time.sleep(7)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un maestro de los patrones! 🧭")
    input("Presiona ENTER para el siguiente paso...")

def show_summarizing_concept():
    """Explica el concepto de elaboración de resúmenes."""
    show_header("Elaborando Resúmenes: ¡La Esencia de la Información!")
    print("Un **resumen** es una versión corta de un texto más largo que solo incluye las **ideas más importantes**.\n")
    print("Piensa en él como la 'versión exprés' de lo que leíste. ¡Debes quitar los detalles menos importantes y dejar solo lo esencial!\n")
    
    print("**Para hacer un buen resumen, pregúntate:**")
    print("  1. ¿De qué se trata el texto? (La idea principal)")
    print("  2. ¿Cuáles son los puntos más importantes que explica el autor?")
    print("  3. ¿Puedo decirlo con mis propias palabras, sin copiar frases completas?\n")
    
    print("**Ejemplo:**")
    print("  **Texto original:** 'Los osos polares viven en las regiones frías del Ártico. Tienen una capa gruesa de grasa y pelaje blanco que les ayuda a camuflarse en la nieve. Se alimentan principalmente de focas, que cazan en el hielo marino. Debido al cambio climático, su hábitat se está derritiendo, lo que los pone en peligro.'")
    print("\n  **Resumen:** 'Los osos polares son animales árticos adaptados al frío y cazan focas. Su hábitat está en peligro por el cambio climático.'\n")
    
    print("¡Un buen resumen es claro, conciso y completo con lo importante!\n")
    input("Presiona ENTER para el juego de resúmenes...")

def game_summarize_text():
    """Juego de identificar el mejor resumen para un texto dado."""
    show_header("Juego 2: ¡El Súper Resumidor!")
    print("Lee el texto. Luego, elige la opción que sea el **mejor resumen**.\n")
    
    texts = [
        {"original_text": "El ciclo del agua describe cómo el agua se mueve en la Tierra. Primero, el sol calienta el agua de los océanos y ríos, y se evapora subiendo al cielo. Luego, el vapor de agua forma nubes. Después, cuando las nubes están llenas, el agua cae como lluvia o nieve. Finalmente, el agua regresa a los ríos y océanos, y el ciclo comienza de nuevo.", 
         "summary_options": ["A) El sol calienta el agua.", "B) El agua se mueve en un ciclo: se evapora, forma nubes y cae como lluvia para volver a los océanos.", "C) Llueve o nieva y el agua regresa al océano."], 
         "correct_summary": "B", "explanation": "La opción B resume todo el ciclo del agua de forma concisa y completa."},
        
        {"original_text": "Los volcanes son montañas con una abertura, llamadas cráter, por donde pueden salir materiales calientes del interior de la Tierra. Cuando un volcán entra en erupción, expulsa lava, ceniza y gases. Estas erupciones pueden ser peligrosas, pero también son responsables de formar nuevas tierras y enriquecer el suelo.", 
         "summary_options": ["A) Los volcanes son montañas peligrosas.", "B) Los volcanes expulsan lava y ceniza.", "C) Los volcanes son aberturas en la Tierra que expulsan materiales calientes, con peligros y beneficios."], 
         "correct_summary": "C", "explanation": "La opción C captura la esencia del volcán, sus actividades y sus efectos."},
    ]
    
    random.shuffle(texts)
    score = 0
    num_texts = 2 # Limitamos a 2 textos

    for i in range(num_texts):
        t = texts[i]
        print(f"\n--- Texto {i+1} de {num_texts} ---")
        print(f"**Texto Original:**\n'{t['original_text']}'")
        
        print("\n¿Cuál es el MEJOR resumen?")
        for j, option in enumerate(t['summary_options']):
            print(f"  {chr(65+j)}) {option}") # A, B, C
        
        while True:
            user_input = input("Tu respuesta (A, B o C): ").upper().strip()
            if user_input in ['A', 'B', 'C']:
                break
            else:
                print("Por favor, escribe 'A', 'B' o 'C'.")
        
        if user_input == t['correct_summary']:
            print("¡Perfecto! 🎉 ¡Ese es un resumen excelente!")
            print(f"Explicación: {t['explanation']}")
            score += 1
        else:
            print(f"¡Oops! No es el mejor resumen. 🤔")
            print(f"La respuesta correcta era '{t['correct_summary']}'. Explicación: {t['explanation']}")
        time.sleep(8)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_texts} resúmenes correctos. ¡Eres un súper resumidor! 🏆")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: Patrones de Organización y Resúmenes Poderosos (5º Grado)")
        print("1. Introducción: ¡Navegando por la Información!")
        print("2. Patrones de Organización: ¿Cómo Están Hechas las Ideas?")
        print("3. Jugar: ¡El Detective de Patrones!")
        print("4. Elaborando Resúmenes: ¡La Esencia de la Información!")
        print("5. Jugar: ¡El Súper Resumidor!")
        print("6. Salir de la Lección")
        print("=" * 80)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_organizational_patterns_concept()
        elif choice == '3':
            game_identify_pattern()
        elif choice == '4':
            show_summarizing_concept()
        elif choice == '5':
            game_summarize_text()
        elif choice == '6':
            print("¡Adiós, futuros genios de la lectura y la escritura! ¡Sigan organizando y resumiendo el mundo! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
