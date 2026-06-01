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

# 📝 20 ejercicios de tesis incompleta
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

# 🎯 Función para evaluar respuesta
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

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TESIS + RAZÓN:")
    for ej in ejemplos:
        print(f"📝 {ej['tesis']}")
        print(f"👉 {ej['razon']}\n")

# 📝 Practicar ejercicios con puntuación
def practicar_con_puntaje():
    print("\n📝 AGREGA UNA RAZÓN A CADA TESIS:")
    seleccion = random.sample(tesis_lista, 5)
    total = 0
    for i, tesis in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip()
        feedback, puntos = evaluar_respuesta(razon)
        total += puntos
        print(f"{feedback} (Puntaje: {puntos}/3)")
        print(f"🧠 Oración completa: {tesis}. {razon}")

    print("\n📊 RESULTADO FINAL:")
    print(f"🌟 Puntaje total: {total}/15")
    if total >= 13:
        print("🎯 ¡Dominio alto en argumentación breve!")
    elif total >= 9:
        print("👍 ¡Nivel medio, puedes mejorar tus razones!")
    else:
        print("📘 ¡Practica más para fortalecer tus ideas!")

# ✍️ Crear argumentos propios
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

    print("\n📘 Tus argumentos:")
    for idx, (t, r, fb, pts) in enumerate(argumentos, 1):
        print(f"{idx}. {t}. {r} — {fb} (Puntaje: {pts}/3)")
    print(f"\n🏅 Puntaje total: {total}/15")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Grado – Lección 7: Tesis + Razón Evaluada")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 5 ejercicios con retroalimentación 📝")
        print("4. Escribir tus propios argumentos ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_con_puntaje()
        elif opcion == "4":
            escribir_propios()
        elif opcion == "5":
            print("👋 ¡Gracias por fortalecer tu pensamiento argumentativo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
