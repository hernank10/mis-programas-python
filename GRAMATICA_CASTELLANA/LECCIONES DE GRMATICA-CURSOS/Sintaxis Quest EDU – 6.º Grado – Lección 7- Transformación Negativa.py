import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO NEGAMOS UNA ORACIÓN?

Negar una idea significa decir que algo NO sucede, NO existe o NO es cierto.

🔹 Para negar usamos:
- no / nunca / tampoco / jamás / ningún / nada / nadie

💡 Ejemplo:
Afirmativa: "Pedro tiene clase hoy."
Negativa: "Pedro no tiene clase hoy."

✅ La negación cambia el significado y debe mantener sentido y orden.
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"afirmativa": "Ella juega fútbol.", "negativa": "Ella no juega fútbol."},
    {"afirmativa": "Nosotros vamos al cine.", "negativa": "Nosotros no vamos al cine."},
    {"afirmativa": "Tú entiendes la tarea.", "negativa": "Tú no entiendes la tarea."},
    {"afirmativa": "Yo tengo deberes hoy.", "negativa": "Yo no tengo deberes hoy."},
    {"afirmativa": "Carlos habla en clase.", "negativa": "Carlos no habla en clase."}
]

# 📝 20 ejercicios de transformación
ejercicios = [
    {"afirmativa": "Ella canta en público.", "negativa": "Ella no canta en público."},
    {"afirmativa": "Marcos escribe poemas.", "negativa": "Marcos no escribe poemas."},
    {"afirmativa": "El perro corre rápido.", "negativa": "El perro no corre rápido."},
    {"afirmativa": "Yo leo todos los días.", "negativa": "Yo no leo todos los días."},
    {"afirmativa": "Ellos viajan mucho.", "negativa": "Ellos no viajan mucho."},
    {"afirmativa": "Nos levantamos temprano.", "negativa": "Nos no levantamos temprano."},
    {"afirmativa": "Tú comes verduras.", "negativa": "Tú no comes verduras."},
    {"afirmativa": "Mi hermano habla inglés.", "negativa": "Mi hermano no habla inglés."},
    {"afirmativa": "La niña escucha música.", "negativa": "La niña no escucha música."},
    {"afirmativa": "Luis estudia matemáticas.", "negativa": "Luis no estudia matemáticas."}
]

elogios = [
    "✅ ¡Negación correcta y clara!",
    "🎯 ¡Excelente transformación!",
    "🌟 ¡Oración negativa con sentido!",
    "🧠 ¡Bien pensado!",
    "👏 ¡Muy buena negación sintáctica!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CONVERSIÓN A NEGATIVA:")
    for ej in ejemplos:
        print(f"📝 Afirmativa: {ej['afirmativa']}")
        print(f"❌ Negativa: {ej['negativa']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 TRANSFORMA LA FRASE EN NEGATIVA:")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Afirmativa: {ej['afirmativa']}")
        respuesta = input("👉 Escribe la oración negativa: ").strip().lower()
        if respuesta == ej['negativa'].lower():
            print(random.choice(elogios))
        else:
            print(f"⚠️ Una forma correcta sería: '{ej['negativa']}'")

# ✍️ Crear pares propias
def escribir_propias():
    print("\n✍️ ESCRIBE 5 PARES DE ORACIONES (AFIRMATIVA Y NEGATIVA):")
    pares = []
    for i in range(1, 6):
        afirmativa = input(f"👉 Afirmativa {i}: ").strip()
        negativa = input("❌ Negativa correspondiente: ").strip()
        pares.append((afirmativa, negativa))

    print("\n📘 Tus pares de oraciones:")
    for idx, (a, n) in enumerate(pares, 1):
        print(f"{idx}. ✅ {a}")
        print(f"   ❌ {n}")
    print("🏅 ¡Muy bien! Ahora sabes cómo cambiar el signo de una idea.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 6.º Grado – Lección 7: Transformación Negativa")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir tus propias frases ✍️")
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
            print("👋 ¡Gracias por aprender a negar con lógica y orden!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    menu()
