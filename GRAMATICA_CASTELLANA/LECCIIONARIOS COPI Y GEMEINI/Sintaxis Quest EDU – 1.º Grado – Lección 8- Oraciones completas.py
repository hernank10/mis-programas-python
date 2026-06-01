# 🧠 Lección 8 – Oraciones completas: sujeto + predicado

import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿QUÉ TIENE UNA ORACIÓN PARA ESTAR COMPLETA?

Una oración completa tiene dos partes:

🔹 Sujeto → ¿Quién hace?
🔹 Predicado → ¿Qué hace? / ¿Qué se dice?

✅ Ejemplo:
"La niña corre rápido."
Sujeto: La niña / Predicado: corre rápido

❌ "Corre rápido." → Falta sujeto
❌ "La niña." → Falta verbo o acción
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"oracion": "El gato duerme tranquilo.", "sujeto": "El gato", "predicado": "duerme tranquilo"},
    {"oracion": "Mi mamá cocina arroz.", "sujeto": "Mi mamá", "predicado": "cocina arroz"},
    {"oracion": "El niño juega en el parque.", "sujeto": "El niño", "predicado": "juega en el parque"},
    {"oracion": "Los pájaros cantan temprano.", "sujeto": "Los pájaros", "predicado": "cantan temprano"},
]

# 📝 20 oraciones incompletas
ejercicios = [
    {"incompleta": "_____ come manzana.", "ejemplo": "El caballo"},
    {"incompleta": "El perro _____ en la casa.", "ejemplo": "duerme"},
    {"incompleta": "_____ pinta con colores.", "ejemplo": "La niña"},
    {"incompleta": "Mi papá _____ la bicicleta.", "ejemplo": "arregla"},
    {"incompleta": "_____ saltan en la cama.", "ejemplo": "Los niños"},
    {"incompleta": "La abuela _____ galletas.", "ejemplo": "hornea"},
    {"incompleta": "_____ corre en el jardín.", "ejemplo": "El conejo"},
    {"incompleta": "El pájaro _____ muy alto.", "ejemplo": "vuela"},
    {"incompleta": "_____ lee un cuento.", "ejemplo": "La maestra"},
    {"incompleta": "Mi hermano _____ feliz.", "ejemplo": "canta"},
    {"incompleta": "_____ brinca en la cuerda.", "ejemplo": "Ella"},
    {"incompleta": "El pez _____ en el agua.", "ejemplo": "nada"},
    {"incompleta": "Mi tío _____ fotos.", "ejemplo": "toma"},
    {"incompleta": "_____ toca la guitarra.", "ejemplo": "El músico"},
    {"incompleta": "La vaca _____ en el campo.", "ejemplo": "camina"},
    {"incompleta": "_____ juega con pelotas.", "ejemplo": "El bebé"},
    {"incompleta": "El carro _____ muy rápido.", "ejemplo": "rueda"},
    {"incompleta": "_____ lava la ropa.", "ejemplo": "Mi mamá"},
    {"incompleta": "La flor _____ al sol.", "ejemplo": "brilla"},
    {"incompleta": "_____ canta en la fiesta.", "ejemplo": "Mi prima"},
]

elogios = [
    "🌟 ¡Oración completa!", "✅ ¡Muy bien!", "👏 ¡Excelente!", "🧠 ¡Buen sujeto y predicado!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES COMPLETAS:")
    for ej in ejemplos:
        print(f"📝 {ej['oracion']}")
        print(f"👉 Sujeto: {ej['sujeto']} | Predicado: {ej['predicado']}\n")

# 📝 Ejercicios para completar
def practicar_ejercicios():
    print("\n📝 COMPLETA LAS ORACIONES:")
    total = 0
    for i, ej in enumerate(ejercicios, 1):
        print(f"\n{str(i).zfill(2)}. {ej['incompleta']}")
        respuesta = input("👉 Tu oración completa: ").strip()
        if len(respuesta.split()) >= 3 and "." in respuesta:
            print(f"{random.choice(elogios)} (Punto: 3)")
            total += 3
        elif len(respuesta.split()) >= 2:
            print("✅ Casi completa. Puedes agregar más detalles. (Punto: 2)")
            total += 2
        elif len(respuesta.split()) == 1:
            print("⚠️ Falta parte de la oración. (Punto: 1)")
            total += 1
        else:
            print("❌ No se detectó oración válida. (Punto: 0)")

    print(f"\n📊 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Muy bien! Tus oraciones están completas y claras.")
    elif total >= 35:
        print("👍 Buen intento. Revisa sujeto y verbo en cada frase.")
    else:
        print("📘 Sigue practicando cómo construir oraciones con sentido.")

# ✍️ Oraciones propias
def crear_oraciones():
    print("\n✍️ ESCRIBE 5 ORACIONES CON SUJETO + PREDICADO:")
    total = 0
    for i in range(1, 6):
        oracion = input(f"📝 Oración {i}: ").strip()
        puntos = 0
        if len(oracion.split()) >= 3 and "." in oracion:
            puntos = 3
        elif len(oracion.split()) >= 2:
            puntos = 2
        elif len(oracion.split()) == 1:
            puntos = 1
        total += puntos
        print(f"👉 Puntaje: {puntos}/3")
    print(f"\n📊 Total creativo: {total}/15")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 1.º Grado – Lección 8: Oraciones completas")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 oraciones incompletas 📝")
        print("4. Escribir tus propias oraciones ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            crear_oraciones()
        elif opcion == "5":
            print("👋 ¡Gracias por construir oraciones completas con inteligencia sintáctica!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
