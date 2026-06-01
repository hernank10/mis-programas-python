def leccion_031():
    print("\n📘 Lección 031 – Acento diacrítico en monosílabos\n")

    # Mostrar teoría
    teoria = """El acento diacrítico se usa para diferenciar palabras que se escriben igual pero tienen diferente función o significado.

🟦 Ejemplos comunes:

- tú (pronombre) / tu (posesivo)
- él (pronombre) / el (artículo)
- mí (pronombre) / mi (posesivo)
- sí (afirmación o pronombre) / si (condicional)
- más (cantidad) / mas (conjunción)
- sé (del verbo saber o ser) / se (pronombre)
- té (bebida) / te (pronombre)
- sólo (cuando equivale a “solamente”) / solo (sin compañía) [actualmente opcional]

📌 Solo se acentúan cuando hay riesgo de ambigüedad en el significado.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = ["tú eres mi amigo / tu libro está aquí", 
                "él llegó temprano / el niño está jugando", 
                "mí me gusta / mi casa es grande",
                "sí, quiero ir / si vienes, te acompaño",
                "más dinero / mas no lo logró",
                "sé bueno / se cayó",
                "quiero té / te dije que no",
                "estoy solo / sólo quiero descansar"]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("Completa con la palabra correcta: ___ vas a decir algo importante (tú/tu)", "tú"),
        ("Completa: ___ hermano es muy simpático (tú/tu)", "tu"),
        ("Completa: ___ tiene la culpa (él/el)", "él"),
        ("Completa: ___ carro está dañado (el/él)", "el"),
        ("Completa: Quiero ir al cine, ___ no tengo dinero (más/mas)", "mas"),
        ("Completa: No sé si vendrá o ___ se quedará (sí/si)", "si"),
        ("Completa: ___, quiero estudiar medicina (sí/si)", "sí"),
        ("Completa: No lo hagas, ___ valiente (sé/se)", "sé"),
        ("Completa: ¿___ tomaste todo el jugo? (te/té)", "te"),
        ("Completa: Me gusta el ___ verde (té/te)", "té"),
        ("Completa: ___ casa es nueva (mi/mí)", "mi"),
        ("Completa: Esto es para ___ (mi/mí)", "mí"),
        ("Completa: Él vive ___ (solo/sólo)", "solo"),
        ("Completa: ___ quiero saber la verdad (solo/sólo)", "sólo"),
        ("Completa: ___ gusta el chocolate (te/té)", "te"),
        ("Completa: ¿Quieres ___? (te/té)", "té"),
        ("Completa: ___ gato duerme mucho (el/él)", "el"),
        ("Completa: ___ llegaré a tiempo (sé/se)", "sé"),
        ("Completa: ___ cayó del columpio (sé/se)", "se"),
        ("Completa: ___ libro está en la mesa (tu/tú)", "tu")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe la palabra correcta):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Muy bien! Has superado la lección con éxito.")
    else:
        print("🔁 Sigue practicando. Puedes volver a intentarlo.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_031()
