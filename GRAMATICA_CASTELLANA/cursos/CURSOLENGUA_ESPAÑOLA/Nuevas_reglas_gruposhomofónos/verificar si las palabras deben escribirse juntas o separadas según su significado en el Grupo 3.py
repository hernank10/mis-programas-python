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
verificar_palabras("quehacer", "que hacer")  # Deben escribirse separadas
verificar_palabras("quienquiera", "quien quiera")  # Deben escribirse separadas
verificar_palabras("sinfín", "sin fin")  # Deben escribirse separadas
verificar_palabras("sinnúmero", "sin número")  # Deben escribirse separadas
# Agrega más ejemplos aquí

# Puedes llamar a la función con otras palabras para practicar
