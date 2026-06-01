import random

# 📘 Teoría explicada
teoria = """
📘 LECCIÓN 6 – CONTRAARGUMENTOS Y CONCESIONES

Una oración argumentativa avanzada considera la opinión contraria (contraargumento) y la matiza con una concesión o refuerzo personal.

🔹 ESTRUCTURA:
1. Tesis → ¿Qué pienso?
2. Contraargumento → ¿Qué piensan otros?
3. Concesión/Refuerzo → ¿Qué reconozco y cómo sostengo mi punto?

🎯 Ejemplo:
"Tesis: Creo que los videojuegos pueden ser beneficiosos.
 Contraargumento: Algunos dicen que causan adicción.
 Concesión: Aunque eso puede ocurrir, su uso moderado mejora habilidades cognitivas."
"""

# 📚 Ejemplos explicados
ejemplos = [
    {
        "oracion": "Pienso que estudiar arte es esencial, aunque algunos creen que no es práctico. Sin embargo, fomenta la creatividad y sensibilidad.",
        "tesis": "estudiar arte es esencial",
        "contraargumento": "no es práctico",
        "refuerzo": "fomenta la creatividad y sensibilidad"
    },
    {
        "oracion": "Creo que los teléfonos móviles son útiles, aunque se diga que distraen. En realidad, ayudan a organizar nuestras tareas.",
        "tesis": "los teléfonos móviles son útiles",
        "contraargumento": "distraen",
        "refuerzo": "ayudan a organizar nuestras tareas"
    },
    {
        "oracion": "Considero que leer en papel es mejor, aunque muchos prefieren lo digital. No obstante, el papel permite mejor concentración.",
        "tesis": "leer en papel es mejor",
        "contraargumento": "prefieren lo digital",
        "refuerzo": "permite mejor concentración"
    }
]

# 📝 20 ejercicios argumentativos
ejercicios = [
    {
        "oracion": "Pienso que usar bicicleta es saludable, aunque algunos creen que es peligroso.",
        "tesis": "usar bicicleta es saludable",
        "contraargumento": "es peligroso"
    },
    {
        "oracion": "Afirmo que estudiar en grupo mejora el aprendizaje, aunque algunos prefieren hacerlo solos.",
        "tesis": "estudiar en grupo mejora el aprendizaje",
        "contraargumento": "prefieren hacerlo solos"
    },
    {
        "oracion": "Creo que la música clásica relaja, aunque otros la consideran aburrida.",
        "tesis": "la música clásica relaja",
        "contraargumento": "la consideran aburrida"
    },
    {
        "oracion": "Opino que cocinar es una habilidad importante, aunque algunos piensan que lleva demasiado tiempo.",
        "tesis": "cocinar es una habilidad importante",
        "contraargumento": "lleva demasiado tiempo"
    },
    {
        "oracion": "Pienso que aprender matemáticas es útil, aunque hay quienes piensan que no se aplica en la vida real.",
        "tesis": "aprender matemáticas es útil",
        "contraargumento": "no se aplica en la vida real"
    },
    {
        "oracion": "Afirmo que leer poesía es enriquecedor, aunque muchos creen que es difícil de entender.",
        "tesis": "leer poesía es enriquecedor",
        "contraargumento": "es difícil de entender"
    },
    {
        "oracion": "Creo que el trabajo voluntario construye carácter, aunque algunos dicen que es pérdida de tiempo.",
        "tesis": "el trabajo voluntario construye carácter",
        "contraargumento": "es pérdida de tiempo"
    },
    {
        "oracion": "Opino que el debate escolar desarrolla pensamiento crítico, aunque no todos disfrutan discutir.",
        "tesis": "el debate escolar desarrolla pensamiento crítico",
        "contraargumento": "no todos disfrutan discutir"
    },
    {
        "oracion": "Pienso que la educación sexual en la escuela es necesaria, aunque algunos piensen que debe tratarse en casa.",
        "tesis": "la educación sexual en la escuela es necesaria",
        "contraargumento": "debe tratarse en casa"
    },
    {
        "oracion": "Afirmo que tener mascotas enseña responsabilidad, aunque hay quienes creen que son una carga.",
        "tesis": "tener mascotas enseña responsabilidad",
        "contraargumento": "son una carga"
    }
]

elogios = [
    "🎯 ¡Análisis reflexivo!",
    "🧠 ¡Concesión bien integrada!",
    "🌟 ¡Gran estructura argumentativa!",
    "👏 ¡Contraargumento identificado!",
    "⭐ ¡Excelente pensamiento crítico!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos explicados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Tesis: {ej['tesis']}\n   Contraargumento: {ej['contraargumento']}\n   Refuerzo: {ej['refuerzo']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['oracion']}")
        tesis = input("👉 ¿Cuál es la tesis?: ").strip().lower()
        contra = input("👉 ¿Cuál es el contraargumento?: ").strip().lower()

        if tesis == ej["tesis"].lower() and contra == ej["contraargumento"].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era:\n👉 Tesis: '{ej['tesis']}'\n👉 Contraargumento: '{ej['contraargumento']}'")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Refutador Elegante! ⚖️")

# ✍️ Crear oraciones propias
def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES CON CONTRAARGUMENTOS")
    print("Escribe 20 frases con: Tesis + Contraargumento + Refuerzo (ej. 'Creo que... aunque... Sin embargo...'):\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo argumentativo y reflexivo!")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Secundaria – Lección 6: Contraargumentos y Concesiones")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
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
            print("👋 ¡Gracias por debatir con precisión y respeto sintáctico!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Iniciar el programa
if __name__ == "__main__":
    menu()
