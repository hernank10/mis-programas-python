# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar palabras agudas que deben llevar tilde
def palabras_agudas_con_tilde(fragmento):
    # Declaramos una lista para almacenar las palabras
    palabras = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if fragmento[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se trata de una palabra aguda
            if fragmento[i + 1] in "aeiou":
                # Si la palabra tiene más de cuatro letras, entonces debe llevar tilde
                if len(fragmento[i:i + 2]) > 4:
                    palabras.append(fragmento[i:i + 2])

    return palabras

# Generamos un fragmento de texto con palabras agudas que deben llevar tilde
fragmento = "El águila saltó al aire. El murciélago voló al cielo. La palabra tilde lleva tilde."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que identifique las palabras
print("Ingrese las palabras agudas que deben llevar tilde:")

# Generamos una lista con 15 palabras agudas que deben llevar tilde
palabras_con_tilde = palabras_agudas_con_tilde(fragmento)

# Recorremos la lista de palabras con tilde
for palabra in palabras_con_tilde:
    # Solicitamos al usuario que identifique la palabra
    palabra_usuario = input("Ingrese la palabra {}: ".format(palabra))
    # Si la palabra coincide con la palabra del fragmento de texto, la consideramos correcta
    if palabra_usuario == palabra:
        print("La palabra {} debe llevar tilde.".format(palabra))
    # Si la palabra no coincide con la palabra del fragmento de texto, la consideramos incorrecta
    else:
        print("La palabra {} no debe llevar tilde.".format(palabra))
