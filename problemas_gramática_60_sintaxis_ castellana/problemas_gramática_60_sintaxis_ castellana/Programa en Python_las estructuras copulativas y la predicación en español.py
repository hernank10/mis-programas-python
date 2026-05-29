import random

def mostrar_teoria():
    teoria = """
    Las oraciones copulativas son aquellas que utilizan los verbos 'ser' o 'estar' 
    como elementos de enlace entre el sujeto y el atributo. Sin embargo, algunas 
    combinaciones pueden resultar anómalas si el adjetivo no admite una interpretación 
    agentiva o de habitualidad.
    Ejemplo:
    - Incorrecto: *Juan es alto habitualmente.
    - Correcto: Juan es atento habitualmente.
    """
    print(teoria)

def realizar_ejercicios():
    ejercicios = [
        {"pregunta": "¿Cuál de las siguientes es gramaticalmente correcta?\n1) Juan es alto habitualmente.\n2) Juan es amable habitualmente.", "respuesta": "2"},
        {"pregunta": "Completa: Juan __ siendo atento con su familia.", "respuesta": "está"},
        {"pregunta": "¿Cuál de estas frases tiene una interpretación agentiva?\n1) Juan es alto a propósito.\n2) Juan es amable a propósito.", "respuesta": "2"}
    ]
    random.shuffle(ejercicios)
    
    for ejercicio in ejercicios:
        print(ejercicio["pregunta"])
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == ejercicio["respuesta"]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
        print()

def escribir_ejercicios():
    print("Escribe una oración copulativa con 'ser' o 'estar' y adverbios de habitualidad o agentivos:")
    oracion = input("Tu oración: ")
    print(f"Has escrito: {oracion}. Revisa si cumple con las reglas explicadas.")

def menu():
    while True:
        print("\nMenú de Práctica")
        print("1. Leer teoría")
        print("2. Realizar ejercicios")
        print("3. Escribir oraciones")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            realizar_ejercicios()
        elif opcion == "3":
            escribir_ejercicios()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
