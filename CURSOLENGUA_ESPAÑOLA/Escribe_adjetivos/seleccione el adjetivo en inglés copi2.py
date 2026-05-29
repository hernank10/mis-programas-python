print("¡Has completado todas las oraciones! ¡Bien hecho!")
def identificar_adjetivo(oracion):
    """
    Identifica el adjetivo en una oración dada.

    Args:
        oracion (str): La oración de entrada.

    Returns:
        str: El adjetivo identificado.
    """
    palabras = oracion.split()
    for palabra in palabras:
        if palabra.lower() in adjetivos:
            return palabra.lower()
    return None

# Lista de adjetivos en inglés
adjetivos = [
    "young", "dirty", "pocket", "ourselves", "beautiful",
    "American", "nice", "young", "alone", "ice-cold",
    "colorful", "gorgeous", "beautiful", "large", "round",
    "different", "gorgeous", "evening", "wild", "interesting",
    "absolutely", "complete", "total", "freezing", "happy",
    "strong", "calm", "dark", "kind", "tired",
    "amazing", "large", "beautiful", "colorful", "gorgeous"
    # ... Agrega más adjetivos aquí ...
]

# Lista de oraciones de ejemplo
oraciones = [
    "We were served by an unfriendly young waiter.",
    "It was a small, dark dirty room.",
    "He used a small, sharp pocket knife.",
    "We found ourselves in a huge, glas conference room",
    "He broke a beautiful, white, Japanese porcelain plate",
    "Susan was going out with a tall, dark handsome American",
    "They had a nice, whit ecurly- haired little dog",
    "We met a handsome young navy lieutenant.",
    "The young girl lived alone in a nice, bright clean room..",
    "He drank a huge ice-cold glass of milk"
    # ... Agrega más oraciones aquí ...
]

# Procesamiento de cada oración
for i, oracion in enumerate(oraciones, 1):
    print(f"Oración {i}: {oracion}")
    adjetivo_correcto = identificar_adjetivo(oracion)
    if adjetivo_correcto:
        respuesta_usuario = input("Identifica el adjetivo en la oración: ")
        if respuesta_usuario.lower() == adjetivo_correcto:
            print("¡Correcto! Reescribe la oración:")
            nueva_oracion = input()
            print(f"Oración reescrita: {nueva_oracion}\n")
        else:
            print(f"El adjetivo correcto era '{adjetivo_correcto}'. Inténtalo de nuevo.\n")
    else:
        print("No se encontró un adjetivo en esta oración.\n")

print("¡Has completado todas las oraciones! ¡Bien hecho!")
