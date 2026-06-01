def leccion_027():
    print("\n📘 Lección 027 – Uso de la letra 'h' en hie-, hue-, hum-\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:
✅ Llevan **h** al comienzo las palabras que inician con:

– hie- (hielo, hierba, hiena)  
– hue- (huevo, hueso, huérfano)  
– hum- (humano, humilde, humedad)

⚠️ Algunas excepciones: oler, ojal, órfano (sin h)
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ hielo, hierba, huevo, hueso, huérfano, humano, humilde",
        "❌ ielo (por hielo), ueso (por hueso), umano (por humano)"
    ]
    print("\n✍️ Ejemplos correctos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: completar con “h” o sin “h” según la regla
    ejercicios = [
        ("Completa: __ielo", "h"),
        ("Completa: __uevo", "h"),
        ("Completa: __ierba", "h"),
        ("Completa: __umano", "h"),
        ("Completa: __ueso", "h"),
        ("Completa: __uérfano", "h"),
        ("Completa: __umilde", "h"),
        ("Completa: __umedad", "h"),
        ("Completa: __iena", "h"),
        ("Completa: __ierro (por hierro)", "h")
    ]

    print("\n🧪 Completa las palabras con la letra correcta (escribe 'h' si la lleva o deja vacío si no):\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ La forma correcta era con '{respuesta_correcta}'")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Ya sabes cuándo usar la h en hie-, hue-, hum-")
    else:
        print("🔁 Sigue practicando. Lo harás excelente la próxima vez.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_027()
