import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO DAMOS MÁS INFORMACIÓN EN UNA ORACIÓN?

Las oraciones nos cuentan qué pasa. Pero también podemos decir:

🔹 ¿Dónde? → lugar → "El gato duerme EN EL SILLÓN."
🔹 ¿Cuándo? → tiempo → "El gato duerme POR LA TARDE."
🔹 ¿Cómo? → modo → "El gato duerme TRANQUILAMENTE."

🎯 Eso se llama "ampliar la oración con complementos". Nos ayuda a expresarnos mejor.
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La niña dibuja en el cuaderno. (lugar)",
    "El perro corre por la mañana. (tiempo)",
    "Mi mamá canta suavemente. (modo)",
    "Los niños juegan en el patio por la tarde. (lugar + tiempo)",
    "El bebé duerme plácidamente en su cuna. (modo + lugar)"
]

# 📝 Oraciones base para ampliar
oraciones_base = [
    "El niño juega.",
    "La maestra explica.",
    "El pájaro canta.",
    "Mi hermana corre.",
    "El gato duerme.",
    "Los estudiantes leen.",
    "Papá cocina.",
    "La niña pinta.",
    "El perro ladra.",
    "Mi primo salta.",
    "Ellos escriben.",
    "La flor crece.",
    "Nosotros bailamos.",
    "El tren llega.",
    "Mamá trabaja.",
    "Los niños dibujan.",
    "El coche avanza.",
    "La pelota rueda.",
    "Mi tío habla.",
    "El árbol tiembla."
]

elogios = [
    "🌟 ¡Frase muy detallada!",
    "✅ ¡Buen uso de complementos!",
    "👏 ¡Ahora la oración tiene lugar o tiempo!",
    "💬 ¡Tu frase suena muy completa!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES CON COMPLEMENTOS:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Ampliar oraciones
def practicar_complementos():
    print("\n📝 AGREGA UNA INFORMACIÓN: ¿Dónde? ¿Cuándo? ¿Cómo?")
    total = 0
    for i, frase in enumerate(oraciones_base, 1):
        print(f"\n{str(i).zfill(2)}. Frase base: {frase}")
        respuesta = input("👉 Tu versión ampliada: ").strip().lower()
        puntos = 0
        if len(respuesta.split()) >= 6:
            puntos += 1
        if any(p in respuesta for p in ["en", "por", "sobre", "al", "durante"]):
            puntos += 1
        if any(m in respuesta for m in ["rápidamente", "suavemente", "tranquilamente", "bien", "con cuidado", "alegremente"]):
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Gran dominio de oraciones detalladas!")
    elif total >= 35:
        print("👍 Buen intento. Puedes agregar más detalles en cada frase.")
    else:
        print("📘 Practica cómo decir dónde, cuándo y cómo ocurren las acciones.")

# ✍️ Composición libre
def redactar_escena():
    print("\n✍️ ESCRIBE UNA ESCENA DE 3 ORACIONES CON COMPLEMENTOS:")
    escena = []
    total = 0
    for i in range(1, 4):
        frase = input(f"📝 Oración {i}: ").strip().lower()
        puntos = 0
        if len(frase.split()) >= 7:
            puntos += 1
        if any(p in frase for p in ["en", "por", "durante", "con"]):
            puntos += 1
        if any(m in frase for m in ["rápidamente", "alegremente", "lentamente", "suavemente"]):
            puntos += 1
        escena.append(frase)
        print(f"🎯 Puntos: {puntos}/3")
        total += puntos
    print(f"\n📊 Puntaje creativo: {total}/9")
    print("📝 Tu escena completa:")
    for frase in escena:
        print(f"- {frase.capitalize()}.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 3.º Grado – Lección 9: Complementos circunstanciales")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Ampliar oraciones básicas 📝")
        print("4. Redactar una escena ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_complementos()
        elif opcion == "4":
            redactar_escena()
        elif opcion == "5":
            print("👋 ¡Gracias por agregar color a tus oraciones!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
