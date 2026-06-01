def leccion_052():
    print("\n📘 Lección 052 – Concordancia del verbo con sujetos colectivos\n")

    teoria = """✍️ Regla gramatical:

✅ Cuando el sujeto es un **nombre colectivo** (como grupo, gente, multitud, mayoría), el verbo suele ir en **singular**, aunque puede haber matices según el contexto:

– La gente **grita** mucho. ✅  
– El equipo **viajó** temprano. ✅  
– Una multitud **se reunió** en la plaza. ✅

⚠️ Excepciones aceptadas (uso culto o enfático):
– La mayoría de los estudiantes **aprobaron**. (cuando se quiere enfatizar a los individuos)
"""

    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ La multitud aplaudía con fuerza.",
        "✅ El grupo camina en silencio.",
        "✅ La mayoría de los votantes eligió a su candidato.",
        "❌ El público aplaudieron. → debe ser: aplaudió"
    ]

    print("\n✍️ Ejemplos correctos e incorrectos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("La gente _____ muy animada.", "estaba"),
        ("La mayoría de los asistentes _____ puntuales.", "fue"),
        ("El grupo de niños _____ en la sala.", "jugaba"),
        ("El equipo _____ el torneo sin perder.", "ganó"),
        ("Una multitud _____ al presidente.", "aplaudió"),
        ("El ejército _____ al norte del país.", "avanzó"),
        ("La muchedumbre _____ hasta que terminó el discurso.", "esperó"),
        ("La clase _____ una carta al director.", "escribió"),
        ("El conjunto de datos _____ incorrecto.", "era"),
        ("El jurado _____ su veredicto final.", "emitió")
    ]

    print("\n🧪 Escribe la forma correcta del verbo en cada oración:\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {respuesta_correcta}")

    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Dominas la concordancia con sujetos colectivos.")
    else:
        print("🔁 Intenta nuevamente. ¡Sigue practicando para mejorar!")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_052()
