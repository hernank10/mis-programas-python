def leccion_001():
    print("\n📘 Lección 001 – Uso de la M antes de B y P\n")

    # Mostrar teoría
    teoria = """En español, cuando una palabra contiene una letra B o P precedida de otra consonante,
esa consonante debe ser M, no N.
✅ Se escribe: 'tambor', 'compás', 'empleado', 'importante'.
❌ No se escribe: 'tanbor', 'conpás', 'inportante'.
Esta regla mejora la pronunciación de las palabras."""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["tambor", "compás", "también", "empleo", "impresión", "complicado", "empezar", "importante"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Lista de ejercicios
    ejercicios = [
        ("¿Cuál palabra está bien escrita?\n1. enpezar\n2. empezar", "2"),
        ("Selecciona la opción correcta:\n1. tanbien\n2. también", "2"),
        ("¿Cómo se escribe correctamente?\n1. inportante\n2. importante", "2"),
        ("¿Cuál es la forma correcta?\n1. compás\n2. conpás", "1"),
        ("¿Qué palabra está bien escrita?\n1. impiar\n2. limpiar", "2"),
        ("Elige la palabra escrita correctamente:\n1. tambor\n2. tanbor", "1"),
        ("Selecciona la correcta:\n1. emplear\n2. enplear", "1"),
        ("¿Cuál es la forma correcta?\n1. imitar\n2. initar", "1"),
        ("¿Qué palabra está escrita correctamente?\n1. embudo\n2. enbudo", "1"),
        ("Elige la opción correcta:\n1. amparo\n2. anparo", "1"),
        ("¿Cómo se escribe correctamente?\n1. campana\n2. canpana", "1"),
        ("Selecciona la palabra correcta:\n1. romper\n2. ronper", "1"),
        ("¿Cuál está bien escrita?\n1. campeón\n2. canpeón", "1"),
        ("Selecciona la opción correcta:\n1. compadre\n2. conpadre", "1"),
        ("¿Qué palabra es correcta?\n1. compilar\n2. conpilar", "1"),
        ("Selecciona la forma correcta:\n1. temprano\n2. tenprano", "1"),
        ("Elige la palabra correcta:\n1. impresionante\n2. inpresionante", "1"),
        ("¿Cuál es la forma correcta?\n1. campeón\n2. canpeón", "1"),
        ("¿Qué palabra está bien escrita?\n1. comprar\n2. conprar", "1"),
        ("Selecciona la opción correcta:\n1. empleo\n2. enpleo", "1")
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
    leccion_001()
