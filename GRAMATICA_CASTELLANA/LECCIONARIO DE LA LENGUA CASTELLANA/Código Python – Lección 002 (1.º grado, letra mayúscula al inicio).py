def leccion_002():
    print("\n📘 Lección 002 – Uso de la letra mayúscula al comenzar una oración\n")

    # Mostrar teoría
    teoria = """✍️ Toda oración debe comenzar con letra mayúscula.

📌 Ejemplos:
- ✅ El perro ladra.
- ✅ Mi mamá cocina.
- ❌ mi gato duerme. (debe comenzar con mayúscula)
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ La niña corre.",
        "✅ Hoy hace sol.",
        "❌ el carro es rojo.",
        "❌ mi casa es grande."
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: el estudiante debe corregir oraciones que no empiezan con mayúscula
    ejercicios = [
        ("Corrige la oración: el perro corre.", "El perro corre."),
        ("Corrige: mi mamá cocina arroz.", "Mi mamá cocina arroz."),
        ("Corrige: la casa es verde.", "La casa es verde."),
        ("Corrige: juan tiene un gato.", "Juan tiene un gato."),
        ("Corrige: en la escuela hay libros.", "En la escuela hay libros."),
        ("Corrige: maria canta bien.", "Maria canta bien."),
        ("Corrige: el sol brilla fuerte.", "El sol brilla fuerte."),
        ("Corrige: mis amigos juegan fútbol.", "Mis amigos juegan fútbol."),
        ("Corrige: un pájaro canta.", "Un pájaro canta."),
        ("Corrige: los niños leen cuentos.", "Los niños leen cuentos.")
    ]

    print("\n🧪 Corrige estas oraciones escribiéndolas con la primera letra en mayúscula:\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == respuesta_correcta:
            print("✅ ¡Muy bien!")
            correctas += 1
        else:
            print(f"❌ Casi. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Ya sabes cómo comenzar una oración con mayúscula.")
    else:
        print("🔁 Intenta otra vez. Practicar te ayudará a recordar.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_002()
