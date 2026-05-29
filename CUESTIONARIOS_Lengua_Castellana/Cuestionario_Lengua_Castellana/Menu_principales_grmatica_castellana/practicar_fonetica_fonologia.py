def practicar_fonetica_fonologia():
    ejercicios = [
        {
            "frase": "¿📚 Cuál es el símbolo fonético del sonido inicial de la palabra 'zapato' en español (AFI)? ",
            "respuesta": "s",
        },
        {
            "frase": "✍️ Clasifica la palabra 'canción' según su acento (aguda, llana, esdrújula): ",
            "respuesta": "aguda",
        },
        {
            "frase": "📖 ¿El sonido /b/ en 'bola' y 'vaca' es un fonema o un alófono? ",
            "respuesta": "fonema",
        },
        {
            "frase": "🖋️ Traduce al inglés el término 'esdrújula': ",
            "respuesta": "proparoxytone",
        },
        {
            "frase": "🏺 Completa la palabra con el sonido correcto: 'ca___to' (elije entre [b] o [β]): ",
            "respuesta": "b",
        },
        {
            "frase": "🎭 ¿Qué tipo de diptongo tiene la palabra 'aire'? (creciente, decreciente, homogéneo): ",
            "respuesta": "decreciente",
        },
        {
            "frase": "🌟 ¿Qué característica tiene el sonido /r/ en 'perro'? (vibrante simple o múltiple): ",
            "respuesta": "múltiple",
        },
        {
            "frase": "🌹 ¿Cuál es la transcripción fonética en español de 'cielo'? ",
            "respuesta": "ˈsje.lo",
        },
        {
            "frase": "🎭 ¿Qué tipo de palabra es 'pájaro' según su acento? (aguda, llana, esdrújula): ",
            "respuesta": "esdrújula",
        },
        {
            "frase": "🌙 ¿El sonido /k/ en inglés de 'cat' es aspirado o no aspirado? ",
            "respuesta": "aspirado",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica de fonética y fonología! 🏛️")
    print("🌟📜✏️🕵 Responde las preguntas correctamente para practicar tus conocimientos.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡🧞‍♂️✍Correcto!✅\n")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Perfecto!🧞‍♂️✍ ¡Eres un experto en fonética y fonología!✅")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡🧞‍♂️✍Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("🧞‍♂️✍No te desanimes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_fonetica_fonologia()
