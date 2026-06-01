def leccion_021():
    print("\n📘 Lección 021 – Uso correcto de la C, S y Z\n")

    # Mostrar teoría
    teoria = """Las letras C, S y Z pueden sonar parecido en español, pero tienen reglas diferentes. Aquí algunas básicas:

🔵 Se escribe con C:
- Los diminutivos terminados en -cito, -ecillo (ej. pececito, panecillo).
- Sustantivos terminados en -ción, cuando vienen de verbos terminados en -ar (ej. educación ← educar).

🟢 Se escribe con S:
- Gentilicios terminados en -ense (ej. canadiense, costarricense).
- Adjetivos terminados en -oso, -osa (ej. precioso, hermosa).

🟡 Se escribe con Z:
- Palabras terminadas en -azo, -aza (golazo, manaza).
- Sustantivos abstractos terminados en -ez, -eza (ej. rapidez, belleza).

📌 Estas reglas ayudan a distinguir las palabras correctas. Se aprende con práctica y atención a la escritura.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["educación", "preciosa", "belleza", "pececito", "golazo", "canadiense", "hermoso", "panecillo"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Lista de ejercicios: (pregunta, respuesta_correcta)
    ejercicios = [
        ("¿Cómo se escribe correctamente: educasión o educación?", "educación"),
        ("¿Cuál es la forma correcta: panesillo o panecillo?", "panecillo"),
        ("¿Qué palabra es correcta: manasa o manaza?", "manaza"),
        ("¿Cuál se escribe bien: golaso o golazo?", "golazo"),
        ("¿Cómo se escribe: pececito o pesesito?", "pececito"),
        ("¿Cuál es la forma correcta: rapidez o rapedes?", "rapidez"),
        ("¿Qué palabra es correcta: preciosa o presiosa?", "preciosa"),
        ("¿Cuál está bien escrita: canadiense o canadiense?", "canadiense"),
        ("¿Cómo se escribe bien: hermosa o hermoza?", "hermosa"),
        ("¿Cuál es la forma correcta: belleza o belleca?", "belleza"),
        ("¿Qué palabra es correcta: golpecito o golpezito?", "golpecito"),
        ("¿Cómo se escribe: tristeza o tristesa?", "tristeza"),
        ("¿Cuál es correcta: velocidad o velocidaz?", "velocidad"),
        ("¿Qué forma es correcta: limpieza o limpiesa?", "limpieza"),
        ("¿Cómo se escribe bien: risa o riza? (de reír)", "risa"),
        ("¿Cuál es correcta: jugoso o jugozo?", "jugoso"),
        ("¿Qué palabra es correcta: audaz o audas?", "audaz"),
        ("¿Cuál es correcta: fuerza o fuerza?", "fuerza"),
        ("¿Cómo se escribe correctamente: grandeza o grandesa?", "grandeza"),
        ("¿Qué palabra es correcta: golosina o golozina?", "golosina")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe la palabra correcta):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Calcular resultado
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has superado la lección con éxito.")
    else:
        print("🔁 Sigue practicando. Puedes volver a intentarlo.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_021()
