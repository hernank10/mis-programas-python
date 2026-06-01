import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("+" * 60)
    print(f"✨ {title.upper()} ✨")
    print("+" * 60)
    print()

def show_introduction():
    """Introduce el concepto de ideas con sentido y sin sentido."""
    show_header("Introducción: Ideas con Sentido y Sin Sentido")
    print("¡Hola, pequeños exploradores de ideas! 👋")
    print("En 1.er grado aprendimos a escuchar, pensar y hablar con claridad y respeto.")
    print("Hoy vamos a jugar a detectives de ideas. 🕵️‍♂️")
    print("Vamos a aprender a saber cuándo una idea **'tiene sentido'** (es clara y verdadera) ")
    print("y cuándo una idea **'no tiene mucho sentido'** (es confusa o no es verdad).\n")
    
    print("Mira estos ejemplos:")
    print("1. 'Mi perro ladra y mueve la cola cuando estoy feliz.' -> ¡Tiene sentido! Los perros hacen eso.")
    print("2. 'Mi perro vuela y habla español cuando estoy triste.' -> ¡No tiene sentido! Los perros no vuelan ni hablan español.\n")
    
    print("Es importante saber si una idea tiene sentido para entender mejor el mundo y a los demás.")
    input("Presiona ENTER para ver más ejemplos...")

def show_examples():
    """Muestra ejemplos de ideas con y sin sentido."""
    show_header("Ejemplos: ¿Tiene Sentido o No Tiene Sentido?")
    
    examples = [
        {"text": "Los peces nadan en el agua.", "sense": True, "explanation": "¡Sí! Los peces viven en el agua y nadan."},
        {"text": "Los pájaros caminan bajo tierra.", "sense": False, "explanation": "¡No! Los pájaros vuelan en el cielo."},
        {"text": "Las manzanas crecen en los árboles.", "sense": True, "explanation": "¡Sí! Las manzanas son frutas de los árboles."},
        {"text": "Los coches comen hierba para funcionar.", "sense": False, "explanation": "¡No! Los coches usan gasolina o electricidad, no comen hierba."},
        {"text": "Cuando llueve, el suelo se moja.", "sense": True, "explanation": "¡Sí! El agua de la lluvia moja el suelo."},
        {"text": "Para dormir, tengo que saltar muy alto.", "sense": False, "explanation": "¡No! Para dormir, te acuestas y cierras los ojos."},
    ]

    print("Lee cada frase y piensa si 'tiene sentido' o 'no tiene sentido'.\n")
    for i, ex in enumerate(examples):
        print(f"--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['sense']:
            print(f"¡Sí, tiene sentido! ✅ {ex['explanation']}\n")
        else:
            print(f"¡No tiene sentido! ❌ {ex['explanation']}\n")
        time.sleep(2)
        print("-" * 30)

    print("\n¡Ahora es tu turno de descubrir si las ideas tienen sentido!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_sense_or_nonsense():
    """Juego de identificar si una frase tiene sentido."""
    show_header("Juego 1: ¡Detectives de Ideas!")
    print("Te daré una frase. Tienes que decir si 'TIENE SENTIDO' (es verdad y clara) o 'NO TIENE SENTIDO' (es rara o falsa).\n")
    print("Escribe 'S' para 'SÍ tiene sentido' o 'N' para 'NO tiene sentido'.\n")

    questions = [
        {"text": "El sol es una estrella que nos da luz.", "answer": "S", "explanation": "El sol es una estrella gigante y nos ilumina."},
        {"text": "Los conejos tienen alas y vuelan al colegio.", "answer": "N", "explanation": "Los conejos no tienen alas ni vuelan."},
        {"text": "Si tengo sed, bebo agua.", "answer": "S", "explanation": "Cuando tenemos sed, el agua nos ayuda."},
        {"text": "Un elefante es más pequeño que un ratón.", "answer": "N", "explanation": "Los elefantes son muy grandes, mucho más que un ratón."},
        {"text": "Las flores necesitan agua y sol para crecer.", "answer": "S", "explanation": "Las plantas necesitan agua y sol para vivir."},
        {"text": "Mi mochila está hecha de nubes.", "answer": "N", "explanation": "Las mochilas se hacen con tela o plástico, no con nubes."},
        {"text": "Si estudio, aprendo cosas nuevas.", "answer": "S", "explanation": "Estudiar nos ayuda a saber más."},
        {"text": "Los árboles hablan con las personas.", "answer": "N", "explanation": "Los árboles no hablan como nosotros."},
        {"text": "Me lavo los dientes con jabón.", "answer": "N", "explanation": "Nos lavamos los dientes con pasta de dientes."},
        {"text": "Si comes frutas y verduras, tu cuerpo estará fuerte.", "answer": "S", "explanation": "Comer sano nos da energía y salud."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 5 # Limitamos a 5 para que no sea muy largo

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿Tiene sentido? (S/N): ").upper().strip()
            if user_input in ['S', 'N']:
                break
            else:
                print("Por favor, escribe 'S' o 'N'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(2)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Excelente trabajo de detective! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_whats_missing():
    """Juego de completar ideas para que tengan sentido."""
    show_header("Juego 2: ¡Completa la Idea!")
    print("Te daré una frase a la que le falta algo. Tú escribirás una palabra para que la frase 'tenga sentido'.\n")

    completions = [
        {"sentence": "Los __________ vuelan en el cielo.", "missing": "pájaros", "options": ["peces", "pájaros", "mesas"]},
        {"sentence": "Para escribir, uso un ___________.", "missing": "lápiz", "options": ["cuchara", "lápiz", "calcetín"]},
        {"sentence": "El pan se come con __________.", "missing": "boca", "options": ["pie", "ojo", "boca"]},
        {"sentence": "Un pez vive en el __________.", "missing": "agua", "options": ["árbol", "agua", "cama"]},
        {"sentence": "Por la noche, vemos las ___________ en el cielo.", "missing": "estrellas", "options": ["flores", "estrellas", "coches"]},
        {"sentence": "Si tengo frío, me pongo un __________.", "missing": "abrigo", "options": ["sombrero", "abrigo", "gafas"]},
    ]
    
    random.shuffle(completions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        c = completions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Completa la frase: '{c['sentence']}'")
        print(f"Opciones: {', '.join(c['options'])}")
        
        user_input = input("Mi palabra es: ").lower().strip()
        
        if user_input == c['missing']:
            print(f"¡Muy bien! ¡'{c['missing']}' es la palabra que tiene sentido! 🎉")
            score += 1
        else:
            print(f"Oops. La palabra que más sentido tenía era '{c['missing']}'. ¡Sigue intentándolo!")
        time.sleep(2)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Excelente completando ideas!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_sense_example():
    """Permite al usuario crear su propio ejemplo de frase con sentido y sin sentido."""
    show_header("✍️ ¡Crea Tus Propias Frases! ✍️")
    print("Vamos a crear tus propias frases que tengan sentido y otras que no lo tengan.\n")

    # Frase con sentido
    print("\n--- Frase que SÍ tiene sentido ---")
    user_sense_sentence = input("Escribe una frase que sea clara y verdadera (Ej: 'Los patos nadan en la laguna'): ").strip()
    if not user_sense_sentence:
        print("No escribiste una frase. Intenta de nuevo.")
        input("Presiona ENTER para volver al menú...")
        return

    # Frase sin sentido
    print("\n--- Frase que NO tiene sentido ---")
    user_nonsense_sentence = input("Escribe una frase que sea rara o que no sea verdad (Ej: 'Los patos hablan por teléfono'): ").strip()
    if not user_nonsense_sentence:
        print("No escribiste una frase. Intenta de nuevo.")
        input("Presiona ENTER para volver al menú...")
        return

    print("\n--- ¡Tus Frases Creadas! ---")
    print(f"Tu frase que SÍ tiene sentido: '{user_sense_sentence}' ✅")
    print(f"Tu frase que NO tiene sentido: '{user_nonsense_sentence}' ❌")
    print("\n¡Qué creativo! ¡Has hecho un gran trabajo identificando el sentido de las palabras! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Tiene Sentido? (2º Grado)")
        print("1. Introducción: Ideas con Sentido")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡Detectives de Ideas!")
        print("4. Jugar: ¡Completa la Idea!")
        print("5. ✍️ ¡Crea Tus Propias Frases! ✍️") # Nueva opción
        print("6. Salir de la Lección")
        print("+" * 60)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_sense_or_nonsense()
        elif choice == '4':
            game_whats_missing()
        elif choice == '5': # Nueva opción
            create_own_sense_example()
        elif choice == '6':
            print("¡Hasta la próxima! Sigue pensando: ¿Tiene sentido? 🤔👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
