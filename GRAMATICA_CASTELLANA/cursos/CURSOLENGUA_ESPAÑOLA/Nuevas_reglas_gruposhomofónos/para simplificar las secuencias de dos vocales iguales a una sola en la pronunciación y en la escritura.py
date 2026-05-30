def reduccion_vocales(palabra):
    """
    Verifica si una palabra cumple con la regla de reducción de vocales iguales contiguas.
    Devuelve la forma simplificada de la palabra.
    """
    # Buscamos la secuencia "-aa-" en la palabra
    if "aa" in palabra:
        # Simplificamos la secuencia a una sola vocal
        palabra_simplificada = palabra.replace("aa", "a")
        return palabra_simplificada
    else:
        return palabra  # La palabra no contiene "-aa-", no es necesario simplificarla

# Lista de palabras
palabras = ["El Aaiún", "Isaac", "Aarón", "Caaguazú", "Caacupé", "Caazapá", "afrikaans"]

# Aplicamos la regla a cada palabra
for palabra in palabras:
    palabra_simplificada = reduccion_vocales(palabra)
    print(f"{palabra} -> {palabra_simplificada}")
