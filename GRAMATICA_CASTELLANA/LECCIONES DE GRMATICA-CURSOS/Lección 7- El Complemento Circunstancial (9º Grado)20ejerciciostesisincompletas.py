import random
import os
import time

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("-" * 60)
    print(f"🧠 {title.upper()} 🧠")
    print("-" * 60)
    print()

def show_theory():
    """Muestra la sección de teoría sobre tesis y argumentos."""
    show_header("Teoría: Tesis y Razones")
    print("¡Hola! Hoy vamos a subir un nivel en cómo pensamos y escribimos.")
    print("Vamos a hablar de las **TESIS** y las **RAZONES**.\n")
    
    print("⭐ ¿Qué es una TESIS?")
    print("   Es la IDEA PRINCIPAL o la AFIRMACIÓN que queremos defender o explicar.")
    print("   Es lo que crees o lo que quieres demostrar.\n")
    print("   Ejemplo de tesis: 'Los perros son mejores mascotas que los gatos.'\n")
    
    print("⭐ ¿Qué es una RAZÓN (o argumento)?")
    print("   Es la EXPLICACIÓN o la PRUEBA que damos para apoyar nuestra tesis.")
    print("   Responde al '¿POR QUÉ?' de tu tesis.\n")
    print("   Ejemplo de razón para la tesis anterior: '...porque los perros son más leales y obedientes.'\n")
    
    print("¡Una buena tesis necesita buenas razones para convencer!\n")
    print("Hoy practicaremos a añadir razones lógicas a diferentes tesis incompletas.\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de tesis incompletas y razones."""
    show_header("Ejemplos: Completando Tesis")
    
    examples = [
        {"incomplete": "Es importante reciclar porque...", 
         "reason_model": "ayuda a proteger el planeta y a ahorrar recursos."},
        {"incomplete": "Los videojuegos pueden ser buenos para la mente porque...", 
         "reason_model": "mejoran la coordinación ojo-mano y la resolución de problemas."},
        {"incomplete": "Leer libros es fundamental porque...", 
         "reason_model": "amplía nuestro vocabulario y nos permite aprender sobre muchas cosas."}
    ]

    print("Mira cómo podemos completar estas ideas:\n")
    for ex in examples:
        print(f"Tesis incompleta: '{ex['incomplete']}'")
        print(f"Razón posible: '{ex['reason_model']}'")
        print("-" * 40)
        time.sleep(2) # Pausa para que el estudiante procese

    print("\n¡Ahora es tu turno de pensar en razones!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def start_exercises():
    """Inicia la sección de ejercicios de tesis incompleta."""
    show_header("¡A Practicar! Completa las Tesis")
    print("Para cada tesis incompleta, escribe UNA razón lógica para completarla.")
    print("Tu razón debe responder al '¿POR QUÉ?' de la tesis.\n")
    print("Al final, verás una posible respuesta y podrás decidir si tu razón fue buena.\n")

    exercises = [
        {"incomplete": "Estudiar todos los días es bueno porque...", 
         "reason_model": "nos ayuda a entender mejor los temas y a sacar buenas notas."},
        {"incomplete": "La tecnología es útil para aprender porque...", 
         "reason_model": "nos da acceso a mucha información y herramientas interactivas."},
        {"incomplete": "Es necesario comer frutas y verduras porque...", 
         "reason_model": "nos aportan vitaminas y minerales esenciales para la salud."},
        {"incomplete": "Hacer ejercicio regularmente es importante porque...", 
         "reason_model": "mantiene nuestro cuerpo fuerte, nuestro corazón sano y nos da energía."},
        {"incomplete": "Dormir las horas suficientes es crucial porque...", 
         "reason_model": "permite que nuestro cerebro y cuerpo descansen y se recuperen."},
        {"incomplete": "Ayudar en casa a mis padres es justo porque...", 
         "reason_model": "ellos se esfuerzan por nosotros y la casa es responsabilidad de todos."},
        {"incomplete": "Proteger los animales es nuestro deber porque...", 
         "reason_model": "son seres vivos que sienten y forman parte del equilibrio de la naturaleza."},
        {"incomplete": "Aprender un segundo idioma es una gran ventaja porque...", 
         "reason_model": "nos abre puertas a nuevas culturas y oportunidades en el futuro."},
        {"incomplete": "No tirar basura en la calle es vital porque...", 
         "reason_model": "mantiene la ciudad limpia, evita inundaciones y protege el medio ambiente."},
        {"incomplete": "Es importante respetar las opiniones de los demás porque...", 
         "reason_model": "todas las personas tienen derecho a pensar diferente y así aprendemos de otros."},
        {"incomplete": "La amistad es valiosa porque...", 
         "reason_model": "los amigos nos apoyan, nos escuchan y comparten momentos especiales con nosotros."},
        {"incomplete": "Ser honesto es fundamental porque...", 
         "reason_model": "genera confianza en los demás y nos permite vivir con tranquilidad."},
        {"incomplete": "Viajar nos enriquece mucho porque...", 
         "reason_model": "conocemos nuevos lugares, personas y diferentes formas de vida."},
        {"incomplete": "La música es importante en nuestras vidas porque...", 
         "reason_model": "nos ayuda a expresar emociones, nos relaja y nos divierte."},
        {"incomplete": "Es bueno leer noticias para informarse porque...", 
         "reason_model": "así sabemos lo que pasa en el mundo y podemos formar nuestra propia opinión."},
        {"incomplete": "Ahorrar dinero es una buena costumbre porque...", 
         "reason_model": "nos permite tener recursos para emergencias o para lograr nuestros objetivos."},
        {"incomplete": "El trabajo en equipo nos hace más fuertes porque...", 
         "reason_model": "unimos nuestras habilidades y logramos metas más grandes."},
        {"incomplete": "Cuidar el agua es una responsabilidad de todos porque...", 
         "reason_model": "es un recurso limitado y vital para la vida en el planeta."},
        {"incomplete": "Los juegos de mesa son una buena forma de diversión porque...", 
         "reason_model": "fomentan la interacción familiar, la estrategia y la sana competencia."},
        {"incomplete": "Es importante pedir ayuda cuando la necesitamos porque...", 
         "reason_model": "nadie lo sabe todo y otras personas pueden ofrecernos una solución o apoyo."}
    ]

    random.shuffle(exercises) # Mezclamos los ejercicios para que no siempre salgan en el mismo orden

    good_reasons_count = 0
    total_exercises = len(exercises)

    for i, ex in enumerate(exercises):
        print(f"\n--- Ejercicio {i+1} de {total_exercises} ---")
        print(f"Tesis: '{ex['incomplete']}'")
        user_reason = input("Tu razón lógica: ").strip()

        print("\n--- Respuesta Modelo ---")
        print(f"Una posible razón sería: '{ex['reason_model']}'")
        
        # Pedimos al estudiante que autoevalúe su razón
        while True:
            evaluation = input("\n¿Consideras que tu razón fue buena y lógica? (s/n): ").lower().strip()
            if evaluation == 's':
                good_reasons_count += 1
                print("¡Muy bien! Estás desarrollando tu pensamiento crítico.")
                break
            elif evaluation == 'n':
                print("Está bien, sigue practicando. Comparar con el modelo te ayudará.")
                break
            else:
                print("Respuesta no válida. Por favor, escribe 's' para sí o 'n' para no.")
        time.sleep(2) # Pausa para que el usuario lea el feedback

    print("\n" * 2)
    print("-" * 60)
    print("¡EJERCICIOS TERMINADOS!")
    print(f"Consideras que diste {good_reasons_count} razones buenas de {total_exercises} ejercicios. 🎉")
    print("¡Sigue practicando la argumentación! Es una habilidad muy importante.\n")
    print("-" * 60)
    input("Presiona ENTER para volver al menú principal...")

def write_arguments():
    """Permite al usuario escribir 5 tesis y sus razones propias."""
    show_header("✍️ ¡Crea Tus Propias Tesis y Razones! ✍️")
    print("Ahora es tu turno de crear tus propias tesis y darles una razón.\n")
    print("Escribe 5 afirmaciones que quieras defender (tesis) y luego UNA razón para cada una.")
    print("Cuando termines una tesis, presiona ENTER, luego escribe su razón y ENTER de nuevo.")
    print("Si quieres terminar antes, escribe 'listo'.\n")

    arguments = []
    for i in range(1, 6):
        print(f"\n--- Argumento {i} ---")
        thesis = input("Tu tesis (tu idea principal): ").strip()
        if thesis.lower() == 'listo':
            break
        if not thesis:
            print("Tesis vacía. Intenta de nuevo o escribe 'listo'.")
            i -= 1 # Para que no cuente la tesis vacía
            continue
        
        reason = input(f"Una razón para '{thesis}': ").strip()
        if reason.lower() == 'listo':
            break
        if not reason:
            print("Razón vacía. Intenta de nuevo o escribe 'listo'.")
            # Podríamos permitir que continúe o que repita, pero por simplicidad, lo guardamos aunque esté vacía
            # La idea es que practiquen la estructura.
        
        arguments.append({"thesis": thesis, "reason": reason})

    print("\n--- Tus Argumentos ---")
    if arguments:
        for i, arg in enumerate(arguments):
            print(f"{i+1}. Tesis: '{arg['thesis']}'")
            print(f"   Razón: '{arg['reason']}'\n")
        print("¡Muy bien! Has practicado creando tus propias ideas y defendiéndolas.\n")
    else:
        print("No creaste ningún argumento esta vez. ¡Anímate para la próxima!\n")
    
    input("Presiona ENTER para volver al menú principal...")

def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Desarrollando Razones y Argumentos (9º Grado)")
        print("1. Aprender la Teoría")
        print("2. Ver Ejemplos")
        print("3. Hacer Ejercicios (20 tesis incompletas)")
        print("4. Crear Mis Propias Tesis y Razones")
        print("5. Salir de la Lección")
        print("-" * 60)

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            show_theory()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            start_exercises()
        elif choice == '4':
            write_arguments()
        elif choice == '5':
            print("¡Hasta pronto! Sigue desarrollando tus ideas. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
