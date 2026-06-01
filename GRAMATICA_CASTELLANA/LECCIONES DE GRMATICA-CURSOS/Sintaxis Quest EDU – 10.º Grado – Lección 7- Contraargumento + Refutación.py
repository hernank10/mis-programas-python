import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO RESPONDEMOS A OTRAS IDEAS CON LÓGICA?

Un contraargumento es una idea que va en contra de nuestra postura.
Una refutación es nuestra respuesta razonada, con datos o lógica, que defiende nuestra opinión.

🎯 Estructura recomendada:
1. Presenta la idea opuesta (contraargumento)
2. Usa un conector de oposición: sin embargo, aunque, no obstante...
3. Refuta con una razón fuerte, clara y justificada

📝 Ejemplo:
"Algunos piensan que los videojuegos distraen a los jóvenes del estudio.
Sin embargo, si se usan con moderación, pueden mejorar la atención y toma de decisiones."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "contra": "Muchas personas creen que el arte no es esencial en el currículo.",
        "refutacion": "No obstante, el arte desarrolla creatividad, expresión emocional y pensamiento crítico."
    },
    {
        "contra": "Algunos opinan que los exámenes son la mejor forma de evaluar.",
        "refutacion": "Aunque son útiles, no siempre reflejan el proceso de aprendizaje completo del estudiante."
    },
    {
        "contra": "Se dice que las redes sociales sólo generan distracción.",
        "refutacion": "Sin embargo, pueden ser herramientas educativas si se usan con responsabilidad."
    },
    {
        "contra": "Muchos creen que escribir ensayos es aburrido y poco útil.",
        "refutacion": "No obstante, ayuda a organizar ideas, argumentar con lógica y mejorar el estilo personal."
    },
]

# 📝 20 contraargumentos para refutar
ejercicios = [
    "Hay quienes piensan que la lectura ya no es necesaria en la era digital.",
    "Algunos afirman que el uniforme escolar limita la libertad individual.",
    "Se cree que las matemáticas solo sirven para ciertas profesiones.",
    "Muchos dicen que la historia no tiene utilidad práctica.",
    "Algunas personas opinan que la educación física debería ser opcional.",
    "Muchos argumentan que aprender otro idioma es innecesario si no se viaja.",
    "Se dice que la música es una pérdida de tiempo escolar.",
    "Algunos creen que los trabajos en grupo no funcionan bien.",
    "Muchos piensan que memorizar fechas es inútil en historia.",
    "Hay quien opina que el arte urbano no debería estar en espacios públicos.",
    "Se afirma que el acceso libre a internet hace innecesarios los libros.",
    "Algunos piensan que los deportes solo sirven para entretener.",
    "Hay quienes opinan que la filosofía no tiene aplicación real.",
    "Se cree que los adolescentes no pueden participar en debates complejos.",
    "Muchos dicen que las reglas escolares son demasiado estrictas.",
    "Algunos sostienen que leer poesía es una actividad anticuada.",
    "Se dice que el diseño gráfico no es una materia seria.",
    "Hay quien piensa que escribir a mano ya no tiene valor.",
    "Algunos afirman que la ortografía no importa si se entiende el mensaje.",
    "Se cree que los proyectos creativos no ayudan a mejorar el aprendizaje."
]

elogios = [
    "✅ Refutación clara y argumentada.",
    "🎯 Buen uso de conectores opositores.",
    "🌟 Tu idea refuerza tu postura con lógica.",
    "👏 Bien razonado, respuesta respetuosa y precisa.",
    "🧠 Contraargumento respondido con evidencia."
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CONTRAARGUMENTO + REFUTACIÓN:")
    for ej in ejemplos:
        print(f"🗣️ Contraargumento: {ej['contra']}")
        print(f"🧠 Refutación: {ej['refutacion']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 REFUTA LAS SIGUIENTES IDEAS CON TU ARGUMENTO:")
    seleccion = random.sample(ejercicios, 5)
    total = 0
    for i, contra in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Contraargumento: {contra}")
        refutacion = input("👉 Refutación: ").strip().lower()
        puntos = 0
        if any(c in refutacion for c in ["sin embargo", "no obstante", "aunque"]):
            puntos += 1
        if len(refutacion.split()) >= 8:
            puntos += 1
        if "." in refutacion or "," in refutacion:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)")
        total += puntos
    print("\n📊 PUNTAJE TOTAL:", total, "/15")
    if total >= 13:
        print("🏅 ¡Excelente! Tus refutaciones son claras y justificadas.")
    elif total >= 9:
        print("👍 ¡Buen nivel! Aún puedes afinar tu argumentación.")
    else:
        print("📘 Practica más el uso de conectores y profundidad lógica.")

# ✍️ Crear propios
def escribir_propios():
    print("\n✍️ ESCRIBE 3 POSTURAS PROPIAS CON CONTRA Y REFUTACIÓN:")
    total = 0
    for i in range(1, 4):
        print(f"\n🔸 Postura {i}")
        contra = input("🗣️ Contraargumento: ").strip()
        refuta = input("🧠 Refutación: ").strip().lower()
        puntos = 0
        if any(c in refuta for c in ["sin embargo", "no obstante", "aunque"]):
            puntos += 1
        if len(refuta.split()) >= 8:
            puntos += 1
        if "." in refuta or "," in refuta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje creativo total: {total}/9")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Grado – Lección 7: Contraargumento + Refutación")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 5 ejercicios con evaluación 📝")
        print("4. Escribir tus propias refutaciones ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            escribir_propios()
        elif opcion == "5":
            print("👋 ¡Gracias por debatir con lógica, respeto y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
