import random

# 📘 Teoría explicada
teoria = """
📘 LECCIÓN 7 – ¿QUÉ DESCRIBE LO QUE NOMBRAMOS?

Los adjetivos son palabras que nos ayudan a describir cosas.

🔹 ¿Qué puede decir un adjetivo?
- Cómo es (grande, pequeño, alegre)
- De qué color (rojo, azul, verde)
- Qué emoción expresa (triste, feliz)
- Qué forma o textura tiene (redondo, suave, rugoso)

🎯 Ejemplo:
- "La niña tiene una mochila." → Sin adjetivo
- "La niña tiene una mochila colorida." → Con adjetivo
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"frase": "El perro es ___", "adjetivo": "grande"},
    {"frase": "Mi casa es ___", "adjetivo": "bonita"},
    {"frase": "El cielo está ___", "adjetivo": "azul"},
    {"frase": "El carro es ___", "adjetivo": "rápido"},
    {"frase": "La flor es ___", "adjetivo": "hermosa"}
]

# 📝 20 ejercicios para completar con adjetivos
ejercicios = [
    "Mi mochila es ___",
    "El gato está ___",
    "La fruta está ___",
    "La pelota es ___",
    "El autobús es ___",
    "La camisa es ___",
    "El árbol es ___",
    "La bicicleta es ___",
    "El libro es ___",
    "La montaña está ___",
    "El café está ___",
    "El bebé está ___",
    "La sopa está ___",
    "El pez es ___",
    "El helado está ___",
    "Mi hermano es ___",
    "La ventana está ___",
    "El reloj es ___",
    "La mesa está ___",
    "La canción es ___"
]

elogios = [
    "🎨 ¡Gran descripción!",
    "🌟 ¡Adjetivo bien usado!",
    "👏 ¡Color y forma en tus palabras!",
    "🧠 ¡Oración más rica con tu adjetivo!",
    "✅ ¡Muy bien, eso se entiende mejor!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON ADJETIVOS:")
    for ej in ejemplos:
        print(f"📝 {ej['frase']} → Ejemplo: {ej['adjetivo']}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 AGREGA UN ADJETIVO QUE DESCRIBA LO QUE SE DICE:")
    seleccion = random.sample(ejercicios, 10)
    for i, frase in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {frase}")
        respuesta = input("👉 Escribe tu adjetivo: ").strip()
        if respuesta:
            print(random.choice(elogios))
        else:
            print("⚠️ No escribiste nada. Intenta describir la frase con una palabra.")

# ✍️ Crear oraciones propias
def escribir_propias():
    print("\n✍️ ESCRIBE 10 ORACIONES QUE INCLUYAN ADJETIVOS:")
    oraciones = []
    for i in range(1, 11):
        frase = input(f"👉 Oración {i}: ").strip()
        oraciones.append(frase)

    print("\n📘 Tus oraciones descriptivas:")
    for idx, f in enumerate(oraciones, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Bien hecho! Tus palabras pintan lo que imaginas.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 2.º Grado – Lección 7: Uso de Adjetivos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos 📚")
        print("3. Practicar con 10 frases 📝")
        print("4. Escribir 10 oraciones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            escribir_propias()
        elif opcion == "5":
            print("👋 ¡Gracias por aprender a describir con adjetivos!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
