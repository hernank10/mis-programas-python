def main():
    print("🏛️ 👩‍🏫 ¡Bienvenido al cuestionario de gramática! 🏛️ ")
    print("👩Responde las preguntas escribiendo la letra de la opción correcta (a, b, c o d).\n")
    
    # Lista de preguntas con opciones y respuestas correctas
    preguntas = [
        {
            "pregunta": "👩¿Cuál es el sujeto en la oración: 'El perro corre por el parque'?",
            "opciones": ["a) corre", "b) perro", "c) parque", "d) el"],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 El sujeto es 'perro' porque es quien realiza la acción."
        },
        {
            "pregunta": "👩¿Qué tipo de palabra es 'rápidamente'?",
            "opciones": ["a) Adjetivo", "b) Sustantivo", "c) Adverbio", "d) Verbo"],
            "respuesta": "c",
            "retroalimentacion": "🎒✏️📘 'Rápidamente' es un adverbio porque modifica a un verbo."
        },
        {
            "pregunta": "👩¿Cuál es la función de la coma en la oración: 'Pedro, ven aquí'?",
            "opciones": ["a) Enumeración", "b) Vocativo", "c) Aclaración", "d) Enumeración y vocativo"],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 La coma indica un vocativo, llamando la atención de Pedro."
        },
        {
            "pregunta": "👩¿Qué es un diptongo?",
            "opciones": [
                "a) Unión de dos consonantes",
                "b) Unión de una vocal fuerte y una débil en la misma sílaba",
                "c) Unión de dos vocales fuertes",
                "d) Dos palabras con la misma raíz"
            ],
            "respuesta": "b",
            "retroalimentacion": "Un diptongo ocurre cuando una vocal fuerte y una débil se pronuncian juntas en la misma sílaba."
        },
        {
            "pregunta": "👩¿Cuál es el tiempo verbal en 'Nosotros habíamos terminado'? ",
            "opciones": ["a) Pretérito perfecto", "b) Pretérito pluscuamperfecto", "c) Futuro perfecto", "d) Pretérito imperfecto"],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 Es pretérito pluscuamperfecto porque indica una acción pasada anterior a otra acción pasada."
        },
        {
            "pregunta": "👩¿Qué signo de puntuación se usa para indicar una cita textual?",
            "opciones": ["a) Comillas", "b) Paréntesis", "c) Guiones", "d) Puntos suspensivos"],
            "respuesta": "a",
            "retroalimentacion": "🎒✏️📘 Las comillas se usan para indicar una cita textual o para resaltar algo."
        },
        {
            "pregunta": "👩¿Qué tipo de oración es 'Aunque llueva, iremos al parque'?",
            "opciones": ["a) Adversativa", "b) Subordinada concesiva", "c) Subordinada causal", "d) Subordinada condicional"],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 Es subordinada concesiva porque expresa una dificultad que no impide la acción."
        },
        {
            "pregunta": "👩¿Qué es un hiato?",
            "opciones": [
                "a) Unión de dos vocales en la misma sílaba",
                "b) Separación de dos vocales en sílabas distintas",
                "c) Pausa breve en una oración",
                "d) Separación entre palabras en una línea"
            ],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 Un hiato ocurre cuando dos vocales se separan en sílabas distintas."
        },
        {
            "pregunta": "👩¿Qué función cumple el punto y coma en la oración: 'Estudio por la mañana; trabajo por la tarde'?",
            "opciones": ["a) Enumeración", "b) Pausa mayor que la coma", "c) Indicar una causa", "d) Conectar ideas independientes relacionadas"],
            "respuesta": "d",
            "retroalimentacion": "🎒✏️📘 El punto y coma conecta ideas independientes relacionadas entre sí."
        },
        {
            "pregunta": "👩¿Cuál es la forma correcta del plural de 'crisis'?",
            "opciones": ["a) Crisises", "b) Crisis", "c) Crisisen", "d) Crises"],
            "respuesta": "b",
            "retroalimentacion": "🎒✏️📘 'Crisis' no cambia en plural porque es un sustantivo invariable."
        },
    ]
    
    puntuacion = 0

    # Bucle para recorrer las preguntas
    for i, pregunta in enumerate(preguntas):
        print(f"Pregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta: ").lower()
        
        if respuesta == pregunta["respuesta"]:
            print("🚀🌠🏅¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto.")
        print("Retroalimentación:", pregunta["retroalimentacion"], "\n")
    
    print(f"👩Tu puntuación final es: {puntuacion}/{len(preguntas)}")
    print("¡👩Gracias por participar!")

if __name__ == "__main__":
    main()
