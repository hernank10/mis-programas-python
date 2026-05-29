def practicar_sintaxis():
    ejercicios = [
        {
            "frase": "📚 Reorganiza las palabras para formar una oración correcta:\n'corrió / rápido / el / niño': ",
            "respuesta": "El niño corrió rápido",
        },
        {
            "frase": "✍️ Identifica el sujeto en la oración:\n'El gato duerme en el sillón.': ",
            "respuesta": "El gato",
        },
        {
            "frase": "📖 Selecciona el tipo de oración compuesta:\n'El profesor explica y los estudiantes escuchan.' (a) copulativa, (b) adversativa, (c) subordinada: ",
            "respuesta": "a",
        },
        {
            "frase": "📜 Completa la oración añadiendo el complemento:\n'María compró ____.': ",
            "respuesta": "un libro",
        },
        {
            "frase": "🖋 Indica el núcleo del predicado en esta oración:\n'Los niños juegan en el parque.': ",
            "respuesta": "juegan",
        },
        {
            "frase": "🏺‍♀️Identifica el complemento directo:\n'Juan come una manzana.': ",
            "respuesta": "una manzana",
        },
        {
            "frase": "🎭 Indica el tipo de oración:\n'¿Cuándo llega el tren?'\n(a) declarativa, (b) interrogativa, (c) exclamativa: ",
            "respuesta": "b",
        },
        {
            "frase": "🌟 Selecciona el tipo de subordinada:\n'Trajimos las flores que pidió mi madre.' (a) sustantiva, (b) adjetiva, (c) adverbial: ",
            "respuesta": "b",
        },
        {
            "frase": "️🌹 Reorganiza las palabras para formar una oración correcta:\n'en / tarde / la / regresó / casa': ",
            "respuesta": "Regresó tarde en la casa",
        },
        {
            "frase": "🌙 Identifica el complemento circunstancial:\n'Laura trabaja los fines de semana.': ",
            "respuesta": "los fines de semana",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica sintáctica! 🏛️")
    print("🌟📜✏️🕵 Responde las preguntas relacionadas con la estructura de las oraciones.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("‍Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡🧞‍♂️Correcto!✅\n")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡🧞‍♂️✍️Perfecto!✅ ¡Tu comprensión sintáctica es excelente!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡🧞✍️‍♂️Buen trabajo! ✅ Sigue practicando para mejorar aún más.")
    else:
        print("🧞✍️‍♂️No te preocupes, ¡puedes intentarlo de nuevo!")

# Ejecutar el programa
practicar_sintaxis()
