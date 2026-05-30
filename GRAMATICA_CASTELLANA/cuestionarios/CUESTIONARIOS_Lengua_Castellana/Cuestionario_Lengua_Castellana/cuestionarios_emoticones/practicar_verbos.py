def practicar_verbos():
    ejercicios = [
        {
            "frase": "📚 Conjuga el verbo 'cantar' en la primera persona del singular en presente: ",
            "respuesta": "canto",
        },
        {
            "frase": "✍️ ¿Es el verbo 'ser' regular o irregular? ",
            "respuesta": "irregular",
        },
        {
            "frase": "📖 Traduce al inglés el verbo 'correr': ",
            "respuesta": "run",
        },
        {
            "frase": "📜 ¿En qué tiempo está el verbo 'cantábamos'? ",
            "respuesta": "pretérito imperfecto",
        },
        {
            "frase": "🖋Traduce al español el verbo 'to eat': ",
            "respuesta": "comer",
        }, 
        {
            "frase": "✍️ Conjuga el verbo 'vivir' en la segunda persona del singular en futuro: ",
            "respuesta": "vivirás",
        },
        {
            "frase": "📖 ¿Es el verbo 'ir' regular o irregular? ",
            "respuesta": "irregular",
        },
        {
            "frase": "📜 Traduce al inglés el verbo 'leer': ",
            "respuesta": "read",
        },
        {
            "frase": "🖋 ¿En qué tiempo está el verbo 'habré hablado'? ",
            "respuesta": "futuro perfecto",
        },
        {
            "frase": "📚 Conjuga el verbo 'amar' en la tercera persona del plural en pretérito perfecto simple: ",
            "respuesta": "amaron",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica de verbos en español e inglés! 🏛️")
    print("🌟📜✏️🕵 Completa los ejercicios respondiendo las preguntas correctamente.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("🧞‍♂️✍ ¡Correcto!✅\n")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"🧞‍♂️✍ Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Perfecto!✅ ¡Eres un experto en verbos!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("🧞‍♂️✍ ¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("🧞‍♂️✍ No te desanimes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_verbos()
