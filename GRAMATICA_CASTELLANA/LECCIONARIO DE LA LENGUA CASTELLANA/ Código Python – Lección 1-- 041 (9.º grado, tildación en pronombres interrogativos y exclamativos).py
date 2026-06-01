def leccion_041():
    print("\n📘 Lección 041 – Tilde en pronombres interrogativos y exclamativos\n")

    # Mostrar teoría
    teoria = """Los pronombres y adverbios interrogativos y exclamativos llevan tilde cuando expresan una pregunta o exclamación, **directa o indirecta**:

🟦 Palabras que llevan tilde: qué, cómo, cuál, cuán, cuánto, cuándo, dónde, quién, etc.

📌 Llevan tilde:
– En preguntas directas: ¿Qué hora es?
– En preguntas indirectas: No sé **qué** hacer.
– En exclamaciones: ¡Cómo has crecido!

❌ No llevan tilde cuando se usan como pronombres relativos sin sentido interrogativo o exclamativo:
– El día que viniste fue especial.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "¿Qué quieres comer? ✅",
        "No sé qué hacer. ✅",
        "¡Cómo me gustaría viajar! ✅",
        "El coche que compró es nuevo. ❌",
        "Dime cuándo vendrás. ✅",
        "Cuando llegues, avísame. ❌"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("¿Debe llevar tilde?: ¿Como estás?", "sí"),
        ("¿Debe llevar tilde?: No sé cuando llegará.", "sí"),
        ("¿Debe llevar tilde?: El día que naciste fue hermoso.", "no"),
        ("¿Debe llevar tilde?: ¡Cuanto te extraño!", "sí"),
        ("¿Debe llevar tilde?: La forma que usaste es correcta.", "no"),
        ("¿Debe llevar tilde?: Dime cómo lo hiciste.", "sí"),
        ("¿Debe llevar tilde?: No sé quien llamó.", "sí"),
        ("¿Debe llevar tilde?: Cuando vengas, trae pan.", "no"),
        ("¿Debe llevar tilde?: ¿Cual es tu color favorito?", "sí"),
        ("¿Debe llevar tilde?: Ese es el lugar donde nací.", "no"),
        ("¿Debe llevar tilde?: ¡Que alegría verte!", "sí"),
        ("¿Debe llevar tilde?: El hombre que viste es mi tío.", "no"),
        ("¿Debe llevar tilde?: ¿Cuantos hay?", "sí"),
        ("¿Debe llevar tilde?: Me pregunto donde están.", "sí"),
        ("¿Debe llevar tilde?: No importa lo que digas.", "no"),
        ("¿Debe llevar tilde?: ¡Como me gusta el chocolate!", "sí"),
        ("¿Debe llevar tilde?: Sabes cual es la respuesta.", "sí"),
        ("¿Debe llevar tilde?: La ciudad donde vivo es tranquila.", "no"),
        ("¿Debe llevar tilde?: ¡Quien pudiera volar!", "sí"),
        ("¿Debe llevar tilde?: No entiendo por qué pasó eso.", "sí")
    ]

    print("\n🧪 Empecemos los ejercicios (responde 'sí' o 'no' según si debe llevar tilde):")
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
        print("🏆 ¡Muy bien! Has superado la lección con éxito.")
    else:
        print("🔁 Sigue practicando. Puedes volver a intentarlo.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_041()
