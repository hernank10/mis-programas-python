def leccion_022():
    print("\n📘 Lección 022 – Uso de la 'g' en palabras con los sufijos -gen, -génico, -gélico, -gia, -gio\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:
✅ Se escriben con **g** las palabras terminadas en los sufijos:
- -gen (origen, imagen)
- -génico (patogénico, alergénico)
- -gélico (angélico)
- -gia y -gio (energía, colegio)

📌 Algunas excepciones se aprenden por uso, pero estas terminaciones siguen reglas regulares.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ imagen, oxígeno, alergénico, colegio, estrategia, geología",
        "❌ imaven (incorrecto), enersía (incorrecto)"
    ]
    print("\n✍️ Ejemplos correctos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: completar con "g" o "j" según la regla
    ejercicios = [
        ("Completa: ima__en", "g"),
        ("Completa: ener__ía", "g"),
        ("Completa: col__io", "g"),
        ("Completa: patriar__a", "g"),
        ("Completa: oxí__eno", "g"),
        ("Completa: ale__énico", "g"),
        ("Completa: an__élico", "g"),
        ("Completa: estrate__ia", "g"),
        ("Completa: pro__enitor", "g"),
        ("Completa: vir__en", "g")
    ]

    print("\n🧪 Completa las palabras escribiendo la letra correcta (g o j):\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta (g/j): ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ La respuesta correcta era: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Usas correctamente la letra g con estos sufijos.")
    else:
        print("🔁 Sigue practicando. ¡Tú puedes lograrlo!")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_022()
