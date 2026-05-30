def practicar_sustantivos():
    ejercicios = [
        {"frase": "Clasifica el sustantivo 'mesa' como común o propio: ", "respuesta": "común"},
        {"frase": "¿Es 'amor' un sustantivo concreto o abstracto? ", "respuesta": "abstracto"},
        {"frase": "Traduce al inglés el sustantivo 'libro': ", "respuesta": "book"},
        {"frase": "Clasifica el sustantivo 'España' como común o propio: ", "respuesta": "propio"},
        {"frase": "Traduce al español el sustantivo 'house': ", "respuesta": "casa"},
        {"frase": "¿Es 'perro' un sustantivo masculino o femenino? ", "respuesta": "masculino"},
        {"frase": "Clasifica 'idea' como concreto o abstracto: ", "respuesta": "abstracto"},
        {"frase": "Traduce al inglés el sustantivo 'ciudad': ", "respuesta": "city"},
        {"frase": "¿Es 'gato' masculino o femenino? ", "respuesta": "masculino"},
        {"frase": "Traduce al español el sustantivo 'tree': ", "respuesta": "árbol"},
    ]

    print("¡Bienvenido al programa de práctica de sustantivos en español e inglés!")
    print("Completa los ejercicios clasificando o traduciendo los sustantivos.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Perfecto! ¡Eres un experto en sustantivos!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡Buen trabajo! Sigue practicando para perfeccionarte.")
    else:
        print("No te desanimes, ¡la práctica hace al maestro!")

# Ejecutar el programa
practicar_sustantivos()
