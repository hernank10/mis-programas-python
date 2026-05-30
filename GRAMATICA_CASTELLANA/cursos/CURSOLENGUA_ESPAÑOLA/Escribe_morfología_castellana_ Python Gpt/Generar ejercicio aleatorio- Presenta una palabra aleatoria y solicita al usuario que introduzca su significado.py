import random

# Diccionario de palabras y sus significados
palabras_diccionario = {
    "parabrisas": "Dispositivo de vidrio en el automóvil que protege del viento y la lluvia.",
    "sacapuntas": "Instrumento para afilar lápices.",
    "montaña rusa": "Atracción de feria o parque de atracciones con un recorrido en vías con muchas subidas y bajadas.",
    "paraguas": "Objeto portátil que se usa para protegerse de la lluvia.",
    "hispanoamericano": "Relativo a los países de América que fueron colonizados por España.",
    "malgastar": "Usar el dinero o recursos de manera ineficiente.",
    "bienvenido": "Expresión de recibimiento cordial."
}

# Función para agregar una palabra y su significado
def agregar_palabra(palabra, significado):
    palabras_diccionario[palabra] = significado
    print(f'Palabra "{palabra}" agregada con éxito.')

# Función para mostrar todas las palabras y sus significados
def mostrar_palabras():
    print("Palabras y sus significados:")
    for palabra, significado in palabras_diccionario.items():
        print(f'{palabra}: {significado}')

# Función para generar ejercicios aleatorios
def generar_ejercicio():
    palabra, significado = random.choice(list(palabras_diccionario.items()))
    print(f'¿Cuál es el significado de "{palabra}"?')
    respuesta = input("Tu respuesta: ")
    
    if respuesta.strip().lower() == significado.strip().lower():
        print("¡Correcto!")
    else:
        print(f'Incorrecto. El significado correcto es: "{significado}".')

# Menú principal del programa
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar palabra y significado")
        print("2. Mostrar todas las palabras y significados")
        print("3. Generar ejercicio aleatorio")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            palabra = input("Introduce la palabra: ")
            significado = input("Introduce el significado: ")
            agregar_palabra(palabra, significado)
        elif opcion == '2':
            mostrar_palabras()
        elif opcion == '3':
            generar_ejercicio()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()
