def leccion_047():
    print("\n📘 Lección 047 – Concordancia gramatical entre sujeto y verbo\n")

    teoria = """✍️ Regla gramatical:

✅ El verbo debe concordar en número (singular/plural) y persona con el sujeto de la oración.

📌 Ejemplos:
– El perro **ladra**. ✅ (sujeto singular → verbo en singular)
– Los estudiantes **escriben** cartas. ✅ (sujeto plural → verbo en plural)
– Tú **eres** muy amable. ✅ (segunda persona singular)

❌ Errores comunes:
– *Los niños juega fútbol.* ❌ → debe ser *juegan*
– *Mi familia son muy unida.* ❌ → debe ser *es muy unida*
"""

    print("📚 Teoría:\n" + teoria)

    ejemplos = [
        "✅ La maestra explica la lección.",
        "✅ Mis amigos viajan mucho.",
        "❌ Los alumnos entrega las tareas. → entrega → entregan"
    ]

    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    ejercicios = [
        ("El niño _____ rápido.", "corre"),
        ("Los pájaros _____ por el cielo.", "vuelan"),
        ("Mi hermana _____ cartas a sus amigas.", "escribe"),
        ("Las chicas _____ al mismo ritmo.", "corren"),
        ("Tú _____ bien en los exámenes.", "respondes"),
        ("Nosotros _____ muy felices hoy.", "estamos"),
        ("Mi madre y yo _____ la cena juntas.", "preparamos"),
        ("Ella _____ muy concentrada en clase.", "está"),
        ("Mis amigos _____ fútbol los domingos.", "juegan"),
        ("El profesor _____ ejercicios difíciles.", "propone")
    ]

    print("\n🧪 Escribe la forma correcta del verbo en cada oración:\n")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {respuesta_correcta}")

    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado: {correctas}/10 correctas ({porcentaje:.0f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente dominio de la concordancia gramatical!")
    else:
        print("🔁 Revisa la lección y vuelve a intentarlo.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_047()
