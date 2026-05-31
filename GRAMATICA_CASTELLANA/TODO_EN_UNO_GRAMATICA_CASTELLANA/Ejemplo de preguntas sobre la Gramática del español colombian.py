def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    """Muestra una pregunta y evalúa la respuesta del usuario."""
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3): "))
        if respuesta_usuario == respuesta_correcta:
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            return True
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")
        return False

def cuestionario_espanol_colombiano():
    """🌟📜✏️🕵🏛Cuestionario interactivo sobre la Gramática del español colombiano.🌟📜✏️🕵🏛"""
    preguntas = [
        ("🌟📜✏️🕵🏛¿Qué característica fonética distingue al español hablado en la región paisa?",
         ["Aspiración de la /s/.", "Uso del voseo.", "Pronunciación de la /s/ como fuerte y clara."],
         3),
        ("🌟📜✏️🕵🏛En el español costeño, la /s/ final de sílaba se suele:",
         ["Aspirar o desaparecer.", "Mantener como en español estándar.", "Pronunciar como /z/."],
         1),
        ("🌟📜✏️🕵🏛En algunas regiones de Colombia, la /r/ final de palabra se puede:",
         ["Convertir en /l/.", "Pronunciar como /rr/.", "Eliminarse por completo."],
         1),
        ("🌟📜✏️🕵🏛El voseo es característico en:",
         ["El español hablado en Bogotá.", "El español hablado en la región paisa.", "Todo el territorio colombiano."],
         2),
        ("🌟📜✏️🕵🏛¿Qué característica morfosintáctica se observa en el español de la región caribeña?",
         ["Uso frecuente de diminutivos.", "Uso extendido del pretérito perfecto compuesto.", "Reducción de artículos en el habla cotidiana."],
         1),
        ("🌟📜✏️🕵🏛La palabra 'parcero' es un término coloquial usado principalmente en:",
         ["Bogotá.", "Medellín.", "Barranquilla."],
         2),
        ("🌟📜✏️🕵🏛El término 'guagua', que se usa en algunas regiones de Colombia, significa:",
         ["Niño pequeño.", "Autobús.", "Comida típica."],
         1),
        ("🌟📜✏️🕵🏛¿Qué significa 'chévere' en el español colombiano?",
         ["Difícil.", "Bueno o agradable.", "Confuso."],
         2),
        ("🌟📜✏️🕵🏛El uso de 'usted' para referirse a personas cercanas como amigos o familiares es común en:",
         ["Todas las regiones de Colombia.", "Principalmente en Bogotá y el altiplano cundiboyacense.", "Solo en la región caribeña."],
         2),
        ("🌟📜✏️🕵🏛El español colombiano tiende a usar el 'usted' incluso con personas jóvenes como signo de:",
         ["Distancia social.", "Cortesía y respeto.", "Formalidad obligatoria."],
         2),
    ]
    
    print("🌟📜✏️🕵🏛¡Bienvenido al Cuestionario sobre la Gramática del español colombiano!🌟📜✏️🕵🏛")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    
    print(f"\n¡Has completado el cuestionario! Tu puntuación final es {puntuacion}/{len(preguntas)}.")

# Ejecutar el cuestionario
cuestionario_espanol_colombiano()
