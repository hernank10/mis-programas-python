def cuestionario_ortografia():
    preguntas = [
        {
            "pregunta": "👩‍🏫 Escribe correctamente la siguiente oración: 'Los niños juegan con vuestros jugetes.'",
            "respuesta": "Los niños juegan con vuestros juguetes.",
            "retroalimentacion": "La palabra 'jugetes' está mal escrita. La forma correcta es 'juguetes', con 'g' antes de la vocal 'u'."
        },
        {
            "pregunta": "👩‍🏫 Corrige esta oración de acuerdo con las reglas de acentuación: 'El arbol esta lleno de frutos.'",
            "respuesta": "El árbol está lleno de frutos.",
            "retroalimentacion": "La palabra 'arbol' lleva tilde en la 'a' porque es una palabra grave terminada en consonante distinta de 'n' o 's'. Además, 'esta' debe acentuarse porque es un verbo y no un determinante."
        },
        {
            "pregunta": "👨‍🏫Completa la regla: 'Se escriben con 'b' los verbos terminados en ______.'",
            "respuesta": "bir",
            "retroalimentacion": "La regla dice que se escriben con 'b' los verbos terminados en 'bir', excepto 'hervir', 'servir' y 'vivir'."
        },
        {
            "pregunta": "👨‍🏫Escribe una oración usando correctamente 'porque' o 'por qué'.",
            "respuesta": "No sé por qué no me llamó ayer.",
            "retroalimentacion": "'Por qué' se utiliza en preguntas directas o indirectas. Asegúrate de usar 'porque' solo en respuestas o explicaciones."
        },
        {
            "pregunta": "👨‍🏫Corrige la siguiente frase: 'Mis compañeros estudiaron y repazaron para el exámen.'",
            "respuesta": "Mis compañeros estudiaron y repasaron para el examen.",
            "retroalimentacion": "La palabra 'repazaron' está mal escrita, la forma correcta es 'repasaron'. Además, 'exámen' no lleva tilde porque es una palabra grave terminada en 'n'."
        }
    ]

    print("🏛️ 👩‍🏫 ¡Bienvenido al cuestionario de ortografía y reglas gramaticales! 👨‍🏫 🏛️")
    puntuacion = 0

    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}:")
        print(pregunta["pregunta"])
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == pregunta["respuesta"].lower():
            print("✅ ¡Correcto!")
            puntuacion += 1
        else:
            print("❌ Incorrecto.")
            print(f"💡 Respuesta esperada: {pregunta['respuesta']}")
        
        print(f"💡 Retroalimentación: {pregunta['retroalimentacion']}")

    print("\n¡Has completado el cuestionario!")
    print(f"Tu puntuación final es: {puntuacion}/{len(preguntas)}")
    if puntuacion == len(preguntas):
        print("🎉 👩‍🏫 ¡Excelente trabajo! Has demostrado un conocimiento sólido de las reglas ortográficas.")
    elif puntuacion > len(preguntas) // 2:
        print("👩👍 Buen trabajo, pero puedes seguir practicando para mejorar aún más.")
    else:
        print("👩😔 Necesitas repasar más las reglas ortográficas. ¡Sigue practicando!")

# Ejecutar el programa
if __name__ == "__main__":
    cuestionario_ortografia()
