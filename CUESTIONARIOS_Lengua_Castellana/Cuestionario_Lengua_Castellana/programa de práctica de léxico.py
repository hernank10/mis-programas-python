def practicar_lexico():
    ejercicios = [
        {
            "frase": "Relaciona el sinónimo correcto: 'rápido' - (a) veloz, (b) lento, (c) grande: ",
            "respuesta": "a",
        },
        {
            "frase": "Elige la palabra que completa mejor esta frase: 'El gato ___ en el tejado.' (a) brincó, (b) escribió, (c) nadó: ",
            "respuesta": "a",
        },
        {
            "frase": "¿Cuál es el antónimo de 'alegría'? ",
            "respuesta": "tristeza",
        },
        {
            "frase": "Clasifica la palabra 'escuela' según su campo semántico (educación, animales, alimentos): ",
            "respuesta": "educación",
        },
        {
            "frase": "Selecciona la opción que contiene un par de palabras homónimas: (a) casa/caza, (b) vino/vino, (c) bello/vello: ",
            "respuesta": "b",
        },
        {
            "frase": "Identifica el parónimo: 'eficaz' y ___ (a) eficaz, (b) eficazmente, (c) eficiente: ",
            "respuesta": "c",
        },
        {
            "frase": "Traduce al inglés la palabra 'coche': ",
            "respuesta": "car",
        },
        {
            "frase": "¿Qué relación léxica tienen las palabras 'grande' y 'enorme'? (sinónimos, antónimos, homónimos): ",
            "respuesta": "sinónimos",
        },
        {
            "frase": "Completa el refrán: 'Más vale tarde que ___.' (a) pronto, (b) nunca, (c) siempre: ",
            "respuesta": "b",
        },
        {
            "frase": "Clasifica la palabra 'pan' según su campo semántico (educación, alimentos, transporte): ",
            "respuesta": "alimentos",
        },
    ]

    print("¡Bienvenido al programa de práctica de léxico!")
    print("Responde las preguntas para mejorar tu vocabulario.\n")

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
        print("¡Perfecto! ¡Tienes un vocabulario amplio y preciso!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡Buen trabajo! Sigue practicando para enriquecer tu léxico aún más.")
    else:
        print("No te preocupes, ¡puedes intentarlo nuevamente!")

# Ejecutar el programa
practicar_lexico()
