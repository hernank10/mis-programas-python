def crear_frases():
    palabras = ["gato", "sol", "risa", "amigo", "mariposa"]
    frases = []

    for i in range(3):
        palabra = input(f"Inventa una frase con la palabra '{palabras[i]}': ")
        frases.append(palabra)

    print("\n¡Frases creadas por el usuario!")
    for frase in frases:
        print(f"- {frase}")

crear_frases()
