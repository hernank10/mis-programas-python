# Juego interactivo: Question Quest

puntos = 0
nivel_desbloqueado = 1

def mostrar_regla(nivel):
    reglas = {
        1: "🟢 Nivel 1 – Pronombres + to be\nEj: Is he? / Are they?",
        2: "🟠 Nivel 2 – + Sustantivos comunes\nEj: Is he a teacher? / Is she your sister?",
        3: "🔴 Nivel 3 – + Sustantivos compuestos / abstractos\nEj: Is she a software developer? / Is she a hope for the family?"
    }
    print("\n📘 Regla del nivel:")
    print(reglas[nivel])

def obtener_ejercicios(nivel):
    return {
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
    }[nivel]

def jugar_nivel(nivel):
    global puntos
    print(f"\n🎮 Jugando Nivel {nivel}")
    mostrar_regla(nivel)
    ejercicios = obtener_ejercicios(nivel)
    aciertos = 0

    for i, ej in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {ej['pista']}")
        respuesta = input("✍️ Escribe la pregunta en inglés: ").strip()
        if respuesta.lower() == ej['respuesta'].lower():
            print("✅ ¡Correcto!")
            puntos += 10
            aciertos += 1
        else:
            print(f"❌ Incorrecto. La respuesta esperada era: {ej['respuesta']}")

    return aciertos == len(ejercicios)

def menu_principal():
    global nivel_desbloqueado
    print("\n🎓 Bienvenido a *Question Quest*")
    while True:
        print(f"\n🔓 Niveles disponibles: 1 a {nivel_desbloqueado}")
        print("1. Nivel 1 – Básico")
        print("2. Nivel 2 – Intermedio")
        print("3. Nivel 3 – Avanzado")
        print("4. Ver puntuación")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "5":
            print(f"\n👋 ¡Gracias por jugar! Tu puntuación final fue: {puntos} puntos.")
            break
        elif opcion in ["1", "2", "3"]:
            nivel = int(opcion)
            if nivel > nivel_desbloqueado:
                print("🔒 Este nivel está bloqueado. Completa el anterior para desbloquearlo.")
            else:
                aprobado = jugar_nivel(nivel)
                if aprobado and nivel == nivel_desbloqueado and nivel < 3:
                    nivel_desbloqueado += 1
                    print(f"🎉 ¡Nivel {nivel + 1} desbloqueado!")
        elif opcion == "4":
            print(f"\n🏆 Puntuación actual: {puntos} puntos")
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el juego
if __name__ == "__main__":
    menu_principal()
