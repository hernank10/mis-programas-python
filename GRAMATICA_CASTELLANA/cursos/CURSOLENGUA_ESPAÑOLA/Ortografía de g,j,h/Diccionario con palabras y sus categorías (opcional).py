import random

# Diccionario con palabras y sus categorías (opcional)
palabras = {
    "diptongos": ["huaca", "huele", "huir"],
    "verbos": ["haber", "hacer", "hablar"],
    "prefijos": ["hecto-", "helio-", "hetero-"],
    # Agrega más categorías y palabras según sea necesario
}

def repasar_palabras(categoria=None):
    """Repasa palabras de una categoría específica o de todas.

    Args:
        categoria (str, optional): Nombre de la categoría a repasar.
            Si es None, se repasan todas las palabras.
    """

    if categoria:
        palabras_a_repasar = palabras[categoria]
    else:
        palabras_a_repasar = [palabra for categoria in palabras.values() for palabra in categoria]

    random.shuffle(palabras_a_repasar)

    for palabra in palabras_a_repasar:
        respuesta = input(f"¿Cómo se escribe? {palabra}: ")
        while respuesta.lower() != palabra:
            print("¡Incorrecto! Intenta de nuevo.")
            respuesta = input(f"¿Cómo se escribe? {palabra}: ")
        print("¡Correcto!")

# Ejemplo de uso:
repasar_palabras("diptongos")  # Repasa solo palabras con diptongos
# repasar_palabras()  # Repasa todas las palabras

