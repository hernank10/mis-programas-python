import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO DESARROLLAMOS UNA TESIS EN PROFUNDIDAD?

Una tesis es una afirmación clara sobre un tema. Desarrollarla implica justificarla con ideas, ejemplos y explicaciones lógicas.

🎯 Estructura recomendada:
Tesis + conector + razón fundamentada

🔹 Conectores útiles:
- porque
- ya que
- debido a que
- además
- por ejemplo
- esto demuestra que

💡 Ejemplo:
"Toda institución educativa debe tener un espacio de lectura,
porque fomenta el pensamiento crítico, la imaginación y el hábito reflexivo."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "tesis": "El aprendizaje autónomo debe ser promovido en el aula.",
        "razon": "Porque permite que el estudiante desarrolle responsabilidad y descubra su propio estilo de aprender."
    },
    {
        "tesis": "La escritura argumentativa es esencial en la educación media.",
        "razon": "Ya que forma pensamiento crítico y enseña a sostener ideas con fundamento."
    },
    {
        "tesis": "Las ciencias sociales deben ocupar un lugar fuerte en el currículo.",
        "razon": "Debido a que ayudan a comprender estructuras sociales y contextos históricos relevantes."
    }
]

# 📝 20 tesis incompletas
ejercicios = [
    "La filosofía debería ser obligatoria en bachillerato",
    "Las TIC deben utilizarse con fines pedagógicos en clase",
    "La educación artística es tan importante como la científica",
    "La lectura crítica debe practicarse en todas las asignaturas",
    "La educación ambiental debe incluirse en cada nivel escolar",
    "La historia local debería tener más espacio en el currículo",
    "Los proyectos interdisciplinarios enriquecen el aprendizaje",
    "La expresión oral debe ser parte del proceso evaluativo",
    "El análisis de noticias debe integrarse al área de lenguaje",
    "Los estudiantes deben tener espacios de participación democrática",
    "La evaluación formativa es más útil que la sumativa",
    "Las salidas pedagógicas fortalecen los contenidos teóricos",
    "El trabajo colaborativo desarrolla habilidades blandas",
    "La creatividad debe ser valorada como competencia académica",
    "El pensamiento científico ayuda a resolver problemas reales",
    "El arte permite comprender emociones y contextos sociales",
    "La argumentación previene los discursos de odio",
    "Las ciencias naturales deben conectarse con la vida cotidiana",
    "La educación financiera debería enseñarse desde secundaria",
    "Los textos literarios permiten construir identidad cultural"
]

elogios = [
    "✅ Justificación clara y relevante.",
    "🌟 Desarrollo lógico y bien escrito.",
    "🎯 Tu tesis gana fuerza con esa razón.",
    "👏 Excelente conexión entre postura y argumento.",
    "🧠 Pensamiento profundo y bien estructurado."
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TESIS + DESARROLLO:")
    for ej in ejemplos:
        print(f"📝 Tesis: {ej['tesis']}")
        print(f"👉 Desarrollo: {ej['razon']}\n")

# 📝 Practicar 20 ejercicios evaluados
def practicar_tesis():
    print("\n📝 AGREGA UNA RAZÓN A CADA TESIS:\n")
    total = 0
    for i, tesis in enumerate(ejercicios, 1):
        print(f"{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip().lower()
        puntos = 0
        if any(c in razon for c in ["porque", "ya que", "debido a", "esto demuestra que", "por ejemplo"]):
            puntos += 1
        if len(razon.split()) >= 8:
            puntos += 1
        if "." in razon or "," in razon:
            puntos += 1
        fb = random.choice(elogios)
        print(f"{fb} (Puntaje: {puntos}/3)\n")
        total += puntos

    print(f"\n📊 TOTAL FINAL: {total}/60")
    if total >= 50:
        print("🏅 ¡Dominio avanzado! Justificas con profundidad y precisión.")
    elif total >= 35:
        print("👍 Buen nivel. Puedes mejorar la riqueza argumentativa.")
    else:
        print("📘 Practica más el uso de conectores y desarrollo lógico.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 11.º Grado – Lección 7: Desarrollo de tesis argumentativa")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar los 20 ejercicios 📝")
        print("4. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_tesis()
        elif opcion == "4":
            print("👋 ¡Gracias por fortalecer tu pensamiento argumentativo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
