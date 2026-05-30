def practicar_adverbios():
    ejercicios = [
        {
            "frase": "¿Qué tipo de adverbio es 'rápidamente'? (modo, tiempo, lugar, cantidad, afirmación, negación, duda): ",
            "respuesta": "modo",
        },
        {
            "frase": "Traduce al inglés el adverbio 'hoy': ",
            "respuesta": "today",
        },
        {
            "frase": "Completa la oración: 'El gato duerme ___.' (adverbio relacionado con el lugar) ",
            "respuesta": "aquí",
        },
        {
            "frase": "Clasifica el adverbio 'nunca' según su tipo (modo, tiempo, lugar, cantidad, afirmación, negación, duda): ",
            "respuesta": "negación",
        },
        {
            "frase": "Traduce al español el adverbio 'always': ",
            "respuesta": "siempre",
        },
        {
            "frase": "¿Qué tipo de adverbio es 'demasiado'? (modo, tiempo, lugar, cantidad, afirmación, negación, duda): ",
            "respuesta": "cantidad",
        },
        {
            "frase": "Traduce al inglés el adverbio 'cerca': ",
            "respuesta": "near",
        },
        {
            "frase": "Completa la oración: 'Me siento ___ seguro de esta decisión.' (adverbio relacionado con cantidad) ",
            "respuesta": "muy",
        },
        {
            "frase": "¿Qué tipo de adverbio es 'quizás'? (modo, tiempo, lugar, cantidad, afirmación, negación, duda): ",
            "respuesta": "duda",
        },
        {
            "frase": "Traduce al español el adverbio 'quickly': ",
            "respuesta": "rápidamente",
        },
    ]

    print("¡Bienvenido al programa de práctica de adverbios en español e inglés!")
    print("Completa los ejercicios respondiendo las preguntas correctamente.\n")

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
        print("¡Perfecto! ¡Eres un experto en adverbios!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("No te desanimes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_adverbios()
