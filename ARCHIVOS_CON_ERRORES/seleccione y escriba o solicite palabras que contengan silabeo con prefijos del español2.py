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

    # Imprimimos las palabras tetrasílabas:
    print("Tetrasílabas:")
    for palabra in palabras:
        if numero_de_silabas(palabra) == 4:
            print(palabra)

# Generamos un fragmento de texto con palabras de diferentes tipos
fragmento = "El perro ladra a la luna. La casa es grande y hermosa. El cielo es azul y el sol brilla."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que identifique 15 palabras
for i in range(15):
    palabra = input("Ingrese una palabra: ")
    # Si la palabra es correcta, la imprimimos
    if palabra in fragmento:
        print(palabra)
    # Si la palabra es incorrecta, avisamos al usuario
    else:
        print("La palabra {} no está en el fragmento de texto.".format(palabra))

# Definimos una lista con los prefijos del español
prefijos = ["des-", "in-", "im-", "re-", "sub-", "super-", "pre-", "post-", "anti-", "ex-", "contra-", "ultra-", "infra-", "supra-"]

# Solicitamos al usuario que seleccione una opción
opcion = input("¿Qué desea hacer?\n1. Identificar palabras con prefijos\n2. Seleccionar palabras con prefijos\n3. Escribir palabras con prefijos\n4. Solicitar palabras con prefijos\nIngrese una opción: ")

# Si el usuario selecciona la opción 1, identificamos palabras con prefijos
if opcion == "1":
    for palabra in fragmento.split():
        for prefijo in prefijos:
            if palabra.startswith(prefijo):
                print(palabra)

# Si el usuario selecciona la opción 2, seleccionamos palabras con prefijos
elif opcion == "2":
    palabras_con_prefijos = []
    for palabra in fragmento.split():
        for prefijo in prefijos:
            if palabra.startswith(prefijo):
                palabras_con_prefijos.append(palabra)
    print(palabras_con_prefijos)

# Si el usuario selecciona la opción 3, escribimos palabras con prefijos
elif opcion == "3":
    for prefijo in prefijos:
        palabra = input("Ingrese una palabra con el prefijo {}
