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

# Definimos una función para generar una lista de palabras que contienen diptongos
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

# Definimos una función para imprimir un poema sobre los diptongos
def imprimir_poema_diptongos():
    print("**Poema sobre los diptongos**")
    print("En español, los diptongos")
    print("Son dos vocales en una sola sílaba")
    print("Pueden ser de dos tipos:")
    print("Ascendentes o descendentes")
    print()
    print("**Ascendentes**")
    print("Comenzan con una vocal abierta y terminan en una cerrada")
    print("Ejemplos: ai, au, ei, eu, oi, ou")
    print()
    print("**Descendentes**")
    print("Comenzan con una vocal cerrada y terminan en una abierta")
    print("Ejemplos: ae, ao, ea, eo, oa, oe")
    print()

# Imprimimos el poema sobre los diptongos
imprimir_poema_diptongos()

# Generamos la lista de palabras que contienen diptongos
palabras_diptongos = generar_lista_diptongos()

# Solicitamos al usuario que identifique las palabras que contienen diptongos
print("¿Quieres identificar las palabras que contienen diptongos?")
opcion = input("(S)í o (N)o: ")

# Si el usuario quiere identificar las palabras, le mostramos una lista
if opcion.lower() == "s":
    print("Aquí hay una lista de palabras que contienen diptongos:")
    for palabra in palabras_diptongos:
        print(palabra)

# Si el usuario quiere escribir las palabras, le solicitamos que ingrese 15 palabras
elif opcion.lower() == "n":
    print("¿Quieres escribir 15 palabras que contengan diptongos?")
    opcion2 = input("(S)í o (N)o: ")

    # Si el usuario quiere escribir las palabras, le solicitamos que ingrese 15 palabras
    if opcion2.lower() == "s":
        palabras = []
        for i in range(15):
            palabra = input("Ingrese una palabra que contenga un diptongo: ")
            palabras.append(palabra)

        # Imprimimos las palabras que ingresó el usuario
        print("Aquí están las palabras que ingresaste:")
        for palabra in palabras:
            print(palabra)

    # Si el usuario no quiere escribir las palabras, mostramos un mensaje
    else:
        print("De acuerdo, no escribirás ninguna palabra.")
