import json

# Función para guardar el progreso
def guardar_progreso(progreso):
    with open("progreso.json", "w") as archivo:
        json.dump(progreso, archivo)
    print("Progreso guardado con éxito.")

# Función para cargar el progreso
def cargar_progreso():
    try:
        with open("progreso.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Ejercicios de ejemplo
ejercicios_nuevos = [
    {"pregunta": "___ gato negro está en la azotea.", "respuesta": "El"},
    {"pregunta": "¿___ cuesta esta bicicleta? (responde: Cien dólares).", "respuesta": "Cuánto"},
    {"pregunta": "Pedro perdió ___ celular en la escuela.", "respuesta": "su"},
    {"pregunta": "Nosotros siempre ___ (salir) a pasear los domingos.", "respuesta": "salimos"},
    {"pregunta": "Mi casa está en el piso ___ de ese edificio. (responde: décimo).", "respuesta": "décimo"},
    {"pregunta": "___ silla que está junto a la puerta es muy cómoda.", "respuesta": "Esa"},
    {"pregunta": "(Cantar) ___ una canción para nosotros.", "respuesta": "Canta"},
    {"pregunta": "(Picar) ___ las verduras en trozos pequeños.", "respuesta": "Pica"}
]

# Introducción
def introduccion():
    print("""
Bienvenido al programa interactivo para practicar español.
Este programa te ayudará a mejorar tus habilidades lingüísticas a través de ejercicios interactivos y prácticos.
Podrás aprender gramática, vocabulario, uso de artículos, posesivos, numerales y más.

Cada sección está diseñada para reforzar un aspecto del idioma.
¡Comencemos a aprender juntos!
""")

# Función para practicar los nuevos ejercicios
def practicar_ejercicios():
    print("¡Vamos a practicar! Completa los ejercicios siguientes.")
    progreso = cargar_progreso()
    for i, ejercicio in enumerate(ejercicios_nuevos, 1):
        print(f"Ejercicio {i}: {ejercicio['pregunta']}")
        respuesta = input("Tu respuesta: ")
        if respuesta.strip().lower() == ejercicio["respuesta"].lower():
            print("¡Correcto!")
            progreso[f"Ejercicio {i}"] = "Correcto"
        else:
            print(f"Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
            progreso[f"Ejercicio {i}"] = "Incorrecto"
    guardar_progreso(progreso)

# Función principal del menú
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Introducción al programa")
        print("2. Practicar ejercicios nuevos")
        print("3. Guardar progreso")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            introduccion()
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            progreso = cargar_progreso()
            guardar_progreso(progreso)
        elif opcion == "4":
            print("¡Gracias por usar el programa! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu_principal()
