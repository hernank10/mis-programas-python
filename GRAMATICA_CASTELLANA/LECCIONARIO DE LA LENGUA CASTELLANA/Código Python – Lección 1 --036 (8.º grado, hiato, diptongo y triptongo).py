def leccion_036():
    print("\n📘 Lección 036 – Hiato, diptongo y triptongo con acentuación\n")

    # Mostrar teoría
    teoria = """Cuando dos o tres vocales se agrupan en una palabra, pueden formar:

🔵 Diptongo:
- Unión de una vocal cerrada (i, u) y una abierta (a, e, o) o dos cerradas distintas.
- Ejemplos: tierra, aire, causa.
- Si la vocal cerrada lleva tilde, se rompe el diptongo y forma un hiato.

🟠 Hiato:
- Dos vocales contiguas se pronuncian en sílabas distintas.
- Se forma con dos vocales abiertas, o con una cerrada tónica acentuada + vocal abierta.
- Ejemplos: poesía, país, aéreo.

🟢 Triptongo:
- Tres vocales en una misma sílaba: cerrada + abierta + cerrada (en ese orden).
- Ejemplos: Uruguay, estudiáis, buey.

📌 La acentuación depende de las reglas generales (aguda, llana, esdrújula), y si hay hiato, puede requerir tilde aún sin las reglas tradicionales.
"""
    print("📚 Teoría:\n" + teoria)

    # Mostrar ejemplos
    ejemplos = [
        "diptongo: cielo, causa, tierra", 
        "hiato: país, aéreo, poesía", 
        "triptongo: estudiáis, buey, Uruguay"
    ]
    print("\n✍️ Ejemplos:")
    for ejemplo in ejemplos:
        print("–", ejemplo)

    # Ejercicios
    ejercicios = [
        ("¿Qué es 'cielo'? (hiato/diptongo/triptongo)", "diptongo"),
        ("¿Qué es 'país'?", "hiato"),
        ("¿Qué es 'buey'?", "triptongo"),
        ("¿Qué es 'poesía'?", "hiato"),
        ("¿Qué es 'aéreo'?", "hiato"),
        ("¿Qué es 'tierra'?", "diptongo"),
        ("¿Qué es 'Uruguay'?", "triptongo"),
        ("¿Qué es 'cuidado'?", "diptongo"),
        ("¿Qué es 'limpiáis'?", "triptongo"),
        ("¿Qué es 'reír'?", "hiato"),
        ("¿Qué es 'caída'?", "hiato"),
        ("¿Qué es 'estudiais'?", "triptongo"),
        ("¿Qué es 'continúa'?", "hiato"),
        ("¿Qué es 'aula'?", "diptongo"),
        ("¿Qué es 'vio'?", "diptongo"),
        ("¿Qué es 'héroe'?", "hiato"),
        ("¿Qué es 'averiguáis'?", "triptongo"),
        ("¿Qué es 'ruido'?", "diptongo"),
        ("¿Qué es 'baúl'?", "hiato"),
        ("¿Qué es 'despreciéis'?", "triptongo")
    ]

    print("\n🧪 Empecemos los ejercicios (escribe hiato, diptongo o triptongo):")
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
    leccion_036()
