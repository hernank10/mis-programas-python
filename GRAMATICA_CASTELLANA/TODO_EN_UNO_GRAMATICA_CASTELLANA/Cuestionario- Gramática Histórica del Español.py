def mostrar_menu():
    print("\n---🌟📜✏️🕵🏛 Cuestionario: Gramática Histórica del Español 🌟📜✏️🕵🏛---")
    print("1️⃣ Fonología")
    print("2️⃣ Morfología")
    print("3️⃣ Sintaxis")
    print("4️⃣ Léxico")
    print("5⃣ Otros temas históricos")
    print("6⃣ Salir")
    opcion = input("Seleccione una opción (1-6): ")
    return opcion

def cuestionario_fonologia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es la ley de la analogía y cómo afectó la evolución fonológica del español?": 
        "Es la tendencia a regularizar formas lingüísticas menos comunes.",
        "🌟📜✏️🕵🏛¿Cómo evolucionaron las vocales largas del latín en español?": 
        "Se convirtieron en vocales abiertas o cerradas dependiendo del contexto.",
        "🌟📜✏️🕵🏛Explica la pérdida de la /h/ inicial en español.": 
        "Se perdió en el español medieval tras debilitarse desde el latín.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_morfologia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Cómo evolucionó la declinación latina en el español medieval?": 
        "Se simplificó reduciéndose a dos casos principales.",
        "🌟📜✏️🕵🏛 Explica la desaparición del género neutro en español.": 
        "Se integró en los géneros masculino y femenino.",
        "🌟📜✏️🕵🏛 ¿Cómo se desarrollaron los pronombres clíticos en español?": 
        "A partir de formas enclíticas y proclíticas en el latín vulgar.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_sintaxis():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛 ¿Cómo cambió el orden de palabras del latín al español medieval?": 
        "Pasó de un orden flexible a un patrón SVO.",
        "🌟📜✏️🕵🏛 ¿Qué cambios se dieron en el uso de los tiempos verbales del latín al español?": 
        "Se simplificaron las formas y se introdujeron tiempos compuestos.",
        "🌟📜✏️🕵🏛 ¿Cómo se desarrollaron las perífrasis verbales en español?": 
        "Se crearon a partir de combinaciones auxiliares y participios.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_lexico():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛 ¿Cuál es el impacto del árabe en el vocabulario del español?": 
        "Introdujo más de 4000 términos relacionados con cultura y agricultura.",
        "🌟📜✏️🕵🏛 Describe la incorporación de préstamos del gótico en español.": 
        "Aportaron términos militares y administrativos.",
        "🌟📜✏️🕵🏛 ¿Cómo evolucionaron los términos agrícolas del latín al español?": 
        "Muchos se mantuvieron con alteraciones fonéticas.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_otros():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛 ¿Qué papel jugaron los glosarios medievales en la normalización del español?": 
        "Ayudaron a fijar formas ortográficas y léxicas.",
        "🌟📜✏️🕵🏛Explica la importancia de Alfonso X en el desarrollo del español escrito.": 
        "Creó las primeras normas ortográficas y promovió el uso del castellano.",
        "🌟📜✏️🕵🏛¿Qué dialectos del latín vulgar influyeron en la formación del español?": 
        "Principalmente los dialectos iberorromances.",
    }
    realizar_cuestionario(preguntas_respuestas)

def realizar_cuestionario(preguntas_respuestas):
    puntaje = 0
    for pregunta, respuesta_correcta in preguntas_respuestas.items():
        print(f"\nPregunta: {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == respuesta_correcta.lower():
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta es: {respuesta_correcta}")
    print(f"\nTu puntaje final: {puntaje}/{len(preguntas_respuestas)}")

# Programa principal
while True:
    opcion = mostrar_menu()
    if opcion == "1":
        cuestionario_fonologia()
    elif opcion == "2":
        cuestionario_morfologia()
    elif opcion == "3":
        cuestionario_sintaxis()
    elif opcion == "4":
        cuestionario_lexico()
    elif opcion == "5":
        cuestionario_otros()
    elif opcion == "6":
        print("🌟📜✏️🕵🏛¡Gracias por participar! Hasta la próxima.")
        break
    else:
        print("Opción inválida❌. Intente de nuevo.")
