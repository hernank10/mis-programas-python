import random
import os

# Lista de oraciones predefinidas para clasificar
oraciones_para_clasificar = [
    ("Hoy hace buen tiempo.", "enunciativa"),
    ("¿Vendrás mañana?", "interrogativa"),
    ("¡Qué alegría verte!", "exclamativa"),
    ("Apaga la luz, por favor.", "imperativa"),
    ("Tal vez llueva esta tarde.", "dubitativa"),
    ("Ojalá gane el equipo local.", "desiderativa"),
    ("Estoy aprendiendo Python.", "enunciativa"),
    ("¿Has terminado tu tarea?", "interrogativa"),
    ("¡Qué hermosa es esa vista!", "exclamativa"),
    ("No salgas sin avisar.", "imperativa"),
    ("Quizás él tenga razón.", "dubitativa"),
    ("Espero que llegues pronto.", "desiderativa"),
    ("Ella no estaba en casa.", "enunciativa"),
    ("¿Por qué no lo intentas?", "interrogativa"),
    ("¡Qué desastre tan grande!", "exclamativa"),
    ("Deja eso ahora mismo.", "imperativa"),
    ("Tal vez podamos salir mañana.", "dubitativa"),
    ("Quisiera que me entendieras.", "desiderativa"),
    ("El examen fue muy difícil.", "enunciativa"),
    ("¿Puedes ayudarme con esto?", "interrogativa")
]

# Archivo para guardar el progreso
progreso_archivo = "progreso_usuario.txt"

# Función para guardar progreso en un archivo
def guardar_progreso(tipo, aciertos, total):
    with open(progreso_archivo, "a") as file:
        file.write(f"{tipo}: {aciertos}/{total} aciertos.\n")
    print("\nProgreso guardado exitosamente.")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n---🌟📜✏️🕵🏛 MENÚ PRINCIPAL 🌟📜✏️🕵🏛---")
    print("1️⃣  Introducción teórica")
    print("2️⃣ Practicar oraciones subordinadas")
    print("3️⃣ Clasificar oraciones por tipo comunicativo")
    print("4️⃣ Transcribir y corregir oraciones o párrafos")
    print("5️⃣ Ver progreso guardado")
    print("6️⃣ Salir")
    return input("Selecciona una opción: ")

# Función de introducción teórica
def introduccion_teorica():
    print("\n---🌟📜✏️🕵🏛 INTRODUCCIÓN TEÓRICA 🌟📜✏️🕵🏛---")
    print("1️⃣  Oraciones subordinadas: aquellas que dependen de una oración principal.")
    print("2️⃣ Tipos comunicativos: enunciativa, interrogativa, exclamativa, imperativa, dubitativa, desiderativa.")

# Función para practicar oraciones subordinadas
def practicar_subordinadas():
    print("\n--- PRÁCTICA DE ORACIONES SUBORDINADAS ---")
    print("Función en desarrollo para añadir nuevas características más adelante.")

# Función para clasificar oraciones
def clasificar_oraciones():
    print("\n---🌟📜✏️🕵🏛 CLASIFICAR ORACIONES POR INTENCIÓN COMUNICATIVA 🌟📜✏️🕵🏛---")
    oraciones = random.sample(oraciones_para_clasificar, 10)
    aciertos = 0

    for i, (oracion, tipo_correcto) in enumerate(oraciones, 1):
        print(f"{i}. {oracion}")
        print("Tipos: enunciativa, interrogativa, exclamativa, imperativa, dubitativa, desiderativa")
        respuesta = input("¿Qué tipo es esta oración? ").strip().lower()

        if respuesta == tipo_correcto:
            print("¡Correcto!✅")
            aciertos += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta es: {tipo_correcto}")

    print(f"\nTu puntuación: {aciertos}/{len(oraciones)}")
    guardar_progreso("Clasificación de oraciones", aciertos, len(oraciones))

# Función para transcribir y corregir oraciones o párrafos
def transcribir_y_corregir():
    print("\n---✏️🕵 TRANSCRIPCIÓN Y CORRECCIÓN DE ORACIONES ✏️🕵---")
    print("Escribe 20 oraciones o un párrafo mal escrito. El programa te ayudará a corregirlos.")
    texto_usuario = []
    for i in range(1, 21):
        oracion = input(f"Oración {i}: ")
        texto_usuario.append(oracion)
    
    print("\n---✏️🕵 TU TEXTO INGRESADO ---")
    for oracion in texto_usuario:
        print(f"- {oracion}")

    print("\n---✏️🕵 CORRECCIÓN DE TEXTO ---")
    correcciones = []
    for oracion in texto_usuario:
        corregida = corregir_oracion(oracion)
        correcciones.append(corregida)
        print(f"- Original: {oracion}")
        print(f"  Corregida: {corregida}")

    guardar_texto("correcciones.txt", correcciones)
    print("\nCorrecciones guardadas en 'correcciones.txt'.")

# Función básica de corrección de oraciones
def corregir_oracion(oracion):
    # Aquí se podría integrar una biblioteca como `LanguageTool` para mejorar la corrección.
    return oracion.capitalize().replace("  ", " ").strip()

# Función para guardar las correcciones en un archivo
def guardar_texto(nombre_archivo, correcciones):
    with open(nombre_archivo, "w") as file:
        file.write("\n".join(correcciones))

# Función para ver el progreso guardado
def ver_progreso():
    if os.path.exists(progreso_archivo):
        print("\n---✏️🕵 PROGRESO GUARDADO ---")
        with open(progreso_archivo, "r") as file:
            print(file.read())
    else:
        print("\nNo hay progreso guardado aún.")

# Función principal
def programa_practica():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            introduccion_teorica()
        elif opcion == "2":
            practicar_subordinadas()
        elif opcion == "3":
            clasificar_oraciones()
        elif opcion == "4":
            transcribir_y_corregir()
        elif opcion == "5":
            ver_progreso()
        elif opcion == "6":
            print("🌟📜✏️🕵🏛Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("✏️🕵Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
programa_practica()
