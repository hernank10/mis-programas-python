def leccion_037():
    print("\n📘 Lección 037 – Diferencias entre: por qué, porque, porqué y por que\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:

1. **por qué** → interrogativo o exclamativo (preguntas directas o indirectas):
   – ¿Por qué lloras?
   – No entiendo por qué se fue.

2. **porque** → conjunción causal, responde a la pregunta:
   – Lloro porque me duele.
   – No fui porque estaba enfermo.

3. **porqué** → sustantivo (el motivo), siempre va con "el":
   – El porqué de su tristeza es desconocido.

4. **por que** → combinación de preposición + conjunción o pronombre relativo:
   – Lucharon por que se hiciera justicia.
   – Esa es la razón por que protestaron.
"""
    print("📚 Teoría:\n" + teoria)

    # Ejemplos
    ejemplos = [
        "✅ ¿Por qué estás triste?",
        "✅ Me fui porque tenía sueño.",
        "✅ El porqué de la decisión no se explicó.",
        "✅ Peleó por que su voz fuera escuchada.",
        "❌ No sé porque lloras. (debe ser por qué)",
        "❌ Esa es el por qué. (debe ser el porqué)"
    ]
    print("\n✍️ Ejemplos correctos e incorrectos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("¿_____ no viniste ayer?", "Por qué"),
        ("No vine _____ estaba enfermo.", "porque"),
        ("No entiendo el _____ de su reacción.", "porqué"),
        ("Lucharon _____ se aprobara la ley.", "por que"),
        ("No sé _____ se queja tanto.", "por qué"),
        ("Esa es la razón _____ no vino.", "por que"),
        ("Ella no come carne _____ es vegetariana.", "porque"),
        ("El niño preguntó el _____ del castigo.", "porqué"),
        ("¿_____ grita tanto ese señor?", "Por qué"),
        ("Te lo explico _____ quiero ayudarte.", "porque")
    ]

    print("\n🧪 Completa con la forma correcta: por qué / porque / porqué / por que\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ La respuesta correcta era: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Has dominado el uso correcto de estas expresiones.")
    else:
        print("🔁 Repite la lección para reforzar el aprendizaje.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_037()
