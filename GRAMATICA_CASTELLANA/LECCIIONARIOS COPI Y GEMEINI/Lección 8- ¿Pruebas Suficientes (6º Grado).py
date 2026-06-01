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
    print(f"🕵️‍♀️ {title.upper()} 🕵️‍♀️")
    print("=" * 80)
    print()

def show_introduction():
    """Introduce los conceptos de generalización apresurada y falsa causa."""
    show_header("Introducción: Pensando con Pruebas y Conexiones")
    print("¡Hola, jóvenes detectives de la lógica! 🧠")
    print("Ya somos expertos en identificar ideas claras y evitar trucos.")
    print("Hoy vamos a subir un nivel. Vamos a aprender a ser más cuidadosos al conectar ideas:\n")
    
    print("1. 📉 **'Saltar a Conclusiones' (Generalización Apresurada):**")
    print("   Imagina que conoces a dos niños que les gusta mucho leer.")
    print("   Y dices: '¡Todos los niños que les gusta leer son muy callados!'")
    print("   ¿Conociste a *todos* los niños que leen? ¡No! Solo a dos.")
    print("   Es un **salto muy grande** de unas pocas pruebas a una idea que abarca a *todos* o *siempre*.\n")
    
    print("2. ⏰ **'Porque Pasó Antes, Entonces lo Causó' (Falsa Causa):**")
    print("   Imagina que te pones una camiseta amarilla y ese día te sacas un 10 en un examen.")
    print("   Y dices: '¡Siempre que me pongo mi camiseta amarilla me saco buenas notas!'")
    print("   ¿La camiseta realmente hizo que sacaras 10? Probablemente estudiaste bien.")
    print("   El hecho de que algo pase **antes** de otra cosa no significa que lo haya **causado**.\n")
    
    print("¡Aprendamos a pedir **más pruebas** y a buscar las **causas reales**!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de generalización apresurada y falsa causa."""
    show_header("Ejemplos: ¿Salto a Conclusión o Falsa Causa?")
    
    examples = [
        {"text": "Mi amiga María tiene el pelo rizado y es muy buena en matemáticas. Conclusión: 'Todas las niñas con pelo rizado son buenas en matemáticas.'", 
         "type": "SALTO", "explanation": "Conoces solo a una niña con pelo rizado. No puedes decir que todas lo son solo por ella."},
        {"text": "Me comí un helado y al día siguiente me dolió la barriga. Conclusión: 'Comer helado siempre me da dolor de barriga.'", 
         "type": "FALSA_CAUSA", "explanation": "El helado quizás no fue la causa real. Podría ser otra cosa que comiste o te sentiste mal por otra razón. ¡Pasó antes, pero no lo causó directamente!"},
        {"text": "Vi a un perro grande y ladró muy fuerte. Conclusión: 'Todos los perros grandes son malos y ladran fuerte.'", 
         "type": "SALTO", "explanation": "Viste solo a un perro. ¡Hay muchos perros grandes amigables que no ladran fuerte!"},
        {"text": "Cada vez que lavo mi carro, llueve al día siguiente. Conclusión: 'Lavar el carro hace que llueva.'", 
         "type": "FALSA_CAUSA", "explanation": "Lavar el carro no cambia el clima. Es solo una coincidencia que llueva después."},
        {"text": "Mi maestra siempre da exámenes difíciles.", 
         "type": "SALTO", "explanation": "¿Siempre? ¿Todos los exámenes? Quizás algunos son difíciles, pero no todos o siempre."},
        {"text": "Me levanté con el pie izquierdo y se me cayó el sándwich. Conclusión: 'Levantarse con el pie izquierdo trae mala suerte.'", 
         "type": "FALSA_CAUSA", "explanation": "El orden en que pones los pies al levantarte no causa que se te caiga el sándwich. Fue un accidente."},
    ]

    print("Lee cada frase y piensa si es un 'salto a conclusión' o una 'falsa causa'.\n")
    for i, ex in enumerate(examples):
        print(f"\n--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "SALTO":
            print(f"¡Es un SALTO A CONCLUSIÓN! 📉 {ex['explanation']}\n")
        else: # FALSA_CAUSA
            print(f"¡Es una FALSA CAUSA! ⏰ {ex['explanation']}\n")
        time.sleep(4)
        print("=" * 45)

    print("\n¡Ahora es tu turno de ser un verdadero detective de la lógica!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_logical_error():
    """Juego de identificar el tipo de error lógico."""
    show_header("Juego 1: ¡El Rastreador de Conexiones!")
    print("Te daré una situación y una conclusión. Dime si es un 'SALTO A CONCLUSIÓN' (S) o una 'FALSA CAUSA' (F).\n")
    print("Escribe 'S' para Salto a Conclusión o 'F' para Falsa Causa.\n")

    questions = [
        {"text": "Vi a dos niños en el parque que no compartían sus juguetes. Conclusión: 'Todos los niños de ese parque son egoístas.'", 
         "answer": "S", "explanation": "Solo viste a dos niños, no puedes juzgar a todos los niños del parque."},
        {"text": "Usé mis calcetines de la suerte y gané el partido. Conclusión: 'Mis calcetines de la suerte me hacen ganar.'", 
         "answer": "F", "explanation": "Los calcetines no tienen poder mágico para que ganes. Fue tu esfuerzo y el de tu equipo."},
        {"text": "En mi escuela, los estudiantes de 6º tienen mucha tarea. Conclusión: 'Todos los estudiantes de 6º en el mundo tienen mucha tarea.'", 
         "answer": "S", "explanation": "Tu escuela es solo una, no puedes generalizar a todas las escuelas del mundo."},
        {"text": "Me puse mi gorra al revés y ese día me resbalé. Conclusión: 'Ponerse la gorra al revés da mala suerte.'", 
         "answer": "F", "explanation": "La gorra no causó la caída, fue un accidente."},
        {"text": "Conocí a un doctor muy serio. Conclusión: 'Todos los doctores son muy serios.'", 
         "answer": "S", "explanation": "Conociste solo a uno. Hay doctores con todo tipo de personalidad."},
        {"text": "Cada vez que mi perro ladra, llega el cartero. Conclusión: 'Mi perro hace que el cartero venga.'", 
         "answer": "F", "explanation": "El cartero viene por su trabajo, no porque tu perro ladre. Coincide que ladra cuando llega."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Situación: '{q['text']}'")
        
        while True:
            user_input = input("¿'SALTO A CONCLUSIÓN' (S) o 'FALSA CAUSA' (F)?: ").upper().strip()
            if user_input in ['S', 'F']:
                break
            else:
                print("Por favor, escribe 'S' o 'F'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(4)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran rastreador de conexiones! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_fix_the_logic():
    """Juego de corregir la lógica de una afirmación."""
    show_header("Juego 2: ¡Arregla la Lógica!")
    print("Te daré una frase que tiene un error lógico (salto a conclusión o falsa causa).")
    print("Tu misión es escribirla de una forma más JUSTA y con una RAZÓN REAL.\n")

    corrections = [
        {"original": "Los estudiantes que usan gafas son los más inteligentes.", 
         "corrected_hint": "Algunos estudiantes que usan gafas son inteligentes, igual que otros que no usan gafas.", 
         "type": "SALTO", "explanation": "No puedes decir que *todos* los que usan gafas son los más inteligentes basándote en unos pocos."},
        {"original": "Desde que tengo mi nuevo juguete, siempre me va bien en el colegio.", 
         "corrected_hint": "Tener un nuevo juguete es divertido, pero mis buenas notas son porque estudio y me esfuerzo.", 
         "type": "FALSA_CAUSA", "explanation": "El juguete no causa tus buenas notas, es tu esfuerzo."},
        {"original": "Todos los deportes son peligrosos.", 
         "corrected_hint": "Algunos deportes tienen más riesgo, pero muchos son seguros y saludables.", 
         "type": "SALTO", "explanation": "Hay muchos deportes, no todos son peligrosos."},
        {"original": "Cuando mi gallo canta, sale el sol. El gallo hace que salga el sol.", 
         "corrected_hint": "El gallo canta cuando amanece, pero el sol sale porque la Tierra gira.", 
         "type": "FALSA_CAUSA", "explanation": "El canto del gallo no causa la salida del sol, es al revés."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase original con error: '{c['original']}'")
        print(f"Tipo de error: {'Salto a Conclusión' if c['type'] == 'SALTO' else 'Falsa Causa'}")
        print(f"Pista: {c['explanation']}")
        
        user_fixed_sentence = input("Escribe la frase de forma más justa y con razón real: ").strip()
        
        print(f"\nTu respuesta: '{user_fixed_sentence}'")
        print(f"Una forma de arreglarlo: '{c['corrected_hint']}'")
        print("\n¡Genial! ¡Has aprendido a arreglar la lógica de las ideas! 🎉")
        time.sleep(5)
    
    print(f"\nJuego terminado. ¡Eres un maestro arreglando la lógica!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_logic_error_example():
    """Permite al usuario crear su propio ejemplo de error lógico y corregirlo."""
    show_header("✍️ ¡Crea y Arregla Tus Propios Errores Lógicos! ✍️")
    print("Vamos a crear una frase con un 'salto a conclusión' o una 'falsa causa'.")
    print("Luego, tú la corregirás para que tenga una buena lógica.\n")

    while True:
        original_sentence = input("1. Escribe una frase con un 'salto a conclusión' o 'falsa causa' (Ej: 'Siempre que uso mi lápiz azul, mis dibujos quedan perfectos'): ").strip()
        if original_sentence:
            break
        else:
            print("Por favor, escribe una frase.")
    
    print(f"\nTu frase original con error: '{original_sentence}'")

    while True:
        fixed_sentence = input("2. Ahora, escribe la misma frase, pero con una lógica correcta y más justa (Ej: 'Mis dibujos quedan perfectos cuando me esfuerzo, no por el lápiz azul'): ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe la frase corregida.")

    print("\n--- ¡Tu Ejemplo Creado y Arreglado! ---")
    print(f"Tu frase con error lógico: '{original_sentence}' 📉⏰")
    print(f"Tu frase con lógica correcta: '{fixed_sentence}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a construir ideas con una lógica fuerte! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Pruebas Suficientes? (6º Grado)")
        print("1. Introducción: Pensando con Pruebas y Conexiones")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡El Rastreador de Conexiones!")
        print("4. Jugar: ¡Arregla la Lógica!")
        print("5. ✍️ ¡Crea y Arregla Tus Propios Errores Lógicos! ✍️")
        print("6. Salir de la Lección")
        print("=" * 80)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_logical_error()
        elif choice == '4':
            game_fix_the_logic()
        elif choice == '5':
            create_own_logic_error_example()
        elif choice == '6':
            print("¡Adiós! Sigue buscando las pruebas y las conexiones reales en todo lo que escuchas. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
