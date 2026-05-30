import random

def practicar_oraciones_alfabeto(idioma):
    oraciones_por_idioma = {
        "Español": {
            "A": ["Ana ama la naturaleza.", "Ayer aprendí algo nuevo."],
            "B": ["Beto busca su pelota.", "Bailar mejora el estado de ánimo."],
            "C": ["Carlos come chocolate.", "Correr es saludable."],
            # Agrega más letras y oraciones aquí
        },
        "Inglés": {
            "A": ["Apples are sweet.", "Alex always arrives early."],
            "B": ["Bob builds big bridges.", "Books bring knowledge."],
            "C": ["Cats chase mice.", "Cooking is fun."],
            # Agrega más letras y oraciones aquí
        },
        "Francés": {
            "A": ["Alice adore les animaux.", "Apprends à aimer chaque jour."],
            "B": ["Bernard boit du café.", "Bouger est essentiel pour la santé."],
            "C": ["Claire chante une chanson.", "Chercher des solutions est important."],
            # Agrega más letras y oraciones aquí
        },
        # Agrega más idiomas aquí
    }

    if idioma not in oraciones_por_idioma:
        print(f"El idioma {idioma} no está disponible.")
        return

    oraciones = oraciones_por_idioma[idioma]
    letras = list(oraciones.keys())
    random.shuffle(letras)

    puntaje = 0
    print(f"Practicando oraciones en {idioma}. Completa la letra correspondiente con su oración.")
    for letra in letras:
        print(f"Letra: {letra}")
        opciones = oraciones[letra]
        respuesta_correcta = random.choice(opciones)

        respuesta_usuario = input(f"Escribe una oración que comience con la letra {letra}: ")
        if respuesta_usuario.strip() in opciones:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. Una oración correcta era: {respuesta_correcta}")

    print(f"¡Práctica terminada! Tu puntaje final es {puntaje}/{len(letras)}.")

def menu_principal():
    while True:
        print("Bienvenido al programa de práctica de oraciones por alfabeto.")
        print("Selecciona un idioma:")
        print("1. Español")
        print("2. Inglés")
        print("3. Francés")
        print("4. Salir")

        opcion = input("Escribe el número de tu opción: ")

        if opcion == "1":
            practicar_oraciones_alfabeto("Español")
        elif opcion == "2":
            practicar_oraciones_alfabeto("Inglés")
        elif opcion == "3":
            practicar_oraciones_alfabeto("Francés")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
