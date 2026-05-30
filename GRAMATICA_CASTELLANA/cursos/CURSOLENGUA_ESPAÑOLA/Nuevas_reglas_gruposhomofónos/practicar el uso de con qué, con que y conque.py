import random

def practicar_conque():
    while True:
        opcion = input("Elige una opción:\n1. Practicar 'con qué'\n2. Practicar 'con que'\n3. Practicar 'conque'\n4. Salir\n")

        if opcion == '1':
            palabra = "con qué"
            oracion = input(f"Completa la oración con '{palabra}':\n¿______ vas a cortar el césped?\n")
            if oracion.lower() == "¿con qué vas a cortar el césped?":
                print("¡Correcto! 'Con qué' se usa para preguntar.")
            else:
                print("Incorrecto. Recuerda que 'con qué' se usa para preguntar.")

        elif opcion == '2':
            palabra = "con que"
            oracion = input(f"Completa la oración con '{palabra}':\nEsta es la herramienta ______ construimos la casa.\n")
            if oracion.lower() in ["esta es la herramienta con que construimos la casa.", "esta es la herramienta con la que construimos la casa."]:
                print("¡Correcto! 'Con que' se usa para indicar el instrumento o medio.")
            else:
                print("Incorrecto. Recuerda que 'con que' se usa para indicar el instrumento o medio.")

        elif opcion == '3':
            palabra = "conque"
            oracion = input(f"Completa la oración con '{palabra}':\nYa terminaste el trabajo, ______ puedes descansar.\n")
            if oracion.lower() in ["ya terminaste el trabajo, conque puedes descansar.", "ya terminaste el trabajo, así que puedes descansar."]:
                print("¡Correcto! 'Conque' se usa para expresar consecuencia.")
            else:
                print("Incorrecto. Recuerda que 'conque' se usa para expresar consecuencia.")

        elif opcion == '4':
            print("¡Hasta luego! Gracias por practicar.")
            break

        else:
            print("Opción inválida. Por favor, elige 1, 2, 3 o 4.")

if __name__ == "__main__":
    practicar_conque()
