import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO DECIMOS LO OPUESTO?

Los antónimos son palabras que significan lo contrario.

🔹 Ejemplos de antónimos:
- grande ↔ pequeño
- feliz ↔ triste
- alto ↔ bajo
- limpio ↔ sucio
- rápido ↔ lento

🎯 Usamos antónimos para comparar, contrastar o expresar diferencias.

📝 Ejemplo:
"La montaña es alta, pero el valle es bajo."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"frase": "El día está soleado, pero ayer estuvo ___", "antonimo": "nublado"},
    {"frase": "El niño es rápido, y su amigo es muy ___", "antonimo": "lento"},
    {"frase": "Mi ropa está limpia, pero la tuya está ___", "antonimo": "sucia"},
    {"frase": "Pedro está feliz, pero Marta está ___", "antonimo": "triste"},
    {"frase": "Ese animal es grande, pero este es ___", "antonimo": "pequeño"}
]

# 📝 20 frases incompletas con antónimos
ejercicios = [
    {"inicio": "Mi mochila es pesada, pero la tuya es ___", "antonimo": "liviana"},
    {"inicio": "Este cuarto está oscuro, el otro está ___", "antonimo": "iluminado"},
    {"inicio": "El camino es largo, aquel es ___", "antonimo": "corto"},
    {"inicio": "Juan es ordenado, Pedro es ___", "antonimo": "desordenado"},
    {"inicio": "El libro está nuevo, el cuaderno está ___", "antonimo": "viejo"},
    {"inicio": "La leche está fría, pero el café está ___", "antonimo": "caliente"},
    {"inicio": "El ejercicio fue fácil, pero el siguiente es ___", "antonimo": "difícil"},
    {"inicio": "El gato está despierto, pero el perro está ___", "antonimo": "dormido"},
    {"inicio": "El cielo está claro, pero antes estuvo ___", "antonimo": "oscuro"},
    {"inicio": "La película fue divertida, pero el libro fue ___", "antonimo": "aburrido"}
]

elogios = [
    "🎯 ¡Antónimo correcto!",
    "🌟 ¡Buen contraste!",
    "✅ ¡Tu oración tiene sentido opuesto!",
    "👏 ¡Muy bien usado el antónimo!",
    "🧠 ¡Pensamiento contrario bien aplicado!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON ANTÓNIMOS:")
    for ej in ejemplos:
        print(f"📝 {ej['frase']} → Ejemplo: {ej['antonimo']}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 COMPLETA LA FRASE CON UN ANTÓNIMO:")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['inicio']}")
        respuesta = input("👉 Escribe el antónimo correcto: ").strip().lower()
        if respuesta == ej['antonimo']:
            print(random.choice(elogios))
        else:
            print(f"⚠️ El antónimo correcto era: '{ej['antonimo']}'")

# ✍️ Crear frases propias con antónimos
def escribir_propias():
    print("\n✍️ ESCRIBE 5 PARES DE FRASES CON PALABRAS OPUESTAS:")
    propias = []
    for i in range(1, 6):
        frase1 = input(f"👉 Frase positiva {i}: ").strip()
        frase2 = input(f"👉 Frase opuesta {i}: ").strip()
        propias.append((frase1, frase2))

    print("\n📘 Tus pares de frases opuestas:")
    for idx, (f1, f2) in enumerate(propias, 1):
        print(f"{idx}. {f1} ↔ {f2}")
    print("🏅 ¡Muy bien! Has usado los contrarios para pensar con precisión.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 4.º Grado – Lección 7: Uso de Antónimos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir frases opuestas ✍️")
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
            print("👋 ¡Gracias por pensar en opuestos y enriquecer tu vocabulario!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    menu()
