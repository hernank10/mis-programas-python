def leccion_042():
    print("\n📘 Lección 042 – Uso del punto y coma (;)\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:

✅ El **punto y coma (;)** se usa para:

1. Separar oraciones relacionadas que ya contienen comas:
   – Compramos lápices, bolígrafos y borradores; cuadernos, carpetas y reglas.

2. Separar oraciones independientes pero estrechamente relacionadas:
   – María estudió toda la noche; Pedro, en cambio, salió a jugar.

3. Antes de conectores adversativos o consecutivos:
   – Quería venir; sin embargo, no pudo.
   – No fue puntual; por lo tanto, no presentó el examen.

📌 Consejo: El punto y coma es una pausa **mayor que la coma**, pero **menor que el punto**.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ A Juan le gusta el cine; a Ana, el teatro.",
        "✅ Llovía fuerte; sin embargo, salimos a caminar.",
        "❌ Ella estudió mucho, sin embargo aprobó. (falta punto y coma)"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: completar con punto y coma o coma
    ejercicios = [
        ("Completa: No fui al cine _____ tenía mucha tarea.", ";"),
        ("Completa: El perro, el gato y el conejo estaban quietos _____ los pájaros no paraban de cantar.", ";"),
        ("Completa: José quería hablar _____ nadie lo escuchaba.", ";"),
        ("Completa: Me gustan las frutas: manzanas, peras, uvas _____ también las verduras: lechuga, tomate, zanahoria.", ";"),
        ("Completa: María llegó tarde _____ además, no trajo su tarea.", ";"),
        ("Completa: Le ofrecieron trabajo _____ no lo aceptó.", ";"),
        ("Completa: Aprendí muchas cosas _____ sin embargo, sigo practicando.", ";"),
        ("Completa: Los niños jugaban, gritaban, reían _____ los adultos los observaban.", ";"),
        ("Completa: Me gusta el español _____ no tanto las matemáticas.", ";"),
        ("Completa: El alumno fue respetuoso _____ fue escuchado con atención.", ";")
    ]

    print("\n🧪 Escribe el signo de puntuación que falta en cada oración: (escribe solo ';')\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta.replace('_____', '_____')}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == response := respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ La respuesta correcta era: {response}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Usas correctamente el punto y coma.")
    else:
        print("🔁 Intenta una vez más. Es importante dominar esta regla.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_042()
