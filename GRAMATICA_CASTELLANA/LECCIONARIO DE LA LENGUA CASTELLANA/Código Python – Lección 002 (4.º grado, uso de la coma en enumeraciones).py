def leccion_017():
    print("\n📘 Lección 017 – Uso de la coma para enumerar elementos\n")

    # Mostrar teoría
    teoria = """✍️ Regla ortográfica:
✅ La coma se usa para separar elementos dentro de una enumeración.

📌 Ejemplo:
– Compré manzanas, peras, uvas y plátanos.

📌 No se pone coma antes de la conjunción final "y" en español estándar:
– Correcto: Compré lápices, cuadernos y colores.
– Incorrecto: Compré lápices, cuadernos, y colores. (coma innecesaria)
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "✅ Me gustan los perros, los gatos y los conejos.",
        "✅ Traje papel, tijeras, pegamento y colores.",
        "❌ Compré leche pan queso. → Falta comas.",
        "❌ Vi a Ana Luis Pedro y María. → Sin comas, hay confusión."
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios: el estudiante debe escribir la oración usando correctamente las comas
    ejercicios = [
        ("Corrige con comas: Compré manzanas peras uvas y melones.", "Compré manzanas, peras, uvas y melones."),
        ("Corrige: Vi a Juan Pedro María y Ana.", "Vi a Juan, Pedro, María y Ana."),
        ("Corrige: Me gusta pintar correr leer y cantar.", "Me gusta pintar, correr, leer y cantar."),
        ("Corrige: Necesito lápiz goma sacapuntas y cuaderno.", "Necesito lápiz, goma, sacapuntas y cuaderno."),
        ("Corrige: Ellos comen arroz pollo ensalada y pan.", "Ellos comen arroz, pollo, ensalada y pan."),
        ("Corrige: En la mochila hay libros cuadernos y carpetas.", "En la mochila hay libros, cuadernos y carpetas."),
        ("Corrige: Visitamos Bogotá Medellín Cali y Cartagena.", "Visitamos Bogotá, Medellín, Cali y Cartagena."),
        ("Corrige: Mis amigos son Luis Marcos Sofía y Carla.", "Mis amigos son Luis, Marcos, Sofía y Carla."),
        ("Corrige: Traje azul rojo verde y negro.", "Traje azul, rojo, verde y negro."),
        ("Corrige: Comimos sopa carne arroz y fruta.", "Comimos sopa, carne, arroz y fruta.")
    ]

    print("\n🧪 Corrige estas oraciones añadiendo comas en el lugar correcto:\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == respuesta_correcta:
            print("✅ ¡Muy bien!")
            correctas += 1
        else:
            print(f"❌ La forma correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Ya sabes cómo usar la coma para enumerar.")
    else:
        print("🔁 Intenta otra vez y mejora tu puntuación.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_017()
