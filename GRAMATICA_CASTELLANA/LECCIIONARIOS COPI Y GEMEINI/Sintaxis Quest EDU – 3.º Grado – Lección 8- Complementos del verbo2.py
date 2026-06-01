import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿DÓNDE, CÓMO Y CUÁNDO OCURRE LA ACCIÓN?

Una oración tiene un verbo (acción). Para dar más detalles, usamos:

🔹 Complemento de lugar → ¿Dónde?
🔹 Complemento de tiempo → ¿Cuándo?
🔹 Complemento de modo → ¿Cómo?

🎯 Ejemplo:
"La niña lee."
↪ ¿Dónde? en la biblioteca
↪ ¿Cuándo? por la tarde
↪ ¿Cómo? con atención

✅ Oración enriquecida:
"La niña lee con atención en la biblioteca por la tarde."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "El perro duerme en la sala por la noche.",
    "Los niños juegan con alegría en el parque por la mañana.",
    "Mi papá trabaja en el hospital con cuidado cada día.",
    "La maestra explica la lección con paciencia en el salón durante la clase.",
]

# 📝 20 oraciones básicas
oraciones_base = [
    "El gato duerme",
    "La niña canta",
    "Mi abuela cocina",
    "El niño corre",
    "El pájaro vuela",
    "Mi tío maneja",
    "Los estudiantes escriben",
    "Mi mamá lee",
    "El tren llega",
    "La vaca pasta",
    "El maestro enseña",
    "Ellos caminan",
    "Yo dibujo",
    "Mi hermana estudia",
    "El perro salta",
    "Los niños ríen",
    "El sol brilla",
    "La flor crece",
    "Mi primo juega",
    "Tú escuchas",
]

elogios = [
    "🌟 ¡Tu oración tiene mucho detalle!",
    "✅ ¡Muy bien! Usaste complementos claros.",
    "👏 ¡Excelente descripción!",
    "🧠 ¡Tu frase está completa y precisa!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES CON COMPLEMENTOS:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Practicar 20 ejercicios
def practicar_complementos():
    print("\n📝 AGREGA DETALLES A CADA ORACIÓN:")
    total = 0
    for i, base in enumerate(oraciones_base, 1):
        print(f"\n{str(i).zfill(2)}. Oración base: {base}")
        nueva = input("👉 Escribe tu oración completa: ").strip()
        puntos = 0
        if any(c in nueva.lower() for c in ["en", "por la", "con", "durante", "cada", "al", "a las"]):
            puntos += 1
        if len(nueva.split()) >= 6:
            puntos += 1
        if "." in nueva or "," in nueva:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total: {total}/60")
    if total >= 50:
        print("🏅 ¡Excelente! Sabes agregar detalles a las acciones.")
    elif total >= 35:
        print("👍 Buen trabajo. Puedes añadir más precisión o lugar.")
    else:
        print("📘 Revisa cómo escribir dónde, cuándo y cómo ocurre la acción.")

# ✍️ Crear oraciones propias
def crear_oraciones():
    print("\n✍️ ESCRIBE 5 ORACIONES CON COMPLEMENTOS:")
    total = 0
    for i in range(1, 6):
        frase = input(f"📝 Oración {i}: ").strip().lower()
        puntos = 0
        if any(c in frase for c in ["en", "por la", "con", "durante", "cada", "a las"]):
            puntos += 1
        if len(frase.split()) >= 6:
            puntos += 1
        if "." in frase or "," in frase:
            puntos += 1
        print(f"👉 Puntaje: {puntos}/3")
        total += puntos
    print(f"\n📊 Total creativo: {total}/15")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 3.º Grado – Lección 8: Complementos del verbo")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 frases 📝")
        print("4. Escribir tus propias oraciones ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_complementos()
        elif opcion == "4":
            crear_oraciones()
        elif opcion == "5":
            print("👋 ¡Gracias por enriquecer tus oraciones con contexto y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
