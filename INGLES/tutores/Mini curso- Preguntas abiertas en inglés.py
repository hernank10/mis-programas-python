# Mini curso interactivo en Python para practicar preguntas abiertas en inglés

def mostrar_regla(nivel):
    reglas = {
        1: "🔹 Nivel 1 – Pronombres + to be\nUsa el verbo 'to be' antes del pronombre para formar preguntas simples.\nEj: Is he? / Are they?",
        2: "🔸 Nivel 2 – Pronombres + to be + sustantivos comunes\nAgrega profesiones, parentescos o grupos con artículos y posesivos.\nEj: Is he a teacher? / Is she your sister?",
        3: "🔶 Nivel 3 – Pronombres + to be + sustantivos compuestos o abstractos\nUsa frases más largas con sustantivos complejos o ideas abstractas.\nEj: Is she a software developer? / Is she a hope for the family?"
    }
    print("\n📘 Regla del nivel:")
    print(reglas.get(nivel, "Nivel no disponible."))

def obtener_ejercicios(nivel):
    ejercicios = {
        1: [
            {"pista": "¿Es él?", "respuesta": "Is he?"},
            {"pista": "¿Son ellos?", "respuesta": "Are they?"}
        ],
        2: [
            {"pista": "¿Es él un maestro?", "respuesta": "Is he a teacher?"},
            {"pista": "¿Es ella tu hermana?", "respuesta": "Is she your sister?"}
        ],
        3: [
            {"pista": "¿Es ella una desarrolladora de software?", "respuesta": "Is she a software developer?"},
            {"pista": "¿Es ella una esperanza para la familia?", "respuesta": "Is she a hope for the family?"}
        ]
    }
    return ejercicios.get(nivel, [])

def practicar_ejercicios(nivel):
    ejercicios = obtener_ejercicios(nivel)
    print(f"\n🧪 Ejercicios del Nivel {nivel}:")
    for i, ej in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}:")
        print(f"Pista: {ej['pista']}")
        respuesta = input("✍️ Escribe la pregunta en inglés: ").strip()
        if respuesta.lower() == ej['respuesta'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta esperada era: {ej['respuesta']}")

def menu_principal():
    while True:
        print("\n🎓 Mini curso: Preguntas abiertas en inglés")
        print("1. Nivel 1 – Pronombres + to be")
        print("2. Nivel 2 – + Sustantivos comunes")
        print("3. Nivel 3 – + Sustantivos compuestos / abstractos")
        print("4. Salir")

        opcion = input("Selecciona un nivel (1-4): ").strip()

        if opcion == "4":
            print("👋 ¡Gracias por aprender! Hasta la próxima.")
            break
        elif opcion in ["1", "2", "3"]:
            nivel = int(opcion)
            mostrar_regla(nivel)
            practicar_ejercicios(nivel)
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
