def leccion_006():
    print("\n📘 Lección 006 – Uso correcto de la B y la V\n")

    # Mostrar teoría
    teoria = """En español, muchas palabras suenan igual con B o V, pero solo una forma es correcta.

🟦 Se escribe con B:
- después de M (como en 'embudo')
- en las terminaciones -bilidad, -bundo

🟩 Se escribe con V:
- después de N (como en 'invierno')
- en las terminaciones -ivo, -iva

💡 Esta regla se aprende con lectura, atención y práctica constante."""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["barco", "vivir", "invierno", "embudo", "valiente", "bueno", "nube", "novio"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Lista de ejercicios: pregunta, palabra correcta (sin opciones)
    ejercicios = [
        ("Escribe la palabra correctamente: invitar o imbitar", "invitar"),
        ("Escribe correctamente: bebesidad o obesidad", "obesidad"),
        ("Escribe correctamente: bevido o bebido", "bebido"),
        ("¿Cuál es la forma correcta: invierno o imvierno?", "invierno"),
        ("¿Cuál es correcta: vienes o bienes?", "bienes"),
        ("¿Cuál es correcta: buelo o vuelo?", "vuelo"),
        ("¿Cómo se escribe correctamente: vaca o baca?", "vaca"),
        ("¿Cuál es la palabra correcta: avlar o hablar?", "hablar"),
        ("¿Cuál es la forma correcta: buelo o abuelo?", "abuelo"),
        ("¿Qué palabra es correcta: escribir o escrivir?", "escribir"),
        ("¿Cómo se escribe bien: valiente o baliente?", "valiente"),
        ("¿Cuál es correcta: bever o beber?", "beber"),
        ("¿Cuál es la forma correcta: biblioteca o vivlioteca?", "biblioteca"),
        ("¿Cómo se escribe bien: bamos o vamos?", "vamos"),
        ("¿Cuál es la correcta: bicicleta o vizicleta?", "bicicleta"),
        ("¿Cuál es correcta: embestida o envestida?", "embestida"),
        ("¿Qué palabra es correcta: balor o valor?", "valor"),
        ("¿Cuál es correcta: vivir o bibir?", "vivir"),
        ("¿Qué palabra es correcta: lavabo o lavavo?", "lavabo"),
        ("¿Cuál se escribe bien: buelta o vuelta?", "vuelta")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe la palabra correcta):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Calcular resultado
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has superado la lección con éxito.")
    else:
        print("🔁 Sigue practicando. Puedes volver a intentarlo.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_006()
