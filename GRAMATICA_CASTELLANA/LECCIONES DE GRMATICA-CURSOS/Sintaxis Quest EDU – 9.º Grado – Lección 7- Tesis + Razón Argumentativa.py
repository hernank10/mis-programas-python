import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO PRESENTAMOS UNA POSTURA Y LA DEFENDEMOS?

Un párrafo argumentativo comienza con una tesis: una frase que presenta una idea clara.
Luego, debe incluir una razón principal que la justifique.

🔹 Estructura básica:
Tesis + Porque / Ya que / Debido a + Razón principal

💡 Ejemplo:
"Toda escuela debería tener biblioteca. Porque fomenta la lectura y el pensamiento independiente."

✅ Evita afirmaciones vagas. Una tesis es más fuerte si tiene una razón clara detrás.
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "tesis": "Las redes sociales deben tener límites de uso.",
        "razon": "Porque el exceso puede afectar la salud mental de los adolescentes."
    },
    {
        "tesis": "La educación artística es necesaria en todas las escuelas.",
        "razon": "Porque estimula la creatividad y mejora el desarrollo personal."
    },
    {
        "tesis": "Los exámenes no deberían ser el único método de evaluación.",
        "razon": "Ya que no todos los estudiantes aprenden de la misma forma."
    },
    {
        "tesis": "Los parques urbanos deben mantenerse limpios.",
        "razon": "Porque son espacios para el bienestar colectivo."
    },
    {
        "tesis": "Es importante aprender otro idioma en el colegio.",
        "razon": "Porque abre puertas culturales y laborales en el futuro."
    }
]

# 📝 20 tesis incompletas (para completar con razón lógica)
ejercicios = [
    "La tecnología debe usarse con responsabilidad",
    "Las tareas escolares deben tener un propósito claro",
    "El deporte debe formar parte del horario escolar",
    "Los estudiantes deben respetar a sus compañeros",
    "El reciclaje debe enseñarse desde primaria",
    "Los videojuegos pueden ser positivos",
    "La alimentación saludable debe ser promovida en el colegio",
    "Las actividades en grupo ayudan al aprendizaje",
    "La lectura diaria mejora el desempeño escolar",
    "Los teléfonos en clase deben estar regulados",
    "La historia es una materia clave en la educación",
    "Los profesores deben recibir apoyo emocional",
    "El arte urbano merece reconocimiento",
    "La puntualidad debe enseñarse como valor escolar",
    "El bullying debe tratarse con firmeza",
    "El descanso entre clases es necesario",
    "Las excursiones educativas son valiosas",
    "La escritura mejora el pensamiento crítico",
    "Los estudiantes deben aprender sobre economía básica",
    "La música estimula la memoria y la concentración"
]

elogios = [
    "✅ ¡Razón clara y lógica!",
    "🎯 ¡Tu tesis tiene fuerza!",
    "🌟 ¡Excelente justificación!",
    "👏 ¡Buena conexión entre postura y argumento!",
    "🧠 ¡Pensamiento argumentativo sólido!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TESIS + RAZÓN:")
    for ej in ejemplos:
        print(f"📝 {ej['tesis']}")
        print(f"👉 {ej['razon']}\n")

# 📝 Practicar con tesis incompletas
def practicar_ejercicios():
    print("\n📝 AGREGA UNA RAZÓN QUE SOSTENGA LA TESIS:")
    seleccion = random.sample(ejercicios, 5)
    for i, tesis in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tesis}")
        razon = input("👉 ¿Por qué?: ").strip()
        if razon:
            print(random.choice(elogios))
            print(f"🧠 Oración completa: {tesis}. {razon}")
        else:
            print("⚠️ Intenta escribir una razón que justifique la postura.")

# ✍️ Crear tesis propias con razón
def escribir_propias():
    print("\n✍️ ESCRIBE 5 POSTURAS Y JUSTIFICACIONES:")
    pares = []
    for i in range(1, 6):
        tesis = input(f"👉 Tesis {i}: ").strip()
        razon = input("👉 ¿Por qué piensas eso?: ").strip()
        pares.append(f"{tesis}. {razon}")

    print("\n📘 Tus argumentos personales:")
    for idx, p in enumerate(pares, 1):
        print(f"{idx}. {p}")
    print("🏅 ¡Excelente! Cada frase tiene una idea y una razón fuerte.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Grado – Lección 7: Tesis + Razón Argumentativa")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 5 tesis con razón 📝")
        print("4. Escribir tus propios argumentos ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            escribir_propias()
        elif opcion == "5":
            print("👋 ¡Gracias por construir argumentos con lógica y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    menu()
