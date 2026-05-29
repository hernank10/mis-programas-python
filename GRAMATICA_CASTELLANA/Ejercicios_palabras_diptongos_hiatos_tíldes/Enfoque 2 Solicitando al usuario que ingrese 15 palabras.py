# Importamos la biblioteca para el manejo de archivos
import random

# Definimos una función para determinar si una palabra contiene un diptongo
def contiene_diptongo(palabra):
    # Recorremos la palabra letra por letra
    for i in range(len(palabra)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if palabra[i] in "aeiou":
            # Si la siguiente letra es también una vocal, entonces la palabra contiene un diptongo
            if palabra[i + 1] in "aeiou":
                return True
    return False

# Solicitamos al usuario que ingrese 15 palabras
palabras = []
for i in range(15):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)

# Recorremos la lista de palabras
for palabra in palabras:
    # Imprimimos la palabra y si contiene un diptongo
    print(palabra, contiene_diptongo(palabra))
