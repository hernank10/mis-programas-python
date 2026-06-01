import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO HABLAMOS SEGÚN LO QUE QUEREMOS DECIR?

Las oraciones pueden tener diferentes intenciones:

1️⃣ ENUNCIATIVAS → dicen algo (“El gato duerme.”)
2️⃣ INTERROGATIVAS → hacen una pregunta (“¿Dónde está mi pelota?”)
3️⃣ EXCLAMATIVAS → muestran emoción (“¡Qué rico el helado!”)
4️⃣ IMPERATIVAS → dan una orden o indicación (“Ven aquí por favor.”)

🎯 Cada tipo usa distintos signos: . ¿? ¡!
"""

# 📚 Ejemplos guiados
ejemplos = {
    "ENUNCIATIVA": "El niño juega en el parque.",
    "INTERROGATIVA": "¿Qué comiste hoy?",
    "EXCLAMATIVA": "¡Estoy muy feliz!",
    "IMPERATIVA": "Escribe tu nombre en la hoja."
}

# 📝 Frases desordenadas para clasificar
frases_clasificar = [
    "¡Qué divertido fue el paseo!",
    "¿Quién rompió el cuaderno?",
    "Apaga la luz, por favor.",
    "Mi abuela hace pan cada mañana.",
    "¡Hace mucho frío!",
    "¿Cuántos años tienes?",
    "Corre rápido al salón.",
    "La flor es amarilla.",
    "¡Me asusté con ese ruido!",
    "¿Dónde están mis zapatos?",
    "Lávate las manos antes de comer.",
    "Pedro tiene una tortuga.",
    "¡Estoy muy cansado!",
    "¿Qué vamos a dibujar hoy?",
    "Haz silencio en la biblioteca.",
    "Mi mochila está en el sillón.",
    "¡Qué sorpresa verte aquí!",
    "¿Cómo se llama tu perro?",
    "Lee el cuento con atención.",
    "Yo tengo dos hermanos.",
]

elogios = [
    "🌟 ¡Clasificaste muy bien!",
    "✅ ¡Buena observación del tipo de oración!",
    "👏 ¡Tus respuestas muestran atención!",
    "🎉 ¡Gran trabajo reconociendo las intenciones!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CADA TIPO DE ORACIÓN:")
    for tipo, frase in ejemplos.items():
        print(f"{tipo}: {frase}")

# 📝 Clasificar frases
def clasificar_oraciones():
    print("\n📝 ESCRIBE EL TIPO DE ORACIÓN: Enunciativa / Interrogativa / Exclamativa / Imperativa")
    total = 0
    for i, frase in enumerate(frases_clasificar, 1):
        print(f"\n{str(i).zfill(2)}. Frase: {frase}")
        respuesta = input("👉 Tipo de oración: ").strip().lower()
        puntos = 0
        if respuesta in ["enunciativa", "interrogativa", "exclamativa", "imperativa"]:
            puntos += 1
        if respuesta in frase.lower():
            puntos += 1
        if len(respuesta) > 5:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total: {total}/60")

# ✍️ Crear oraciones
def crear_oraciones():
    print("\n✍️ ESCRIBE UNA ORACIÓN DE CADA TIPO:")
    tipos = ["Enunciativa", "Interrogativa", "Exclamativa", "Imperativa"]
    total = 0
    for tipo in tipos:
        frase = input(f"📝 Tu oración {tipo}: ").strip()
        puntos = 0
        if tipo.lower() in frase.lower():
            puntos += 1
        if len(frase.split()) >= 5:
            puntos += 1
        if any(s in frase for s in [".", "?", "¡", "!"]):
            puntos += 1
        print(f"🎯 Puntos: {puntos}/3")
        total += puntos
    print(f"\n📊 Total creativo: {total}/12")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 2.º Grado – Lección 9: Tipos de oración según intención")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Clasificar 20 oraciones 📝")
        print("4. Escribir tus propias oraciones ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            clasificar_oraciones()
        elif opcion == "4":
            crear_oraciones()
        elif opcion == "5":
            print("👋 ¡Gracias por aprender a expresar lo que pensamos con intención y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
