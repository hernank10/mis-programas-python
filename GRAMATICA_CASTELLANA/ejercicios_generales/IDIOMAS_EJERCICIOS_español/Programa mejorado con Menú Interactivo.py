import random

def identificar_significado():
    palabras = {"correr": "Moverse rápidamente con pasos largos", "brillante": "Que refleja mucha luz"}
    palabra, significado = random.choice(list(palabras.items()))
    opciones = [significado, "Opción incorrecta 1", "Opción incorrecta 2"]
    random.shuffle(opciones)
    print(f"¿Cuál es el significado de '{palabra}'?")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    respuesta = int(input("Elige la opción correcta: "))
    print("Correcto!" if opciones[respuesta - 1] == significado else "Incorrecto")

def sinonimos_antonimos():
    sinonimos = {"feliz": "alegre", "rápido": "veloz"}
    antonimos = {"feliz": "triste", "rápido": "lento"}
    palabra = random.choice(list(sinonimos.keys()))
    print(f"Escribe un sinónimo o antónimo de '{palabra}':")
    respuesta = input().strip()
    if respuesta in (sinonimos[palabra], antonimos[palabra]):
        print("Correcto!")
    else:
        print(f"Incorrecto. Un sinónimo sería '{sinonimos[palabra]}' y un antónimo '{antonimos[palabra]}'")

def completar_oracion():
    oraciones = {"brillante": "El sol está muy ______ hoy."}
    palabra, oracion = random.choice(list(oraciones.items()))
    print(oracion)
    respuesta = input("Completa la oración: ").strip()
    if respuesta == palabra:
        print("Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es '{palabra}'")

def clasificar_palabras():
    palabras_contexto = {"científico": "técnico", "pintoresco": "literario"}
    palabra, categoria = random.choice(list(palabras_contexto.items()))
    print(f"¿En qué contexto se usa la palabra '{palabra}'?")
    respuesta = input("Responde: técnico, coloquial, literario: ").strip().lower()
    if respuesta == categoria:
        print("Correcto!")
    else:
        print(f"Incorrecto. La categoría correcta es '{categoria}'")

def definir_palabra():
    palabra = "correr"
    print(f"Escribe una definición para la palabra '{palabra}':")
    respuesta = input()
    print("Gracias por tu respuesta! Aquí está la definición correcta: Moverse rápidamente con pasos largos.")

def menu():
    while True:
        print("\nMenú de Práctica de Palabras")
        print("1. Identificación de Significados")
        print("2. Relación de Sinónimos y Antónimos")
        print("3. Uso en Oraciones")
        print("4. Clasificación de Palabras según su Contexto")
        print("5. Construcción de Definiciones")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            identificar_significado()
        elif opcion == "2":
            sinonimos_antonimos()
        elif opcion == "3":
            completar_oracion()
        elif opcion == "4":
            clasificar_palabras()
        elif opcion == "5":
            definir_palabra()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
