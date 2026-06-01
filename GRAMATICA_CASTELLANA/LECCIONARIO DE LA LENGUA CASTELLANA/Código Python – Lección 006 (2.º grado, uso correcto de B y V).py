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

    # Lista de ejercicios
    ejercicios = [
        ("¿Cuál palabra está bien escrita?\n1. bebesidad\n2. obesidad", "2"),
        ("Selecciona la correcta:\n1. invitar\n2. imbitar", "1"),
        ("¿Cómo se escribe correctamente?\n1. bevido\n2. bebido", "2"),
        ("¿Qué forma es correcta?\n1. invierno\n2. imvierno", "1"),
        ("¿Cuál palabra es correcta?\n1. vienes\n2. bienes", "2"),
        ("Elige la palabra correcta:\n1. buelo\n2. vuelo", "2"),
        ("¿Cómo se escribe bien?\n1. vaca\n2. baca (para animal)", "1"),
        ("Selecciona la correcta:\n1. avlar\n2. hablar", "2"),
        ("¿Cuál palabra es correcta?\n1. buelo\n2. abuelo", "2"),
        ("¿Cuál está bien escrita?\n1. escribir\n2. escrivir", "1"),
        ("Selecciona la palabra escrita correctamente:\n1. valiente\n2. baliente", "1"),
        ("¿Cuál palabra está bien escrita?\n1. bever\n2. beber", "2"),
        ("¿Cómo se escribe correctamente?\n1. biblioteca\n2. vivlioteca", "1"),
        ("¿Qué palabra es correcta?\n1. bamos\n2. vamos", "2"),
        ("Selecciona la opción correcta:\n1. bicicleta\n2. vizicleta", "1"),
        ("¿Cuál es la forma correcta?\n1. embestida\n2. envestida", "1"),
        ("Selecciona la palabra bien escrita:\n1. balor\n2. valor", "2"),
        ("¿Cómo se escribe bien?\n1. vivir\n2. bibir", "1"),
        ("¿Cuál está correcta?\n1. lavabo\n2. lavavo", "1"),
        ("Elige la palabra correcta:\n1. buelta\n2. vuelta", "2")
    ]

    print("\n🧪 Empecemos los ejercicios (20 preguntas):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {respuesta_correcta}")

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
