import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – TIPO DE ORACIÓN SEGÚN INTENCIÓN

Las oraciones pueden cambiar según lo que queremos expresar:

🔹 ENUNCIATIVA: dice algo (afirma o niega)
   Ej.: "El perro duerme."

🔹 INTERROGATIVA: pregunta algo
   Ej.: "¿Dónde duerme el perro?"

🔹 EXCLAMATIVA: expresa emoción o sorpresa
   Ej.: "¡Qué bonito es el perro!"

Cada oración tiene una intención diferente. ¡Aprendamos a reconocerlas!
"""

# 📚 Ejemplos explicados
ejemplos = [
    {"oracion": "El niño juega en el parque.", "tipo": "enunciativa"},
    {"oracion": "¿Qué haces en el parque?", "tipo": "interrogativa"},
    {"oracion": "¡Me encanta el parque!", "tipo": "exclamativa"},
    {"oracion": "La maestra lee un cuento.", "tipo": "enunciativa"},
    {"oracion": "¿Dónde está la maestra?", "tipo": "interrogativa"}
]

# 📝 20 ejercicios
ejercicios = [
    {"oracion": "¿Por qué lloras?", "respuesta": "interrogativa"},
    {"oracion": "Mi hermana canta una canción.", "respuesta": "enunciativa"},
    {"oracion": "¡Qué deliciosa es la sopa!", "respuesta": "exclamativa"},
    {"oracion": "¿Cuándo iremos al zoológico?", "respuesta": "interrogativa"},
    {"oracion": "¡Me caí de la silla!", "respuesta": "exclamativa"},
    {"oracion": "Nosotros leemos juntos.", "respuesta": "enunciativa"},
    {"oracion": "¡Qué grande es ese árbol!", "respuesta": "exclamativa"},
    {"oracion": "¿Quién me llamó?", "respuesta": "interrogativa"},
    {"oracion": "Hoy comí arroz con pollo.", "respuesta": "enunciativa"},
    {"oracion": "¡Estoy muy feliz!", "respuesta": "exclamativa"},
    {"oracion": "¿Qué hay en la caja?", "respuesta": "interrogativa"},
    {"oracion": "Ayer llovió mucho.", "respuesta": "enunciativa"},
    {"oracion": "¡Qué divertido fue el juego!", "respuesta": "exclamativa"},
    {"oracion": "¿Cómo se llama tu amigo?", "respuesta": "interrogativa"},
    {"oracion": "Jugamos con nuestros juguetes.", "respuesta": "enunciativa"},
    {"oracion": "¡Auxilio!", "respuesta": "exclamativa"},
    {"oracion": "¿Dónde quedó mi mochila?", "respuesta": "interrogativa"},
    {"oracion": "El gato duerme en su cama.", "respuesta": "enunciativa"},
    {"oracion": "¡Qué miedo me dio!", "respuesta": "exclamativa"},
    {"oracion": "¿Puedo salir a jugar?", "respuesta": "interrogativa"}
]

elogios = ["🎉 ¡Muy bien!", "🧠 ¡Qué atento estás!", "👏 ¡Excelente análisis!", "🌟 ¡Dominio de intenciones!", "⭐ ¡Perfecto!"]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Tipo: {ej['tipo'].capitalize()}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['oracion']}")
        respuesta = input("👉 ¿Qué tipo es? (enunciativa / interrogativa / exclamativa): ").strip().lower()
        if respuesta == ej["respuesta"]:
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: '{ej['respuesta']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Detective de Intenciones! 🎭")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES")
    print("Escribe 20 frases diferentes: unas deben decir algo, otras preguntar y otras exclamar.\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo creativo!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 3.º Primaria – Lección 6")
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
            print("👋 ¡Gracias por descubrir cómo hablamos y preguntamos!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
