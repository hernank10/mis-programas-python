def generar_ejercicio(palabra):
    significados = palabras[palabra]
    significado_aleatorio = random.choice(significados)

    # Elige un tipo de oración aleatoriamente
    tipo_oracion = random.choice(["simple", "compuesta", "pregunta"])

    if tipo_oracion == "simple":
        oracion = "Pedro corroboró ____ la afirmación de Felipe."  # Ejemplo para "asimismo"
    elif tipo_oracion == "compuesta":
        oracion = "Así lo hizo él; ____ debes hacerlo tú."  # Ejemplo para "así mismo"
    else:
        oracion = "¿Le concede lo que pide, aunque se perjudica ____?"  # Ejemplo para "a sí mismo"

    oracion = oracion.replace("____", palabra, 1)  # Reemplaza la primera ocurrencia
    oracion = oracion.replace("____", significado_aleatorio, 1)

    return oracion
