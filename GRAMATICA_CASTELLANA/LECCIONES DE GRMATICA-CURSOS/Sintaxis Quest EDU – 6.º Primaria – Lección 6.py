import random

teoria = """
📘 LECCIÓN 6 – COMPLEMENTO DIRECTO

El complemento directo (CD) completa el significado del verbo. Es aquello sobre lo que recae la acción.

🔹 ¿Cómo encontrarlo?
- Preguntamos: ¿Qué...? / ¿A quién...? después del verbo
- Si responde claramente sin preposición, es CD

🎯 Ejemplo:
- "El perro mordió el zapato."
  👉 ¿Qué mordió? → el zapato → CD
"""

ejemplos = [
    {"oracion": "Ana escribió una carta.", "verbo": "escribió", "cd": "una carta"},
    {"oracion": "Juan pintó un paisaje.", "verbo": "pintó", "cd": "un paisaje"},
    {"oracion": "La maestra explicó el tema.", "verbo": "explicó", "cd": "el tema"},
    {"oracion": "Los niños leyeron el cuento.", "verbo": "leyeron", "cd": "el cuento"},
    {"oracion": "Mi amiga escuchó la canción.", "verbo": "escuchó", "cd": "la canción"}
]

ejercicios = [
    {"oracion": "Carlos dibujó un árbol.", "cd": "un árbol"},
    {"oracion": "María comió una manzana.", "cd": "una manzana"},
    {"oracion": "La policía atrapó al ladrón.", "cd": "al ladrón"},
    {"oracion": "El jugador pateó el balón.", "cd": "el balón"},
    {"oracion": "Los estudiantes escribieron sus nombres.", "cd": "sus nombres"},
    {"oracion": "Papá arregló la bicicleta.", "cd": "la bicicleta"},
    {"oracion": "El perro rompió el cojín.", "cd": "el cojín"},
    {"oracion": "La niña abrazó a su abuela.", "cd": "a su abuela"},
    {"oracion": "El chef cocinó la sopa.", "cd": "la sopa"},
    {"oracion": "Los soldados defendieron la ciudad.", "cd": "la ciudad"},
    {"oracion": "Mi hermana leyó una revista.", "cd": "una revista"},
    {"oracion": "El gato atrapó un ratón.", "cd": "un ratón"},
    {"oracion": "Los niños rompieron el papel.", "cd": "el papel"},
    {"oracion": "La profesora entregó las tareas.", "cd": "las tareas"},
    {"oracion": "El mago mostró el truco.", "cd": "el truco"},
    {"oracion": "Mi tío compró un coche.", "cd": "un coche"},
    {"oracion": "La madre lavó la ropa.", "cd": "la ropa"},
    {"oracion": "Los amigos jugaron el videojuego.", "cd": "el videojuego"},
    {"oracion": "El niño lanzó la pelota.", "cd": "la pelota"},
    {"oracion": "El grupo escuchó la música.", "cd": "la música"}
]

elogios = ["🎯 ¡Muy bien!", "🧠 ¡Complemento directo identificado!", "🌟 ¡Análisis preciso!", "👏 ¡Respuesta correcta!", "⭐ ¡Excelente sintaxis!"]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Verbo: {ej['verbo']} | Complemento directo: {ej['cd']}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Oración: {ej['oracion']}")
        respuesta = input("👉 ¿Cuál es el complemento directo?: ").strip().lower()
        if respuesta == ej["cd"].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: '{ej['cd']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Cazador de Complementos! 🧠📝")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES")
    print("Escribe 20 oraciones con complemento directo:\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo estructural!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 6.º Primaria – Lección 6")
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
            print("👋 ¡Gracias por descubrir lo esencial en el predicado!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
