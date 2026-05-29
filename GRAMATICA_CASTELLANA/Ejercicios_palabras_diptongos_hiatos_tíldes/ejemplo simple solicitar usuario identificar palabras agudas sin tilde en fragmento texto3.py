def identificar_palabras_sin_tilde(texto):
    palabras_sin_tilde = []
    palabras = texto.split()
    for palabra in palabras:
        if palabra[-1] not in "nsaeiouáéíóú" and palabra[-2:] not in ["ch", "sh"]:
            if palabra == palabra.lower():
                palabras_sin_tilde.append(palabra)
    if len(palabras_sin_tilde) > 5:
        palabras_sin_tilde = palabras_sin_tilde[:5]
    return palabras_sin_tilde

texto = input("Por favor, ingrese un fragmento de texto: ")
palabras_sin_tilde = identificar_palabras_sin_tilde(texto)
if len(palabras_sin_tilde) == 0:
    print("No se encontraron palabras agudas sin tilde en el texto.")
else:
    print("Las siguientes palabras agudas sin tilde se encontraron en el texto:")
    for palabra in palabras_sin_tilde:
        print("- " + palabra)
