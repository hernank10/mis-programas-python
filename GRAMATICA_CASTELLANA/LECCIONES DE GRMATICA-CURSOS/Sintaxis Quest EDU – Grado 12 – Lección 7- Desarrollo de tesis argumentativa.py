# Sintaxis Quest EDU – Grado 12 – Lección 7

import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO SOSTENEMOS UNA TESIS EN PROFUNDIDAD?

Una tesis no solo afirma una idea: requiere contexto, justificación lógica y desarrollo argumentativo.

🎯 Estructura recomendada:
Tesis + conector + razón + ampliación argumentativa

🔹 Conectores:
- porque
- ya que
- debido a que
- por otro lado
- esto revela que
- además

💡 Ejemplo:
“La filosofía debería estar presente en todos los grados educativos,
porque estimula la reflexión crítica, permite discutir ideas complejas
y enseña a argumentar con respeto en contextos diversos.”
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "tesis": "La educación debe fomentar la investigación en estudiantes desde temprana edad.",
        "razon": "Porque los hábitos indagatorios despiertan autonomía intelectual y preparan para la vida universitaria."
    },
    {
        "tesis": "La cultura científica debería ser parte del discurso ciudadano.",
        "razon": "Ya que permite comprender temas complejos como salud pública, ecología o avances tecnológicos con criterio."
    },
    {
        "tesis": "El análisis de discursos mediáticos debería enseñarse en lengua.",
        "razon": "Porque fortalece la capacidad de distinguir información, manipulación o sesgos ideológicos en textos cotidianos."
    }
]

# 📝 20 tesis incompletas
ejercicios = [
    "El pensamiento crítico debería ser eje transversal en la educación secundaria",
    "La formación ética debe vincularse con problemáticas reales y actuales",
    "La alfabetización mediática debería impartirse desde la adolescencia",
    "La lectura literaria fomenta más que solo habilidades comunicativas",
    "La educación financiera es esencial en sociedades de consumo",
    "El estudio del arte promueve perspectivas diversas sobre lo humano",
    "La historia no debe limitarse a fechas, sino comprender procesos sociales",
    "Los modelos educativos deben adaptarse a realidades territoriales",
    "Las habilidades discursivas son clave en entornos profesionales",
    "El conocimiento interdisciplinario amplía la comprensión de fenómenos complejos",
    "La oralidad académica necesita más espacios de práctica escolar",
    "El análisis de noticias debe vincularse con competencias argumentativas",
    "La lógica formal contribuye a una comunicación más rigurosa",
    "La neuroeducación puede transformar la forma en que enseñamos",
    "La educación ambiental debería incluir dilemas éticos y debates sociales",
    "El diseño curricular debe incluir pluralidad cultural y enfoque de género",
    "El aprendizaje colaborativo fortalece procesos cognitivos y sociales",
    "La investigación escolar debería tener impacto local y comunitario",
    "El ensayo como forma permite articular múltiples perspectivas con rigor",
    "La narrativa personal también tiene valor como recurso académico"
]

elogios = [
    "🧠 Excelente desarrollo argumentativo.",
    "🌟 Tu postura está bien sustentada.",
    "🎯 Justificación sólida y profunda.",
    "✅ Razón coherente, clara y pertinente.",
    "👏 Redacción académica bien lograda."
]

# 🧠 Evaluador automático
def evaluar_respuesta(razon):
    razon = razon.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a que", "por ejemplo", "esto revela que", "además"]
    if any(c in razon for c in conectores):
        puntos += 1
    if len(razon.split()) >= 12:
        puntos += 1
    if "." in razon or "," in razon:
        puntos += 1
    return puntos

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TESIS + DESARROLLO:")
    for ej in ejemplos:
        print(f"📝 Tesis: {ej['tesis']}")
        print(f"👉 Desarrollo: {ej['razon']}\n")

# 📝 Practicar los 20 ejercicios
def practicar_ejercicios():
    print("\n📝 AGREGA UNA RAZÓN Y DESARROLLO A CADA TESIS:\n")
    total = 0
    for i, tesis in enumerate(ejercicios, 1):
        print(f"{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip()
        puntos = evaluar_respuesta(razon)
        total += puntos
        if puntos == 3:
            fb = "🏅 Justificación profunda y bien desarrollada."
        elif puntos == 2:
            fb = "✅ Buen argumento. Puedes ampliar o profundizar más."
        elif puntos == 1:
            fb = "⚠️ Razonamiento débil. Añade conectores y explicación."
        else:
            fb = "❌ No se detectó argumento claro ni conectores adecuados."
        print(f"{random.choice(elogios)} ({fb} Puntaje: {puntos}/3)\n")
    print(f"\n📊 TOTAL FINAL: {total}/60")
    if total >= 50:
        print("🏅 ¡Nivel universitario avanzado! Tus respuestas evidencian pensamiento académico.")
    elif total >= 35:
        print("👍 Buen nivel. Puedes afinar estilo y profundidad argumentativa.")
    else:
        print("📘 Revisa conectores, amplitud de ideas y claridad lógica.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – Grado 12 – Lección 7: Desarrollo de tesis argumentativa")
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
            practicar_ejercicios()
        elif opcion == "4":
            print("👋 ¡Gracias por entrenar tu razonamiento con claridad y madurez!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
