import random

# Base de datos de verbos compuestos
verbos_compuestos = [
    {"auxiliar": "he", "principal": "estudiado", "modo": "indicativo", "tiempo": "pretérito perfecto"},
    {"auxiliar": "había", "principal": "leído", "modo": "indicativo", "tiempo": "pretérito pluscuamperfecto"},
    {"auxiliar": "estaré", "principal": "trabajando", "modo": "indicativo", "tiempo": "futuro compuesto"},
    {"auxiliar": "habría", "principal": "dormido", "modo": "condicional", "tiempo": "condicional perfecto"},
    {"auxiliar": "haya", "principal": "escrito", "modo": "subjuntivo", "tiempo": "pretérito perfecto"},
]

def mostrar_ejemplos():
    print("\nEjemplos de verbos compuestos:")
    for verbo in verbos_compuestos:
        print(f"{verbo['auxiliar']} {verbo['principal']} ({verbo['modo']} - {verbo['tiempo']})")

def practica_identificacion():
    print("\nPráctica: Identificar el auxiliar y el verbo principal")
    verbo = random.choice(verbos_compuestos)
    print(f"Frase: {verbo['auxiliar']} {verbo['principal']}")
    auxiliar = input("Escribe el verbo auxiliar: ")
    principal = input("Escribe el verbo principal: ")
    if auxiliar == verbo['auxiliar'] and principal == verbo['principal']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. El auxiliar es '{verbo['auxiliar']}' y el principal es '{verbo['principal']}'")
        return 0

def practica_escritura():
    print("\nPráctica: Completar un verbo compuesto")
    verbo = random.choice(verbos_compuestos)
    print(f"Completa el verbo compuesto: {verbo['auxiliar']} _______")
    principal = input("Escribe el verbo principal: ")
    if principal == verbo['principal']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. La respuesta correcta es '{verbo['principal']}'")
        return 0

def menu():
    puntuacion = 0
    while True:
        print("\n*** Práctica de Verbos Compuestos ***")
        print("1. Ver ejemplos")
        print("2. Practicar identificando auxiliares y principales")
        print("3. Practicar completando verbos compuestos")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_ejemplos()
        elif opcion == "2":
            puntuacion += practica_identificacion()
        elif opcion == "3":
            puntuacion += practica_escritura()
        elif opcion == "4":
            print(f"Tu puntuación final es: {puntuacion}")
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
