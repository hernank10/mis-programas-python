# Programa interactivo para practicar preguntas abiertas en inglés

def mostrar_regla(tipo):
    reglas = {
        "Who": "Usa 'Who' + verbo 'to be' + pronombre para preguntar por identidad.\nEj: Who is she?",
        "What": "Usa 'What' + verbo 'to be' + pronombre para preguntar por profesión o rol.\nEj: What is he?",
        "Where": "Usa 'Where' + verbo 'to be' + pronombre para preguntar por ubicación.\nEj: Where are they?",
        "How": "Usa 'How' + verbo 'to be' + pronombre para preguntar por estado o emoción.\nEj: How are you?",
        "Whose": "Usa 'Whose' + sustantivo + verbo 'to be' para preguntar por posesión.\nEj: Whose book is this?"
    }
    print("\n📘 Regla:")
    print(reglas.get(tipo, "Regla no disponible."))

def ejercicio(tipo):
    ejemplos = {
        "Who": {
            "pista": "Ella es la líder de la misión.",
            "respuesta": "Who is she?"
        },
        "What": {
            "pista": "Él toca la guitarra.",
            "respuesta": "What is he?"
        },
        "Where": {
            "pista": "Ellos están en la biblioteca.",
            "respuesta": "Where are they?"
        },
        "How": {
            "pista": "Tú estás cansado.",
            "respuesta": "How are you?"
        },
        "Whose": {
            "pista": "Este es el libro de Ana.",
            "respuesta": "Whose book is this?"
        }
    }

    item = ejemplos.get(tipo)
    if item:
        print(f"\n🧩 Pista: {item['pista']}")
        user_input = input("✍️ Escribe la pregunta en inglés: ").strip()
        if user_input.lower() == item['respuesta'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta esperada era: {item['respuesta']}")
    else:
        print("Ejercicio no disponible.")

def menu():
    while True:
        print("\n🔍 Menú de práctica de preguntas abiertas en inglés")
        print("1. Who – Identidad")
        print("2. What – Profesión o rol")
        print("3. Where – Ubicación")
        print("4. How – Estado o emoción")
        print("5. Whose – Posesión")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        tipos = {
            "1": "Who",
            "2": "What",
            "3": "Where",
            "4": "How",
            "5": "Whose"
        }

        if opcion == "6":
            print("👋 ¡Gracias por practicar! Hasta pronto.")
            break
        elif opcion in tipos:
            tipo = tipos[opcion]
            mostrar_regla(tipo)
            ejercicio(tipo)
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
