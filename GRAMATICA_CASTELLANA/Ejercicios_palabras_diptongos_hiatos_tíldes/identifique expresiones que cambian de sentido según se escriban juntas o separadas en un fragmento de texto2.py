# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar las expresiones que cambian de sentido según se escriban juntas o separadas
def expresiones_cambian_sentido(fragmento):
    # Declaramos una lista para almacenar las expresiones
    expresiones = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if fragmento[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se trata de una expresión que puede cambiar de sentido
            if fragmento[i + 1] in "aeiou":
                # Verificamos si la expresión unida tiene un significado diferente a la expresión separada
                expresion_unida = fragmento[i:i + 2]
                expresion_separada = fragmento[i] + " " + fragmento[i + 1]
                if expresion_unida != expresion_separada:
                    expresiones.append(expresion_unida)

    return expresiones

# Generamos un fragmento de texto con expresiones que pueden cambiar de sentido
fragmento = "El perro ladra a la luna. La casa es grande y hermosa. El cielo es azul y el sol brilla."

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que identifique las expresiones
print("Ingrese las expresiones que cambian de sentido:")

# Recorremos el fragmento de texto
for i in range(len(fragmento)):
    # Si la letra actual es una vocal, verificamos la siguiente letra
    if fragmento[i] in "aeiou":
        # Si la siguiente letra también es una vocal, entonces se trata de una expresión que puede cambiar de sentido
        if fragmento[i + 1] in "aeiou":
            # Verificamos si la expresión unida tiene un significado diferente a la expresión separada
            expresion_unida = fragmento[i:i + 2]
            expresion_separada = fragmento[i] + " " + fragmento[i + 1]
            if expresion_unida != expresion_separada:
                # Solicitamos al usuario que identifique la expresión
                expresion = input("Ingrese la expresión {}: ".format(expresion_unida))
                # Si la expresión coincide con la expresión del fragmento de texto, la consideramos correcta
                if expresion == expresion_unida:
                    print("La expresión {} cambia de sentido según se escriba unida o separada.".format(expresion_unida))
                # Si la expresión no coincide con la expresión del fragmento de texto, la consideramos incorrecta
                else:
                    print("La expresión {} no cambia de sentido según se escriba unida o separada.".format(expresion_unida))
