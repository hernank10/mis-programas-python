# Base de datos de palabras con prefijos, sufijos y significados
raices_etimologicas = {
    "transatlántico": {
        "prefijo": "trans-",
        "significado_prefijo": "a través de",
        "raíz": "atlántico",
        "significado_raíz": "relativo al océano Atlántico"
    },
    "bicicleta": {
        "prefijo": "bi-",
        "significado_prefijo": "dos",
        "raíz": "cicleta",
        "significado_raíz": "relacionado con ruedas"
    },
    "invisible": {
        "prefijo": "in-",
        "significado_prefijo": "no",
        "raíz": "visible",
        "significado_raíz": "que se puede ver"
    },
    "antídoto": {
        "prefijo": "anti-",
        "significado_prefijo": "contra",
        "raíz": "doto",
        "significado_raíz": "veneno o sustancia dañina"
    },
    "submarino": {
        "prefijo": "sub-",
        "significado_prefijo": "debajo de",
        "raíz": "marino",
        "significado_raíz": "relativo al mar"
    }
}

# Función para practicar raíces etimológicas
def practicar_etimologia():
    print("\n--- Práctica de Vocabulario y Raíces Etimológicas ---")
    correctas = 0
    total = len(raices_etimologicas)

    for palabra, detalles in raices_etimologicas.items():
        print(f"\nPalabra: {palabra}")
        print("1. Identificar el prefijo")
        print("2. Identificar el significado del prefijo")
        print("3. Identificar la raíz principal")
        print("4. Identificar el significado de la raíz")
        
        # Preguntas una por una
        respuesta_prefijo = input("¿Cuál es el prefijo de esta palabra? ").strip()
        if respuesta_prefijo == detalles["prefijo"]:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. El prefijo es '{detalles['prefijo']}'.")

        respuesta_significado_prefijo = input("¿Qué significa este prefijo? ").strip()
        if respuesta_significado_prefijo == detalles["significado_prefijo"]:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. El significado correcto es: '{detalles['significado_prefijo']}'.")

        respuesta_raiz = input("¿Cuál es la raíz principal? ").strip()
        if respuesta_raiz == detalles["raíz"]:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La raíz principal es '{detalles['raíz']}'.")

        respuesta_significado_raiz = input("¿Qué significa esta raíz? ").strip()
        if respuesta_significado_raiz == detalles["significado_raíz"]:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. El significado correcto es: '{detalles['significado_raíz']}'.")

    print(f"\nTu puntuación final es: {correctas}/{total * 4}")
    guardar_progreso("Práctica de raíces etimológicas", correctas, total * 4)

# Función para guardar progreso
def guardar_progreso(actividad, correctas, total):
    from datetime import datetime
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_etimologia.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_etimologia.txt'.")

# Menú principal
def menu_etimologia():
    while True:
        print("\n--- Menú: Raíces Etimológicas ---")
        print("1. Practicar raíces etimológicas")
        print("2. Ver progreso")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            practicar_etimologia()
        elif opcion == "2":
            try:
                with open("progreso_etimologia.txt", "r") as archivo:
                    print("\n--- Progreso del Usuario ---")
                    print(archivo.read())
            except FileNotFoundError:
                print("\nAún no hay progreso guardado. Realiza la práctica para comenzar.")
        elif opcion == "3":
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_etimologia()
