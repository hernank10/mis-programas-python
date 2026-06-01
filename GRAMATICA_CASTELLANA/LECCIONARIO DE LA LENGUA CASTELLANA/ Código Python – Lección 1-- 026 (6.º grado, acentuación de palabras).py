def leccion_026():
    print("\n📘 Lección 026 – Reglas generales de acentuación\n")

    # Mostrar teoría
    teoria = """Las palabras en español se dividen según la sílaba tónica (la que se pronuncia con más fuerza):

🔴 Agudas:
- Llevan tilde si terminan en N, S o vocal.
- Ejemplos: café, balón, compás.

🟠 Llanas (o graves):
- Llevan tilde si NO terminan en N, S o vocal.
- Ejemplos: lápiz, árbol, césped.

🟡 Esdrújulas:
- Siempre llevan tilde.
- Ejemplos: matemática, música, lágrima.

📌 La sílaba tónica y las reglas de terminación determinan si una palabra lleva tilde.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["camión (aguda)", "lápiz (llana)", "música (esdrújula)", "pared (aguda, sin tilde)", "césped (llana con tilde)", "árbol (llana con tilde)"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Ejercicios (pregunta, respuesta_correcta)
    ejercicios = [
        ("¿Qué tipo de palabra es 'camión'?", "aguda"),
        ("¿Qué tipo de palabra es 'lápiz'?", "llana"),
        ("¿Qué tipo de palabra es 'matemática'?", "esdrújula"),
        ("¿Qué tipo de palabra es 'reloj'?", "aguda"),
        ("¿Qué tipo de palabra es 'árbol'?", "llana"),
        ("¿Qué tipo de palabra es 'canción'?", "aguda"),
        ("¿Qué tipo de palabra es 'música'?", "esdrújula"),
        ("¿Qué tipo de palabra es 'avión'?", "aguda"),
        ("¿Qué tipo de palabra es 'césped'?", "llana"),
        ("¿Qué tipo de palabra es 'teléfono'?", "esdrújula"),
        ("¿Qué tipo de palabra es 'sofá'?", "aguda"),
        ("¿Qué tipo de palabra es 'luz'?", "aguda"),
        ("¿Qué tipo de palabra es 'fácil'?", "llana"),
        ("¿Qué tipo de palabra es 'pájaro'?", "esdrújula"),
        ("¿Qué tipo de palabra es 'menú'?", "aguda"),
        ("¿Qué tipo de palabra es 'débil'?", "llana"),
        ("¿Qué tipo de palabra es 'próximo'?", "esdrújula"),
        ("¿Qué tipo de palabra es 'hotel'?", "aguda"),
        ("¿Qué tipo de palabra es 'fútbol'?", "llana"),
        ("¿Qué tipo de palabra es 'lógica'?", "esdrújula")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe aguda, llana o esdrújula):")
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
    leccion_026()
