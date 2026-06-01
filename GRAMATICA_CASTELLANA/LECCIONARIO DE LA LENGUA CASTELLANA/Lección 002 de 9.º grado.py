def leccion_042():
    print("\n📘 Lección 042 – Uso del punto y coma (;)\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:

1. Se usa punto y coma (;) para:
- Separar oraciones relacionadas que ya contienen comas.
- Separar ideas independientes pero relacionadas.
- Antes de conectores: sin embargo, por lo tanto, en cambio, etc.
"""
    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ A Juan le gusta el cine; a Ana, el teatro.",
        "✅ Llovía fuerte; sin embargo, salimos a caminar.",
        "❌ Ella estudió mucho, sin embargo aprobó. (Incorrecto: falta el punto y coma)"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("No fui al cine _____ tenía mucha tarea.", ";"),
        ("José quería hablar _____ nadie lo escuchaba.", ";"),
        ("Me gustan las frutas: manzanas, peras, uvas _____ también las verduras: lechuga, tomate, zanahoria.", ";"),
        ("María llegó tarde _____ además, no trajo su tarea.", ";"),
        ("Le ofrecieron trabajo _____ no lo aceptó.", ";"),
        ("Aprendí muchas cosas _____ sin embargo, sigo practicando.", ";"),
        ("Los niños jugaban, gritaban, reían _____ los adultos los observaban.", ";"),
        ("Me gusta el español _____ no tanto las matemáticas.", ";"),
        ("El alumno fue respetuoso _____ fue escuchado con atención.", ";"),
        ("Comimos pizza, pasta, ensalada _____ bebimos jugo, gaseosa y agua.", ";")
    ]

    print("\n🧪 Completa las siguientes oraciones escribiendo el signo de puntuación adecuado (escribe solo ';'):\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta.replace('_____', '_____')}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ La respuesta correcta era: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has aprendido a usar el punto y coma correctamente.")
    else:
        print("🔁 Intenta una vez más. La práctica hace al maestro.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_042()
