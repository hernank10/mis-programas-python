# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar palabras agudas que no deben llevar tilde
def palabras_agudas_sin_tilde(fragmento):
    # Declaramos una lista para almacenar las palabras
    palabras = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if fragmento[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se trata de una palabra aguda
            if fragmento[i + 1] in "aeiou":
                # Si la palabra tiene menos de cinco letras, entonces no debe llevar tilde
                if len(fragmento[i:i + 2]) <= 5:
                    palabras.append(fragmento[i:i + 2])

    return palabras

# Generamos un fragmento de texto con palabras agudas que no deben llevar tilde
fragmento = "El lápiz y el papel son útiles para escribir. El libro está en la mesa."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que identifique las palabras
print("Ingrese las palabras agudas que no deben llevar tilde:")

# Recorremos el fragmento de texto
for i in range(len(fragmento)):
    # Si la letra actual es una vocal, verificamos la siguiente letra
    if fragmento[i] in "aeiou":
        # Si la siguiente letra también es una vocal, entonces se trata de una palabra aguda
        if fragmento[i + 1] in "aeiou":
            # Si la palabra tiene menos de cinco letras, entonces no debe llevar tilde
            if len(fragmento[i:i + 2]) <= 5:
                # Solicitamos al usuario que identifique la palabra
                palabra = input("Ingrese la palabra {}: ".format(fragmento[i:i + 2]))
                # Si la palabra coincide con la palabra del fragmento de texto, la consideramos correcta
                if palabra == fragmento[i:i + 2]:
                    print("La palabra {} no debe llevar tilde.".format(fragmento[i:i + 2]))
                # Si la palabra no coincide con la palabra del fragmento de texto, la consideramos incorrecta
                else:
                    print("La palabra {} debe llevar tilde.".format(fragmento[i:i + 2]))
