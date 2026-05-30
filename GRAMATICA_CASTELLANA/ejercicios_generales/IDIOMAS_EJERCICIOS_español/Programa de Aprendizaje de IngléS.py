def menu():
    print("=== Programa de Aprendizaje de Inglés ===")
    print("1. Corrección ortográfica y gramatical")
    print("2. Aprender vocabulario")
    print("3. Práctica de gramática")
    print("4. Traducción de oraciones")
    print("5. Salir")

def correccion_texto():
    print("Función de corrección de texto en inglés activada.")
    # Aquí puedes usar bibliotecas como TextBlob o LanguageTool para implementar la corrección.

def aprender_vocabulario():
    print("Aprende nuevas palabras en inglés:")
    palabras = {"dog": "perro", "house": "casa", "book": "libro"}
    for palabra, traduccion in palabras.items():
        print(f"{palabra} - {traduccion}")
    # También puedes implementar ejercicios interactivos para reforzar.

def practica_gramatica():
    print("Práctica de gramática básica:")
    preguntas = [
        {"pregunta": "¿Cómo se dice 'correr' en inglés?", "respuesta": "run"},
        {"pregunta": "¿Qué significa 'apple'?", "respuesta": "manzana"}
    ]
    for pregunta in preguntas:
        respuesta = input(pregunta["pregunta"] + " ")
        if respuesta.lower() == pregunta["respuesta"]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es {pregunta['respuesta']}.")

def traduccion_oraciones():
    print("Traducción de oraciones:")
    oraciones = [
        {"ingles": "I am happy.", "espanol": "Estoy feliz."},
        {"ingles": "The cat is on the table.", "espanol": "El gato está en la mesa."}
    ]
    for oracion in oraciones:
        print(f"Inglés: {oracion['ingles']} \nEspañol: {oracion['espanol']}")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        correccion_texto()
    elif opcion == "2":
        aprender_vocabulario()
    elif opcion == "3":
        practica_gramatica()
    elif opcion == "4":
        traduccion_oraciones()
    elif opcion == "5":
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
