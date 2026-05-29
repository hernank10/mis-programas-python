import json

# Lista de ejercicios
EJERCICIOS = [
    "Forme los femeninos de una serie de sustantivos.",
    "Separe sujeto y predicado.",
    "Escriba la familia de palabras del sustantivo 'flor'.",
    "Determine cuántos fonemas y cuántas letras tienen las palabras de la serie.",
    "Señale los complementos del sujeto.",
    "Señale la función de los siguientes grupos.",
    "Forme el plural de los siguientes grupos sustantivos.",
    "Extraiga los sustantivos abstractos.",
    "Enuncie la regla de los verbos terminados en '-bir'.",
    "Señale los núcleos de los grupos subrayados.",
    "Extraiga del texto los adjetivos relacionales.",
    "De la siguiente lista de adjetivos y verbos derive sustantivos abstractos."
]

RESPUESTAS_USUARIO = {}

# Guardar en archivo JSON
def guardar_respuestas():
    with open('respuestas_ejercicios.json', 'w', encoding='utf-8') as f:
        json.dump(RESPUESTAS_USUARIO, f, indent=4, ensure_ascii=False)

# Mostrar menú principal
def mostrar_menu():
    print("\n=== Ejercicios de lengua ===")
    for i, ejercicio in enumerate(EJERCICIOS):
        print(f"{i+1}. {ejercicio}")
    print("0. Guardar y salir")

# Ejecutar programa
while True:
    mostrar_menu()
    opcion = input("Seleccione un número de ejercicio: ")
    
    if opcion == "0":
        guardar_respuestas()
        print("Respuestas guardadas. ¡Hasta luego!")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= len(EJERCICIOS):
        idx = int(opcion) - 1
        print(f"\nEjercicio: {EJERCICIOS[idx]}")
        respuesta = input("Escriba su respuesta: ")
        RESPUESTAS_USUARIO[EJERCICIOS[idx]] = respuesta
        print("✔ Respuesta registrada.")
    else:
        print("Opción inválida. Intente nuevamente.")
