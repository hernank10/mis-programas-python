def leccion_057():
    print("\n📘 Lección 057 – Uso correcto de oraciones impersonales\n")

    teoria = """✍️ Regla gramatical:

✅ Las oraciones impersonales no tienen un sujeto concreto. El verbo aparece en tercera persona singular.

📌 Tipos comunes:

1. **Fenómenos naturales**:
   – Llueve mucho en esta ciudad.
   – Amaneció nublado.

2. **Con 'se' impersonal**:
   – Se vive bien en este barrio.
   – Se trabaja mucho aquí.

3. **Con verbos como 'haber', 'hacer', 'ser' en uso impersonal**:
   – Hay muchos problemas. ❗ Nunca: *habían muchos problemas*
   – Hace frío.
   – Es tarde.

❌ Error común:
– *Habían muchas personas* → debe ser *Había muchas personas*
"""

    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ Llueve desde la madrugada.",
        "✅ Se dice que habrá cambios.",
        "✅ Hay varias opciones disponibles.",
        "❌ Habían muchas quejas. → debe ser: Había muchas quejas."
    ]

    print("\n✍️ Ejemplos correctos e incorrectos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("_____ muchos errores en el examen.", "Había"),
        ("_____ frío en la mañana.", "Hace"),
        ("_____ tarde para salir.", "Es"),
        ("_____ que tener paciencia.", "Hay"),
        ("En esta zona _____ mucho.", "llueve"),
        ("_____ bien en este lugar.", "Se vive"),
        ("_____ hambre después de la clase.", "Hay"),
        ("_____ tiempo para estudiar.", "Hay"),
        ("_____ rumores sobre el tema.", "Se escuchan"),
        ("No _____ nadie en la casa.", "había")
    ]

    print("\n🧪 Escribe la forma correcta del verbo en cada oración (responde en minúsculas):\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {respuesta_correcta}")

    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Manejas bien las oraciones impersonales.")
    else:
        print("🔁 Sigue practicando. Este tema es esencial en redacción académica.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_057()
