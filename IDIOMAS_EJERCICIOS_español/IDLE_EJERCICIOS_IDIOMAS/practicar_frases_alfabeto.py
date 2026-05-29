import random

def practicar_frases_alfabeto(idioma):
    frases_por_idioma = {
        "Español": {
            "A": ["Amar es vivir.", "Ayer fue un gran día."],
            "B": ["Bailar alegra el corazón.", "Busca siempre la verdad."],
            "C": ["Cantar es divertido.", "Corre tras tus sueños."],
            # Agrega más letras y frases aquí
        },
        "Inglés": {
            "A": ["Always be kind.", "Apples are delicious."],
            "B": ["Be yourself.", "Books open minds."],
            "C": ["Create your own path.", "Cats are adorable."],
            # Agrega más letras y frases aquí
        },
        "Francés": {
            "A": ["Amour et paix.", "Apprends quelque chose de nouveau."],
            "B": ["Beaucoup de bonheur.", "Bouge avec joie."],
            "C": ["Chante avec ton âme.", "Cherche la vérité."],
            # Agrega más letras y frases aquí
        },
        # Agrega más idiomas aquí
    }

    if idioma not in frases_por_idioma:
        print(f"El idioma {idioma} no está disponible.")
        return

    frases = frases_por_idioma[idioma]
    letras = list(frases.keys())
    random.shuffle(letras)

    puntaje = 0
    print(f"Practicando frases en {idioma}. Escribe la frase correcta según la letra mostrada.")
    for letra in letras:
        print(f"Letra: {letra}")
        opciones = frases[letra]
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
        print("Bienvenido al programa de práctica de frases por alfabeto.")
        print("Selecciona un idioma:")
        print("1. Español")
        print("2. Inglés")
        print("3. Francés")
        print("4. Salir")

        opcion = input("Escribe el número de tu opción: ")

        if opcion == "1":
            practicar_frases_alfabeto("Español")
        elif opcion == "2":
            practicar_frases_alfabeto("Inglés")
        elif opcion == "3":
            practicar_frases_alfabeto("Francés")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
