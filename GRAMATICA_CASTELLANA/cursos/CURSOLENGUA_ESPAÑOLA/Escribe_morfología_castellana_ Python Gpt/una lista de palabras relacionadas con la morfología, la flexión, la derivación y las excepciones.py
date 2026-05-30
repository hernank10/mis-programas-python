import random

# Diccionario de palabras de morfología, flexión, derivación y excepciones
palabras_diccionario = {
    "morfología": "Estudio de la estructura y formación de las palabras.",
    "flexión": "Modificación de una palabra para expresar diferentes categorías gramaticales como tiempo, modo, número y persona.",
    "derivación": "Proceso de formación de palabras mediante la adición de afijos.",
    "composición": "Proceso de formación de palabras combinando dos o más raíces.",
    "sufijo": "Afijo que se añade al final de una palabra.",
    "prefijo": "Afijo que se añade al principio de una palabra.",
    "infijo": "Afijo que se inserta dentro de una palabra.",
    "lexema": "Unidad mínima con significado léxico.",
    "morfema": "Unidad mínima con significado gramatical.",
    "raíz": "Elemento básico de una palabra que contiene su significado principal.",
    "excepción": "Palabra que no sigue las reglas generales de la gramática."
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
