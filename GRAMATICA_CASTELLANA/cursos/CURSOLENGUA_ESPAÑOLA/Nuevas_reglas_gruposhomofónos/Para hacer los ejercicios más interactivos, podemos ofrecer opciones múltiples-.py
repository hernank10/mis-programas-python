def generar_ejercicio_multiple(palabra):
    significados = palabras[palabra]
    significado_correcto = random.choice(significados)

    # Genera opciones incorrectas de manera aleatoria (implementación más avanzada)
    opciones_incorrectas = obtener_opciones_incorrectas(palabra, significado_correcto)

    # Mezcla las opciones y presenta el ejercicio
    opciones = [significado_correcto] + opciones_incorrectas
    random.shuffle(opciones)

    oracion = f"Elige el significado correcto de '{palabra}' en la oración: {generar_ejercicio(palabra)}"
    print(oracion)
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

    return opciones.index(significado_correcto) + 1  # Devuelve el índice de la respuesta correcta
