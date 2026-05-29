import random

# Lista de ejemplos de oraciones causativas
ejemplos_causativos = [
    "La guerra hizo subir los precios.",
    "La lluvia hace crecer las plantas.",
    "El jefe nos hizo trabajar más.",
    "El profesor hizo estudiar a los alumnos.",
    "El calor hizo derretir el hielo.",
    "El terremoto hizo caer los edificios.",
    "El viento hizo volar las hojas.",
    "El ruido hizo despertar al bebé.",
    "El médico hizo tomar la medicina al paciente.",
    "El entrenador hizo correr a los jugadores.",
    "La película hizo llorar a la audiencia.",
    "El discurso hizo reflexionar a todos.",
    "La noticia hizo alegrar a la gente.",
    "El café hizo mantener despierto a Juan.",
    "El ejercicio hizo mejorar su salud."
]

# Función para generar un ejemplo aleatorio
def generar_ejemplo():
    ejemplo = random.choice(ejemplos_causativos)
    print(f"\nEjemplo de oración causativa:\n{ejemplo}\n")

# Función para completar una oración
def completar_oracion():
    sujetos = ["La guerra", "La lluvia", "El jefe", "El profesor", "El calor", "El terremoto", "El viento", "El ruido", "El médico", "El entrenador", "La película", "El discurso", "La noticia", "El café", "El ejercicio"]
    verbos = ["subir", "crecer", "trabajar", "estudiar", "derretir", "caer", "volar", "despertar", "tomar", "correr", "llorar", "reflexionar", "alegrar", "mantener", "mejorar"]
    objetos = ["los precios", "las plantas", "más", "a los alumnos", "el hielo", "los edificios", "las hojas", "al bebé", "la medicina al paciente", "a los jugadores", "a la audiencia", "a todos", "a la gente", "a Juan", "su salud"]

    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)

    print(f"\nCompleta la siguiente oración causativa:\n{sujeto} hizo _____ {objeto}.")
    respuesta = input("Escribe el verbo en infinitivo: ").strip()

    if respuesta:
        oracion_completa = f"{sujeto} hizo {respuesta} {objeto}."
        print(f"\nTu oración completa es:\n{oracion_completa}")
        print(f"\n¡Buen trabajo! Aquí tienes un ejemplo similar:\n{random.choice(ejemplos_causativos)}\n")
    else:
        print("\nDebes completar la oración.\n")

# Función para verificar si una oración es correcta
def verificar_oracion():
    print("\nEscribe una oración causativa con 'hacer':")
    print("Por ejemplo, 'La guerra hizo subir los precios' o 'El jefe nos hizo trabajar más'.")
    oracion_usuario = input("Tu oración: ").strip()

    if oracion_usuario:
        if oracion_usuario.lower().startswith(("la", "el")) and "hizo" in oracion_usuario.lower():
            print("\n¡Correcto! Es una oración causativa válida.\n")
        else:
            print("\nLa oración no es válida. Asegúrate de usar 'hacer' como verbo causativo.\n")
    else:
        print("\nDebes escribir una oración.\n")

# Función para practicar con ejercicios personalizados
def practicar_ejercicios():
    print("\nVamos a practicar con ejercicios personalizados.")
    print("Completa las siguientes oraciones causativas:\n")

    ejercicios = [
        ("La película hizo _____ a la audiencia.", "llorar"),
        ("El discurso hizo _____ a todos.", "reflexionar"),
        ("La noticia hizo _____ a la gente.", "alegrar"),
        ("El café hizo _____ despierto a Juan.", "mantener"),
        ("El ejercicio hizo _____ su salud.", "mejorar")
    ]

    for ejercicio, respuesta_correcta in ejercicios:
        print(ejercicio)
        respuesta_usuario = input("Escribe el verbo en infinitivo: ").strip()

        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}\n")

# Menú principal
def mostrar_menu():
    while True:
        print("\n--- Menú de Práctica: Oraciones Causativas ---")
        print("1. Generar un ejemplo aleatorio")
        print("2. Completar una oración")
        print("3. Verificar si una oración es correcta")
        print("4. Practicar con ejercicios personalizados")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            generar_ejemplo()
        elif opcion == "2":
            completar_oracion()
        elif opcion == "3":
            verificar_oracion()
        elif opcion == "4":
            practicar_ejercicios()
        elif opcion == "5":
            print("\n¡Gracias por practicar! Hasta luego.\n")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 5.\n")

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
