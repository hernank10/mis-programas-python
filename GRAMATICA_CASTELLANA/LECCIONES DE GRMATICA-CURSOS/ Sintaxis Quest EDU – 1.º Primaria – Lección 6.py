import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – ¿QUIÉN HACE QUÉ?

Toda oración tiene dos partes importantes:
🔹 SUJETO: quien realiza la acción (persona, animal o cosa)
🔹 VERBO: la acción que se realiza

🎯 Ejemplo:
- Oración: "La niña canta."
  ¿Quién hace? → La niña (sujeto)
  ¿Qué hace? → canta (verbo)

Podemos descubrir esto haciendo preguntas como:
👉 ¿Quién hace?
👉 ¿Qué hace?
"""

# 📚 Ejemplos resueltos
ejemplos = [
    {"oracion": "El gato duerme.", "sujeto": "El gato", "verbo": "duerme"},
    {"oracion": "La niña salta.", "sujeto": "La niña", "verbo": "salta"},
    {"oracion": "Papá cocina.", "sujeto": "Papá", "verbo": "cocina"},
    {"oracion": "El pájaro vuela.", "sujeto": "El pájaro", "verbo": "vuela"},
    {"oracion": "Mi hermano corre.", "sujeto": "Mi hermano", "verbo": "corre"}
]

# 📝 20 ejercicios
ejercicios = [
    {"oracion": "La maestra escribe.", "sujeto": "La maestra", "verbo": "escribe"},
    {"oracion": "El niño juega.", "sujeto": "El niño", "verbo": "juega"},
    {"oracion": "Mi perro ladra.", "sujeto": "Mi perro", "verbo": "ladra"},
    {"oracion": "La tortuga camina.", "sujeto": "La tortuga", "verbo": "camina"},
    {"oracion": "El bebé ríe.", "sujeto": "El bebé", "verbo": "ríe"},
    {"oracion": "El abuelo lee.", "sujeto": "El abuelo", "verbo": "lee"},
    {"oracion": "La mamá barre.", "sujeto": "La mamá", "verbo": "barre"},
    {"oracion": "Mi amiga dibuja.", "sujeto": "Mi amiga", "verbo": "dibuja"},
    {"oracion": "El tren avanza.", "sujeto": "El tren", "verbo": "avanza"},
    {"oracion": "El sol brilla.", "sujeto": "El sol", "verbo": "brilla"},
    {"oracion": "La vaca muge.", "sujeto": "La vaca", "verbo": "muge"},
    {"oracion": "El pez nada.", "sujeto": "El pez", "verbo": "nada"},
    {"oracion": "La flor crece.", "sujeto": "La flor", "verbo": "crece"},
    {"oracion": "El carro gira.", "sujeto": "El carro", "verbo": "gira"},
    {"oracion": "La abeja zumba.", "sujeto": "La abeja", "verbo": "zumba"},
    {"oracion": "El ratón corre.", "sujeto": "El ratón", "verbo": "corre"},
    {"oracion": "La niña ríe.", "sujeto": "La niña", "verbo": "ríe"},
    {"oracion": "El pato nada.", "sujeto": "El pato", "verbo": "nada"},
    {"oracion": "Mi tío maneja.", "sujeto": "Mi tío", "verbo": "maneja"},
    {"oracion": "La hormiga camina.", "sujeto": "La hormiga", "verbo": "camina"}
]

elogios = ["🎉 ¡Muy bien!", "⭐ ¡Correcto!", "👏 ¡Estás aprendiendo!", "🧠 ¡Buena observación!", "🌟 ¡Bravo!"]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos explicados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Sujeto: {ej['sujeto']} | Verbo: {ej['verbo']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Oración: {ej['oracion']}")
        sujeto = input("👉 ¿Quién hace? (Sujeto): ").strip().lower()
        verbo = input("👉 ¿Qué hace? (Verbo): ").strip().lower()

        if sujeto == ej["sujeto"].lower() and verbo == ej["verbo"].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: Sujeto: '{ej['sujeto']}' | Verbo: '{ej['verbo']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia: Maestro de las Preguntas Activas! 🧒🔍")

# ✍️ Crear oraciones propias
def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES")
    print("Escribe 20 oraciones que respondan: ¿Quién hace qué? (ej. 'El niño salta.')\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo creativo!")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 1.º Primaria – Lección 6")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar con 10 ejercicios 📝")
        print("4. Escribir 20 oraciones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            crear_ejemplos_usuario()
        elif opcion == "5":
            print("👋 ¡Gracias por seguir aprendiendo quién hace qué!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
