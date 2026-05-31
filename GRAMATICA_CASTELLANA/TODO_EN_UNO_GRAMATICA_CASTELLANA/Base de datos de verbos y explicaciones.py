import random
import json

# Base de datos de verbos y explicaciones
verbos_espanol = [
    {"verbo": "estudiar", "forma": "estudié", "tiempo": "pretérito perfecto simple", "modo": "indicativo"},
    {"verbo": "leer", "forma": "leeremos", "tiempo": "futuro simple", "modo": "indicativo"},
    {"verbo": "correr", "forma": "corría", "tiempo": "pretérito imperfecto", "modo": "indicativo"},
]

verbos_ingles = [
    {"base": "study", "past": "studied", "participle": "studied"},
    {"base": "run", "past": "ran", "participle": "run"},
    {"base": "write", "past": "wrote", "participle": "written"},
]

teoria = {
    "espanol": "En español, los tiempos verbales se dividen en presente, pasado y futuro, con modos indicativo, subjuntivo e imperativo. Ejemplo: Yo estudio (presente indicativo).",
    "ingles": "En inglés, los tiempos básicos son: presente simple (I study), pasado simple (I studied) y presente perfecto (I have studied)."
}

# Cargar y guardar progreso
def cargar_progreso(usuario):
    try:
        with open("progreso.json", "r") as archivo:
            progreso = json.load(archivo)
        return progreso.get(usuario, {"puntuacion": 0, "nivel": "básico"})
    except FileNotFoundError:
        return {"puntuacion": 0, "nivel": "básico"}

def guardar_progreso(usuario, progreso):
    try:
        with open("progreso.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}
    datos[usuario] = progreso
    with open("progreso.json", "w") as archivo:
        json.dump(datos, archivo)

# Funciones de práctica
def practica_tiempos_espanol():
    verbo = random.choice(verbos_espanol)
    print(f"Oración: Yo {verbo['forma']}")
    tiempo = input("¿Qué tiempo verbal es? ")
    modo = input("¿Qué modo verbal es? ")
    if tiempo.lower() == verbo['tiempo'] and modo.lower() == verbo['modo']:
        print("¡Correcto!")
        return 1
    else:
        print(f"Incorrecto. Es '{verbo['tiempo']}' en modo '{verbo['modo']}'")
        return 0

def practica_tiempos_ingles():
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

def cuestionario_interactivo():
    preguntas = [
        {"pregunta": "¿Cuál es el participio del verbo 'write' en inglés?", "respuesta": "written"},
        {"pregunta": "¿Cómo se conjuga 'leer' en pretérito perfecto simple en español?", "respuesta": "leí"},
    ]
    aciertos = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == pregunta["respuesta"]:
            print("¡Correcto!")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{pregunta['respuesta']}'")
    return aciertos

# Menú principal
def menu():
    usuario = input("Ingresa tu nombre: ")
    progreso = cargar_progreso(usuario)
    puntuacion = progreso["puntuacion"]
    nivel = progreso["nivel"]

    while True:
        print("\n*** Menú de Práctica de Verbos ***")
        print("1. Leer teoría de tiempos verbales")
        print("2. Practicar tiempos verbales en español")
        print("3. Practicar tiempos verbales en inglés")
        print("4. Cuestionario interactivo")
        print("5. Guardar y salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nTeoría:")
            print(teoria["espanol"])
            print(teoria["ingles"])
        elif opcion == "2":
            puntuacion += practica_tiempos_espanol()
        elif opcion == "3":
            puntuacion += practica_tiempos_ingles()
        elif opcion == "4":
            puntuacion += cuestionario_interactivo()
        elif opcion == "5":
            guardar_progreso(usuario, {"puntuacion": puntuacion, "nivel": nivel})
            print(f"Puntuación final: {puntuacion}. ¡Progreso guardado!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
