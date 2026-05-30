import random

# Base de datos de preguntas (colocaciones léxicas)
preguntas = [
    {
        "pregunta": "¿Qué verbo se usa con 'vuelta'?",
        "opciones": ["hacer", "dar", "tomar", "crear"],
        "respuesta": "dar",
        "explicacion": "RAE: La combinación correcta es 'dar una vuelta'. Es una convención idiomática histórica."
    },
    {
        "pregunta": "¿Qué verbo acompaña a 'matrimonio'?",
        "opciones": ["contraer", "hacer", "construir", "desarrollar"],
        "respuesta": "contraer",
        "explicacion": "RAE: 'Contraer matrimonio' viene del latín 'contrahere' (unir), usado solo para compromisos legales."
    },
    {
        "pregunta": "¿Cómo se completa? 'Desarrollar ______'",
        "opciones": ["velocidad", "desaliento", "sacerdocio", "virtud"],
        "respuesta": "velocidad",
        "explicacion": "RAE: 'Desarrollar velocidad' es una colocación técnica aceptada, frente a 'ejercitar virtud'."
    },
    {
        "pregunta": "¿Qué preposición usa 'inverso'?",
        "opciones": ["a", "de", "en", "por"],
        "respuesta": "de",
        "explicacion": "RAE: Según la norma, 'inverso' siempre lleva preposición 'de' (ej: inverso de la proporción)."
    },
    {
        "pregunta": "¿Qué verbo NO es correcto? '______ influencia'",
        "opciones": ["ejercer", "tener", "contraer", "desplegar"],
        "respuesta": "contraer",
        "explicacion": "RAE: 'Contraer' se usa para deudas/enfermedades, no para influencia. Lo correcto es 'ejercer influencia'."
    }
]

def practicar_colocaciones():
    random.shuffle(preguntas)
    puntaje = 0

    print("¡Practiquemos colocaciones léxicas! (Escribe el número de la opción)\n")

    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['pregunta']}")
        for idx, opcion in enumerate(pregunta['opciones'], 1):
            print(f"{idx}. {opcion}")

        while True:
            try:
                respuesta = int(input("\nTu respuesta: ")) - 1
                if 0 <= respuesta < len(pregunta['opciones']):
                    break
                else:
                    print("¡Número inválido! Intenta de nuevo.")
            except ValueError:
                print("¡Solo números! Intenta de nuevo.")

        opcion_elegida = pregunta['opciones'][respuesta]
        correcta = pregunta['respuesta']

        if opcion_elegida == correcta:
            print(f"\n✅ ¡Correcto! {pregunta['explicacion']}")
            puntaje += 1
        else:
            print(f"\n❌ Incorrecto. La respuesta era: {correcta}")
            print(f"Explicación: {pregunta['explicacion']}")

    print(f"\n¡Práctica completada! Puntaje final: {puntaje}/{len(preguntas)}")
    if puntaje == len(preguntas):
        print("¡Perfecto! Dominas estas colocaciones 👑")
    elif puntaje >= len(preguntas) * 0.7:
        print("¡Buen trabajo! Sigue practicando 💪")
    else:
        print("¡Sigue intentándolo! La práctica hace al maestro 📚")

# Ejecutar el programa
practicar_colocaciones()
