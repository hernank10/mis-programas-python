# Función para mostrar una pregunta
def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3/4): "))
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            return True
        else:
            print(f"Incorrecto. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")
        return False

# Cuestionarios por tipo de adjetivo
def cuestionario_descriptivos():
    return [
        ("¿Cuál es un adjetivo descriptivo?", ["Beautiful", "This", "His", "Two"], 1),
        ("Selecciona el adjetivo descriptivo en: 'The sky is blue.'", ["Sky", "Blue", "The", "Is"], 2),
    ]

def cuestionario_demostrativos():
    return [
        ("¿Cuál es un adjetivo demostrativo?", ["This", "Good", "Three", "Who"], 1),
        ("Selecciona el adjetivo demostrativo en: 'I like that car.'", ["I", "Like", "That", "Car"], 3),
    ]

def cuestionario_posesivos():
    return [
        ("¿Cuál es un adjetivo posesivo?", ["My", "Tall", "This", "Ten"], 1),
        ("Selecciona el adjetivo posesivo en: 'Her book is on the table.'", ["Book", "Her", "On", "Table"], 2),
    ]

def cuestionario_numerales():
    return [
        ("¿Cuál es un adjetivo numeral?", ["Five", "Who", "Happy", "Those"], 1),
        ("Selecciona el adjetivo numeral en: 'She has three cats.'", ["She", "Three", "Cats", "Has"], 2),
    ]

def cuestionario_interrogativos():
    return [
        ("¿Cuál es un adjetivo interrogativo?", ["Which", "Happy", "Five", "My"], 1),
        ("Selecciona el adjetivo interrogativo en: 'What book are you reading?'", ["What", "Book", "Are", "You"], 1),
    ]

def cuestionario_comparativos_superlativos():
    return [
        ("¿Cuál es un adjetivo comparativo?", ["Bigger", "Biggest", "Big", "This"], 1),
        ("Selecciona el adjetivo superlativo en: 'This is the largest house in the city.'", ["Largest", "House", "This", "City"], 1),
    ]

# Función para guardar progreso
def guardar_progreso(usuario, tipo, puntuacion, total):
    with open("progreso_adjetivos_tipos.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas):
    print(f"\n--- Cuestionario de {tipo} ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Tipos de Adjetivos en Inglés!")
    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Adjetivos Descriptivos")
        print("2. Adjetivos Demostrativos")
        print("3. Adjetivos Posesivos")
        print("4. Adjetivos Numerales")
        print("5. Adjetivos Interrogativos")
        print("6. Adjetivos Comparativos y Superlativos")
        print("7. Salir")
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            preguntas = cuestionario_descriptivos()
            puntuacion, total = iniciar_cuestionario("Adjetivos Descriptivos", preguntas)
        elif opcion == "2":
            preguntas = cuestionario_demostrativos()
            puntuacion, total = iniciar_cuestionario("Adjetivos Demostrativos", preguntas)
        elif opcion == "3":
            preguntas = cuestionario_posesivos()
            puntuacion, total = iniciar_cuestionario("Adjetivos Posesivos", preguntas)
        elif opcion == "4":
            preguntas = cuestionario_numerales()
            puntuacion, total = iniciar_cuestionario("Adjetivos Numerales", preguntas)
        elif opcion == "5":
            preguntas = cuestionario_interrogativos()
            puntuacion, total = iniciar_cuestionario("Adjetivos Interrogativos", preguntas)
        elif opcion == "6":
            preguntas = cuestionario_comparativos_superlativos()
            puntuacion, total = iniciar_cuestionario("Adjetivos Comparativos y Superlativos", preguntas)
        elif opcion == "7":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        guardar_progreso(usuario, opcion, puntuacion, total)

# Ejecutar el programa
menu_principal()
