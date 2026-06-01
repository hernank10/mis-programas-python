import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO SE CONECTAN IDEAS PARA PENSAR MEJOR?

Un texto argumentativo usa conectores lógicos que unen ideas y muestran relaciones como:

🔹 Causa y consecuencia → por lo tanto, en consecuencia
🔹 Contraste → sin embargo, en cambio, a pesar de eso
🔹 Énfasis → de hecho, en efecto
🔹 Explicación o aclaración → es decir, o sea

🎯 Ejemplo:
"Muchos creen que el videojuego distrae. Sin embargo, estudios muestran que mejora habilidades cognitivas."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La contaminación es grave. Por lo tanto, debemos reciclar con urgencia.",
    "No todos disfrutan las matemáticas. En cambio, otros se sienten motivados por los desafíos.",
    "La lectura mejora el lenguaje. De hecho, fortalece la comprensión y la escritura.",
    "El transporte público es lento. A pesar de eso, muchas personas lo prefieren por su bajo costo.",
    "La participación estudiantil es baja. Es decir, pocos alumnos intervienen en debates o decisiones escolares."
]

# 📝 20 pares de ideas para conectar con un conector argumentativo
ejercicios = [
    ("El estudiante no entregó su tarea.", "Sacó mala nota."),
    ("La biblioteca tiene pocos libros nuevos.", "Los alumnos buscan información en internet."),
    ("La lluvia fue intensa.", "Las calles se inundaron."),
    ("A muchos no les gusta la poesía.", "Expresa emociones profundas."),
    ("La clase fue larga.", "Varios alumnos perdieron la concentración."),
    ("Los niños leen cada tarde.", "Mejoran su vocabulario."),
    ("El grupo no llegó a tiempo.", "Fue penalizado en el concurso."),
    ("La comida del colegio es saludable.", "Algunos estudiantes la rechazan."),
    ("Juan no hizo el experimento.", "Aprobó gracias al trabajo escrito."),
    ("El patio estaba mojado.", "Los alumnos jugaron igual."),
    ("Lucía escribe relatos.", "También ilustra sus personajes."),
    ("No hubo presentación oral.", "El profesor evaluó el informe escrito."),
    ("El examen fue difícil.", "Muchos obtuvieron buenos resultados."),
    ("Pedro no participó en la discusión.", "Su reflexión escrita fue profunda."),
    ("El equipo perdió el partido.", "Jugó con esfuerzo y respeto."),
    ("La película era divertida.", "De hecho, muchos la recomiendan."),
    ("La escuela enseña ciencias.", "En cambio, otras instituciones priorizan lo artístico."),
    ("Los jóvenes usan redes sociales.", "A pesar de eso, también leen artículos y libros."),
    ("La maestra propuso un reto.", "El grupo respondió con entusiasmo."),
    ("El alumno faltó varios días.", "Por lo tanto, tuvo que ponerse al día con sus tareas."),
]

elogios = [
    "🌟 ¡Conector preciso y bien usado!",
    "✅ ¡Tu oración muestra buena articulación lógica!",
    "👏 ¡Muy buen nivel de pensamiento!",
    "🧠 ¡Oración madura y conectada!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CONECTORES EN USO:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Práctica
def practicar_conectores():
    print("\n📝 UNE LAS IDEAS CON UN CONECTOR ARGUMENTATIVO:")
    total = 0
    conectores = ["por lo tanto", "sin embargo", "en cambio", "de hecho", "en efecto", "a pesar de eso", "es decir"]
    for i, (idea1, idea2) in enumerate(ejercicios, 1):
        print(f"\n{str(i).zfill(2)}. Parte 1: {idea1}")
        print(f"     Parte 2: {idea2}")
        respuesta = input("👉 Escribe la oración completa: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in conectores):
            puntos += 1
        if len(respuesta.split()) >= 10:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/60")
    if total >= 50:
        print("🏅 ¡Gran dominio de conectores argumentativos!")
    elif total >= 35:
        print("👍 Buen avance. Puedes variar más los tipos de conector.")
    else:
        print("📘 Practica cómo unir ideas con sentido lógico y precisión.")

# ✍️ Composición creativa
def redactar_parrafo():
    print("\n✍️ ESCRIBE UN PÁRRAFO USANDO 3 CONECTORES DIFERENTES:")
    texto = input("📝 Tu párrafo: ").strip().lower()
    conectores_usados = [c for c in ["por lo tanto", "sin embargo", "de hecho", "en cambio", "a pesar de eso", "en efecto", "es decir"] if c in texto]
    cantidad = len(conectores_usados)
    puntos = 3 if cantidad >= 3 else 2 if cantidad == 2 else 1 if cantidad == 1 else 0
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Excelente variedad y profundidad de conectores!")
    elif puntos == 2:
        print("✅ Buen trabajo. Puedes probar con más tipos de conector.")
    elif puntos == 1:
        print("⚠️ Solo un conector detectado. Prueba ampliar más.")
    else:
        print("❌ No se detectó ninguno. Intenta otra vez.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 7.º Grado – Lección 8: Conectores argumentativos complejos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 pares de ideas 📝")
        print("4. Escribir tu propio párrafo ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_conectores()
        elif opcion == "4":
            redactar_parrafo()
        elif opcion == "5":
            print("👋 ¡Gracias por escribir con lógica, conexión y estilo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
