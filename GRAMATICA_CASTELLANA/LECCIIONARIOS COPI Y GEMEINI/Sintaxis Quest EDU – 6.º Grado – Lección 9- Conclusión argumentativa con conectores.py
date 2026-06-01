import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO SE CIERRA UN PÁRRAFO CON FUERZA?

Una buena conclusión:

🔹 Usa conectores de cierre → por eso, en conclusión, por lo tanto, de este modo
🔹 Reafirma la idea principal
🔹 Tiene sentido lógico con lo que se dijo antes

🎯 Ejemplo:
"Las mascotas enseñan cuidado y empatía. Muchos niños aprenden a respetar a otros al tener un animal en casa.
POR ESO, adoptar una mascota puede ser una buena forma de formar valores positivos."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "Leer todos los días mejora el vocabulario y la comprensión.\nPor lo tanto, debemos tener un momento diario para leer en silencio.",
    "El reciclaje ayuda al planeta y a nuestra comunidad.\nEn conclusión, es necesario enseñar a separar los residuos desde pequeños.",
    "Los trabajos en grupo enseñan colaboración y respeto.\nDe este modo, los estudiantes aprenden a dialogar y compartir responsabilidades.",
    "Hacer deporte mejora el cuerpo y el ánimo.\nPor eso, es bueno tener actividad física todos los días.",
]

# 📝 Mini párrafos para completar con conclusión
mini_parrafos = [
    "Los videojuegos pueden desarrollar estrategia y concentración.",
    "Estudiar con amigos permite resolver dudas y compartir ideas.",
    "Cuidar las plantas enseña paciencia y responsabilidad.",
    "Participar en clase ayuda a aprender y confiar en uno mismo.",
    "Dormir bien mejora la memoria y el rendimiento escolar.",
    "Leer noticias nos hace entender lo que pasa en el mundo.",
    "Hacer arte expresa emociones y desarrolla la creatividad.",
    "Ordenar el espacio ayuda a estudiar con más claridad.",
    "Hacer preguntas demuestra interés y ayuda a pensar mejor.",
    "Respetar las opiniones crea un ambiente sano en el aula.",
]

elogios = [
    "🌟 ¡Tu conclusión cierra la idea con claridad!",
    "✅ ¡Usaste un buen conector para cerrar!",
    "👏 ¡La idea final está bien conectada!",
    "🧠 ¡Tu cierre resume lo más importante!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CONCLUSIONES ARGUMENTATIVAS:")
    for ej in ejemplos:
        print(f"📝 {ej}\n")

# 📝 Completar párrafos con conclusión
def practicar_cierre():
    print("\n📝 AGREGA UNA CONCLUSIÓN A CADA TEXTO:")
    total = 0
    for i, texto in enumerate(mini_parrafos, 1):
        print(f"\n{str(i).zfill(2)}. Texto base:\n{texto}")
        respuesta = input("👉 Tu conclusión: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in ["por eso", "en conclusión", "por lo tanto", "de este modo"]):
            puntos += 1
        if len(respuesta.split()) >= 7:
            puntos += 1
        if "." in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/30")

# ✍️ Redacción libre
def redactar_parrafo():
    print("\n✍️ ESCRIBE UN PÁRRAFO CON DESARROLLO + CONCLUSIÓN:")
    desarrollo = input("📝 Escribe tu idea principal y desarrollo: ").strip()
    cierre = input("👉 Escribe una conclusión clara con conector: ").strip()
    texto = f"{desarrollo} {cierre}"
    puntos = 0
    if any(c in cierre.lower() for c in ["por eso", "en conclusión", "por lo tanto", "de este modo"]):
        puntos += 1
    if len(texto.split()) >= 30:
        puntos += 1
    if "." in cierre:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu párrafo está completo y bien cerrado!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes afinar la conexión entre ideas.")
    else:
        print("📘 Intenta hacer que tu cierre tenga más fuerza y claridad.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 6.º Grado – Lección 9: Conclusión argumentativa con conectores")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar conclusiones 📝")
        print("4. Escribir tu propio párrafo ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_cierre()
        elif opcion == "4":
            redactar_parrafo()
        elif opcion == "5":
            print("👋 ¡Gracias por cerrar tus ideas con fuerza y sentido!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
