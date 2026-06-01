import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO PRESENTAMOS UNA TESIS Y LA SOSTENEMOS?

Una tesis es una afirmación clara sobre un tema. Debe ir acompañada de una razón principal que la justifique.

🎯 Estructura recomendada:
Tesis + conector + razón

🔹 Conectores comunes:
- porque
- ya que
- debido a

💡 Ejemplo:
"Toda escuela debería tener biblioteca, porque fomenta la lectura y el pensamiento independiente."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "tesis": "Las redes sociales deben tener límites de uso.",
        "razon": "Porque el exceso puede afectar la salud mental."
    },
    {
        "tesis": "La educación artística debe estar presente en el currículo.",
        "razon": "Ya que potencia la creatividad y las emociones."
    },
    {
        "tesis": "Los exámenes no deben ser el único método de evaluación.",
        "razon": "Debido a que existen diferentes formas de aprender."
    }
]

# 📝 20 ejercicios
tesis_lista = [
    "Las tareas escolares deben tener un propósito claro",
    "El reciclaje debe enseñarse desde primaria",
    "La lectura diaria mejora el desempeño escolar",
    "Los teléfonos en clase deben estar regulados",
    "Los videojuegos pueden ser positivos",
    "La puntualidad debe enseñarse como valor escolar",
    "Las excursiones educativas son valiosas",
    "La alimentación saludable debe ser promovida",
    "El arte urbano merece reconocimiento",
    "El descanso entre clases es necesario",
    "Los estudiantes deben respetar a sus compañeros",
    "La historia es una materia clave en la educación",
    "El deporte debe formar parte del horario escolar",
    "La escritura mejora el pensamiento crítico",
    "Los estudiantes deben aprender sobre economía básica",
    "La música estimula la memoria y la concentración",
    "Los profesores deben recibir apoyo emocional",
    "Las actividades en grupo ayudan al aprendizaje",
    "El bullying debe tratarse con firmeza",
    "La tecnología debe usarse con responsabilidad"
]

elogios = [
    "✅ ¡Razón clara y lógica!",
    "🎯 ¡Tu tesis tiene fuerza!",
    "🌟 ¡Excelente justificación!",
    "👏 ¡Buena conexión entre postura y argumento!",
    "🧠 ¡Pensamiento argumentativo sólido!"
]

# 🎯 Evaluar razonamiento
def evaluar_respuesta(razon):
    razon = razon.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a"]
    if any(c in razon for c in conectores):
        puntos += 1
    if len(razon.split()) >= 5:
        puntos += 1
    if "." in razon or "," in razon:
        puntos += 1

    if puntos == 3:
        return "🏅 ¡Argumento sólido, bien estructurado!", 3
    elif puntos == 2:
        return "✅ ¡Buena razón, podrías agregar más detalle!", 2
    elif puntos == 1:
        return "⚠️ Tu razón tiene potencial, pero le falta estructura.", 1
    else:
        return "❌ Falta conexión lógica o desarrollo en la respuesta.", 0

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TESIS + RAZÓN:")
    for ej in ejemplos:
        print(f"📝 {ej['tesis']}")
        print(f"👉 {ej['razon']}\n")

# 🧠 5 ejercicios aleatorios
def practicar_aleatorios():
    print("\n📝 AGREGA UNA RAZÓN A CADA TESIS (5 aleatorias):")
    seleccion = random.sample(tesis_lista, 5)
    total = 0
    for i, tesis in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip()
        feedback, puntos = evaluar_respuesta(razon)
        total += puntos
        print(f"{feedback} (Puntaje: {puntos}/3)")
        print(f"🧠 Oración completa: {tesis}. {razon}")
    print("\n📊 TOTAL: ", total, "/15")

# ✍️ Argumentos del estudiante
def escribir_propios():
    print("\n✍️ ESCRIBE 5 TESIS Y SUS RAZONES:")
    total = 0
    argumentos = []
    for i in range(1, 6):
        tesis = input(f"👉 Tesis {i}: ").strip()
        razon = input("👉 ¿Por qué?: ").strip()
        feedback, puntos = evaluar_respuesta(razon)
        total += puntos
        argumentos.append((tesis, razon, feedback, puntos))

    print("\n📘 TUS ARGUMENTOS:")
    for idx, (t, r, fb, pts) in enumerate(argumentos, 1):
        print(f"{idx}. {t}. {r} — {fb} (Puntaje: {pts}/3)")
    print(f"\n🏅 TOTAL: {total}/15")

# 🧠 Los 20 ejercicios completos
def practicar_20_ejercicios():
    print("\n🧠 PRACTICA LOS 20 EJERCICIOS COMPLETOS:")
    total = 0
    for i, tesis in enumerate(tesis_lista, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip()
        feedback, puntos = evaluar_respuesta(razon)
        total += puntos
        print(f"{feedback} (Puntaje: {puntos}/3)")
        print(f"🧠 Oración completa: {tesis}. {razon}")
    print("\n📊 RESULTADO FINAL:")
    print(f"🌟 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Nivel avanzado! Tu habilidad argumentativa está muy bien desarrollada.")
    elif total >= 35:
        print("👍 ¡Buen nivel! Aún puedes mejorar tus razones.")
    else:
        print("📘 Practica más para fortalecer tus ideas con claridad.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Grado – Lección 7: Tesis + Razón Evaluada")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 5 ejercicios aleatorios 📝")
        print("4. Escribir tus propios argumentos ✍️")
        print("5. Practicar los 20 ejercicios completos 🧠")
        print("6. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_aleatorios()
        elif opcion == "4":
            escribir_propios()
        elif opcion == "5":
            practicar_20_ejercicios()
        elif opcion == "6":
            print("👋 ¡Gracias por fortalecer tu pensamiento argumentativo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
