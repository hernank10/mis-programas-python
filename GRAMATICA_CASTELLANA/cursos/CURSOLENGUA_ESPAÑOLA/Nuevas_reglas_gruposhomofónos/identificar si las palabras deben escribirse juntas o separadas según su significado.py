def verificar_palabras(palabra1, palabra2):
    """
    Verifica si las dos palabras deben escribirse juntas o separadas según su significado.
    :param palabra1: Primera palabra
    :param palabra2: Segunda palabra
    """
    if palabra1.lower() == palabra2.lower():
        print(f"{palabra1} y {palabra2} se escriben juntas.")
    else:
        print(f"{palabra1} y {palabra2} se escriben separadas.")

# Ejemplos de palabras
verificar_palabras("acerca", "acerca")  # Deben escribirse juntas
verificar_palabras("a", "cerca")  # Deben escribirse separadas
verificar_palabras("abajo", "a bajo")  # Deben escribirse separadas
verificar_palabras("abordo", "a bordo")  # Deben escribirse juntas
# Agrega más ejemplos aquí

# Puedes llamar a la función con otras palabras para practicar
