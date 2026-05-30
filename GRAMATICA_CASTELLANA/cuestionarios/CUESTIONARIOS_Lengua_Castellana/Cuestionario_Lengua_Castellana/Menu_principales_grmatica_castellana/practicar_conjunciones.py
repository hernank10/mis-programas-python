def practicar_conjunciones():
    ejercicios = [
        {
            "frase": "📚 Identifica el tipo de conjunción en esta oración: 'Pedro y Juan fueron al mercado.' (coordinante o subordinante): ",
            "respuesta": "coordinante",
        },
        {
            "frase": "✍️ Traduce al inglés la conjunción 'aunque': ",
            "respuesta": "although",
        },
        {
            "frase": "📖 Completa la oración: 'No iremos a la playa ___ llueva.' (conjunción subordinante): ",
            "respuesta": "si",
        },
        {
            "frase": "🌙 Clasifica la conjunción 'o' según su tipo (copulativa, disyuntiva, adversativa, causal, consecutiva, condicional): ",
            "respuesta": "disyuntiva",
        },
        {
            "frase": "🖋️ Traduce al español la conjunción 'because': ",
            "respuesta": "porque",
        },
        {
            "frase": "🏺 ¿Qué tipo de conjunción es 'pero' (copulativa, disyuntiva, adversativa, causal, consecutiva, condicional)? ",
            "respuesta": "adversativa",
        },
        {   "frase": "🎭 Traduce al inglés la conjunción 'ni': ",
            "respuesta": "nor",
        },
        {
            "frase": "🌟 Completa la oración: '___ no estudies, no aprobarás el examen.' (conjunción causal): ",
            "respuesta": "Si",
        },
        {
            "frase": "🌹 ¿Qué tipo de conjunción es 'así que' (copulativa, disyuntiva, adversativa, causal, consecutiva, condicional)? ",
            "respuesta": "consecutiva",
        },
        {
            "frase": "📜 Traduce al español la conjunción 'however': ",
            "respuesta": "sin embargo",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica de conjunciones en español e inglés! 🏛️")
    print("🌟📜✏️🕵 Completa los ejercicios respondiendo las preguntas correctamente.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("🧞‍♂️✍¡Correcto!✅\n")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"🧞‍♂️✍Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("🧞‍♂️✍¡Perfecto! ¡Eres un experto en conjunciones!✅")
    elif puntaje >= len(ejercicios) * 0.7:
        print("🧞‍♂️✍¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("🧞‍♂️✍No te desanimes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_conjunciones()
