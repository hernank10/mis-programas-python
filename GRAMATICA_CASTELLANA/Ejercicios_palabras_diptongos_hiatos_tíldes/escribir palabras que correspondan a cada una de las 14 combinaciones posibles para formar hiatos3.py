def tiene_hiatos(palabra):
    vocales_abiertas = "aeoáéó"
    vocales_cerradas = "iuíú"

    palabra = palabra.lower()  # Convertir a minúsculas para la verificación

    for i in range(len(palabra) - 1):
        if palabra[i] in vocales_abiertas and palabra[i + 1] in vocales_cerradas:
            return True
    return False


def main():
    combinaciones_hiatos = [
        "ai", "au", "ei", "eu", "oi", "ou", "ia",
        "ua", "ie", "ue", "io", "uo", "ui", "iu"
    ]

    palabras_por_combinacion = {}

    for comb in combinaciones_hiatos:
        palabra = input(f"Ingresa una palabra con la combinación '{comb}': ")
        if tiene_hiatos(palabra):
            palabras_por_combinacion[comb] = palabra

    print("\nPalabras ingresadas:")
    for comb, palabra in palabras_por_combinacion.items():
        print(f"{comb}: {palabra}")


if __name__ == "__main__":
    main()
