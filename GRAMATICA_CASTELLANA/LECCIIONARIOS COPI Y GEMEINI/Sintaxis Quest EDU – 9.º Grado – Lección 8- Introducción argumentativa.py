import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO REDACTAMOS UNA INTRODUCCIÓN EFECTIVA?

Una buena introducción incluye:

1️⃣ Gancho → Algo que despierte interés (pregunta, dato curioso, cita, problema)
2️⃣ Contexto → Breve explicación del tema o situación
3️⃣ Tesis → Postura clara que se argumentará

🎯 Ejemplo:
"¿Qué pasaría si nuestras ideas fueran escuchadas desde la adolescencia?
En muchas escuelas, los jóvenes son vistos como receptores, no como participantes.
Sin embargo, deben tener voz en decisiones escolares, porque eso fortalece el compromiso y la ciudadanía."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "¿Puede el arte cambiar la forma en que entendemos el mundo?\nDesde la antigüedad, la creación artística ha sido una forma de expresión profunda y transformadora.\nPor eso, incluir educación artística en todas las etapas escolares es fundamental para el desarrollo humano.",
    "Las redes sociales son parte de nuestra vida diaria.\nMuchos jóvenes las utilizan para informarse, aprender y compartir ideas.\nPor lo tanto, deben incluirse dentro del enfoque educativo como herramienta reflexiva.",
    "¿Deberían los adolescentes opinar sobre lo que aprenden?\nEn muchos colegios, el currículo se impone sin consulta.\nSin embargo, permitir participación juvenil fortalece la motivación y responsabilidad escolar."
]

# 📝 20 temas para redactar introducciones
temas = [
    "Los videojuegos pueden tener valor educativo.",
    "Las normas escolares deben construirse con participación estudiantil.",
    "La escritura creativa fomenta el pensamiento crítico.",
    "Los adolescentes deberían aprender sobre finanzas personales.",
    "La lectura digital es tan rica como la lectura impresa.",
    "Los exámenes escritos no deben ser la única forma de evaluación.",
    "El debate escolar debe ser parte de todas las materias.",
    "La educación ambiental necesita más espacio en el currículo.",
    "La filosofía estimula el pensamiento lógico en jóvenes.",
    "Las redes sociales pueden formar ciudadanía crítica.",
    "Los adolescentes deben tener espacios para expresar emociones.",
    "Las salidas pedagógicas enriquecen el aprendizaje en el aula.",
    "La música desarrolla concentración y sensibilidad.",
    "La poesía permite explorar la identidad personal.",
    "Los docentes deben usar tecnología con fines pedagógicos.",
    "Aprender otro idioma abre oportunidades laborales.",
    "La alimentación escolar debe incluir opciones saludables.",
    "El cine puede ser usado como recurso para enseñar historia.",
    "La participación en proyectos comunitarios educa más allá del aula.",
    "Los juegos de mesa pueden enseñar lógica y estrategia."
]

elogios = [
    "🌟 ¡Introducción clara y bien estructurada!",
    "✅ ¡Gancho y tesis bien conectadas!",
    "👏 ¡Tu texto invita a pensar!",
    "🧠 ¡Excelente apertura argumentativa!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE INTRODUCCIONES:")
    for ej in ejemplos:
        print(f"📝 {ej}\n")

# 📝 Practicar con temas base
def practicar_intro():
    print("\n📝 REDACTA UNA INTRODUCCIÓN CON GANCHO + CONTEXTO + TESIS:")
    total = 0
    for i, tema in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Tema: {tema}")
        intro = input("👉 Escribe tu introducción: ").strip().lower()
        puntos = 0
        if any(c in intro for c in ["¿", "por eso", "por lo tanto", "sin embargo", "en consecuencia"]):
            puntos += 1
        if len(intro.split()) >= 30:
            puntos += 1
        if "." in intro and "," in intro:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/60")
    if total >= 50:
        print("🏅 ¡Gran dominio de estructura argumentativa!")
    elif total >= 35:
        print("👍 Buen comienzo. Puedes afinar conexión entre ideas.")
    else:
        print("📘 Practica más cómo abrir con claridad y profundidad.")

# ✍️ Redacción libre
def crear_intro():
    print("\n✍️ ESCRIBE UNA INTRODUCCIÓN PARA TU TEMA:")
    tema = input("📝 ¿Cuál es tu tema?: ").strip()
    gancho = input("👉 Gancho (pregunta, dato, cita): ").strip()
    contexto = input("👉 Contexto breve: ").strip()
    tesis = input("👉 Tesis clara: ").strip()
    texto = f"{gancho} {contexto} {tesis}"
    puntos = 0
    if len(texto.split()) >= 40:
        puntos += 1
    if "." in texto and "," in texto:
        puntos += 1
    if any(c in gancho for c in ["¿", "?"]):
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu introducción está completa y atractiva!")
    elif puntos == 2:
        print("✅ Buen esfuerzo. Puedes mejorar la conexión entre partes.")
    else:
        print("📘 Revisa cómo conectar el gancho, el contexto y la tesis.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Grado – Lección 8: Introducción argumentativa")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar con 20 temas 📝")
        print("4. Escribir tu propia introducción ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_intro()
        elif opcion == "4":
            crear_intro()
        elif opcion == "5":
            print("👋 ¡Gracias por aprender a abrir tus textos con estrategia y estilo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
