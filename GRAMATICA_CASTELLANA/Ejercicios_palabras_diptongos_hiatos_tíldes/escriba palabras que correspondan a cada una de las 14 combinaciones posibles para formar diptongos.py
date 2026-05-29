def obtener_palabras():
    combinaciones_diptongos = [
        "ai", "ei", "oi", "ui", "au", "eu", "iu", "ay", "ey", "oy", "uy", "aí", "eí", "oí"
    ]

    palabras_diptongos = {}

    print("Piensa y escribe una palabra para cada combinación de diptongos:")

    for combinacion in combinaciones_diptongos:
        palabra = input(f"Palabra con diptongo {combinacion}: ").strip().lower()
        palabras_diptongos[combinacion] = palabra

    return palabras_diptongos


def mostrar_resultados(palabras_diptongos):
    print("\nPalabras con diptongos:")
    for combinacion, palabra in palabras_diptongos.items():
        print(f"{combinacion}: {palabra.capitalize()}")


def main():
    palabras_diptongos = obtener_palabras()
    mostrar_resultados(palabras_diptongos)


if __name__ == "__main__":
    main()
