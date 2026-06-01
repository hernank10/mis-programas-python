import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO SUENAN LAS EMOCIONES EN NUESTRAS PALABRAS?

Las emociones nos ayudan a decir cómo nos sentimos.
🎯 Algunas emociones que usamos para escribir:

😀 ALEGRÍA → “¡Estoy feliz porque juego con mi perro!”
😢 TRISTEZA → “Estoy triste porque se fue mi amigo.”
😠 ENOJO → “Me enojé cuando rompieron mi dibujo.”
😲 SORPRESA → “¡Qué sorpresa ver un arco iris!”
😨 MIEDO → “Tengo miedo cuando hay muchos truenos.”
"""

# 🎭 Ejemplos guiados
ejemplos = [
    "¡Estoy feliz porque voy al parque!",
    "Estoy triste porque no vino mi abuela.",
    "Me enojé cuando perdí mi juguete.",
    "¡Qué sorpresa ver tantos globos!",
    "Tengo miedo cuando el cuarto está oscuro.",
]

# 📝 20 emociones para completar con oraciones
emociones = [
    "ALEGRÍA",
    "TRISTEZA",
    "ENOJO",
    "SORPRESA",
    "MIEDO",
] * 4  # 5 emociones x 4 = 20 frases

elogios = [
    "😊 ¡Tu oración expresa la emoción muy bien!",
    "👍 ¡Buen trabajo! Tu emoción está clara.",
    "🎉 ¡Tu frase suena como el corazón habla!",
    "💬 ¡Gran forma de decir cómo te sientes!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 🎭 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES CON EMOCIONES:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Practicar emociones
def practicar_emociones():
    print("\n📝 ESCRIBE UNA ORACIÓN QUE EXPRESE LA EMOCIÓN:")
    total = 0
    for i, emocion in enumerate(emociones, 1):
        print(f"\n{str(i).zfill(2)}. Emoción: {emocion}")
        frase = input("👉 Escribe tu oración: ").strip()
        puntos = 0
        if len(frase.split()) >= 5:
            puntos += 1
        if emocion.lower() in frase.lower():
            puntos += 1
        if "!" in frase or "." in frase:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Eres muy bueno expresando lo que sientes!")
    elif total >= 35:
        print("🙂 Vas muy bien. Puedes usar más palabras para cada emoción.")
    else:
        print("📘 Practica cómo decir lo que sientes con claridad.")

# ✍️ Escribir emociones propias
def escribir_personales():
    print("\n✍️ ESCRIBE 3 FRASES SOBRE CÓMO TE SIENTES:")
    total = 0
    for i in range(1, 4):
        frase = input(f"📝 Frase {i}: ").strip()
        puntos = 0
        if any(e in frase.lower() for e in ["alegría", "feliz", "triste", "enojo", "enojado", "miedo", "sorpresa"]):
            puntos += 1
        if len(frase.split()) >= 5:
            puntos += 1
        if "." in frase or "!" in frase:
            puntos += 1
        print(f"🎯 Puntos: {puntos}/3")
        total += puntos
    print(f"\n📊 Total creativo: {total}/9")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 1.º Grado – Lección 9: Emociones en oraciones")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 🎭")
        print("3. Practicar 20 oraciones con emociones 📝")
        print("4. Escribir emociones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_emociones()
        elif opcion == "4":
            escribir_personales()
        elif opcion == "5":
            print("👋 ¡Gracias por compartir tus emociones con palabras!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
