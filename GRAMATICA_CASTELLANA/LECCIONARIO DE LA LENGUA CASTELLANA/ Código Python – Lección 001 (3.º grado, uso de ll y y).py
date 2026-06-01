def leccion_011():
    print("\n📘 Lección 011 – Uso correcto de LL y Y\n")

    # Mostrar teoría
    teoria = """En español, muchas palabras contienen las letras 'll' o 'y', que suenan igual en algunos dialectos.
Pero no se escriben igual. Aquí algunas reglas generales:

🟡 Se escribe con LL:
- Las palabras que terminan en -illo, -illa (ej. rodilla, pasillo).
- Verbos derivados de 'llevar', 'llover', 'llamar'.

🔵 Se escribe con Y:
- Las formas de los verbos que terminan en -uir (como 'construyó').
- Palabras terminadas en -yec (como 'proyectar').

📌 La mejor forma de aprender es practicar, leer mucho y memorizar algunas excepciones."""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["llave", "camilla", "llover", "huyó", "leyó", "yema", "caballo", "reyes"]
    print("\n✍️ Ejemplos:", ", ".join(ejemplos))

    # Ejercicios: (enunciado, respuesta correcta)
    ejercicios = [
        ("¿Cómo se escribe correctamente: yave o llave?", "llave"),
        ("¿Cuál es correcta: camiya o camilla?", "camilla"),
        ("¿Cuál es la forma correcta: yuvia o lluvia?", "lluvia"),
        ("¿Qué palabra está bien escrita: yamar o llamar?", "llamar"),
        ("¿Cómo se escribe: yema o llema?", "yema"),
        ("¿Cuál es correcta: caballo o cabayo?", "caballo"),
        ("¿Qué forma es correcta: yeno o lleno?", "lleno"),
        ("¿Cuál se escribe bien: apoyó o apolló?", "apoyó"),
        ("¿Cómo se escribe: yegua o llegua?", "yegua"),
        ("¿Cuál es correcta: cayó o calló? (para verbo 'caer')", "cayó"),
        ("¿Cómo se escribe: leyó o lelló?", "leyó"),
        ("¿Cuál es correcta: huyó o hulló?", "huyó"),
        ("¿Qué palabra es correcta: reyes o relleyes?", "reyes"),
        ("¿Cómo se escribe: apoyar o apollar?", "apoyar"),
        ("¿Cuál es la forma correcta: poyo o pollo? (para banco de madera)", "poyo"),
        ("¿Cuál está bien escrita: cuello o cuyeyo?", "cuello"),
        ("¿Qué palabra es correcta: amarillo o amariyo?", "amarillo"),
        ("¿Cómo se escribe bien: desarrolla o desaroya?", "desarrolla"),
        ("¿Cuál se escribe bien: ellos o eyos?", "ellos"),
        ("¿Qué palabra es correcta: llama o yama?", "llama")
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
    leccion_011()
