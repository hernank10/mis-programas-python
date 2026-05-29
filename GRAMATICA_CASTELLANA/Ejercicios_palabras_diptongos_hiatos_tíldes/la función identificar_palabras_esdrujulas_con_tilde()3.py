def identificar_palabras_esdrujulas_con_tilde(texto):
    palabras_esdrujulas_con_tilde = []
    palabras = texto.split()
    for palabra in palabras:
        if palabra[-1] not in "nsaeiouáéíóú" and palabra[-2:] not in ["ch", "sh"]:
            if palabra == palabra.lower():
                if palabra[-1] in "áéíóú":
                    if palabra not in palabras_esdrujulas_con_tilde:
                        palabras_esdrujulas_con_tilde.append(palabra)
    if len(palabras_esdrujulas_con_tilde) > 15:
        palabras_esdrujulas_con_tilde = palabras_esdrujulas_con_tilde[:15]
    return palabras_esdrujulas_con_tilde

texto = input("Por favor, ingrese un fragmento de texto: ")
palabras_esdrujulas_con_tilde = identificar_palabras_esdrujulas_con_tilde(texto)
if len(palabras_esdrujulas_con_tilde) == 0:
    print("No se encontraron palabras esdrújulas con tilde en el texto.")
else:
    print("Las siguientes palabras esdrújulas con tilde se encontraron en el texto:")
    for palabra in palabras_esdrujulas_con_tilde:
        print("- " + palabra)
