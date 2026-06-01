import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO RESPONDER PREGUNTAS COMPLEJAS CON ESCRITURA CRÍTICA?

Un buen ensayo reflexivo parte de una pregunta abierta. Debe incluir:

1️⃣ Tesis compleja → No una respuesta simple, sino una posición razonada  
2️⃣ Experiencia personal → Qué has vivido o observado que conecte con el tema  
3️⃣ Fuente externa → Cita, estudio o opinión que apoye o desafíe tu idea  
4️⃣ Reflexión ética o cultural → ¿Por qué este tema importa? ¿Qué implica?

🎯 Ejemplo de pregunta:
"¿La inteligencia artificial nos vuelve más sabios o más dependientes?"

✅ Tesis: "La sabiduría no depende de la herramienta, sino del uso que le damos."

↪ Desarrollo: Se incluye una anécdota, una fuente académica, y una reflexión sobre cómo pensamos hoy.
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "pregunta": "¿El progreso tecnológico mejora nuestras vidas o las complica?",
        "tesis": "La tecnología mejora nuestras posibilidades, pero exige responsabilidad para no perder lo humano.",
        "experiencia": "Durante el confinamiento, las videollamadas me acercaron a personas lejanas, pero también me alejaron de quienes estaban cerca.",
        "cita": "Según Sherry Turkle, 'la tecnología nos conecta, pero también nos aleja de la presencia plena'.",
        "reflexion": "La pregunta no tiene una respuesta definitiva, pero sí exige una conciencia crítica sobre cómo vivimos con las máquinas."
    },
    {
        "pregunta": "¿Debemos siempre decir lo que pensamos?",
        "tesis": "La sinceridad es valiosa, pero el contexto y el respeto definen su impacto.",
        "experiencia": "Recuerdo haber dicho una verdad dolorosa sin pensar, y lastimé a alguien por querer ser honesto.",
        "cita": "En palabras de Confucio: 'La sabiduría consiste en saber cuándo hablar y cuándo callar.'",
        "reflexion": "Ser auténtico no significa ser impulsivo. Pensar antes de hablar es también una forma de ética."
    }
]

# 📝 20 preguntas abiertas
preguntas = [
    "¿La educación debería enseñar a cuestionar lo que creemos?",
    "¿El arte tiene el poder de cambiar la sociedad?",
    "¿Somos más libres gracias a la tecnología o más vigilados?",
    "¿Qué significa ser auténtico en la era digital?",
    "¿La ciencia puede responder todas nuestras preguntas?",
    "¿El éxito académico garantiza el éxito en la vida?",
    "¿Es más valioso saber pensar o saber obedecer?",
    "¿Debemos olvidar el pasado para avanzar?",
    "¿El humor tiene límites éticos?",
    "¿La felicidad depende de nosotros o de los demás?",
    "¿El activismo juvenil tiene impacto real?",
    "¿Podemos aprender sin equivocarnos?",
    "¿El consumo nos define como sociedad?",
    "¿El sistema educativo prepara para el mundo real?",
    "¿La empatía puede aprenderse?",
    "¿La globalización borra las culturas locales?",
    "¿Las redes sociales nos hacen más visibles o más vulnerables?",
    "¿El arte debe tener una función social?",
    "¿La escritura puede cambiar la manera de pensar?",
    "¿La inteligencia artificial debe tener límites éticos?"
]

elogios = [
    "🌟 ¡Tu reflexión plantea ideas profundas!",
    "✅ ¡Tesis y fuentes bien articuladas!",
    "👏 ¡Tu párrafo conecta lo personal con lo ético!",
    "🧠 ¡Gran desarrollo de pensamiento complejo!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE PÁRRAFOS REFLEXIVOS:")
    for ej in ejemplos:
        print(f"📝 Pregunta: {ej['pregunta']}\nTesis: {ej['tesis']}\nExperiencia: {ej['experiencia']}\nCita: {ej['cita']}\nReflexión: {ej['reflexion']}\n")

# 📝 Practicar desarrollo
def practicar_ensayo():
    print("\n📝 RESPONDE CADA PREGUNTA CON TESIS + EXPERIENCIA + CITA + REFLEXIÓN:")
    total = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n{str(i).zfill(2)}. Pregunta: {pregunta}")
        tesis = input("👉 Tesis compleja: ").strip().lower()
        experiencia = input("👉 Relato o experiencia personal breve: ").strip().lower()
        fuente = input("👉 Cita o referencia (real o ficticia): ").strip().lower()
        reflexion = input("👉 Reflexión ética o cultural: ").strip().lower()
        texto = f"{tesis} {experiencia} {fuente} {reflexion}"
        puntos = 0
        if len(texto.split()) >= 40:
            puntos += 1
        if any(p in fuente for p in ["según", "como afirma", "en palabras de", "dice", "escribe"]):
            puntos += 1
        if "." in texto and "," in texto:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/60")

# ✍️ Composición libre
def redactar_libre():
    print("\n✍️ REDACTA UN PÁRRAFO REFLEXIVO COMPLETO:")
    pregunta = input("📝 ¿Cuál es tu pregunta abierta?: ").strip()
    tesis = input("👉 Tesis compleja: ").strip()
    experiencia = input("👉 Relato breve personal: ").strip()
    fuente = input("👉 Cita o referencia: ").strip()
    reflexion = input("👉 Reflexión ética o cultural: ").strip()
    texto = f"{pregunta} {tesis} {experiencia} {fuente} {reflexion}"
    puntos = 0
    if len(texto.split()) >= 50:
        puntos += 1
    if any(p in fuente.lower() for p in ["según", "como afirma", "en palabras de", "dice", "escribe"]):
        puntos += 1
    if "." in texto and "," in texto:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu texto invita a pensar con madurez y profundidad!")
    elif puntos == 2:
        print("✅ Buen comienzo. Puedes desarrollar más la conexión entre elementos.")
    else:
        print("📘 Intenta afinar tu tesis y comentario sobre la cita.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 12.º Grado – Lección 8: Ensayo reflexivo con pregunta abierta")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar con 20 preguntas 📝")
        print("4. Redactar tu propio texto ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ensayo()
        elif opcion == "4":
            redactar_libre()
        elif opcion == "5":
            print("👋 ¡Gracias por escribir con profundidad, ética y pensamiento crítico!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
