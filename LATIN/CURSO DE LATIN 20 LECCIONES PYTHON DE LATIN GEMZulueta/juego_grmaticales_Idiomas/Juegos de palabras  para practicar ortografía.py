import random

# Variables para almacenar el progreso del usuario
progreso = {
    "Ahorcado ortográfico": 0,
    "Sopa de letras": 0,
    "Dominó ortográfico": 0,
    "Bingo de palabras": 0,
    "Cadena de palabras correctas": 0
}

# Función para el juego de Ahorcado Ortográfico
def ahorcado_ortografico():
    palabras = ["caballo", "vaca", "zapato", "bicicleta", "jirafa"]
    palabra = random.choice(palabras)
    adivinanza = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    print("\n¡Bienvenido al Ahorcado Ortográfico!")
    print(" ".join(adivinanza))

    while intentos > 0 and "_" in adivinanza:
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    adivinanza[i] = letra
            print("¡Correcto!")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")

        print(" ".join(adivinanza))

    if "_" not in adivinanza:
        print("¡Felicidades! Has adivinado la palabra.")
        progreso["Ahorcado ortográfico"] += 1
    else:
        print(f"¡Oh no! La palabra era '{palabra}'. Mejor suerte la próxima vez.")

# Función para el juego de Sopa de Letras
def sopa_de_letras():
    print("\n¡Bienvenido a la Sopa de Letras!")
    print("Encuentra las palabras mal escritas y corrígelas.")
    # Aquí podrías implementar una sopa de letras interactiva
    print("(Este juego está en desarrollo).")
    progreso["Sopa de letras"] += 1

# Función para el juego de Dominó Ortográfico
def domino_ortografico():
    print("\n¡Bienvenido al Dominó Ortográfico!")
    print("Conecta las fichas según las reglas ortográficas.")
    # Aquí podrías implementar un dominó interactivo
    print("(Este juego está en desarrollo).")
    progreso["Dominó ortográfico"] += 1

# Función para el juego de Bingo de Palabras
def bingo_de_palabras():
    print("\n¡Bienvenido al Bingo de Palabras!")
    print("Marca las palabras correctas en tu tarjeta.")
    # Aquí podrías implementar un bingo interactivo
    print("(Este juego está en desarrollo).")
    progreso["Bingo de palabras"] += 1

# Función para el juego de Cadena de Palabras Correctas
def cadena_de_palabras_correctas():
    print("\n¡Bienvenido a la Cadena de Palabras Correctas!")
    print("Sigue la cadena de palabras sin cometer errores ortográficos.")
    # Aquí podrías implementar una cadena de palabras interactiva
    print("(Este juego está en desarrollo).")
    progreso["Cadena de palabras correctas"] += 1

# Función para mostrar el progreso del usuario
def mostrar_progreso():
    print("\n--- Tu Progreso ---")
    for juego, puntaje in progreso.items():
        print(f"{juego}: {puntaje} puntos")
    input("\nPresiona Enter para volver al menú principal.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar Ahorcado Ortográfico")
        print("2. Jugar Sopa de Letras")
        print("3. Jugar Dominó Ortográfico")
        print("4. Jugar Bingo de Palabras")
        print("5. Jugar Cadena de Palabras Correctas")
        print("6. Ver Progreso")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ahorcado_ortografico()
        elif opcion == "2":
            sopa_de_letras()
        elif opcion == "3":
            domino_ortografico()
        elif opcion == "4":
            bingo_de_palabras()
        elif opcion == "5":
            cadena_de_palabras_correctas()
        elif opcion == "6":
            mostrar_progreso()
        elif opcion == "7":
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    menu()
