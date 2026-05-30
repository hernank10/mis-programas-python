def practicar_morfologia():
    ejercicios = [
        {
            "frase": "Identifica el morfema derivado en la palabra 'felicidad': ",
            "respuesta": "idad",
        },
        {
            "frase": "¿Cuál es el prefijo en la palabra 'imposible'? ",
            "respuesta": "im",
        },
        {
            "frase": "Analiza la palabra 'corredor': ¿Cuál es la raíz? ",
            "respuesta": "corred",
        },
        {
            "frase": "Deconstruye la palabra 'reutilizar'. ¿Cuál es el sufijo? ",
            "respuesta": "izar",
        },
        {
            "frase": "Identifica el tipo de palabra derivada: 'reconstruir' (a) verbos, (b) sustantivos, (c) adjetivos: ",
            "respuesta": "a",
        },
        {
            "frase": "Clasifica la palabra 'manzanas' según su morfología: (a) sustantivo plural, (b) adjetivo plural, (c) verbo plural: ",
            "respuesta": "a",
        },
        {
            "frase": "¿Cuál es el sufijo que indica pluralidad en la palabra 'niños'? ",
            "respuesta": "s",
        },
        {
            "frase": "¿Qué tipo de palabra es 'rápidamente'? (a) sustantivo, (b) adverbio, (c) verbo: ",
            "respuesta": "b",
        },
        {
            "frase": "Identifica el morfema flexivo en la palabra 'hablando': ",
            "respuesta": "ando",
        },
        {
            "frase": "Deconstruye la palabra 'inmortal'. ¿Cuál es el sufijo? ",
            "respuesta": "al",
        },
    ]

    print("¡Bienvenido al programa de práctica morfológica!")
    print("Responde las preguntas relacionadas con la formación y estructura de las palabras.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Perfecto! ¡Tu comprensión morfológica es excelente!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("No te preocupes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_morfologia()
