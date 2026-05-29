import random

# Diccionario de conectores y consejos por categoría
conectores = {
    "Adición": {
        "ejemplos": ["además", "también", "incluso", "asimismo"],
        "consejos": [
            "Usa 'además' para sumar ideas relacionadas.",
            "Evita repetir 'también' varias veces.",
            "Prefiere 'asimismo' en contextos formales.",
            "Usa 'incluso' para enfatizar lo inesperado."
        ]
    },
    "Contraste": {
        "ejemplos": ["pero", "aunque", "sin embargo", "no obstante"],
        "consejos": [
            "Usa 'pero' para introducir una objeción ligera.",
            "'Sin embargo' indica oposición con más fuerza.",
            "No combines 'pero' con 'sin embargo'.",
            "'Aunque' introduce una idea opuesta dentro de una oración."
        ]
    },
    "Causa": {
        "ejemplos": ["porque", "ya que", "dado que", "debido a que"],
        "consejos": [
            "Usa 'porque' para causas claras.",
            "Prefiere 'dado que' en textos académicos.",
            "'Debido a que' necesita un verbo después.",
            "Evita usar 'por' como si fuera 'porque'."
        ]
    },
    "Consecuencia": {
        "ejemplos": ["por eso", "por lo tanto", "en consecuencia", "así que"],
        "consejos": [
            "Usa 'por eso' en lenguaje informal.",
            "'Por lo tanto' es ideal para argumentar.",
            "'En consecuencia' es perfecto para cerrar ideas.",
            "Evita usar 'entonces' sin lógica clara."
        ]
    }
    # Puedes seguir agregando más categorías y consejos aquí...
}

def mostrar_menu():
    print("\n📘 MENÚ PRINCIPAL")
    print("1. Estudiar consejos por tipo de conector")
    print("2. Ver ejemplos de conectores")
    print("3. Practicar con ejercicios")
    print("4. Salir")

def estudiar_consejos():
    print("\n📘 Estudio de consejos:")
    for tipo, data in conectores.items():
        print(f"\n🔹 {tipo}:")
        for consejo in data["consejos"]:
            print(f" - {consejo}")

def ver_ejemplos():
    print("\n📗 Ejemplos de conectores por tipo:")
    for tipo, data in conectores.items():
        ejemplos = ', '.join(data["ejemplos"])
        print(f"🔸 {tipo}: {ejemplos}")

def practicar():
    puntos = 0
    categorias = list(conectores.keys())
    print("\n🧠 Ejercicios de práctica (5 preguntas):")
    for _ in range(5):
        tipo_correcto = random.choice(categorias)
        ejemplo = random.choice(conectores[tipo_correcto]["ejemplos"])
        opciones = random.sample(categorias, k=3)
        if tipo_correcto not in opciones:
            opciones[random.randint(0, 2)] = tipo_correcto
        random.shuffle(opciones)

        print(f"\n👉 ¿A qué tipo de conector pertenece la palabra '{ejemplo}'?")
        for i, op in enumerate(opciones):
            print(f"{i + 1}. {op}")
        respuesta = input("Tu respuesta (1-3): ")
        if opciones[int(respuesta) - 1] == tipo_correcto:
            print("✅ ¡Correcto!")
            puntos += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {tipo_correcto}")
    print(f"\n🔚 Tu puntuación final: {puntos}/5")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-4): ")
    if opcion == "1":
        estudiar_consejos()
    elif opcion == "2":
        ver_ejemplos()
    elif opcion == "3":
        practicar()
    elif opcion == "4":
        print("👋 ¡Hasta pronto!")
        break
    else:
        print("❗ Opción inválida. Intenta de nuevo.")
