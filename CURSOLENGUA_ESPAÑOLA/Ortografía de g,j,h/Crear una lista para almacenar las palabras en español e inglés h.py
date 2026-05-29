# Crear una lista para almacenar las palabras en español e inglés
palabras_ejemplo = [
    "huérfanos",
    "huida",
    "ahuecar",
    "huevo",
    # ... otras palabras ...
]

# Iterar sobre la lista y pedir al usuario que ingrese cada palabra
for palabra_espanol in palabras_ejemplo:
    palabra_ingles = input(f"Ingrese la versión en inglés de '{palabra_espanol}': ")
    print(f"Palabra en español: {palabra_espanol}")
    print(f"Palabra en inglés: {palabra_ingles}")
    print()  # Agregar una línea en blanco para separar las palabras

# Puedes personalizar este código según tus necesidades y agregar más palabras si lo deseas.
