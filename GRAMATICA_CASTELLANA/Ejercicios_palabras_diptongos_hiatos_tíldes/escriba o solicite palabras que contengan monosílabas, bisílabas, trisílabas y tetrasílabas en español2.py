# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar el número de sílabas de una palabra
def numero_de_silabas(palabra):
    # Recorremos la palabra letra por letra
    for i in range(len(palabra)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if palabra[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se cuenta como una sílaba
            if palabra[i + 1] in "aeiou":
                return 1
            else:
                # Si la siguiente letra no es una vocal, entonces se cuenta como dos sílabas
                return 2
    return 1

# Definimos una función para imprimir las palabras de un fragmento de texto según su número de sílabas
def imprimir_palabras_por_numero_de_silabas(fragmento):
    # Declaramos una lista para almacenar las palabras
    palabras = fragmento.split()

    # Imprimimos las palabras monosílabas
    print("Monosílabas:")
    for palabra in palabras:
        if numero_de_silabas(palabra) == 1:
            print(palabra)

    # Imprimimos las palabras bisílabas
    print("Bisílabas:")
    for palabra in palabras:
        if numero_de_silabas(palabra) == 2:
            print(palabra)

    # Imprimimos las palabras trisílabas
    print("Trisílabas:")
    for palabra in palabras:
        if numero_de_silabas(palabra) == 3:
            print(palabra)

    # Imprimimos las palabras tetrasílabas
    print("Tetrasílabas:")
    for palabra in palabras:
        if numero_de_silabas(palabra) == 4:
            print(palabra)

# Solicitamos al usuario que ingrese un fragmento de texto
fragmento = input("Ingrese un fragmento de texto: ")

# Imprimimos las palabras del fragmento de texto según su número de sílabas
imprimir_palabras_por_numero_de_silabas(fragmento)
