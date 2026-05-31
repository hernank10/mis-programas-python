# Base de datos con ejemplos de oraciones compuestas y sus tipos
oraciones_compuestas = [
    {"oracion": "Juan estudia, pero María descansa.", "tipo": "Coordinada adversativa"},
    {"oracion": "Estudié mucho porque quiero aprobar el examen.", "tipo": "Subordinada causal"},
    {"oracion": "Hace calor; iremos a la playa.", "tipo": "Yuxtapuesta"},
    {"oracion": "Compré frutas y verduras para la semana.", "tipo": "Coordinada copulativa"},
    {"oracion": "Salió temprano; no llegó a tiempo.", "tipo": "Yuxtapuesta"},
    {"oracion": "No solo canta, sino que también baila.", "tipo": "Coordinada distributiva"},
    {"oracion": "Quiero que me ayudes con la tarea.", "tipo": "Subordinada sustantiva"},
    {"oracion": "Aunque estaba cansado, terminó su trabajo.", "tipo": "Subordinada concesiva"}
]

# Función para practicar análisis sintáctico
def practicar_sintaxis():
    print("\n--- Práctica de Análisis de Estructuras Sintácticas ---")
    correctas = 0
    total = len(oraciones_compuestas)

    for item in oraciones_compuestas:
        print(f"\nOración: {item['oracion']}")
        respuesta = input("¿Qué tipo de oración compuesta es esta? ").strip()

        if respuesta.lower() == item["tipo"].lower():
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. Es una oración compuesta de tipo '{item['tipo']}'.")

    print(f"\nTu puntuación final es: {correctas}/{total}")
    guardar_progreso("Análisis sintáctico", correctas, total)

# Función para construir oraciones
def construir_oraciones():
    print("\n--- Construcción de Oraciones Compuestas ---")
    print("Crea una oración del tipo especificado.\n")
    tipos = [
        "Coordinada adversativa",
        "Subordinada causal",
        "Yuxtapuesta",
        "Coordinada copulativa",
        "Subordinada sustantiva"
    ]
    for tipo in tipos:
        print(f"\nConstruye una oración de tipo: {tipo}")
        oracion = input("Escribe tu oración: ").strip()
        print(f"¡Gracias! Revisaremos esta oración más tarde.\n")
    print("Ejercicio completado. ¡Sigue practicando!")

# Función para guardar progreso
def guardar_progreso(actividad, correctas, total):
    from datetime import datetime
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_sintaxis.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_sintaxis.txt'.")

# Menú principal
def menu_sintaxis():
    while True:
        print("\n--- Menú: Análisis de Estructuras Sintácticas ---")
        print("1. Practicar análisis sintáctico")
        print("2. Construir oraciones")
        print("3. Ver progreso")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            practicar_sintaxis()
        elif opcion == "2":
            construir_oraciones()
        elif opcion == "3":
            try:
                with open("progreso_sintaxis.txt", "r") as archivo:
                    print("\n--- Progreso del Usuario ---")
                    print(archivo.read())
            except FileNotFoundError:
                print("\nAún no hay progreso guardado. Realiza la práctica para comenzar.")
        elif opcion == "4":
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_sintaxis()
