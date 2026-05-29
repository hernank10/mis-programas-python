# Importamos la biblioteca para el manejo de archivos
import random

# Definimos una función para generar una lista de las 14 combinaciones posibles para formar diptongos
def generar_combinaciones_diptongos():
    # Creamos una lista vacía para almacenar las combinaciones
    combinaciones = []

    # Recorremos todas las combinaciones posibles
    for vocal1 in "aeiou":
        for vocal2 in "aeiou":
            # Si las vocales son diferentes, entonces forman un diptongo
            if vocal1 != vocal2:
                combinaciones.append((vocal1, vocal2))

    return combinaciones

# Generamos la lista de combinaciones
combinaciones = generar_combinaciones_diptongos()

# Imprimimos las combinaciones
for combinación in combinaciones:
    print(combinación)

# Solicitamos al usuario que ingrese palabras para cada combinación
for combinación in combinaciones:
    palabra = input("Ingrese una palabra que contenga el diptongo {}: ".format(combinación))
    print("La palabra {} contiene el diptongo {}.".format(palabra, combinación))
