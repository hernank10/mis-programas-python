import random

def practicar_oraciones_compuestas(idioma):
    oraciones_por_idioma = {
        "Español": {
            "A": ["Aunque hace frío, el sol brilla en el cielo.", "A veces estudio en la mañana, pero prefiero hacerlo por la tarde."],
            "B": ["Bebí café porque tenía sueño.", "Busqué mis llaves y no las encontré."],
            "C": ["Cuando llegué a casa, ya había oscurecido.", "Comí pizza, pero después me arrepentí."],
            # Agrega más letras y oraciones aquí
        },
        "Inglés": {
            "A": ["Although it was raining, we decided to go hiking.", "Anna stayed home, but her brother went to the park."],
            "B": ["Because I was tired, I went to bed early.", "Bob studied hard, yet he didn’t pass the test."],
            "C": ["When I called her, she didn’t answer the phone.", "Cooking is fun, and it’s also a useful skill."],
            # Agrega más letras y oraciones aquí
        },
        "Francés": {
            "A": ["Alors qu'il pleuvait, nous sommes sortis pour une promenade.", "Apprends bien tes leçons, sinon tu risques d'échouer."],
            "B": ["Bien que fatigué, il a continué à travailler.", "Bernard voulait partir, mais il a changé d'avis."],
            "C": ["Comme je n'avais pas de parapluie, je suis resté à la maison.", "Claire chante une chanson et joue de la guitare."],
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
    print(f"Practicando oraciones compuestas en {idioma}. Completa la letra correspondiente con su oración.")
    for letra in letras:
        print(f"Letra: {letra}")
        opciones = oraciones[letra]
        respuesta_correcta = random.choice(opciones)

        respuesta_usuario = input(f"Escribe una oración compuesta que comience con la letra {letra}: ")
        if respuesta_usuario.strip() in opciones:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. Una oración correcta era: {respuesta_correcta}")

    print(f"¡Práctica terminada! Tu puntaje final es {puntaje}/{len(letras)}.")

def mostrar_ejemplo(idioma):
    oraciones_por_idioma = {
        "Español": {
            "A": ["Aunque hace frío, el sol brilla en el cielo."],
            "B": ["Bebí café porque tenía sueño."],
            "C": ["Cuando llegué a casa, ya había oscurecido."],
        },
        "Inglés": {
            "A": ["Although it was raining, we decided to go hiking."],
            "B": ["Because I was tired, I went to bed early."],
            "C": ["When I called her, she didn’t answer the phone."],
        },
        "Francés": {
            "A": ["Alors qu'il pleuvait, nous sommes sortis pour une promenade."],
            "B": ["Bien que fatigué, il a continué à travailler."],
            "C": ["Comme je n'avais pas de parapluie, je suis resté à la maison."],
        },
    }

    if idioma not in oraciones_por_idioma:
        print(f"El idioma {idioma} no está disponible.")
        return

    ejemplos = oraciones_por_idioma[idioma]
    print(f"Ejemplos de oraciones compuestas en {idioma}:\n")
    for letra, oracion in ejemplos.items():
        print(f"{letra}: {oracion[0]}")

def menu_principal():
    while True:
        print("Bienvenido al programa de práctica de oraciones compuestas por alfabeto.")
        print("Selecciona una opción:")
        print("1. Practicar Español")
        print("2. Practicar Inglés")
        print("3. Practicar Francés")
        print("4. Ver ejemplos en Español")
        print("5. Ver ejemplos en Inglés")
        print("6. Ver ejemplos en Francés")
        print("7. Salir")

        opcion = input("Escribe el número de tu opción: ")

        if opcion == "1":
            practicar_oraciones_compuestas("Español")
        elif opcion == "2":
            practicar_oraciones_compuestas("Inglés")
        elif opcion == "3":
            practicar_oraciones_compuestas("Francés")
        elif opcion == "4":
            mostrar_ejemplo("Español")
        elif opcion == "5":
            mostrar_ejemplo("Inglés")
        elif opcion == "6":
            mostrar_ejemplo("Francés")
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
