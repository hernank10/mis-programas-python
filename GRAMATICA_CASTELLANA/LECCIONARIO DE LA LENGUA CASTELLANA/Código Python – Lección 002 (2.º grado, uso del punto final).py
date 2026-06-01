def leccion_007():
    print("\n📘 Lección 007 – Uso del punto al final de la oración\n")

    # Mostrar teoría
    teoria = """✍️ El punto (.) se usa al final de una oración para indicar que la idea ha terminado.

📌 Tipos de punto:
– Punto final: termina un texto.
– Punto y seguido: separa oraciones en un mismo párrafo.
– Punto y aparte: separa párrafos.

📌 En esta lección practicaremos el uso del punto al final de oraciones simples.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ El gato duerme.",
        "✅ Mi papá cocina arroz.",
        "❌ El perro ladra (falta punto)",
        "❌ Ana canta una canción (falta punto)"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: el estudiante debe corregir oraciones sin punto al final
    ejercicios = [
        ("Corrige la oración: El niño corre", "El niño corre."),
        ("Corrige: La maestra escribe en la pizarra", "La maestra escribe en la pizarra."),
        ("Corrige: Me gusta el helado", "Me gusta el helado."),
        ("Corrige: Juan lee un libro", "Juan lee un libro."),
        ("Corrige: El avión vuela alto", "El avión vuela alto."),
        ("Corrige: Mi abuela cocina bien", "Mi abuela cocina bien."),
        ("Corrige: El sol brilla mucho", "El sol brilla mucho."),
        ("Corrige: Hoy hace calor", "Hoy hace calor."),
        ("Corrige: La niña canta", "La niña canta."),
        ("Corrige: El gato juega", "El gato juega.")
    ]

    print("\n🧪 Corrige estas oraciones escribiéndolas con punto final:\n")
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
        print("🏆 ¡Excelente! Ya sabes usar el punto al final de una oración.")
    else:
        print("🔁 Sigue practicando. Escribe cada oración completa.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_007()
