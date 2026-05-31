import random
from datetime import datetime

# Base de datos de palabras y oraciones predispuestas
palabras = [
    "sol", "estrella", "luz", "árbol", "jardín", "niño", "escuela", "montaña", 
    "río", "ciudad", "pájaro", "mañana", "camino", "silencio", "libro", "música", 
    "familia", "amistad", "ventana", "mar", "cielo", "viaje", "historia", 
    "vida", "tiempo", "naturaleza", "puerta", "casa", "película", "trabajo",
    "esperanza", "amor", "felicidad", "día", "noche", "sueño", "calor", "frío", 
    "comida", "juego", "roca", "perro", "gato", "agua", "fuego", "color", 
    "flores", "bosque", "nieve", "playa", "coche"
]

oraciones_predispuestas = {
    "sol": {
        "simple": "El sol brilla en el cielo.",
        "compuesta": "El sol brilla en el cielo, y las nubes flotan tranquilamente."
    },
    "niño": {
        "simple": "El niño juega en el parque.",
        "compuesta": "El niño juega en el parque mientras su madre lo observa."
    },
    "libro": {
        "simple": "El libro está sobre la mesa.",
        "compuesta": "El libro está sobre la mesa porque lo dejé ahí después de leer."
    }
    # Puedes agregar más palabras con oraciones predispuestas aquí.
}

# Función para guardar progreso
def guardar_progreso(palabra, tipo, correcta, usuario):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado = "correcto" if correcta else "incorrecto"
    with open("progreso_redaccion.txt", "a") as archivo:
        archivo.write(f"{fecha} - Palabra: {palabra} - Oración {tipo}: {resultado} - Usuario: {usuario}\n")

# Función para practicar con una palabra
def practicar_palabra(palabra):
    print(f"\nPalabra seleccionada: {palabra}")
    print("1. Redacta una oración simple.")
    usuario_simple = input("Escribe tu oración simple: ").strip()
    print("2. Redacta una oración compuesta.")
    usuario_compuesta = input("Escribe tu oración compuesta: ").strip()

    simple_correcta = oraciones_predispuestas.get(palabra, {}).get("simple", "").lower()
    compuesta_correcta = oraciones_predispuestas.get(palabra, {}).get("compuesta", "").lower()

    if simple_correcta:
        correcta_simple = usuario_simple.lower() == simple_correcta
        print(f"Oración simple: {'Correcto' if correcta_simple else 'Incorrecto'}")
        if not correcta_simple:
            print(f"Oración correcta: {simple_correcta}")
        guardar_progreso(palabra, "simple", correcta_simple, usuario_simple)

    if compuesta_correcta:
        correcta_compuesta = usuario_compuesta.lower() == compuesta_correcta
        print(f"Oración compuesta: {'Correcto' if correcta_compuesta else 'Incorrecto'}")
        if not correcta_compuesta:
            print(f"Oración correcta: {compuesta_correcta}")
        guardar_progreso(palabra, "compuesta", correcta_compuesta, usuario_compuesta)

# Mostrar la lista completa de palabras y sus oraciones predispuestas
def mostrar_lista():
    print("\nLista de palabras y sus oraciones predispuestas:")
    for palabra, oraciones in oraciones_predispuestas.items():
        print(f"\nPalabra: {palabra}")
        print(f"- Oración simple: {oraciones['simple']}")
        print(f"- Oración compuesta: {oraciones['compuesta']}")
    input("\nPresiona Enter para volver al menú principal...\n")

# Menú principal
def menu_principal():
    while True:
        print("=== Menú Principal ===")
        print("1. Ver lista de palabras y oraciones predispuestas")
        print("2. Practicar redacción")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_lista()
        elif opcion == "2":
            palabras_seleccionadas = random.sample(palabras, 10)  # Selecciona 10 palabras al azar
            for palabra in palabras_seleccionadas:
                practicar_palabra(palabra)
                print("-" * 40)
            print("\n¡Has terminado la práctica! Revisa tu progreso en 'progreso_redaccion.txt'.")
        elif opcion == "3":
            print("¡Gracias por usar el programa! Hasta pronto.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_principal()
