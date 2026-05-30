import random
import time

# Base de datos de fonemas en castellano
fonemas = {
    "vocales": {
        "a": "Vocal abierta y central",
        "e": "Vocal semiabierta y anterior",
        "i": "Vocal cerrada y anterior",
        "o": "Vocal semiabierta y posterior",
        "u": "Vocal cerrada y posterior",
    },
    "consonantes": {
        "p": "Consonante bilabial oclusiva sorda",
        "b": "Consonante bilabial oclusiva sonora",
        "m": "Consonante bilabial nasal sonora",
        "t": "Consonante dental oclusiva sorda",
        "d": "Consonante dental oclusiva sonora",
        "s": "Consonante alveolar fricativa sorda",
        "l": "Consonante alveolar lateral sonora",
        "r": "Consonante alveolar vibrante sonora",
        "ɾ": "Consonante alveolar vibrante simple sonora",
        "x": "Consonante velar fricativa sorda",
        "k": "Consonante velar oclusiva sorda",
    }
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Sistema Fonético Castellano ---")
    print("1. Escuchar Fonemas (simulado)")
    print("2. Ver explicación de Fonemas")
    print("3. Practicar identificación de Fonemas")
    print("4. Salir")

# Opción 1: Simular sonidos
def escuchar_fonemas():
    print("\n--- Simulación de sonidos fonéticos ---")
    for tipo, sonidos in fonemas.items():
        print(f"\n{tipo.capitalize()}:")
        for fonema in sonidos.keys():
            print(f"[{fonema}] --> Imagina el sonido aquí")

# Opción 2: Mostrar explicación de los fonemas
def mostrar_explicacion():
    print("\n--- Explicación de los Fonemas ---")
    for tipo, sonidos in fonemas.items():
        print(f"\n{tipo.capitalize()}:")
        for fonema, descripcion in sonidos.items():
            print(f"[{fonema}]: {descripcion}")

# Opción 3: Practicar
def practicar():
    print("\n--- Práctica Interactiva ---")
    correctas = 0
    incorrectas = 0
    preguntas = list(fonemas["vocales"].items()) + list(fonemas["consonantes"].items())
    random.shuffle(preguntas)

    for fonema, descripcion in preguntas[:10]:
        print(f"\n¿Qué tipo de fonema es el siguiente?: {descripcion}")
        respuesta = input("Escribe 'vocal' o 'consonante': ").strip().lower()
        if (respuesta == "vocal" and fonema in fonemas["vocales"]) or (
            respuesta == "consonante" and fonema in fonemas["consonantes"]
        ):
            print("¡Correcto! 😊")
            correctas += 1
        else:
            print(f"Incorrecto. El fonema '{fonema}' es {'vocal' if fonema in fonemas['vocales'] else 'consonante'}.")
            incorrectas += 1

    # Mostrar resultados
    print("\n--- Resultados de la práctica ---")
    print(f"Respuestas correctas: {correctas}")
    print(f"Respuestas incorrectas: {incorrectas}")

# Programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == "1":
            escuchar_fonemas()
        elif opcion == "2":
            mostrar_explicacion()
        elif opcion == "3":
            practicar()
        elif opcion == "4":
            print("¡Hasta luego! 😊")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar programa
if __name__ == "__main__":
    main()
