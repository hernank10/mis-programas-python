import random

# Lista de sustantivos de la primera declinación (tema en -a)
sustantivos = ["puella" , "rosa", "terra", "casa", "silva", "insula", "aqua", "via", "cura", "fama"]

# Reglas de la primera declinación
terminaciones = {
    "singular": {
        "nominativo": "a",
        "genitivo": "ae",
        "dativo": "ae",
        "acusativo": "am",
        "ablativo": "a",
        "vocativo": "a"
    },
    "plural": {
        "nominativo": "ae",
        "genitivo": "arum",
        "dativo": "is",
        "acusativo": "as",
        "ablativo": "is",
        "vocativo": "ae"
    }
}

casos = ["nominativo", "genitivo", "dativo", "acusativo", "ablativo", "vocativo"]
numeros = ["singular", "plural"]


def declinar(palabra, numero, caso):
    tema = palabra[:-1]  # quitamos la -a final del nominativo singular
    return tema + terminaciones[numero][caso]


def juego_declinar():
    print("=== ENTRENADOR DE PRIMERA DECLINACIÓN LATINA ===")
    print("Tienes 30 ejercicios para practicar. Escribe la forma correcta.\n")
    puntos = 0

    for i in range(1, 31):
        palabra = random.choice(sustantivos)
        numero = random.choice(numeros)
        caso = random.choice(casos)

        print(f"Ejercicio {i}: Declina '{palabra}' en {caso} {numero}.")
        respuesta = input("> ").strip().lower()

        correcta = declinar(palabra, numero, caso)

        if respuesta == correcta:
            print("✅ Correcto!")
            puntos += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {correcta}")
        print("-")

    print(f"Juego terminado. Tu puntuación: {puntos}/30")


if __name__ == "__main__":
    juego_declinar()
