# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para generar un grupo de palabras ordenadas en tres columnas
def generar_grupo_de_palabras():
    # Declaramos una lista para almacenar las palabras
    palabras = []

    # Generamos 10 palabras aleatorias
    for _ in range(10):
        palabra = random.choice([
            "casa", "coche", "gato", "perro", "libro", "mesa", "silla", "reloj", "ordenador", "teléfono"
        ])
        palabras.append(palabra)

    # Ordenamos las palabras en tres columnas
    palabras.sort()
    palabras_columna_1 = palabras[:3]
    palabras_columna_2 = palabras[3:6]
    palabras_columna_3 = palabras[6:]

    return palabras_columna_1, palabras_columna_2, palabras_columna_3

# Generamos un grupo de palabras
palabras_columna_1, palabras_columna_2, palabras_columna_3 = generar_grupo_de_palabras()

# Imprimimos el grupo de palabras
print("Columna 1:", palabras_columna_1)
print("Columna 2:", palabras_columna_2)
print("Columna 3:", palabras_columna_3)

# Solicitamos al usuario que identifique un término
print("Ingrese el término que desee usar en las oraciones:")
termino = input()

# Generamos cinco oraciones
for _ in range(5):
    # Seleccionamos una palabra aleatoria de cada columna
    palabra_1 = random.choice(palabras_columna_1)
    palabra_2 = random.choice(palabras_columna_2)
    palabra_3 = random.choice(palabras_columna_3)

    # Generamos una oración
    oracion = "El {} {} el {} del {}.".format(palabra_1, termino, palabra_2, palabra_3)

    # Imprimimos la oración
    print(oracion)
