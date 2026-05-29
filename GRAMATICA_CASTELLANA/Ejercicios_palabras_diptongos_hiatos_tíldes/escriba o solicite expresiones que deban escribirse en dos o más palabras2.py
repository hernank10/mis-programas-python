# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar las expresiones que deben escribirse en dos o más palabras
def expresiones_en_dos_o_mas_palabras(fragmento):
    # Declaramos una lista para almacenar las expresiones
    expresiones = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es un espacio en blanco, verificamos la siguiente letra
        if fragmento[i] == " ":
            # Si la siguiente letra también es un espacio en blanco, entonces se trata de una expresión que debe escribirse en dos o más palabras
            if fragmento[i + 1] == " ":
                expresiones.append(fragmento[i:i + 2])

    return expresiones

# Generamos un fragmento de texto con expresiones que deben escribirse en dos o más palabras
fragmento = "El perro ladra a la luna. La casa es grande y hermosa. El cielo es azul y el sol brilla."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que seleccione una opción
opcion = input("¿Qué desea hacer?\n1. Identificar expresiones en dos o más palabras\n2. Seleccionar expresiones en dos o más palabras\n3. Escribir expresiones en dos o más palabras\n4. Solicitar expresiones en dos o más palabras\nIngrese una opción: ")

# Si el usuario selecciona la opción 1, identificamos expresiones en dos o más palabras
if opcion == "1":
    for expresion in expresiones_en_dos_o_mas_palabras(fragmento):
        print(expresion)

# Si el usuario selecciona la opción 2, seleccionamos expresiones en dos o más palabras
elif opcion == "2":
    expresiones_en_dos_o_mas_palabras = expresiones_en_dos_o_mas_palabras(fragmento)
    print(expresiones_en_dos_o_mas_palabras)

# Si el usuario selecciona la opción 3, escribimos expresiones en dos o más palabras
elif opcion == "3":
    for expresion in expresiones_en_dos_o_mas_palabras(fragmento):
        print(input("Ingrese una expresión en dos o más palabras: "))

# Si el usuario selecciona la opción 4, solicita expresiones en dos o más palabras
elif opcion == "4":
    expresion = input("Ingrese una expresión en dos o más palabras: ")
    if expresion in expresiones_en_dos_o_mas_palabras(fragmento):
        print("La expresión {} debe escribirse en dos o más palabras.".format(expresion))
    else:
        print("La expresión {} no debe escribirse en dos o más palabras.".format(expresion))
