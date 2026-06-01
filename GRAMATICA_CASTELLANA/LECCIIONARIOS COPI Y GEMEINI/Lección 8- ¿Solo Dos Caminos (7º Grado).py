import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 85)
    print(f"🛤️ {title.upper()} 🛤️")
    print("=" * 85)
    print()

def show_introduction():
    """Introduce los conceptos de falso dilema y pendiente resbaladiza."""
    show_header("Introducción: Buscando Más Opciones y Cuidado con los Miedos Grandes")
    print("¡Hola, exploradores del pensamiento crítico! 🗺️")
    print("Ya sabemos cómo buscar la verdad y las buenas razones.")
    print("Hoy vamos a desenmascarar dos trucos de la comunicación que nos limitan o nos asustan:\n")
    
    print("1. 🛣️ **'Solo Hay Dos Caminos' (Falso Dilema):**")
    print("   A veces alguien dice: 'O estudias todo el tiempo, o no sacarás buenas notas.'")
    print("   ¿Es eso verdad? ¿No puedes estudiar un poco y también jugar, y aun así sacar buenas notas?")
    print("   Este truco nos hace creer que solo hay **dos opciones**, cuando en realidad hay **muchas más**.\n")
    
    print("2. 🎢 **'La Pendiente Resbaladiza' (Cadena de Miedos):**")
    print("   Imagina que alguien dice: 'Si no hacemos nuestra cama hoy, mañana no ordenaremos el cuarto, luego la casa será un desastre, y al final nos sacarán de casa.'")
    print("   ¿Un pequeño paso (no hacer la cama) realmente lleva a algo tan terrible (ser sacado de casa)?")
    print("   Este truco nos asusta al mostrar una **cadena de eventos cada vez peores**, sin pruebas de que realmente vayan a pasar.\n")
    
    print("¡Aprendamos a buscar todas las opciones y a no asustarnos con cadenas de miedos!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de falso dilema y pendiente resbaladiza."""
    show_header("Ejemplos: ¿Solo Dos Caminos o Cadena de Miedos?")
    
    examples = [
        {"text": "O amamos a todos los animales, o los odiamos a todos.", 
         "type": "DILEMA", "explanation": "¡No! Puedes amar a algunos y no a otros, o simplemente respetarlos sin amarlos a todos. Hay más opciones."},
        {"text": "Si te comes un solo dulce ahora, no podrás parar, te comerás todos los dulces de la casa y te enfermarás del estómago para siempre.", 
         "type": "PENDIENTE", "explanation": "Comer un dulce no significa que te vayas a comer TODOS ni que te enfermes para siempre. ¡Es una exageración de consecuencias!"},
        {"text": "O eres mi amigo, o eres mi enemigo.", 
         "type": "DILEMA", "explanation": "¡Hay muchas formas de relación! Puedes ser un compañero, un conocido, o simplemente alguien que no es ni amigo ni enemigo."},
        {"text": "Si dejamos que los niños jueguen videojuegos un poco, terminarán jugando todo el día, no estudiarán, no saldrán de casa y nunca tendrán amigos.", 
         "type": "PENDIENTE", "explanation": "Jugar un poco no significa que las consecuencias sean tan extremas. Se pueden establecer límites."},
        {"text": "Para estar sano, o haces ejercicio todo el día, o te enfermas.", 
         "type": "DILEMA", "explanation": "¡No! Puedes hacer ejercicio moderado, comer bien y descansar. No es todo o nada."},
        {"text": "Si el profesor nos da un poco más de tiempo para el proyecto, luego siempre querrán más tiempo para todo, no aprenderán a ser responsables y nunca entregarán nada a tiempo.", 
         "type": "PENDIENTE", "explanation": "Pedir un poco más de tiempo en un proyecto no significa que se vuelvan irresponsables para siempre. Es una exageración."},
    ]

    print("Lee cada frase y piensa si presenta 'solo dos caminos' o una 'cadena de miedos'.\n")
    for i, ex in enumerate(examples):
        print(f"\n--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "DILEMA":
            print(f"¡Es 'SOLO DOS CAMINOS'! 🛣️ {ex['explanation']}\n")
        else: # PENDIENTE
            print(f"¡Es una CADENA DE MIEDOS! 🎢 {ex['explanation']}\n")
        time.sleep(5)
        print("=" * 50)

    print("\n¡Ahora es tu turno de ser un detective de opciones y consecuencias!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_fallacy_type():
    """Juego de identificar el tipo de error lógico."""
    show_header("Juego 1: ¡El Detector de Trampas de Pensamiento!")
    print("Te daré una frase. Dime si es 'SOLO DOS CAMINOS' (C) o 'CADENA DE MIEDOS' (M).\n")
    print("Escribe 'C' para Solo Dos Caminos o 'M' para Cadena de Miedos.\n")

    questions = [
        {"text": "O eres muy bueno en los deportes, o eres muy malo.", 
         "answer": "C", "explanation": "Puedes ser regular, o bueno en algunos deportes y no en otros. Hay muchas posibilidades."},
        {"text": "Si permitimos a los alumnos usar sus teléfonos en clase, pronto no prestarán atención, no aprenderán nada, y la escuela se convertirá en un desorden.", 
         "answer": "M", "explanation": "Usar el teléfono un poco no lleva necesariamente a un desorden total."},
        {"text": "O te gusta toda la comida del colegio, o no te gusta nada.", 
         "answer": "C", "explanation": "Puedes que te gusten algunas cosas y otras no."},
        {"text": "Si le doy un postre a mi perro, luego querrá comer solo postres, se enfermará, y no podrá correr ni jugar.", 
         "answer": "M", "explanation": "Un postre no significa que solo querrá eso ni que enfermará tan gravemente."},
        {"text": "O apoyamos esta idea ahora, o todo el proyecto fracasará.", 
         "answer": "C", "explanation": "Puede haber otras formas de apoyar el proyecto o de que salga adelante, incluso sin esa idea."},
        {"text": "Si un estudiante copia en un examen, entonces copiará en todos los exámenes, luego copiará en la universidad, y al final no encontrará trabajo y vivirá sin dinero.", 
         "answer": "M", "explanation": "Copiar una vez no significa que su vida se arruinará de esa manera. Es una exageración de las consecuencias."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿'SOLO DOS CAMINOS' (C) o 'CADENA DE MIEDOS' (M)?: ").upper().strip()
            if user_input in ['C', 'M']:
                break
            else:
                print("Por favor, escribe 'C' o 'M'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(5)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detector de trampas! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_find_more_options():
    """Juego de encontrar más opciones para un falso dilema o detener una cadena de miedos."""
    show_header("Juego 2: ¡Amplía las Opciones y Detén los Miedos!")
    print("Te daré una frase que usa 'solo dos caminos' o una 'cadena de miedos'.")
    print("Tu misión es pensar en **más opciones** o explicar por qué la **cadena de miedos no es real**.\n")

    corrections = [
        {"original": "O te gusta el chocolate, o no te gusta ningún dulce.", 
         "type": "DILEMA", "corrected_hint": "Pueden gustarme otros dulces como las gominolas o caramelos. O me puede gustar un poco el chocolate, no todo.",
         "explanation": "No es solo chocolate o nada. Hay muchos otros dulces."},
        {"original": "Si hoy no me acuesto temprano, mañana me levantaré tarde, llegaré tarde al colegio, me regañarán y reprobaré el año.", 
         "type": "PENDIENTE", "corrected_hint": "Si me acuesto un poco tarde, quizás esté un poco cansado, pero puedo levantarme a tiempo y esforzarme en el colegio para no reprobar.",
         "explanation": "Una sola noche no arruina todo el año. Hay formas de recuperarse."},
        {"original": "En mi proyecto, o lo hago yo solo, o no saldrá bien.", 
         "type": "DILEMA", "corrected_hint": "Puedo pedir ayuda a un compañero o a la maestra. Así saldrá aún mejor y aprendo a colaborar.",
         "explanation": "Hay más formas de hacer el proyecto que solo tú, y trabajar en equipo puede ser bueno."},
        {"original": "Si los vecinos usan un poco de música, luego la pondrán muy alta, nos molestarán toda la noche y nunca podremos dormir.", 
         "type": "PENDIENTE", "corrected_hint": "Si ponen música un poco alta, puedo ir a hablar con ellos o cerrar la ventana. No significa que nos molesten toda la noche y nunca podamos dormir.",
         "explanation": "Hay soluciones antes de que las cosas escalen a ese nivel."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase con trampa: '{c['original']}'")
        print(f"Tipo de trampa: {'Solo Dos Caminos' if c['type'] == 'DILEMA' else 'Cadena de Miedos'}")
        print(f"Pista para pensar: {c['explanation']}")
        
        user_fixed_sentence = input("Escribe cómo lo resolverías, con más opciones o deteniendo la cadena: ").strip()
        
        print(f"\nTu respuesta: '{user_fixed_sentence}'")
        print(f"Una forma de pensarlo: '{c['corrected_hint']}'")
        print("\n¡Excelente! ¡Has aprendido a pensar en más opciones y a no caer en los miedos! 🎉")
        time.sleep(6)
    
    print(f"\nJuego terminado. ¡Eres un maestro encontrando opciones y desmintiendo miedos!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_fallacy_example():
    """Permite al usuario crear su propio ejemplo de falso dilema o pendiente resbaladiza y corregirlo."""
    show_header("✍️ ¡Crea y Arregla Tus Propias Trampas de Pensamiento! ✍️")
    print("Vamos a crear una frase que presente 'solo dos caminos' o una 'cadena de miedos'.")
    print("Luego, tú la corregirás para que sea más justa y verdadera.\n")

    while True:
        original_sentence = input("1. Escribe una frase con un 'solo dos caminos' o 'cadena de miedos' (Ej: 'O me das mi pelota, o no juego más contigo'): ").strip()
        if original_sentence:
            break
        else:
            print("Por favor, escribe una frase.")
    
    print(f"\nTu frase original con trampa: '{original_sentence}'")

    while True:
        fixed_sentence = input("2. Ahora, escribe cómo la corregirías, buscando más opciones o deteniendo la cadena de miedos (Ej: 'Si me das mi pelota, podemos seguir jugando, y si no, quizás podríamos turnarnos'): ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe la frase corregida.")

    print("\n--- ¡Tu Ejemplo Creado y Arreglado! ---")
    print(f"Tu frase con trampa: '{original_sentence}' 🛣️🎢")
    print(f"Tu frase con lógica correcta: '{fixed_sentence}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a construir ideas con opciones y sin miedos exagerados! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Solo Dos Caminos? (7º Grado)")
        print("1. Introducción: Buscando Más Opciones y Cuidado con los Miedos Grandes")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡El Detector de Trampas de Pensamiento!")
        print("4. Jugar: ¡Amplía las Opciones y Detén los Miedos!")
        print("5. ✍️ ¡Crea y Arregla Tus Propias Trampas de Pensamiento! ✍️")
        print("6. Salir de la Lección")
        print("=" * 85)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_fallacy_type()
        elif choice == '4':
            game_find_more_options()
        elif choice == '5':
            create_own_fallacy_example()
        elif choice == '6':
            print("¡Adiós! Sigue buscando todas las opciones y no te dejes asustar por cadenas de miedos. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
