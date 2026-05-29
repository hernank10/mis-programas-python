# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para generar un conjunto de oraciones
def generar_conjunto_de_oraciones():
    # Declaramos una lista para almacenar las oraciones
    oraciones = []

    # Generamos 10 oraciones
    for _ in range(10):
        # Generamos una oración aleatoria
        oracion = random.choice([
            "¿**Dónde** está el **por** qué de esta situación?",
            "**Tú** y **yo** somos **los** únicos que podemos **hacer** algo.",
            "**El** **qué** y el **cómo** son **importantes**.",
            "**Sí**, **acepto** tu propuesta.",
            "**No**, **no** estoy de acuerdo.",
            "**Hoy** es **un** día **importante**.",
            "**El** **él** es **mi** amigo.",
            "**Ella** es **mi** hermana.",
            "**Tú** eres **mi** mejor amigo."
        ])
        oraciones.append(oracion)

    return oraciones

# Generamos un conjunto de oraciones
oraciones = generar_conjunto_de_oraciones()

# Imprimimos el conjunto de oraciones
print("Las oraciones a analizar son:")
for oracion in oraciones:
    print(oracion)

# Imprimimos la regla para diferenciar los monosílabos homónimos o polisémicos mediante una tilde diacrítica
print("**Regla:**")
print("* Los monosílabos **tónicos** que tienen **diptongo** o **triptongo** y **no** terminan en **n** o **s**, llevan **tilde**.")
print("* Los monosílabos **tónicos** que **no** tienen **diptongo** ni **triptongo** y **no** terminan en **n** o **s**, **no** llevan **tilde**.")

# Solicitamos al usuario que identifique, seleccione y transcriba la palabra homónima o polisémica en cada oración
for oracion in oraciones:
    # Imprimimos la oración
    print(oracion)

    # Solicitamos al usuario que identifique la palabra homónima o polisémica
    palabra = input("¿Cuál es la palabra homónima o polisémica en esta oración?: ")

    # Imprimimos la palabra identificada por el usuario
    print("La palabra identificada es: ", palabra)
