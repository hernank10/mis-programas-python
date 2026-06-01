import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 70)
    print(f"💡 {title.upper()} 💡")
    print("=" * 70)
    print()

def show_introduction():
    """Introduce el concepto de razones reales y falsas."""
    show_header("Introducción: Razones Reales y Razones Falsas")
    print("¡Hola, pequeños detectives de la verdad! 🕵️‍♂️")
    print("Ya sabemos identificar ideas grandes y si nos tocan el corazón.")
    print("Hoy vamos a ser muy listos y aprender a diferenciar entre:")
    print("   👉 **Razones Reales:** Son las que te dicen por qué algo es verdad o por qué debes hacer algo, y tiene sentido.")
    print("   👉 **Razones Falsas:** Son las que no te dan una buena explicación, ¡y a veces nos quieren engañar!\n")
    
    print("Vamos a ver dos tipos de 'razones falsas' muy comunes:\n")
    
    print("1. 🚶‍♀️🚶‍♂️ **'Porque Todos lo Hacen':**")
    print("   A veces alguien dice: '¡Todos mis amigos van a esa fiesta, tú también deberías ir!'")
    print("   O: '¡Todos están jugando con el nuevo juguete, es el mejor!'")
    print("   Pero... ¿que todos lo hagan significa que sea lo mejor o lo correcto para ti? ¡No siempre!\n")
    
    print("2. 🎓 **'Porque Alguien lo Dijo' (sin saber quién o si sabe de verdad):**")
    print("   Alguien podría decir: 'Tienes que comer toda tu comida, mi maestra dice que es la regla número uno.'")
    print("   O: 'Ese juego es el más divertido, lo escuché en la tele.'")
    print("   Pero... ¿quién es esa persona? ¿Es un experto en lo que habla? ¿Es de verdad una regla? ¡Necesitamos saber más!\n")
    
    print("¡Aprendamos a pedir **razones reales**!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de razones reales y falsas."""
    show_header("Ejemplos: ¿Razón Real o Razón Falsa?")
    
    examples = [
        {"text": "Debes ponerte el abrigo porque hace mucho frío afuera.", 
         "type": "REAL", "explanation": "¡Es una razón real! El frío te hace enfermar si no te abrigas."},
        {"text": "Tienes que leer este libro porque todos en la clase lo están leyendo.", 
         "type": "FALSA_TODOS", "explanation": "¡Razón falsa de 'todos'! Que todos lo lean no significa que a ti te vaya a gustar o que debas hacerlo."},
        {"text": "No toques eso, mi papá dice que es peligroso.", 
         "type": "REAL", "explanation": "¡Es una razón real! Los papás suelen saber cuándo algo es peligroso para protegerte."},
        {"text": "Este refresco es el mejor porque un famoso de la tele lo dijo.", 
         "type": "FALSA_ALGUIEN", "explanation": "¡Razón falsa de 'alguien lo dijo'! Un famoso no es experto en bebidas para todos."},
        {"text": "Debes cepillarte los dientes para que no te salgan caries.", 
         "type": "REAL", "explanation": "¡Es una razón real! Los dentistas nos enseñan que así cuidamos los dientes."},
        {"text": "Tira la cáscara al suelo, todos mis amigos lo hacen.", 
         "type": "FALSA_TODOS", "explanation": "¡Razón falsa de 'todos'! Que otros lo hagan no significa que esté bien ensuciar."},
        {"text": "Ese juguete es el mejor, lo vi en una publicidad.", 
         "type": "FALSA_ALGUIEN", "explanation": "¡Razón falsa de 'alguien lo dijo'! Las publicidades quieren que compres, no siempre te dicen la verdad completa."},
    ]

    print("Lee cada frase y piensa si es una 'razón real' o una 'razón falsa'.\n")
    for i, ex in enumerate(examples):
        print(f"--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "REAL":
            print(f"¡Es una RAZÓN REAL! ✅ {ex['explanation']}\n")
        elif ex['type'] == "FALSA_TODOS":
            print(f"¡Es una RAZÓN FALSA! (Porque 'todos lo hacen') ❌ {ex['explanation']}\n")
        else: # FALSA_ALGUIEN
            print(f"¡Es una RAZÓN FALSA! (Porque 'alguien lo dijo') ❌ {ex['explanation']}\n")
        time.sleep(3)
        print("=" * 35)

    print("\n¡Ahora es tu turno de encontrar las razones reales y las falsas!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_real_or_fake_reason():
    """Juego de identificar si una razón es real o falsa."""
    show_header("Juego 1: ¡Detectives de Razones!")
    print("Te daré una frase. Tienes que decir si es una 'RAZÓN REAL' (R) o una 'RAZÓN FALSA' (F).\n")
    print("Escribe 'R' para Razón Real o 'F' para Razón Falsa.\n")

    questions = [
        {"text": "Debes cruzar la calle por el paso de cebra porque es más seguro.", "answer": "R", "explanation": "Es más seguro para no ser atropellado por un coche."},
        {"text": "Compra este cereal porque todos tus amigos lo tienen.", "answer": "F", "explanation": "Que tus amigos lo tengan no lo hace mejor para ti."},
        {"text": "Este es el mejor equipo de fútbol, lo dijo el director de mi colegio.", "answer": "F", "explanation": "El director es bueno en el colegio, no necesariamente en fútbol."},
        {"text": "Lávate las manos antes de comer para quitar los microbios.", "answer": "R", "explanation": "Los microbios pueden enfermarte, y lavarse las manos los quita."},
        {"text": "Ponte este disfraz, todos los demás lo van a usar.", "answer": "F", "explanation": "No tienes que usarlo solo porque los demás lo hagan si no te gusta."},
        {"text": "No comas dulces antes de cenar porque la abuelita dice que es malo.", "answer": "R", "explanation": "Aunque es la abuela, ¡tiene razón! Los dulces quitan el apetito para la comida sana."},
        {"text": "Este parque es el más divertido, lo oí de un señor que estaba allí.", "answer": "F", "explanation": "Solo lo oíste de 'un señor', no sabes si sabe de verdad o si es divertido para ti."},
        {"text": "Debes dormir temprano para tener energía al día siguiente.", "answer": "R", "explanation": "Dormir bien nos da mucha energía para jugar y aprender."},
        {"text": "Salta muy alto para tocar el cielo, todos los niños pueden hacerlo.", "answer": "F", "explanation": "No todos pueden tocar el cielo saltando, es una exageración."},
        {"text": "Es importante cuidar tus juguetes porque así te durarán más tiempo.", "answer": "R", "explanation": "Cuidar las cosas hace que duren mucho."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 6 # Limitamos a 6

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿Es 'RAZÓN REAL' (R) o 'RAZÓN FALSA' (F)?: ").upper().strip()
            if user_input in ['R', 'F']:
                break
            else:
                print("Por favor, escribe 'R' o 'F'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(3)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detective de razones! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_give_a_real_reason():
    """Juego de dar una razón real para una acción."""
    show_header("Juego 2: ¡Dame una Razón Real!")
    print("Te daré una situación y una acción. Tú debes dar una **RAZÓN REAL** por qué es bueno o importante hacerla.\n")

    situations = [
        {"action": "Ayudar a un amigo a recoger sus colores caídos.",
         "real_reason_hint": "Porque es bueno ser amable y ayudar a los demás."},
        {"action": "Comer frutas y verduras todos los días.",
         "real_reason_hint": "Porque te dan energía y te mantienen sano."},
        {"action": "Estudiar para el examen de matemáticas.",
         "real_reason_hint": "Porque así aprenderás más y sacarás una buena nota."},
        {"action": "Compartir tus juguetes con tus hermanos.",
         "real_reason_hint": "Porque así todos pueden jugar y divertirse juntos."},
        {"action": "Cuidar las plantas del jardín.",
         "real_reason_hint": "Porque necesitan agua y sol para vivir y dar flores bonitas."},
    ]
    
    random.shuffle(situations)
    num_questions = 3 # Limitamos a 3

    for i in range(num_questions):
        s = situations[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Acción: '{s['action']}'")
        
        user_reason = input("Da una RAZÓN REAL para hacer esto: ").strip()
        
        print(f"\nTu razón: '{user_reason}'")
        print(f"Una posible razón real: '{s['real_reason_hint']}'")
        print("\n¡Muy bien! Has pensado en razones reales. ¡Eso es ser un buen pensador! 🎉")
        time.sleep(3)
    
    print(f"\nJuego terminado. ¡Has aprendido a dar razones reales para tus acciones!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_reason_example():
    """Permite al usuario crear su propio ejemplo de razón falsa y luego una real."""
    show_header("✍️ ¡Crea Tus Propias Razones! ✍️")
    print("Vamos a crear una 'razón falsa' y luego la convertiremos en una 'razón real'.\n")

    while True:
        false_reason_scenario = input("1. Piensa en una situación donde alguien da una razón falsa (Ej: 'Debes comprar este dulce porque todos lo compran'): ").strip()
        if false_reason_scenario:
            break
        else:
            print("Por favor, describe una situación.")
    
    print(f"\nTu razón falsa: '{false_reason_scenario}'")

    while True:
        real_reason_transform = input("2. Ahora, piensa en una RAZÓN REAL y verdadera para esa misma acción, o por qué es mejor no hacerla (Ej: 'Este dulce tiene mucho azúcar, es mejor comer una fruta'): ").strip()
        if real_reason_transform:
            break
        else:
            print("Por favor, escribe una razón real.")

    print("\n--- ¡Tu Ejemplo Creado! ---")
    print(f"Tu razón falsa: '{false_reason_scenario}' ❌")
    print(f"Tu razón real: '{real_reason_transform}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a cambiar las razones falsas por razones reales! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¿Por qué debo Creerte? (4º Grado)")
        print("1. Introducción: Razones Reales y Falsas")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡Detectives de Razones!")
        print("4. Jugar: ¡Dame una Razón Real!")
        print("5. ✍️ ¡Crea Tus Propias Razones! ✍️")
        print("6. Salir de la Lección")
        print("=" * 70)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_real_or_fake_reason()
        elif choice == '4':
            game_give_a_real_reason()
        elif choice == '5':
            create_own_reason_example()
        elif choice == '6':
            print("¡Adiós! Sigue buscando las razones reales en todo lo que te digan. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
