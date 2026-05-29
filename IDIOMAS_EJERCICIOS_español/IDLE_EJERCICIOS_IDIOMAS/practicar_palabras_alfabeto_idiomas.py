import random

def practicar_palabras_alfabeto(idioma):
    palabras_por_idioma = {
        "Español": {
            "A": ["Amor", "Amigo", "Aventura"],
            "B": ["Bueno", "Bailar", "Barco"],
            "C": ["Casa", "Cielo", "Cantar"],
            # Agrega más letras y palabras aquí
        },
        "Inglés": {
            "A": ["Apple", "Ant", "Adventure"],
            "B": ["Book", "Ball", "Bridge"],
            "C": ["Cat", "Cloud", "Climb"],
            # Agrega más letras y palabras aquí
        },
        "Francés": {
            "A": ["Amour", "Ami", "Arbre"],
            "B": ["Beau", "Bateau", "Bon"],
            "C": ["Chien", "Ciel", "Chanter"],
            # Agrega más letras y palabras aquí
        },
        # Agrega más idiomas aquí
    }

    if idioma not in palabras_por_idioma:
        print(f"El idioma {idioma} no está disponible.")
        return

    palabras = palabras_por_idioma[idioma]
    letras = list(palabras.keys())
    random.shuffle(letras)

    puntaje = 0
    print(f"Practicando palabras en {idioma}. Escribe la palabra correcta según la letra mostrada.")
    for letra in letras:
        print(f"Letra: {letra}")
        opciones = palabras[letra]
        respuesta_correcta = random.choice(opciones)
        opciones_barajadas = opciones[:]
        random.shuffle(opciones_barajadas)

        print("Opciones:")
        for i, opcion in enumerate(opciones_barajadas):
            print(f"{i + 1}. {opcion}")

        respuesta_usuario = input("Escribe el número de tu respuesta: ")
        if opciones_barajadas[int(respuesta_usuario) - 1] == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")

    print(f"¡Práctica terminada! Tu puntaje final es {puntaje}/{len(letras)}.")

def menu_principal():
    while True:
        print("Bienvenido al programa de práctica de palabras por alfabeto.")
        print("Selecciona un idioma:")
        print("1. Español")
        print("2. Inglés")
        print("3. Francés")
        print("4. Salir")

        opcion = input("Escribe el número de tu opción: ")

        if opcion == "1":
            practicar_palabras_alfabeto("Español")
        elif opcion == "2":
            practicar_palabras_alfabeto("Inglés")
        elif opcion == "3":
            practicar_palabras_alfabeto("Francés")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
