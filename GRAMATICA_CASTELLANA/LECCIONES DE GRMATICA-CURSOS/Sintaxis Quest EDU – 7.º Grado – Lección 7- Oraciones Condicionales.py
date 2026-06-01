import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿QUÉ PASARÍA SI…?

Las oraciones condicionales expresan algo que puede ocurrir si otra cosa sucede.

🎯 Estructura básica:
"Si + condición, + consecuencia."

🔹 Ejemplo:
"Si estudio, saco buena nota."
"Si llueve, no saldremos."
"Si estás cansado, descansa un poco."

✅ El uso de "si" nos ayuda a pensar en opciones, consecuencias o hipótesis.
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"condicion": "Si me levanto temprano", "consecuencia": "llego a tiempo."},
    {"condicion": "Si practico mucho", "consecuencia": "mejoro en matemáticas."},
    {"condicion": "Si no como", "consecuencia": "me da hambre."},
    {"condicion": "Si hace frío", "consecuencia": "uso abrigo."},
    {"condicion": "Si estudio para el examen", "consecuencia": "lo apruebo."}
]

# 📝 20 ejercicios (mitad de la oración)
ejercicios = [
    {"inicio": "Si corro rápido,", "final": "llego primero."},
    {"inicio": "Si no duermo bien,", "final": "estoy cansado."},
    {"inicio": "Si tengo dinero,", "final": "compro un libro."},
    {"inicio": "Si el semáforo está en rojo,", "final": "debo detenerme."},
    {"inicio": "Si no respetas las reglas,", "final": "puedes tener problemas."},
    {"inicio": "Si ayudas a otros,", "final": "te sientes bien."},
    {"inicio": "Si cocino solo,", "final": "aprendo más."},
    {"inicio": "Si olvidamos la tarea,", "final": "nos llaman la atención."},
    {"inicio": "Si el cielo está oscuro,", "final": "va a llover."},
    {"inicio": "Si no estudias,", "final": "puedes reprobar."}
]

elogios = [
    "✅ ¡Oración condicional bien construida!",
    "🌟 ¡Excelente uso de ‘si’ y consecuencia!",
    "🎯 ¡Pensaste con lógica!",
    "👏 ¡Muy buen trabajo!",
    "🧠 ¡Tu idea tiene causa y resultado!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES CONDICIONALES:")
    for ej in ejemplos:
        print(f"📝 {ej['condicion']}, {ej['consecuencia']}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 COMPLETA LAS ORACIONES CON LA CONSECUENCIA:")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['inicio']}")
        respuesta = input("👉 ¿Qué sucedería?: ").strip()
        if respuesta:
            print(random.choice(elogios))
            print(f"🧠 Oración completa: {ej['inicio']} {respuesta}")
        else:
            print(f"⚠️ Puedes completar con algo como: '{ej['final']}'")

# ✍️ Crear oraciones propias
def escribir_propias():
    print("\n✍️ ESCRIBE 5 ORACIONES CONDICIONALES:")
    oraciones = []
    for i in range(1, 6):
        condicion = input(f"👉 Condición {i} (empieza con 'Si...'): ").strip()
        consecuencia = input("👉 ¿Qué pasa si eso ocurre?: ").strip()
        oraciones.append(f"{condicion}, {consecuencia}")

    print("\n📘 Tus oraciones condicionales:")
    for idx, o in enumerate(oraciones, 1):
        print(f"{idx}. {o}")
    print("🏅 ¡Muy bien! Pensaste en posibilidades con claridad.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 7.º Grado – Lección 7: Oraciones Condicionales")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar ejercicios 📝")
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
            escribir_propias()
        elif opcion == "5":
            print("👋 ¡Gracias por imaginar posibilidades con inteligencia sintáctica!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    menu()
