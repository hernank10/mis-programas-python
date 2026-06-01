def leccion_051():
    print("\n📘 Lección 051 – Concordancia gramatical: sujeto-verbo y sustantivo-adjetivo\n")

    # Mostrar teoría
    teoria = """La concordancia gramatical es la correspondencia correcta entre las partes de una oración.

🔷 Sujeto – Verbo:
- El verbo debe concordar con el sujeto en número (singular/plural) y persona (1.ª, 2.ª, 3.ª).
- Ejemplo: Ella **canta** / Ellas **cantan**

🔶 Sustantivo – Adjetivo:
- El adjetivo debe concordar con el sustantivo al que califica, en género (masculino/femenino) y número.
- Ejemplo: El niño **alegre** / Las niñas **alegres**

📌 La falta de concordancia gramatical genera errores comunes de redacción.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "El perro negro corre rápido. ✅",
        "Las flores rojas perfuman el ambiente. ✅",
        "Yo estudio / Nosotros estudiamos. ✅",
        "El niño están cansados. ❌ (verbo mal conjugado)",
        "La casa bonitos. ❌ (adjetivo no concuerda)"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("Corrige la oración: El profesor explicaron bien.", "El profesor explicó bien."),
        ("Corrige la oración: Los niños juega en el parque.", "Los niños juegan en el parque."),
        ("Corrige la oración: La niña son feliz.", "La niña es feliz."),
        ("Corrige la oración: El perro y el gato corre.", "El perro y el gato corren."),
        ("Corrige la oración: El coche rojas está dañado.", "El coche rojo está dañado."),
        ("Corrige la oración: Las mesas es grandes.", "Las mesas son grandes."),
        ("Corrige la oración: Tú habla mucho.", "Tú hablas mucho."),
        ("Corrige la oración: Nosotros come pizza.", "Nosotros comemos pizza."),
        ("Corrige la oración: El problema están resuelto.", "El problema está resuelto."),
        ("Corrige la oración: La casa bonito y grande.", "La casa bonita y grande."),
        ("Corrige la oración: Ellas camina juntas.", "Ellas caminan juntas."),
        ("Corrige la oración: El árbol y la flor es bellos.", "El árbol y la flor son bellos."),
        ("Corrige la oración: El estudiante y su amiga estudia juntos.", "El estudiante y su amiga estudian juntos."),
        ("Corrige la oración: María y Juan está felices.", "María y Juan están felices."),
        ("Corrige la oración: El lápiz son nuevos.", "El lápiz es nuevo."),
        ("Corrige la oración: Mis amigos tiene mucha tarea.", "Mis amigos tienen mucha tarea."),
        ("Corrige la oración: La señora y su hija es amable.", "La señora y su hija son amables."),
        ("Corrige la oración: Yo vamos a la biblioteca.", "Yo voy a la biblioteca."),
        ("Corrige la oración: Usted saben la respuesta.", "Usted sabe la respuesta."),
        ("Corrige la oración: Esos libros es interesantes.", "Esos libros son interesantes.")
    ]

    print("\n🧪 Empecemos los ejercicios (reescribe la oración correctamente):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Dominas la concordancia gramatical.")
    else:
        print("🔁 Sigue practicando. La concordancia es esencial en la buena escritura.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_051()
