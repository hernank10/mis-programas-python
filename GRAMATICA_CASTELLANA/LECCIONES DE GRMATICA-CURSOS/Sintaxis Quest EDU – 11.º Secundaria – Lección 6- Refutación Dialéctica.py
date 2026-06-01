import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – REFUTACIÓN ARGUMENTATIVA

Una refutación bien estructurada incluye tres partes clave:

1. TESIS: posición personal o idea principal
2. ARGUMENTO CONTRARIO: reconocimiento de una postura opuesta
3. REFUTACIÓN: respuesta crítica basada en evidencia, lógica o contraejemplo

🎯 Ejemplo:
"Tesis: Considero que el teletrabajo es una solución eficiente.
 Argumento contrario: Muchos afirman que reduce la productividad.
 Refutación: Sin embargo, estudios recientes muestran que permite mayor concentración y autonomía."

🔹 Conectores útiles:
- Contraste: aunque, sin embargo, no obstante
- Refuerzo lógico: en realidad, lo cierto es que, según estudios
"""

# 📚 Ejemplos explicados
ejemplos = [
    {
        "oracion": "Creo que los videojuegos pueden estimular la mente. Aunque algunos afirman que promueven violencia, estudios muestran que mejoran habilidades cognitivas.",
        "tesis": "los videojuegos pueden estimular la mente",
        "contrario": "promueven violencia",
        "refutacion": "mejoran habilidades cognitivas"
    },
    {
        "oracion": "Opino que la educación en línea es efectiva. Sin embargo, hay quienes dicen que reduce la interacción social. No obstante, permite flexibilidad y autonomía.",
        "tesis": "la educación en línea es efectiva",
        "contrario": "reduce la interacción social",
        "refutacion": "permite flexibilidad y autonomía"
    },
    {
        "oracion": "Pienso que leer novelas es enriquecedor. Aunque algunos creen que es una pérdida de tiempo, fortalece la imaginación y comprensión emocional.",
        "tesis": "leer novelas es enriquecedor",
        "contrario": "es una pérdida de tiempo",
        "refutacion": "fortalece la imaginación y comprensión emocional"
    }
]

# 📝 20 ejercicios
ejercicios = [
    {
        "oracion": "Afirmo que el uso de tecnología en clase mejora el aprendizaje. Algunos creen que distrae demasiado.",
        "tesis": "el uso de tecnología en clase mejora el aprendizaje",
        "contrario": "distrae demasiado"
    },
    {
        "oracion": "Creo que aprender idiomas en la adolescencia es más fácil. Sin embargo, otros opinan que genera confusión.",
        "tesis": "aprender idiomas en la adolescencia es más fácil",
        "contrario": "genera confusión"
    },
    {
        "oracion": "Considero que trabajar en equipo fortalece habilidades sociales. Aunque algunos prefieren trabajar solos.",
        "tesis": "trabajar en equipo fortalece habilidades sociales",
        "contrario": "prefieren trabajar solos"
    },
    {
        "oracion": "Pienso que llevar uniforme escolar ayuda a la disciplina. Algunos creen que limita la expresión personal.",
        "tesis": "llevar uniforme escolar ayuda a la disciplina",
        "contrario": "limita la expresión personal"
    },
    {
        "oracion": "Opino que las redes sociales conectan a las personas. Aunque muchos dicen que generan aislamiento.",
        "tesis": "las redes sociales conectan a las personas",
        "contrario": "generan aislamiento"
    }
]

elogios = [
    "👏 ¡Refutación clara y coherente!",
    "🧠 ¡Excelente estructura argumentativa!",
    "🌟 ¡Gran razonamiento dialéctico!",
    "🎯 ¡Matiz crítico logrado!",
    "⭐ ¡Pensamiento profundo y elegante!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos explicados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"\n🔹 Oración completa: {ej['oracion']}")
        print(f"👉 Tesis: {ej['tesis']}")
        print(f"👉 Argumento contrario: {ej['contrario']}")
        print(f"👉 Refutación: {ej['refutacion']}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['oracion']}")
        tesis = input("👉 ¿Cuál es la tesis?: ").strip().lower()
        contrario = input("👉 ¿Cuál es el argumento contrario?: ").strip().lower()

        if tesis == ej['tesis'].lower() and contrario == ej['contrario'].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era:\n👉 Tesis: '{ej['tesis']}'\n👉 Contrario: '{ej['contrario']}'")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Refutador Razonado! ⚖️")

# ✍️ Crear oraciones propias
def crear_ejemplos_usuario():
    print("\n✍️ REDACTA TUS PROPIAS REFUTACIONES")
    print("Escribe 20 estructuras completas (Tesis + Argumento contrario + Refutación):\n")
    personales = []
    for i in range(1, 21):
        print(f"\n💡 Oración {i}")
        tesis = input("👉 Tesis: ").strip()
        contrario = input("👉 Argumento contrario: ").strip()
        refutacion = input("👉 Refutación: ").strip()
        personales.append((tesis, contrario, refutacion))

    print("\n📘 Tus construcciones dialécticas:")
    for idx, (t, c, r) in enumerate(personales, 1):
        print(f"{idx}. Tesis: {t}")
        print(f"   Contrario: {c}")
        print(f"   Refutación: {r}")
    print("🏅 ¡Muy buen trabajo como Arquitecto del Pensamiento!")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 11.º Secundaria – Lección 6: Refutación Dialéctica")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir 20 estructuras propias ✍️")
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
            print("👋 ¡Gracias por debatir con lógica, respeto y estilo argumentativo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
