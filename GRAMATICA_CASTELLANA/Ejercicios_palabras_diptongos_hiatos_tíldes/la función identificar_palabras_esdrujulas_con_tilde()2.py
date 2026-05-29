# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para identificar palabras esdrújulas que deben llevar tilde
def palabras_esdrujulas_con_tilde(fragmento):
    # Declaramos una lista para almacenar las palabras
    palabras = []

    # Recorremos el fragmento de texto letra por letra
    for i in range(len(fragmento)):
        # Si la letra actual es una vocal, verificamos la siguiente letra
        if fragmento[i] in "aeiou":
            # Si la siguiente letra también es una vocal, entonces se trata de una palabra esdrújula
            if fragmento[i + 1] in "aeiou":
                # Si la palabra tiene más de cuatro letras, entonces debe llevar tilde
                if len(fragmento[i:i + 3]) > 4:
                    palabras.append(fragmento[i:i + 3])

    return palabras

# Generamos un fragmento de texto con palabras esdrújulas que deben llevar tilde
fragmento = """
La importancia de la educación radica en su capacidad de transformar vidas. La educación permite a las personas adquirir conocimientos, habilidades y valores que les permiten desarrollarse plenamente y contribuir a la sociedad.

La educación es un derecho fundamental de todos los seres humanos, independientemente de su origen, condición social o económica. Todos los niños, niñas y adolescentes tienen derecho a acceder a una educación de calidad que les permita alcanzar su pleno potencial.

La educación es un bien público que beneficia a toda la sociedad. Una sociedad educada es una sociedad más justa, equitativa y sostenible.
"""

# Imprimimos el fragmento de texto
print(fragmento)

# Solicitamos al usuario que identifique las palabras
print("Ingrese las palabras esdrújulas que deben llevar tilde:")

# Generamos una lista con 15 palabras esdrújulas que deben llevar tilde
palabras_con_tilde = palabras_esdrujulas_con_tilde(fragmento)

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
