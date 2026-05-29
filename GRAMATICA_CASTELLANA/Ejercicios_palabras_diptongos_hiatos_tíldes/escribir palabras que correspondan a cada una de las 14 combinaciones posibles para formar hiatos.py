def obtener_palabras_hiatos():
    combinaciones_hiatos = [
        "a-a", "a-e", "a-o",
        "e-a", "e-e", "e-o",
        "i-a", "i-e", "i-o",
        "o-a", "o-e", "o-o",
        "u-a", "u-e"
    ]

    palabras_hiatos = {}

    print("Piensa y escribe una palabra para cada combinación de hiatos:")

    for combinacion in combinaciones_hiatos:
        palabra = input(f"Palabra con hiatos {combinacion}: ").strip().lower()
        palabras_hiatos[combinacion] = palabra

    return palabras_hiatos

def mostrar_resultados_hiatos(palabras_hiatos):
    print("\nPalabras con hiatos:")
    for combinacion, palabra in palabras_hiatos.items():
        print(f"{combinacion}: {palabra.capitalize()}")

def main_hiatos():
    palabras_hiatos = obtener_palabras_hiatos()
    mostrar_resultados_hiatos(palabras_hiatos)

if __name__ == "__main__":
    main_hiatos()
