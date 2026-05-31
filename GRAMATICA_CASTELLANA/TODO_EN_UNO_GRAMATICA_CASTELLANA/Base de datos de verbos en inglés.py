import random

# Base de datos de verbos en inglés
verbos_ingles = [
    {"base": "study", "past": "studied", "participle": "studied"},
    {"base": "run", "past": "ran", "participle": "run"},
    {"base": "write", "past": "wrote", "participle": "written"},
    {"base": "eat", "past": "ate", "participle": "eaten"},
    {"base": "be", "past": "was/were", "participle": "been"},
]

def practica_verbos_ingles():
    print("\nPráctica: Identificar las formas de un verbo en inglés")
    verbo = random.choice(verbos_ingles)
    print(f"Verbo base: {verbo['base']}")
    past = input("Escribe el pasado simple: ")
    participle = input("Escribe el participio pasado: ")
    
    if past.lower() == verbo['past'] and participle.lower() == verbo['participle']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. El pasado es '{verbo['past']}' y el participio es '{verbo['participle']}'")
        return 0

def practica_completar_ingles():
    print("\nPráctica: Completar tiempos verbales en inglés")
    verbo = random.choice(verbos_ingles)
    tiempo = random.choice(["past", "participle"])
    if tiempo == "past":
        print(f"Completa: She _______ (verbo: {verbo['base']}, pasado simple)")
        respuesta = input("Escribe la forma correcta: ")
        if respuesta.lower() == verbo['past']:
            print("¡Correcto!")
            return 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{verbo['past']}'")
            return 0
    else:
        print(f"Completa: They have _______ (verbo: {verbo['base']}, participio pasado)")
        respuesta = input("Escribe la forma correcta: ")
        if respuesta.lower() == verbo['participle']:
            print("¡Correcto!")
            return 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{verbo['participle']}'")
            return 0

def menu():
    puntuacion = 0
    while True:
        print("\n*** Menú de Práctica de Verbos ***")
        print("1. Practicar tiempos verbales en español")
        print("2. Completar tiempos verbales en español")
        print("3. Practicar tiempos verbales en inglés")
        print("4. Completar tiempos verbales en inglés")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            puntuacion += practica_tiempos()
        elif opcion == "2":
            puntuacion += practica_completar_tiempos()
        elif opcion == "3":
            puntuacion += practica_verbos_ingles()
        elif opcion == "4":
            puntuacion += practica_completar_ingles()
        elif opcion == "5":
            print(f"Tu puntuación final es: {puntuacion}")
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
