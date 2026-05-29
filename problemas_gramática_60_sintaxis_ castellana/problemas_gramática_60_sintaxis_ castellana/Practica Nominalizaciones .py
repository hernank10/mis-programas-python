import random

def mostrar_teoria():
    print("\nLas nominalizaciones con 'lo' permiten convertir adjetivos en sustantivos abstractos.\n"
          "Ejemplo:\n - Lo bueno de Juan (expresión neutra sobre una cualidad)\n"
          " - La bondad de Juan (sustantivo abstracto que denota la cualidad como entidad)")

def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario.strip().lower() == respuesta_correcta:
        print("\n¡Correcto!")
    else:
        print(f"\nIncorrecto. La respuesta correcta es: {respuesta_correcta}")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "Transforma en nominalización con 'lo': 'La generosidad de María'", "respuesta": "lo generoso de maria"},
        {"pregunta": "Transforma en nominalización con sustantivo: 'Lo bello del paisaje'", "respuesta": "la belleza del paisaje"},
        {"pregunta": "Completa: ____ honesto de Luis es admirable.", "respuesta": "lo"},
        {"pregunta": "¿Qué forma es correcta? 'Lo inteligente de Pedro' o 'La inteligencia de Pedro'?", "respuesta": "la inteligencia de pedro"}
    ]
    random.shuffle(ejercicios)
    
    for ejercicio in ejercicios:
        print(f"\n{ejercicio['pregunta']}")
        respuesta_usuario = input("Tu respuesta: ")
        verificar_respuesta(respuesta_usuario, ejercicio['respuesta'])

def menu():
    while True:
        print("\nMenú de Práctica")
        print("1. Leer teoría sobre nominalizaciones")
        print("2. Realizar ejercicios")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
