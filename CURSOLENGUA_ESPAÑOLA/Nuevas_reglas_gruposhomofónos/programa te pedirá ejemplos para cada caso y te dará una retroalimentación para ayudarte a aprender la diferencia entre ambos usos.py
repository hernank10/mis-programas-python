import random

def practicar_porques():
    while True:
        opcion = input("Elige una opción:\n1. Practicar 'porqué'\n2. Practicar 'por qué'\n3. Salir\n")

        if opcion == '1':
            palabra = "porqué"
            oracion = input(f"Completa la oración con '{palabra}':\nNo entiendo el ______ de tu decisión.\n")
            if oracion.lower() == "no entiendo el porqué de tu decisión.":
                print("¡Correcto! 'Porqué' se usa como sustantivo para referirse a la razón.")
            else:
                print("Incorrecto. Recuerda que 'porqué' se usa como sustantivo.")

        elif opcion == '2':
            palabra = "por qué"
            oracion = input(f"Completa la oración con '{palabra}':\n______ no me llamas?\n")
            if oracion.lower() == "por qué no me llamas?":
                print("¡Correcto! 'Por qué' se usa para hacer preguntas.")
            else:
                print("Incorrecto. Recuerda que 'por qué' se usa para hacer preguntas.")

        elif opcion == '3':
            print("¡Hasta luego! Gracias por practicar.")
            break

        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    practicar_porques()
