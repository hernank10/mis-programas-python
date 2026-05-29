import random

def mostrar_teoria():
    teoria = """
    En español, los dativos no seleccionados aparecen en construcciones anticausativas
    y pueden interpretarse como causantes accidentales. Ejemplo:
    - Juan rompió el móvil. (transitiva)
    - A Juan se le rompió el móvil. (anticausativa con dativo)
    """
    print(teoria)

def mostrar_ejemplos():
    ejemplos = [
        "A Pedro se le cayó el vaso.",
        "A María se le perdió la llave.",
        "A Juan se le olvidó la cita.",
        "A Sofía se le quemó la comida."
    ]
    for ejemplo in ejemplos:
        print(f"- {ejemplo}")

def practicar_escritura():
    print("Escribe una oración con un dativo no seleccionado:")
    oracion = input("Tu oración: ")
    if "se le" in oracion or "a " in oracion:
        print("¡Bien! Tu oración contiene un dativo no seleccionado.")
    else:
        print("Revisa la estructura, intenta incluir 'se le' y un verbo de cambio de estado.")

def test_interactivo():
    preguntas = {
        "¿Cuál de estas oraciones tiene un dativo no seleccionado?": {
            "A": "Pedro rompió el vaso.",
            "B": "A Pedro se le rompió el vaso.",
            "C": "Pedro tiene un vaso azul.",
            "respuesta": "B"
        },
        "En la oración 'A Sofía se le cayó el libro', ¿qué función tiene 'A Sofía'?": {
            "A": "Sujeto",
            "B": "Objeto directo",
            "C": "Dativo no seleccionado",
            "respuesta": "C"
        }
    }
    
    for pregunta, opciones in preguntas.items():
        print(pregunta)
        for clave, valor in opciones.items():
            if clave != "respuesta":
                print(f"{clave}) {valor}")
        respuesta = input("Tu respuesta: ").strip().upper()
        if respuesta == opciones["respuesta"]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era {opciones['respuesta']}.")

def menu():
    while True:
        print("\nMenú de práctica")
        print("1. Leer teoría")
        print("2. Ver ejemplos")
        print("3. Practicar escritura")
        print("4. Test interactivo")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_escritura()
        elif opcion == "4":
            test_interactivo()
        elif opcion == "5":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
