def leccion_016():
    print("\n📘 Lección 016 – Uso correcto de la letra H\n")

    # Mostrar teoría
    teoria = """La H es una letra muda, pero es muy importante en la escritura. Estas son algunas reglas:

🟨 Se escribe con H:
- Las palabras que empiezan con hum- (ej. humano, humilde).
- Los verbos haber, hacer, hallar y hablar, y sus formas derivadas.
- Las palabras que empiezan con hie-, hue- (hielo, huevo), salvo excepciones como 'uello'.

📌 Aunque no se pronuncia, su omisión es un error ortográfico. Se aprende con práctica y lectura frecuente.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["hablar", "humano", "huevo", "hielo", "hacer", "hecho", "hallar", "hermano"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Lista de ejercicios (enunciado, respuesta correcta)
    ejercicios = [
        ("¿Cómo se escribe correctamente: hablar o ablar?", "hablar"),
        ("¿Cuál palabra es correcta: umano o humano?", "humano"),
        ("¿Qué palabra está bien escrita: huevo o uevo?", "huevo"),
        ("¿Cuál es la forma correcta: hecho o echo (verbo hacer)?", "hecho"),
        ("¿Cómo se escribe bien: hielo o ielo?", "hielo"),
        ("¿Qué forma es correcta: hacer o acer?", "hacer"),
        ("¿Cuál es correcta: hallar o ayar?", "hallar"),
        ("¿Qué palabra es correcta: herida o erida?", "herida"),
        ("¿Cuál es la forma correcta: héroe o éroe?", "héroe"),
        ("¿Cómo se escribe correctamente: humedad o umedad?", "humedad"),
        ("¿Cuál está bien escrita: hablaban o ablabán?", "hablaban"),
        ("¿Qué palabra es correcta: hospital o ospital?", "hospital"),
        ("¿Cuál se escribe correctamente: humilde o umilde?", "humilde"),
        ("¿Cómo se escribe bien: hervir o ervir?", "hervir"),
        ("¿Qué palabra es correcta: hecho o eecho?", "hecho"),
        ("¿Cuál es correcta: hielo o hiele?", "hielo"),
        ("¿Qué palabra es correcta: huésped o uésped?", "huésped"),
        ("¿Cómo se escribe bien: herencia o erencia?", "herencia"),
        ("¿Qué palabra es correcta: harina o arina?", "harina"),
        ("¿Cuál forma es correcta: historia o istoria?", "historia")
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
    leccion_016()
