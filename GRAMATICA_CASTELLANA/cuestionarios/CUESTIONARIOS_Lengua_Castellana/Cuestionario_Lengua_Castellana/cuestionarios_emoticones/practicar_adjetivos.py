def practicar_adjetivos():
    ejercicios = [
        {
            "frase": "📚 Clasifica el adjetivo 'rápido' como calificativo o determinativo: ",
            "respuesta": "calificativo",
        },
        {
            "frase": "✍️ Traduce al inglés el adjetivo 'hermoso': ",
            "respuesta": "beautiful",
        },
        {
            "frase": "📖 Completa la oración: 'El cielo está muy ___.' (adjetivo relacionado con el color azul) ",
            "respuesta": "azul",
        },
        {
            "frase": "¿📜 Es 'este' un adjetivo demostrativo o posesivo? ",
            "respuesta": "demostrativo",
        },
        {
            "frase": "🖋Traduce al español el adjetivo 'happy': ",
            "respuesta": "feliz",
        },
        {
            "frase": "📚¿El adjetivo 'inteligente' varía en género? (sí o no): ",
            "respuesta": "no",
        },
        {
            "frase": "📖 Clasifica el adjetivo 'mi' como posesivo o demostrativo: ",
            "respuesta": "posesivo",
        },
        {
            "frase": "✍️  Traduce al inglés el adjetivo 'pequeño': ",
            "respuesta": "small",
        },
        {
            "frase": "📚 Completa la oración: 'Ella tiene una actitud muy ___.' (adjetivo positivo) ",
            "respuesta": "amable",
        },
        {
            "frase": "📜 Clasifica 'esos' como posesivo o demostrativo: ",
            "respuesta": "demostrativo",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica de adjetivos en español e inglés! 🏛️")
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

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("🧞‍♂️✍ ¡Perfecto!✅ ¡Eres un experto en adjetivos!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("🧞‍♂️✍ ¡Buen trabajo! Sigue practicando para mejorar aún más.")
    else:
        print("No te desanimes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_adjetivos()
