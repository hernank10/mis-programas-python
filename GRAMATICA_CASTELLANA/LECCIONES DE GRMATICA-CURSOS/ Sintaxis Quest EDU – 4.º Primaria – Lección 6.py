import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – NÚCLEO DEL PREDICADO

Cada oración tiene dos partes:
🔹 SUJETO: quien realiza la acción
🔹 PREDICADO: todo lo que se dice sobre el sujeto

El núcleo del predicado es su palabra más importante: el VERBO principal.

🎯 Ejemplo:
- "Mi hermana juega con la pelota."
  👉 Predicado: 'juega con la pelota'
  👉 Núcleo del predicado: 'juega'
"""

# 📚 Ejemplos explicados
ejemplos = [
    {"oracion": "El perro corre por el parque.", "nucleo": "corre"},
    {"oracion": "La maestra explica la lección.", "nucleo": "explica"},
    {"oracion": "Mi hermano lee un cuento.", "nucleo": "lee"},
    {"oracion": "Los niños juegan fútbol.", "nucleo": "juegan"},
    {"oracion": "Papá cocina arroz con pollo.", "nucleo": "cocina"}
]

# 📝 20 ejercicios
ejercicios = [
    {"oracion": "La tortuga camina lento.", "nucleo": "camina"},
    {"oracion": "Mi prima escribe una carta.", "nucleo": "escribe"},
    {"oracion": "El gato duerme en el sillón.", "nucleo": "duerme"},
    {"oracion": "La señora barre la casa.", "nucleo": "barre"},
    {"oracion": "Los alumnos estudian historia.", "nucleo": "estudian"},
    {"oracion": "Mi papá maneja el carro.", "nucleo": "maneja"},
    {"oracion": "El bebé ríe fuerte.", "nucleo": "ríe"},
    {"oracion": "La profesora lee un libro.", "nucleo": "lee"},
    {"oracion": "Los pájaros vuelan alto.", "nucleo": "vuelan"},
    {"oracion": "La niña pinta su dibujo.", "nucleo": "pinta"},
    {"oracion": "Mi amigo salta en la cama.", "nucleo": "salta"},
    {"oracion": "El tren avanza lentamente.", "nucleo": "avanza"},
    {"oracion": "Mamá limpia la cocina.", "nucleo": "limpia"},
    {"oracion": "El pez nada en el estanque.", "nucleo": "nada"},
    {"oracion": "Mi tío trabaja en el hospital.", "nucleo": "trabaja"},
    {"oracion": "Los niños corren en el parque.", "nucleo": "corren"},
    {"oracion": "El abuelo escucha la radio.", "nucleo": "escucha"},
    {"oracion": "La flor crece bajo el sol.", "nucleo": "crece"},
    {"oracion": "Mi hermana canta una canción.", "nucleo": "canta"},
    {"oracion": "La vaca muge en la granja.", "nucleo": "muge"}
]

elogios = ["🎉 ¡Muy bien!", "🧠 ¡Detectaste el núcleo!", "🌟 ¡Excelente observación!", "👏 ¡Correcto!", "⭐ ¡Buen análisis!"]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Núcleo del predicado: {ej['nucleo']}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Oración: {ej['oracion']}")
        respuesta = input("👉 ¿Cuál es el núcleo del predicado?: ").strip().lower()
        if respuesta == ej["nucleo"]:
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: '{ej['nucleo']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Explorador del Predicado! 🧠")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES")
    print("Escribe 20 oraciones donde puedas identificar el núcleo del predicado:\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Gran trabajo sintáctico!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 4.º Primaria – Lección 6")
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
            print("👋 ¡Gracias por seguir explorando el corazón del predicado!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
