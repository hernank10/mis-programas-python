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
    "excepción": "Palabra que no sigue las reglas generales de la gramática.",
    "paradigma": "Conjunto de formas flexivas de una palabra.",
    "desinencia": "Morfema flexivo que se añade al lexema para formar diferentes palabras.",
    "afijo": "Elemento añadido a una raíz para modificar su significado.",
    "sufijación": "Proceso de añadir sufijos a una raíz.",
    "prefijación": "Proceso de añadir prefijos a una raíz.",
    "composición": "Formación de palabras a partir de la unión de dos o más palabras.",
    "sintagma": "Grupo de palabras que forman una unidad sintáctica.",
    "concordancia": "Relación gramatical en la que las formas de las palabras deben corresponder en género, número, persona, etc.",
    "verbo": "Palabra que expresa acción, estado o proceso.",
    "sustantivo": "Palabra que designa seres, cosas o ideas.",
    "adjetivo": "Palabra que califica o determina al sustantivo.",
    "pronombre": "Palabra que sustituye al sustantivo.",
    "adverbio": "Palabra que modifica al verbo, adjetivo u otro adverbio.",
    "preposición": "Palabra que relaciona elementos de la oración.",
    "conjunción": "Palabra que une palabras o proposiciones.",
    "interjección": "Palabra o expresión que manifiesta una emoción o sentimiento.",
    "género": "Categoría gramatical que distingue entre masculino, femenino y neutro.",
    "número": "Categoría gramatical que distingue entre singular y plural.",
    "persona": "Categoría gramatical que distingue entre primera, segunda y tercera persona.",
    "tiempo": "Categoría gramatical que sitúa la acción del verbo en el pasado, presente o futuro.",
    "modo": "Categoría gramatical que expresa la actitud del hablante hacia la acción del verbo (indicativo, subjuntivo, imperativo).",
    "aspecto": "Categoría gramatical que expresa la duración o completitud de la acción del verbo (perfecto, imperfecto)."
}

# Función para agregar una palabra y su significado
def agregar_palabra():
    palabra = input("Introduce la palabra: ")
    significado = input("Introduce el significado: ")
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
            agregar_palabra()
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
