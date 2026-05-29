def identificar_palabras_agudas_con_tilde(texto):
    palabras_agudas_con_tilde = []
    palabras = texto.split()
    for palabra in palabras:
        if palabra[-1] not in "nsaeiouáéíóú" and palabra[-2:] not in ["ch", "sh"]:
            if palabra == palabra.lower():
                if palabra[-1] in "náéíóú":
                    palabras_agudas_con_tilde.append(palabra)
    if len(palabras_agudas_con_tilde) > 15:
        palabras_agudas_con_tilde = palabras_agudas_con_tilde[:15]
    return palabras_agudas_con_tilde

texto = input("Por favor, ingrese un fragmento de texto: ")
palabras_agudas_con_tilde = identificar_palabras_agudas_con_tilde(texto)
if len(palabras_agudas_con_tilde) == 0:
    print("No se encontraron palabras agudas con tilde en el texto.")
else:
    print("Las siguientes palabras agudas con tilde se encontraron en el texto:")
    for palabra in palabras_agudas_con_tilde:
        print("- " + palabra)
