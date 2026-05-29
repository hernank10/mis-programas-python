def cuestionario_transformaciones():
    preguntas = [
        {
            "tipo": "transformar",
            "pregunta": "👩Escribe la forma pasiva de esta oración: 'El chef preparó una deliciosa cena.'",
            "respuesta": "Una deliciosa cena fue preparada por el chef.",
            "retroalimentacion": "La forma pasiva correcta es 'Una deliciosa cena fue preparada por el chef'."
        },
        {
            "tipo": "transformar",
            "pregunta": "👩Cambia esta oración al tiempo futuro: 'Los niños juegan en el parque.'",
            "respuesta": "Los niños jugarán en el parque.",
            "retroalimentacion": "El verbo 'juegan' en futuro es 'jugarán', conservando el resto de la oración."
        },
        {
            "tipo": "escribir",
            "pregunta": "👩Escribe una oración en la que el sujeto sea implícito y el verbo esté en pretérito.",
            "respuesta": "Fui al mercado.",
            "retroalimentacion": "Un ejemplo de sujeto implícito es 'Fui al mercado', donde el sujeto 'yo' no está explícito."
        },
        {
            "tipo": "transformar",
            "pregunta": "👩Transforma esta oración en una pregunta: 'Tienes tiempo libre para leer libros.'",
            "respuesta": "¿Tienes tiempo libre para leer libros?",
            "retroalimentacion": "Para transformar en pregunta, agrega los signos de interrogación: '¿Tienes tiempo libre para leer libros?'."
        },
        {
            "tipo": "escribir",
            "pregunta": "👩Escribe una oración compuesta que use una conjunción adversativa ('pero', 'sin embargo').",
            "respuesta": "Estudié para el examen, pero olvidé entregar la tarea.",
            "retroalimentacion": "Una oración compuesta puede ser: 'Estudié para el examen, pero olvidé entregar la tarea.'"
        }
    ]

    print("🏛️ 👩¡Bienvenido al cuestionario de escritura y transformación de oraciones! ‍🏫 🏛")
    puntuacion = 0

    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}:")
        print(pregunta["pregunta"])
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == pregunta["respuesta"].lower():
            print("✅ ¡👩Correcto!")
            puntuacion += 1
        else:
            print("❌ Incorrecto.")
            print(f"💡 Respuesta esperada: {pregunta['respuesta']}")

        print(f"💡 Retroalimentación: {pregunta['retroalimentacion']}")

    print("\n¡Has completado el cuestionario!")
    print(f"👩Tu puntuación final es: {puntuacion}/{len(preguntas)}")

# Ejecutar el programa
if __name__ == "__main__":
    cuestionario_transformaciones()
