def leccion_012():
    print("\n📘 Lección 012 – Uso de la 'b' en verbos terminados en -bir\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:
✅ Los verbos terminados en -bir se escriben con **b**, excepto:
    – hervir, servir y vivir (y sus derivados).
    
🟢 Ejemplos correctos con "b":
- Escribir, recibir, concebir, subir, describir.

🔴 Excepciones que se escriben con "v":
- Vivir, hervir, servir.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ Voy a escribir una carta.",
        "✅ Ellos deben recibir el paquete.",
        "❌ El niño va a *ervir* la sopa. (debe ser 'hervir', con v)",
        "❌ Ella quiere *subir* la montaña. ✅ (correcto con b)"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: el estudiante debe completar con "b" o "v"
    ejercicios = [
        ("Completa correctamente: Ella va a escri__ir una carta.", "b"),
        ("Completa: El niño va a reci__ir un regalo.", "b"),
        ("Completa: Vamos a con__ivir con alegría.", "b"),
        ("Completa: El arroz empieza a her__ir.", "v"),
        ("Completa: Quiero su__ir a la montaña.", "b"),
        ("Completa: Vamos a descri__ir lo que vimos.", "b"),
        ("Completa: El médico va a prescri__ir un remedio.", "b"),
        ("Completa: Voy a vi__ir en otro país.", "v"),
        ("Completa: El chef va a ser__ir la comida.", "v"),
        ("Completa: El autor quiere reescri__ir el texto.", "b")
    ]

    print("\n🧪 Completa las palabras escribiendo la letra correcta (b o v):\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta (b/v): ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has aprendido esta regla de ortografía.")
    else:
        print("🔁 Practica un poco más. Puedes repetir la lección.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_012()
