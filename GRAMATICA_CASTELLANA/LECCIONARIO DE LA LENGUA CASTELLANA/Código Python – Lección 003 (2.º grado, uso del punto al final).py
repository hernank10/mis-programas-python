def leccion_008():
    print("\n📘 Lección 008 – Uso correcto del punto al final de la oración\n")

    teoria = """✍️ Regla ortográfica:

✅ Toda oración enunciativa debe terminar con un **punto (.)**.

📌 Ejemplos correctos:
– Mi gato duerme todo el día.
– Jugamos en el parque.
– El cielo está azul.

❌ Ejemplos incorrectos:
– Mi gato duerme todo el día
– Jugamos en el parque
"""

    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ El sol brilla por la mañana.",
        "✅ Mi hermana canta una canción.",
        "❌ Mi hermana canta una canción → falta el punto."
    ]

    print("\n✍️ Ejemplos correctos e incorrectos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("La maestra lee un cuento", "La maestra lee un cuento."),
        ("El perro ladra fuerte", "El perro ladra fuerte."),
        ("Mi mamá cocina arroz", "Mi mamá cocina arroz."),
        ("Vamos al colegio en bus", "Vamos al colegio en bus."),
        ("El gato corre rápido", "El gato corre rápido."),
        ("Tengo una bicicleta roja", "Tengo una bicicleta roja."),
        ("Nos gusta el helado", "Nos gusta el helado."),
        ("El libro está sobre la mesa", "El libro está sobre la mesa."),
        ("Hoy hace mucho calor", "Hoy hace mucho calor."),
        ("Mi papá maneja un carro azul", "Mi papá maneja un carro azul."),
        ("Comemos frutas en la tarde", "Comemos frutas en la tarde."),
        ("Los pájaros cantan al amanecer", "Los pájaros cantan al amanecer."),
        ("Me gusta dibujar", "Me gusta dibujar."),
        ("Jugamos con los amigos", "Jugamos con los amigos."),
        ("La flor es amarilla", "La flor es amarilla."),
        ("El reloj está en la pared", "El reloj está en la pared."),
        ("Tenemos clase de arte", "Tenemos clase de arte."),
        ("El bebé duerme tranquilo", "El bebé duerme tranquilo."),
        ("Hoy vamos al zoológico", "Hoy vamos al zoológico."),
        ("La luna brilla en el cielo", "La luna brilla en el cielo.")
    ]

    print("\n🧪 Corrige las oraciones agregando el punto final (escribe la oración completa):\n")
    correctas = 0

    for i, (incorrecta, correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {incorrecta}")
        respuesta = input("Tu corrección: ").strip()
        if respuesta == correcta:
            print("✅ ¡Muy bien!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {correcta}")

    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏅 ¡Excelente trabajo! Usas el punto correctamente.")
    else:
        print("🔁 Repasa la lección y vuelve a intentarlo. ¡Tú puedes!")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_008()
