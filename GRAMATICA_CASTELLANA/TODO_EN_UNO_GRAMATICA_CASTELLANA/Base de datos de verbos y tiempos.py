import random

# Base de datos de verbos y tiempos
tiempos_verbales = [
    {"verbo": "estudiar", "forma": "estudié", "tiempo": "pretérito perfecto simple", "modo": "indicativo"},
    {"verbo": "leer", "forma": "leeremos", "tiempo": "futuro simple", "modo": "indicativo"},
    {"verbo": "correr", "forma": "corría", "tiempo": "pretérito imperfecto", "modo": "indicativo"},
    {"verbo": "escribir", "forma": "escriba", "tiempo": "presente", "modo": "subjuntivo"},
    {"verbo": "hacer", "forma": "hagan", "tiempo": "presente", "modo": "subjuntivo"},
    {"verbo": "vivir", "forma": "viviría", "tiempo": "condicional simple", "modo": "indicativo"},
]

def practica_tiempos():
    print("\nPráctica: Identificar el tiempo verbal")
    verbo = random.choice(tiempos_verbales)
    print(f"Oración: Yo {verbo['forma']}")
    tiempo = input("¿Qué tiempo verbal es? (Ejemplo: pretérito perfecto simple): ")
    modo = input("¿Qué modo verbal es? (Ejemplo: indicativo): ")
    
    if tiempo.lower() == verbo['tiempo'] and modo.lower() == verbo['modo']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. Es '{verbo['tiempo']}' en modo '{verbo['modo']}'")
        return 0

def practica_completar_tiempos():
    print("\nPráctica: Completar el tiempo verbal")
    verbo = random.choice(tiempos_verbales)
    print(f"Oración: Yo ___________ (verbo: {verbo['verbo']}, tiempo: {verbo['tiempo']}, modo: {verbo['modo']})")
    forma = input("Escribe la forma correcta del verbo: ")
    
    if forma == verbo['forma']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. La forma correcta es '{verbo['forma']}'")
        return 0

def menu():
    puntuacion = 0
    while True:
        print("\n*** Práctica de Tiempos Verbales ***")
        print("1. Identificar tiempo y modo")
        print("2. Completar tiempos verbales")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            puntuacion += practica_tiempos()
        elif opcion == "2":
            puntuacion += practica_completar_tiempos()
        elif opcion == "3":
            print(f"Tu puntuación final es: {puntuacion}")
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
