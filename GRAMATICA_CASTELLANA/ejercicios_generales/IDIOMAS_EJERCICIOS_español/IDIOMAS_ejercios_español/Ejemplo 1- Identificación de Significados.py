import random
palabras = {"correr": "Moverse rápidamente con pasos largos", "brillante": "Que refleja mucha luz"}
def identificar_significado():
    palabra, significado = random.choice(list(palabras.items()))
    opciones = [significado, "Opción incorrecta 1", "Opción incorrecta 2"]
    random.shuffle(opciones)
    print(f"¿Cuál es el significado de '{palabra}'?")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    respuesta = int(input("Elige la opción correcta: "))
    print("Correcto!" if opciones[respuesta - 1] == significado else "Incorrecto")

identificar_significado()
