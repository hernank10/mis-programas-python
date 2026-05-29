# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar las expresiones que deben escribirse unidas
def expresiones_unidas(fragmento):
    # Declaramos una lista para almacenar las expresiones
    expresiones = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if fragmento[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se trata de una expresión que debe escribirse unida
            if fragmento[i + 1] in "aeiou":
                expresiones.append(fragmento[i:i + 2])

    return expresiones

# Generamos un fragmento de texto con expresiones que deben escribirse unidas
fragmento = "El perro ladra a la luna. La casa es grande y hermosa. El cielo es azul y el sol brilla."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que seleccione una opción
opcion = input("¿Qué desea hacer?\n1. Identificar expresiones unidas\n2. Seleccionar expresiones unidas\n3. Escribir expresiones unidas\n4. Solicitar expresiones unidas\nIngrese una opción: ")

# Si el usuario selecciona la opción 1, identificamos expresiones unidas
if opcion == "1":
    for expresion in expresiones_unidas(fragmento):
        print(expresion)

# Si el usuario selecciona la opción 2, seleccionamos expresiones unidas
elif opcion == "2":
    expresiones_unidas = expresiones_unidas(fragmento)
    print(expresiones_unidas)

# Si el usuario selecciona la opción 3, escribimos expresiones unidas
elif opcion == "3":
    for expresion in expresiones_unidas(fragmento):
        print(input("Ingrese una expresión unida: "))

# Si el usuario selecciona la opción 4, solicita expresiones unidas
elif opcion == "4":
    expresion = input("Ingrese una expresión unida: ")
    if expresion in expresiones_unidas(fragmento):
        print("La expresión {} debe escribirse unida.".format(expresion))
    else:
        print("La expresión {} no debe escribirse unida.".format(expresion))
