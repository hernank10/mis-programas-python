import os

# Diccionario para guardar ejemplos de oraciones subordinadas
oraciones_subordinadas = {
    "Causal": "No fuimos al parque porque estaba lloviendo.",
    "Concesiva": "Aunque estaba cansado, terminó el trabajo.",
    "Condicional": "Si estudias, aprobarás el examen.",
    "Final": "Estudia para que puedas entender mejor.",
    "Temporal": "Cuando llegó la lluvia, ya estábamos en casa.",
    "Sustantiva": "Es necesario que vengas a la reunión.",
    "Adjetiva": "El libro que me prestaste es muy interesante.",
    "Comparativa": "Este ejercicio es más fácil de lo que parece."
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Introducción teórica")
    print("2. Cuestionario teórico")
    print("3. Ejercicios prácticos")
    print("4. Progreso del usuario")
    print("5. Agregar más ejemplos")
    print("6. Guardar ejercicios en archivo")
    print("7. Salir")

# Introducción teórica
def introduccion():
    print("\n--- Introducción a las Oraciones Subordinadas ---")
    print("""Las oraciones subordinadas son aquellas que dependen de otra oración principal 
y cumplen una función dentro de ella. Se clasifican en:
1. Subordinadas sustantivas: Funcionan como sustantivo.
2. Subordinadas adjetivas: Funcionan como adjetivo.
3. Subordinadas adverbiales: Funcionan como adverbio.""")
    input("\nPresiona Enter para volver al menú.")

# Cuestionario teórico
def cuestionario():
    print("\n--- Cuestionario Teórico ---")
    preguntas = {
        "¿Qué son las oraciones subordinadas?": "Dependen de otra oración principal.",
        "¿Cuál es la función de una subordinada sustantiva?": "Actúa como un sustantivo.",
        "¿Qué hace una subordinada adjetiva?": "Describe un sustantivo."
    }
    correctas = 0
    for pregunta, respuesta in preguntas.items():
        print(f"\nPregunta: {pregunta}")
        user_respuesta = input("Tu respuesta: ")
        if user_respuesta.lower() == respuesta.lower():
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta}")
    print(f"\nTu puntuación: {correctas}/{len(preguntas)}")
    input("\nPresiona Enter para volver al menú.")

# Ejercicios prácticos
def ejercicios():
    print("\n--- Ejercicios Prácticos ---")
    for tipo, ejemplo in oraciones_subordinadas.items():
        print(f"\nTipo: {tipo}")
        print(f"Ejemplo: {ejemplo}")
        respuesta = input("Intenta crear una oración similar: ")
        print("¡Gracias por practicar! Revisa si tu oración cumple la misma función.")
    input("\nPresiona Enter para volver al menú.")

# Progreso
def progreso():
    print("\n--- Progreso del Usuario ---")
    print("Por ahora, esta función está en desarrollo.")
    input("\nPresiona Enter para volver al menú.")

# Agregar ejemplos
def agregar_ejemplos():
    print("\n--- Agregar Más Ejemplos ---")
    tipo = input("Indica el tipo de subordinada: ")
    ejemplo = input("Escribe un ejemplo para este tipo: ")
    oraciones_subordinadas[tipo] = ejemplo
    print(f"Ejemplo agregado: {tipo} - {ejemplo}")
    input("\nPresiona Enter para volver al menú.")

# Guardar ejercicios en archivo
def guardar_en_archivo():
    archivo = "oraciones_subordinadas.txt"
    with open(archivo, "w") as file:
        file.write("--- Ejemplos de Oraciones Subordinadas ---\n")
        for tipo, ejemplo in oraciones_subordinadas.items():
            file.write(f"{tipo}: {example}\n")
    print(f"Ejercicios guardados en {archivo}")
    input("\nPresiona Enter para volver al menú.")

# Programa principal
def programa_principal():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            introduccion()
        elif opcion == "2":
            cuestionario()
        elif opcion == "3":
            ejercicios()
        elif opcion == "4":
            progreso()
        elif opcion == "5":
            agregar_ejemplos()
        elif opcion == "6":
            guardar_en_archivo()
        elif opcion == "7":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
programa_principal()
