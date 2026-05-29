# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

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

# Definimos una función para imprimir las combinaciones posibles para formar hiatos
def imprimir_combinaciones_hiatos():
    # Declaramos una lista para almacenar las combinaciones
    combinaciones = []

    # Generamos todas las combinaciones posibles
    for vocal1 in "aeiou":
        for vocal2 in "aeiou":
            # Si las vocales son diferentes, entonces forman un hiato
            if vocal1 != vocal2:
                combinaciones.append((vocal1, vocal2))

    # Imprimimos las combinaciones
    for vocal1, vocal2 in combinaciones:
        print("{}-{}".format(vocal1, vocal2))

# Imprimimos las combinaciones posibles para formar hiatos
imprimir_combinaciones_hiatos()

# Solicitamos al usuario que ingrese palabras
for vocal1, vocal2 in combinaciones:
    palabra = input("Ingrese una palabra con el hiato {}-{}: ".format(vocal1, vocal2))
    print("La palabra {} contiene el hiato {}-{}.".format(palabra, vocal1, vocal2))
