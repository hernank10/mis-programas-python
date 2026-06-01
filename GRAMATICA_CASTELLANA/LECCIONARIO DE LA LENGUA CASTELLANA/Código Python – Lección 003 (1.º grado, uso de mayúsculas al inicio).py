def leccion_003():
    print("\n📘 Lección 003 – Uso de la mayúscula al inicio de una oración\n")

    teoria = """✍️ Regla ortográfica:

✅ Toda oración debe comenzar con letra **mayúscula**.

📌 Ejemplos:
– **La casa es grande.**
– **Mi mamá cocina arroz.**
– **Hoy vamos a jugar.**

❌ No se debe comenzar con minúscula:
– *la casa es grande.* (Incorrecto)
– *mi mamá cocina arroz.* (Incorrecto)
"""

    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ El sol brilla.",
        "✅ Mi perro es blanco.",
        "❌ mi perro es blanco. → debe ser: Mi perro es blanco."
    ]

    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("la niña canta.", "La niña canta."),
        ("mi papá trabaja.", "Mi papá trabaja."),
        ("el gato duerme.", "El gato duerme."),
        ("juan juega fútbol.", "Juan juega fútbol."),
        ("vamos al parque.", "Vamos al parque."),
        ("mi abuela cocina.", "Mi abuela cocina."),
        ("el perro ladra.", "El perro ladra."),
        ("lucía lee un libro.", "Lucía lee un libro."),
        ("tengo una bicicleta.", "Tengo una bicicleta."),
        ("hoy hace calor.", "Hoy hace calor.")
    ]

    print("\n🧪 Corrige las oraciones escribiendo la primera palabra con mayúscula:\n")
    correctas = 0

    for i, (frase, solucion) in enumerate(ejercicios, 1):
        print(f"{i}. {frase}")
        respuesta = input("Tu corrección: ").strip()
        if respuesta == solucion:
            print("✅ ¡Muy bien!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {solucion}")

    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏅 ¡Excelente! Ya sabes cuándo usar la mayúscula al comenzar una oración.")
    else:
        print("🔁 Intenta de nuevo. ¡La práctica hace al maestro!")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_003()
