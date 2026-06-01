def leccion_056():
    print("\n📘 Lección 056 – Coherencia y cohesión textual: conectores y puntuación\n")

    # Mostrar teoría
    teoria = """✍️ Coherencia y cohesión textual

🔹 Coherencia:
– La relación lógica entre ideas. El texto debe tener sentido global.
– Ejemplo: Primero se presenta un problema, luego se explica, y finalmente se ofrece una solución.

🔸 Cohesión:
– Se logra mediante el uso correcto de conectores, pronombres, puntuación y orden de ideas.
– Conectores comunes:

👉 Causa: porque, ya que, debido a que  
👉 Consecuencia: por lo tanto, así que, en consecuencia  
👉 Contraste: sin embargo, aunque, no obstante  
👉 Adición: además, también, incluso  
👉 Ejemplificación: por ejemplo, en particular  
👉 Orden: primero, luego, finalmente  

📌 Una buena puntuación ayuda a separar ideas, evitar ambigüedad y guiar al lector.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "Estudié mucho, por lo tanto, aprobé el examen.",
        "Aunque estaba cansado, siguió trabajando.",
        "No solo estudió, sino que también ayudó a sus compañeros.",
        "Primero explicaremos la teoría, luego pasaremos a los ejercicios."
    ]
    print("\n✍️ Ejemplos de uso correcto de conectores:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("Completa la oración con un conector adecuado: Estaba lloviendo, ___ salimos a caminar.", "sin embargo"),
        ("Completa: No me gustan las matemáticas; ___, debo estudiarlas.", "sin embargo"),
        ("Completa: Llegó tarde ___ había mucho tráfico.", "porque"),
        ("Completa: No lo logró, ___ lo intentó varias veces.", "aunque"),
        ("Completa: No solo llegó temprano, ___ trajo regalos.", "sino que"),
        ("Completa: No estudió, ___ reprobó el examen.", "por lo tanto"),
        ("Completa: ___, veremos los conceptos básicos.", "Primero"),
        ("Completa: Fue un día largo; ___, muy productivo.", "sin embargo"),
        ("Completa: Está lloviendo mucho, ___ no iremos al parque.", "por lo tanto"),
        ("Completa: No lo entendí, ___ lo repetí varias veces.", "así que"),
        ("Completa: Me encanta leer; ___, me gusta escribir.", "además"),
        ("Completa: Perdí el autobús, ___ llegué tarde a clase.", "por eso"),
        ("Completa: ___ hace frío, saldré a correr.", "Aunque"),
        ("Completa: Estudió toda la noche, ___ no aprobó.", "pero"),
        ("Completa: Le gusta el café, ___ no el té.", "pero"),
        ("Completa: ___ de la tormenta, viajaron igual.", "A pesar"),
        ("Completa: Lo hizo bien, ___ no ganó el concurso.", "aunque"),
        ("Completa: ___ estaba nervioso, habló con claridad.", "Aunque"),
        ("Completa: ___, revisaremos las preguntas frecuentes.", "Finalmente"),
        ("Completa: Dijo que vendría; ___, no llegó.", "sin embargo")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe el conector correcto según el contexto):")
    correctas = 0

    for i, (pregunta, respuesta_correcta) in enumerate(ejercicios, 1):
        print(f"\n{i}. {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta.lower():
            print("✅ ¡Correcto!")
            correctas += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

    # Resultado final
    porcentaje = (correctas / len(ejercicios)) * 100
    print(f"\n🎯 Resultado final: {correctas}/20 correctas ({porcentaje:.2f}%)")
    if porcentaje >= 80:
        print("🏆 ¡Excelente! Has demostrado dominio en la cohesión y puntuación textual.")
    else:
        print("🔁 Intenta de nuevo. La práctica te ayudará a escribir con mayor claridad.")

# Ejecutar directamente
if __name__ == "__main__":
    leccion_056()
