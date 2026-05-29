# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar si una palabra contiene diptongo
def contiene_diptongo(palabra):
    # Recorremos la palabra letra por letra
    for i in range(len(palabra)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if palabra[i] in "aeiou":
            # Si la siguiente letra es también una vocal, entonces la palabra contiene un diptongo
            if palabra[i + 1] in "aeiou":
                return True
    return False

# Definimos una función para imprimir el fragmento de texto
def imprimir_fragmento_texto(fragmento):
    print(fragmento)

# Definimos una función para identificar los diptongos de un párrafo narrativo
def identificar_diptongos_parrafo_narrativo():
    # Declaramos una lista para almacenar los párrafos narrativos
    parametros = [
        "El perro ladra a la luna.",
        "La rana salta en el estanque.",
        "El viento sopla en el bosque.",
        "El sol brilla en el cielo.",
        "La lluvia cae sobre la tierra.",
    ]

    # Generamos un párrafo narrativo aleatorio
    parametro = random.choice(parametros)

    # Imprimimos el párrafo narrativo
    imprimir_fragmento_texto(parametro)

    # Declaramos una lista para almacenar las palabras con diptongos
    palabras_diptongos = []

    # Recorremos el párrafo narrativo, palabra por palabra
    for palabra in parametro.split():
        # Si la palabra contiene un diptongo, la agregamos a la lista de palabras con diptongos
        if contiene_diptongo(palabra):
            palabras_diptongos.append(palabra)

    # Imprimimos las palabras con diptongos
    print("Palabras con diptongo:")
    for palabra in palabras_diptongos:
        print(palabra)

# Solicitamos al usuario que identifique los diptongos de un párrafo narrativo
identificar_diptongos_parrafo_narrativo()
