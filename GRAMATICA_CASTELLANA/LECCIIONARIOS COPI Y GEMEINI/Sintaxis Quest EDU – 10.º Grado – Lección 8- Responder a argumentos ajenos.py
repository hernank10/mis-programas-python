import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO RESPONDER A UNA POSTURA CON RESPETO Y RAZÓN?

Cuando respondemos a un argumento ajeno, debemos:

1️⃣ Reconocer la tesis del otro (aunque no estemos de acuerdo)  
2️⃣ Evaluar si sus razones son sólidas o débiles  
3️⃣ Formular nuestra propia postura con argumentos lógicos y respeto

🎯 Ejemplo:
"La educación debe centrarse en resultados medibles."
↪ RESPUESTA: "Es cierto que los resultados ayudan a evaluar avances.
Sin embargo, limitar la educación a lo medible ignora valores como la empatía o la creatividad,
que no siempre se cuantifican pero son esenciales en la formación humana."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "TEXTO: \"Los adolescentes no deberían opinar en temas educativos.\"\nRESPUESTA: \"Aunque algunos creen que no están preparados, opinar les permite formarse como ciudadanos activos y responsables.\"",
    "TEXTO: \"La literatura clásica ya no tiene valor para los jóvenes.\"\nRESPUESTA: \"Si bien puede parecer distante, la literatura clásica ofrece temas universales que conectan con emociones e historias actuales.\"",
    "TEXTO: \"El arte no debería ser parte del currículo obligatorio.\"\nRESPUESTA: \"A pesar de esa visión, el arte desarrolla sensibilidad, pensamiento lateral y expresión personal. Su ausencia empobrece la formación integral.\""
]

# 📝 20 ideas polémicas para evaluar y responder
temas = [
    "La educación debe enfocarse solo en materias científicas.",
    "Los celulares deberían prohibirse totalmente en clase.",
    "La escritura a mano es una habilidad obsoleta.",
    "La música no contribuye al desarrollo académico.",
    "Las redes sociales son una pérdida de tiempo.",
    "Los estudiantes deben competir para mejorar.",
    "La lectura digital arruina la capacidad de concentración.",
    "El deporte no tiene valor educativo real.",
    "La televisión educa más que la escuela.",
    "Los exámenes son la única forma justa de evaluar.",
    "La poesía es inútil en el mundo actual.",
    "Los adolescentes no deberían tener redes sociales.",
    "Los proyectos colaborativos no funcionan bien.",
    "El arte solo sirve para entretener.",
    "Los juegos en clase impiden el aprendizaje.",
    "Estudiar filosofía no sirve para la vida real.",
    "Los estudiantes no deben cuestionar a sus maestros.",
    "La memoria es más importante que el razonamiento.",
    "Las salidas pedagógicas son una distracción.",
    "La participación democrática en la escuela genera caos."
]

elogios = [
    "🌟 ¡Tu postura es crítica y respetuosa!",
    "✅ ¡Buen razonamiento y tono cordial!",
    "👏 ¡Tu respuesta equilibra análisis y argumento!",
    "🧠 ¡Excelente respuesta con fundamentos sólidos!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 RESPUESTAS CRÍTICAS A POSTURAS:")
    for ej in ejemplos:
        print(f"{ej}\n")

# 📝 Practicar respuestas
def practicar_respuestas():
    print("\n📝 RESPONDE A CADA FRASE POLÉMICA CON TU POSTURA:")
    total = 0
    for i, frase in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Postura ajena: \"{frase}\"")
        respuesta = input("👉 Tu respuesta crítica: ").strip().lower()
        puntos = 0
        if any(p in respuesta for p in ["aunque", "a pesar de", "sin embargo", "por otro lado", "es cierto que", "no obstante"]):
            puntos += 1
        if len(respuesta.split()) >= 20:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/60")
    if total >= 50:
        print("🏅 ¡Gran dominio del análisis crítico argumentativo!")
    elif total >= 35:
        print("👍 Buen avance. Puedes trabajar la profundidad y el respeto.")
    else:
        print("📘 Revisa cómo reconocer, evaluar y responder con equilibrio lógico.")

# ✍️ Respuesta libre a texto externo
def responder_libre():
    print("\n✍️ ESCRIBE TU RESPUESTA A UN TEXTO DE OPINIÓN:")
    texto = input("📝 ¿Cuál es la frase que vas a responder?: ").strip()
    respuesta = input("👉 Tu postura crítica y razonada: ").strip().lower()
    puntos = 0
    if any(p in respuesta for p in ["aunque", "a pesar de", "sin embargo", "es cierto que", "por otro lado", "no obstante"]):
        puntos += 1
    if len(respuesta.split()) >= 30:
        puntos += 1
    if "." in respuesta and "," in respuesta:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu respuesta es clara, respetuosa y bien argumentada!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes desarrollar más tus razones.")
    else:
        print("📘 Intenta ser más preciso y equilibrado al responder.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Grado – Lección 8: Responder a argumentos ajenos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 respuestas críticas 📝")
        print("4. Escribir una respuesta libre ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_respuestas()
        elif opcion == "4":
            responder_libre()
        elif opcion == "5":
            print("👋 ¡Gracias por aprender a pensar con respeto y criterio propio!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
