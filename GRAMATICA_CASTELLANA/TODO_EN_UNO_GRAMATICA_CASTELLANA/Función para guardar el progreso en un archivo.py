import datetime

# Base de datos de abreviaturas
abreviaturas = {
    "art.": "artículo",
    "adj.": "adjetivo",
    "s.": "sustantivo",
    "v.": "verbo",
    "cf.": "confróntese",
    "etc.": "et cetera",
    "p. ej.": "por ejemplo",
    "ed.": "edición",
    "núm.": "número",
    "cap.": "capítulo"
}

# Función para guardar el progreso en un archivo
def guardar_progreso(actividad, correctas, total):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_usuario.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_usuario.txt'.")

def mostrar_abreviaturas():
    print("\nLista de abreviaturas disponibles:")
    for abreviatura in abreviaturas:
        print(f"- {abreviatura}")

def interpretar_abreviatura():
    abreviatura = input("\nIntroduce la abreviatura que deseas interpretar: ").strip()
    if abreviatura in abreviaturas:
        print(f"\nEl significado de '{abreviatura}' es: {abreviaturas[abreviatura]}")
    else:
        print("\nLo siento, esa abreviatura no está en la base de datos.")

def cuestionario():
    print("\n--- Cuestionario de Abreviaturas ---")
    correctas = 0
    for abreviatura, significado in abreviaturas.items():
        respuesta = input(f"¿Qué significa '{abreviatura}'? ").strip().lower()
        if respuesta == significado:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {significado}")
    print(f"\nTu puntuación final es: {correctas}/{len(abreviaturas)}")
    guardar_progreso("Cuestionario", correctas, len(abreviaturas))

def escribir_abreviaturas():
    print("\n--- Escribir todas las abreviaturas ---")
    correctas = 0
    for abreviatura in abreviaturas:
        respuesta = input(f"Escribe correctamente la abreviatura para '{abreviaturas[abreviatura]}': ").strip()
        if respuesta == abreviatura:
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La abreviatura correcta es: {abreviatura}")
    print(f"\nTu puntuación final es: {correctas}/{len(abreviaturas)}")
    guardar_progreso("Escribir abreviaturas", correctas, len(abreviaturas))

def ver_progreso():
    try:
        with open("progreso_usuario.txt", "r") as archivo:
            contenido = archivo.read()
            print("\n--- Progreso del Usuario ---")
            print(contenido)
    except FileNotFoundError:
        print("\nAún no hay progreso guardado. Realiza alguna actividad para comenzar a registrar tu progreso.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver lista de abreviaturas")
        print("2. Interpretar una abreviatura")
        print("3. Realizar cuestionario")
        print("4. Escribir todas las abreviaturas")
        print("5. Ver progreso")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            mostrar_abreviaturas()
        elif opcion == "2":
            interpretar_abreviatura()
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            escribir_abreviaturas()
        elif opcion == "5":
            ver_progreso()
        elif opcion == "6":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu()
