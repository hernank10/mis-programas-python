def simplificar_ps(palabra):
    """
    Simplifica palabras con el grupo consonántico "ps" según las reglas mencionadas.
    """
    # Palabras que comienzan con "pseudo" se mantienen igual
    if palabra.startswith("pseudo"):
        return palabra
    # Reemplaza "ps" por "s"
    return palabra.replace("ps", "s")

# Ejemplos de palabras con "ps"
palabras_ejemplo = [
    "psicoanálisis",
    "psicología",
    "psicólogo",
]

for palabra in palabras_ejemplo:
    print(f"{palabra} -> {simplificar_ps(palabra)}")
