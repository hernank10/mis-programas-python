def leccion_032():
    print("\n📘 Lección 032 – Uso de la tilde en palabras interrogativas y exclamativas\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:

✅ Las palabras qué, cuál, cuánto, cómo, cuándo, dónde, quién y por qué se escriben con tilde **cuando tienen valor interrogativo o exclamativo**, ya sea en preguntas directas o indirectas.

📌 Ejemplos:

– ¿Qué quieres? ✅  
– ¡Cómo has crecido! ✅  
– No sé cuándo llegará. ✅  
– No sé cuando llegará. ❌ (debe llevar tilde: cuándo)

❌ No llevan tilde cuando son pronombres relativos sin tono interrogativo/exclamativo:

– El día que naciste...  
– El lugar donde vivimos...
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ ¿Qué hora es?",
        "✅ ¡Cuánto lo siento!",
        "✅ Dime cuándo llegaste.",
        "❌ Dime cuando llegaste. (Debe llevar tilde: cuándo)"
    ]
    print("\n✍️ Ejemplos correctos e incorrectos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: el estudiante elige si lleva tilde o no
    ejercicios = [
        ("¿___ es tu nombre?", "Qué"),
        ("No sé ___ lo hizo.", "quién"),
        ("Dime ___ fuiste a casa.", "cuándo"),
        ("___ bonito es tu jardín!", "¡Qué"),
        ("No sé ___ camino tomar.", "qué"),
        ("Fuimos al lugar ___ nos dijeron.", "que"),
        ("El día ___ me llamó, llovía.", "que"),
        ("No sabemos ___ llegará primero.", "quién"),
        ("¿___ cuesta este libro?", "Cuánto"),
        ("No importa ___ digas, ya lo sé.", "qué")
    ]

    print("\n🧪 Escribe la palabra correcta con tilde si corresponde:\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has aprendido cuándo usar tilde en oraciones interrogativas y exclamativas.")
    else:
        print("🔁 Intenta nuevamente. ¡Cada práctica te acerca al dominio!")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_032()
