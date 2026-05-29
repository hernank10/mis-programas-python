import json

def cargar_diccionario():
    with open('diccionario.json', 'r') as file:
        return json.load(file)

def guardar_diccionario(diccionario):
    with open('diccionario.json', 'w') as file:
        json.dump(diccionario, file, indent=4)

def agregar_palabra(diccionario):
    palabra = input("Introduce la nueva palabra: ")
    tipo = input("Introduce el tipo de palabra (verbo, adjetivo, etc.): ")
    diccionario[palabra] = tipo
    guardar_diccionario(diccionario)
    print(f"La palabra '{palabra}' ha sido añadida al diccionario.")

# Cargar el diccionario
diccionario = cargar_diccionario()

# Agregar una nueva palabra
agregar_palabra(diccionario)
