import random
palabras_contexto = {"científico": "técnico", "pintoresco": "literario"}
def clasificar_palabras():
    palabra, categoria = random.choice(list(palabras_contexto.items()))
    print(f"¿En qué contexto se usa la palabra '{palabra}'?")
    respuesta = input("Responde: técnico, coloquial, literario: ").strip().lower()
    if respuesta == categoria:
        print("Correcto!")
    else:
        print(f"Incorrecto. La categoría correcta es '{categoria}'")

clasificar_palabras()
