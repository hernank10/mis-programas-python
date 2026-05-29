# Importamos la biblioteca para el manejo de archivos
import random

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

# Definimos una función para generar una lista de 15 palabras que contengan diptongo
def generar_lista_diptongos():
    # Abrimos el archivo con las palabras del diccionario español
    with open("diccionario.txt", "r") as f:
        # Leemos todas las palabras del archivo
        palabras = f.read().splitlines()

    # Creamos una lista vacía para almacenar las palabras que contienen diptongo
    palabras_diptongos = []

    # Recorremos la lista de palabras
    for palabra in palabras:
        # Si la palabra contiene un diptongo, la agregamos a la lista
        if contiene_diptongo(palabra):
            palabras_diptongos.append(palabra)

    # Regresamos la lista de palabras que contienen diptongo
    return palabras_diptongos

# Generamos la lista de palabras que contienen diptongo
palabras_diptongos = generar_lista_diptongos()

# Imprimimos las 15 primeras palabras de la lista
for i in range(15):
    # Si la palabra es demasiado larga, la imprimimos de forma abreviada
    if len(palabras_diptongos[i]) > 20:
        print(palabras_diptongos[i][:20] + "...")
    else:
        print(palabras_diptongos[i])
