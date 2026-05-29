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

# Definimos una función para identificar si una palabra contiene hiato
def contiene_hiato(palabra):
    # Recorremos la palabra letra por letra
    for i in range(len(palabra)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if palabra[i] in "aeiou":
            # Si la siguiente letra no es una vocal, entonces la palabra contiene un hiato
            if palabra[i + 1] not in "aeiou":
                return True
    return False

# Definimos una función para imprimir el fragmento de texto
def imprimir_fragmento_texto(fragmento):
    print(fragmento)

# Definimos una función para solicitar al usuario que identifique palabras con diptongos y hiatos
def solicitar_identificacion_diptongos_hiatos():
    # Solicitamos al usuario que ingrese un fragmento de texto
    fragmento = input("Ingrese un fragmento de texto: ")

    # Imprimimos el fragmento de texto
    imprimir_fragmento_texto(fragmento)

    # Declaramos una lista para almacenar las palabras con diptongos
    palabras_diptongos = []

    # Declaramos una lista para almacenar las palabras con hiatos
    palabras_hiatos = []

    # Recorremos el fragmento de texto, palabra por palabra
    for palabra in fragmento.split():
        # Si la palabra contiene un diptongo, la agregamos a la lista de palabras con diptongos
        if contiene_diptongo(palabra):
            palabras_diptongos.append(palabra)
        # Si la palabra contiene un hiato, la agregamos a la lista de palabras con hiatos
        elif contiene_hiato(palabra):
            palabras_hiatos.append(palabra)

    # Imprimimos las palabras con diptongos
    print("Palabras con diptongo:")
    for palabra in palabras_diptongos:
        print(palabra)

    # Imprimimos las palabras con hiatos
    print("Palabras con hiato:")
    for palabra in palabras_hiatos:
        print(palabra)

# Solicitamos al usuario que identifique palabras con diptongos y hiatos
solicitar_identificacion_diptongos_hiatos()
