import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("*" * 50)
    print(f"🌟 {title.upper()} 🌟")
    print("*" * 50)
    print()

def show_story():
    """Muestra un cuento corto para introducir el tema."""
    show_header("Cuento: El Problema de los Juguetes")
    
    story_text = """
    Había una vez, en un salón de clases, dos amigos, Leo y Sofía.
    Estaban jugando con los bloques de construcción.

    Leo quería construir una torre muy alta, y Sofía quería construir una casa para su muñeco.
    De repente, Leo tomó el bloque rojo grande que Sofía quería.

    Sofía se enojó y dijo: "¡Siempre me quitas mis cosas! ¡Eres malo!" 😠
    Leo se sintió triste y dijo: "Pero si yo solo quería ponerlo aquí para que fuera más fuerte..." 😢

    La maestra se acercó y les preguntó: "¿Qué pasó aquí, pequeños?"
    Sofía, aún un poco enojada, repitió: "¡Él siempre me quita todo!"
    La maestra preguntó a Leo: "¿Es cierto, Leo? ¿Siempre le quitas las cosas a Sofía?"
    Leo respondió: "No, maestra. Solo quería el bloque rojo para mi torre. Pensé que no lo estaba usando."

    La maestra dijo: "¡Ah! Parece que hubo un malentendido. Sofía, ¿escuchaste lo que Leo quería hacer? Leo, ¿preguntaste a Sofía si podías tomar el bloque?"
    Ambos negaron con la cabeza.

    La maestra sonrió y dijo: "A veces, cuando nos enojamos, decimos cosas sin pensar o sin escuchar bien. Es importante **escuchar** lo que el otro dice, **pensar** en lo que queremos decir, y luego **hablar** con claridad y con respeto."

    Sofía y Leo se miraron.
    Sofía dijo: "Lo siento, Leo. No te escuché."
    Leo dijo: "Lo siento, Sofía. Debí haberte preguntado."

    Compartieron el bloque rojo, y juntos construyeron una torre con una casita arriba. 😊🏠
    """
    
    for line in story_text.split('\n'):
        print(line)
        time.sleep(0.5) # Pausa para que puedan leer cómodamente
    
    print("\n¿Qué aprendimos del cuento?")
    input("Presiona ENTER para continuar...")

def show_rules():
    """Muestra las reglas básicas."""
    show_header("Nuestras Reglas para Hablar y Escuchar")
    print("Para llevarnos bien y entender a los demás, vamos a recordar 3 reglas muy importantes:\n")
    
    print("1. 👂 **ESCUCHA BIEN:**")
    print("   Cuando alguien habla, pon mucha atención. No interrumpas. Intenta entender lo que quiere decir.\n")
    print("2. 🧠 **PIENSA ANTES DE HABLAR:**")
    print("   Antes de decir algo, pregúntate: '¿Es verdad lo que voy a decir?' '¿Ayuda lo que voy a decir?' '¿Lo entenderán bien?'\n")
    print("3. 🗣️ **HABLA CON CLARIDAD Y RESPETO:**")
    print("   Usa palabras fáciles de entender. No grites. No digas cosas feas de los demás. Podemos no estar de acuerdo, pero siempre con respeto.\n")
    
    print("¡Practiquemos estas reglas!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_listen_and_repeat():
    """Juego de escuchar y repetir (simulado)."""
    show_header("Juego 1: ¡Escucho con Atención!")
    print("Te voy a dar una instrucción o una frase. Intenta 'repetirla' en tu mente o en voz baja exactamente como la escuchaste.")
    print("Luego, te haré una pregunta para ver si la entendiste bien.\n")

    phrases = [
        {"text": "El perro marrón corre rápido en el parque.", "q": "¿De qué color es el perro?", "ans": "marrón"},
        {"text": "Mi juguete favorito es un coche azul con ruedas grandes.", "q": "¿Qué tipo de juguete es mi favorito?", "ans": "coche"},
        {"text": "Para pintar, necesitamos pinceles y muchos colores.", "q": "¿Qué necesitamos para pintar, además de pinceles?", "ans": "colores"},
        {"text": "Hoy vamos a comer manzanas rojas y plátanos amarillos.", "q": "¿Qué color son las manzanas?", "ans": "rojas"},
        {"text": "El gato duerme en la cama suave al lado de la ventana.", "q": "¿Dónde duerme el gato?", "ans": "cama"},
    ]
    
    random.shuffle(phrases)
    score = 0

    for i, p in enumerate(phrases[:3]): # Solo 3 para no alargar demasiado
        print(f"\n--- Ronda {i+1} ---")
        print(f"Escucha bien: '{p['text']}'")
        time.sleep(2) # Pausa para "escuchar"
        user_answer = input(f"{p['q']} (Escribe tu respuesta): ").lower().strip()

        if user_answer == p['ans']:
            print("¡Muy bien! ¡Escuchaste con atención! 🎉")
            score += 1
        else:
            print(f"Casi... la respuesta era '{p['ans']}'. ¡No te preocupes, sigamos escuchando!")
        time.sleep(2)
    
    print(f"\nTerminamos. Obtuviste {score} de 3. ¡Excelente escucha!👂")
    input("Presiona ENTER para el siguiente juego...")

def game_think_before_speak():
    """Juego de pensar antes de hablar."""
    show_header("Juego 2: ¡Pienso antes de Hablar!")
    print("Imagina que tienes una idea o vas a responder algo. Te daré una situación y opciones. Elige la mejor.\n")

    situations = [
        {
            "scenario": "Tu amigo dice que le encanta el brócoli, ¡y a ti no te gusta nada!",
            "options": [
                "A. Decir: '¡El brócoli es horrible! ¡No sabes de lo que hablas!'",
                "B. Decir: 'A mí no me gusta mucho el brócoli, pero me alegra que a ti sí te guste.'",
                "C. Quedarte callado y poner cara de asco."
            ],
            "correct_idx": 1,
            "explanation": "La opción B es respetuosa y expresa tu opinión sin ofender."
        },
        {
            "scenario": "Tu hermano está llorando porque se le cayó su helado.",
            "options": [
                "A. Decir: '¡Qué tonto eres por dejar caer tu helado!'",
                "B. Decir: 'No llores, es solo un helado.'",
                "C. Decir: 'Oh no, se te cayó. ¿Quieres que te ayude a limpiar o te dé un abrazo?'"
            ],
            "correct_idx": 2,
            "explanation": "La opción C muestra empatía y ofrece ayuda, pensando en los sentimientos del otro."
        },
        {
            "scenario": "Un compañero dibuja un perro verde en clase.",
            "options": [
                "A. Decir: '¡Qué dibujo tan raro! ¡Los perros no son verdes!'",
                "B. Decir: 'Qué original tu perro verde, me gusta cómo usaste el color.'",
                "C. Reírte y señalar su dibujo a los demás."
            ],
            "correct_idx": 1,
            "explanation": "La opción B es respetuosa con la creatividad del otro y busca algo positivo."
        }
    ]

    score = 0
    for i, s in enumerate(situations):
        print(f"\n--- Situación {i+1} ---")
        print(s["scenario"])
        for idx, opt in enumerate(s["options"]):
            print(f"{opt}")
        
        while True:
            user_choice = input("Elige A, B o C: ").upper().strip()
            if user_choice in ['A', 'B', 'C']:
                break
            else:
                print("Opción no válida. Elige A, B o C.")
        
        if (user_choice == 'A' and s["correct_idx"] == 0) or \
           (user_choice == 'B' and s["correct_idx"] == 1) or \
           (user_choice == 'C' and s["correct_idx"] == 2):
            print("¡Muy bien! ¡Pensaste antes de hablar! 🎉")
            score += 1
        else:
            print("Hmm, no fue la mejor opción. Recuerda:", s["explanation"])
        time.sleep(3)
    
    print(f"\nTerminamos. Obtuviste {score} de {len(situations)}. ¡Eres un gran pensador!")
    input("Presiona ENTER para el último juego...")

def game_speak_clearly():
    """Juego de hablar con claridad (simulado)."""
    show_header("Juego 3: ¡Hablo con Claridad!")
    print("Imagina que quieres explicar algo para que todos te entiendan bien. Te daré algo que quieres 'decir', y tú elegirás la mejor manera de decirlo.\n")

    explanations = [
        {
            "idea": "Quieres pedirle a tu mamá que te ayude a atar los cordones.",
            "options": [
                "A. '¡Mamá! ¡Los cordones! ¡Ayuda!' (Gritando)",
                "B. 'Mamá, por favor, ¿me ayudas a atarme los cordones de los zapatos?'",
                "C. Señalar tus zapatos y quejarte."
            ],
            "correct_idx": 1,
            "explanation": "La opción B es clara, respetuosa y le dice exactamente lo que necesitas."
        },
        {
            "idea": "Quieres decirle a tu amigo que te preste un lápiz rojo.",
            "options": [
                "A. 'Dame eso.' (Señalando)",
                "B. '¿Me prestas el lápiz rojo, por favor?'",
                "C. 'Quiero ese lápiz rojo y lo quiero ahora.'"
            ],
            "correct_idx": 1,
            "explanation": "La opción B es amable, clara y específica sobre lo que pides."
        },
        {
            "idea": "Quieres contarle a tu papá que viste un perro grande en el parque.",
            "options": [
                "A. 'Papá, ¡había una cosa grande allá afuera! ¡Guau guau!'",
                "B. 'Papá, vi un perro muy grande en el parque cuando salimos.'",
                "C. 'Uhm... algo... grande... ¡en el parque!' (Murmurando)"
            ],
            "correct_idx": 1,
            "explanation": "La opción B explica claramente qué viste, dónde y cuándo."
        }
    ]

    score = 0
    for i, exp in enumerate(explanations):
        print(f"\n--- Situación {i+1} ---")
        print(f"Quieres decir: '{exp['idea']}'")
        for idx, opt in enumerate(exp["options"]):
            print(f"{opt}")
        
        while True:
            user_choice = input("Elige A, B o C: ").upper().strip()
            if user_choice in ['A', 'B', 'C']:
                break
            else:
                print("Opción no válida. Elige A, B o C.")
        
        if (user_choice == 'A' and exp["correct_idx"] == 0) or \
           (user_choice == 'B' and exp["correct_idx"] == 1) or \
           (user_choice == 'C' and exp["correct_idx"] == 2):
            print("¡Genial! ¡Lo dijiste con claridad y respeto! 🎉")
            score += 1
        else:
            print("Oops, intenta ser más claro y respetuoso. Recuerda:", exp["explanation"])
        time.sleep(3)
    
    print(f"\nTerminamos. Obtuviste {score} de {len(explanations)}. ¡Excelente orador!")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: Escuchar, Pensar y Hablar (1º Grado)")
        print("1. Escuchar un Cuento")
        print("2. Conocer las Reglas Importantes")
        print("3. Jugar a Escuchar con Atención")
        print("4. Jugar a Pensar antes de Hablar")
        print("5. Jugar a Hablar con Claridad")
        print("6. Salir de la Lección")
        print("*" * 50)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_story()
        elif choice == '2':
            show_rules()
        elif choice == '3':
            game_listen_and_repeat()
        elif choice == '4':
            game_think_before_speak()
        elif choice == '5':
            game_speak_clearly()
        elif choice == '6':
            print("¡Adiós! Recuerda escuchar, pensar y hablar con claridad y respeto cada día. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
