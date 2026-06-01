def leccion_046():
    print("\n📘 Lección 046 – Uso de por qué, porque, porqué y por que\n")

    # Mostrar teoría
    teoria = """Estas cuatro expresiones suenan igual, pero tienen funciones gramaticales distintas:

🔹 por qué (separado y con tilde):
– Se usa en preguntas directas e indirectas.
– Ejemplo: ¿Por qué llegaste tarde? / No entiendo por qué te fuiste.

🔸 porque (junto y sin tilde):
– Se usa para responder, da una causa o razón.
– Ejemplo: Llegué tarde porque llovía.

🔸 porqué (junto y con tilde):
– Es un sustantivo que significa "la razón" o "el motivo".
– Ejemplo: No comprendo el porqué de su actitud.

🔹 por que (separado y sin tilde):
– Es una combinación de preposición + conjunción o pronombre relativo.
– Ejemplo: Luchó por que se hiciera justicia.

📌 Cada una tiene función distinta. Se deben distinguir según el contexto.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "¿Por qué no viniste ayer? → interrogación directa",
        "No entiendo por qué te vas. → interrogación indirecta",
        "No vine porque estaba enfermo. → causa",
        "El porqué de su decisión fue justo. → sustantivo",
        "Luchamos por que se apruebe la ley. → preposición + conjunción"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("¿Cuál forma es correcta?: ¿___ no me avisaste?", "por qué"),
        ("¿Cuál forma es correcta?: No fui ___ estaba enfermo.", "porque"),
        ("¿Cuál forma es correcta?: Aún no comprendo el ___ de su reacción.", "porqué"),
        ("¿Cuál forma es correcta?: Trabajamos ___ todo saliera bien.", "por que"),
        ("¿Cuál forma es correcta?: Me pregunto ___ lloras tanto.", "por qué"),
        ("¿Cuál forma es correcta?: No vino ___ tenía miedo.", "porque"),
        ("¿Cuál forma es correcta?: Nadie sabe el ___ del problema.", "porqué"),
        ("¿Cuál forma es correcta?: Rezó ___ su hijo aprobara el examen.", "por que"),
        ("¿Cuál forma es correcta?: ¿___ estás tan enojado?", "por qué"),
        ("¿Cuál forma es correcta?: Grité ___ me dolía.", "porque"),
        ("¿Cuál forma es correcta?: El niño preguntó ___ se van todos.", "por qué"),
        ("¿Cuál forma es correcta?: Esta es la razón ___ no quiero ir.", "por qué"),
        ("¿Cuál forma es correcta?: El maestro explicó el ___ de la norma.", "porqué"),
        ("¿Cuál forma es correcta?: Luchamos ___ haya justicia.", "por que"),
        ("¿Cuál forma es correcta?: No sé ___ estoy triste.", "por qué"),
        ("¿Cuál forma es correcta?: Me quedé ___ estaba lloviendo.", "porque"),
        ("¿Cuál forma es correcta?: Su ___ fue razonable.", "porqué"),
        ("¿Cuál forma es correcta?: Deseo ___ me comprendan.", "por que"),
        ("¿Cuál forma es correcta?: ¿___ razón discutiste?", "por qué"),
        ("¿Cuál forma es correcta?: Votaron ___ querían un cambio.", "porque")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe por qué, porque, porqué o por que):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Has dominado el uso de estas expresiones.")
    else:
        print("🔁 Inténtalo de nuevo. Revisa la teoría y vuelve a practicar.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_046()
