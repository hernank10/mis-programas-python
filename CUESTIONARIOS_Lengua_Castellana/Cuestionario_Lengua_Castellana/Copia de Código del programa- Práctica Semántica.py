def practicar_semantica():
    ejercicios = [
        {
            "frase": "📚 Identifica el sinónimo de 'feliz': (a) triste, (b) contento, (c) rápido: ",
            "respuesta": "b",
        },
        {
            "frase": "✍️ ¿Cuál es el hipónimo de 'animal'? (a) mamífero, (b) perro, (c) ser vivo: ",
            "respuesta": "b",
        },
        {
            "frase": "📖 La palabra 'banco' tiene múltiples significados. ¿Cuál es un significado válido? (a) institución financiera, (b) tipo de comida, (c) herramienta para pintar: ",
            "respuesta": "a",
        },
        {
            "frase": "📜 Clasifica la palabra 'rosa' según su campo semántico (colores, flores, emociones): ",
            "respuesta": "flores",
        },
        {
            "frase": "🖋️ ¿Qué relación semántica existe entre 'manzana' y 'fruta'? (a) sinónimos, (b) hiponimia, (c) antónimos: ",
            "respuesta": "b",
        },
        {
            "frase": "🏺 Completa la metáfora: 'La vida es un ___.' (a) río, (b) edificio, (c) espejo: ",
            "respuesta": "río",
        },
        {
            "frase": "🎭 ¿Cuál de las siguientes palabras pertenece al mismo campo semántico que 'camisa'? (a) pantalón, (b) botella, (c) silla: ",
            "respuesta": "a",
        },
        {
            "frase": "🌟 Relaciona el antónimo de 'denso': (a) ligero, (b) pesado, (c) oscuro: ",
            "respuesta": "a",
        },
        {
            "frase": "🌹 Elige el significado correcto de la polisemia de 'llave': (a) instrumento para abrir, (b) movimiento en lucha, (c) ambas: ",
            "respuesta": "c",
        },
        {
            "frase": "🌙 Selecciona la hiperonimia de 'gato': (a) felino, (b) animal, (c) ambas: ",
            "respuesta": "c",
        },
    ]

    print("🏛️ ¡Bienvenido al programa de práctica semántica! 🏛️")
    print("🌟📜✏️🕵Responde las preguntas para mejorar tu comprensión del significado y las relaciones de las palabras.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Ejercicio {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("🧞Tu respuesta: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("🧞‍♂️✍¡Correcto!✅\n")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Perfecto!✅ ¡Tu comprensión semántica es excelente!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡🧞‍♂️✍Buen trabajo! Sigue practicando para perfeccionarte.")
    else:
        print("🧞‍♂️✍ No te preocupes, ¡puedes intentarlo nuevamente!")

# Ejecutar el programa
practicar_semantica()
