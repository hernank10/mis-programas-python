import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO RESPONDEMOS A OTRAS IDEAS CON LÓGICA?

Un contraargumento es una idea contraria a nuestra postura.
Una refutación es nuestra respuesta razonada, con datos o lógica, que defiende nuestra opinión.

🎯 Estructura recomendada:
1. Presenta la idea opuesta (contraargumento)
2. Usa un conector de oposición: sin embargo, aunque, no obstante...
3. Refuta con una razón fuerte y justificada

📝 Ejemplo:
"Algunos piensan que los videojuegos distraen a los jóvenes del estudio.
Sin embargo, si se usan con moderación, pueden mejorar la atención y toma de decisiones."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"contra": "Muchas personas creen que el arte no es esencial en el currículo.",
     "refutacion": "No obstante, el arte desarrolla creatividad, expresión emocional y pensamiento crítico."},
    {"contra": "Algunos opinan que los exámenes son la mejor forma de evaluar.",
     "refutacion": "Aunque son útiles, no siempre reflejan el proceso de aprendizaje completo del estudiante."},
    {"contra": "Se dice que las redes sociales sólo generan distracción.",
     "refutacion": "Sin embargo, pueden ser herramientas educativas si se usan con responsabilidad."},
    {"contra": "Muchos creen que escribir ensayos es aburrido y poco útil.",
     "refutacion": "No obstante, ayuda a organizar ideas, argumentar con lógica y mejorar el estilo personal."},
]

# 📝 20 ejercicios con modelo
ejercicios = [
    {"contra": "Hay quienes piensan que la lectura ya no es necesaria en la era digital.",
     "modelo": "Sin embargo, leer desarrolla pensamiento crítico, algo que las redes no siempre promueven."},
    {"contra": "Algunos afirman que el uniforme escolar limita la libertad individual.",
     "modelo": "Aunque limita la vestimenta, fomenta la igualdad visual y reduce presión social."},
    {"contra": "Se cree que las matemáticas solo sirven para ciertas profesiones.",
     "modelo": "No obstante, enseñan lógica, resolución de problemas y toma de decisiones cotidianas."},
    {"contra": "Muchos dicen que la historia no tiene utilidad práctica.",
     "modelo": "Aunque no se aplique literalmente, ayuda a comprender conflictos y evitar errores del pasado."},
    {"contra": "Algunas personas opinan que la educación física debería ser opcional.",
     "modelo": "Sin embargo, fortalece la salud, reduce el estrés y mejora la disciplina personal."},
    {"contra": "Muchos argumentan que aprender otro idioma es innecesario si no se viaja.",
     "modelo": "No obstante, conocer otro idioma abre puertas mentales, culturales y profesionales."},
    {"contra": "Se dice que la música es una pérdida de tiempo escolar.",
     "modelo": "Aunque no todos la estudien profesionalmente, potencia la memoria y la expresión."},
    {"contra": "Algunos creen que los trabajos en grupo no funcionan bien.",
     "modelo": "Sin embargo, son clave para desarrollar habilidades colaborativas y responsabilidad compartida."},
    {"contra": "Muchos piensan que memorizar fechas es inútil en historia.",
     "modelo": "No obstante, las fechas estructuran hechos, permiten relaciones cronológicas y análisis profundo."},
    {"contra": "Hay quien opina que el arte urbano no debería estar en espacios públicos.",
     "modelo": "Aunque puede ser controversial, refleja realidades sociales y estimula el pensamiento crítico."},
    {"contra": "Se afirma que el acceso libre a internet hace innecesarios los libros.",
     "modelo": "Sin embargo, los libros ofrecen profundidad, contexto y criterio que no siempre da internet."},
    {"contra": "Algunos piensan que los deportes solo sirven para entretener.",
     "modelo": "No obstante, enseñan esfuerzo, estrategia, disciplina y compañerismo."},
    {"contra": "Hay quienes opinan que la filosofía no tiene aplicación real.",
     "modelo": "Aunque no dé respuestas simples, enseña a preguntar, analizar y argumentar de forma sólida."},
    {"contra": "Se cree que los adolescentes no pueden participar en debates complejos.",
     "modelo": "Sin embargo, con guía pueden construir opiniones propias, respetar ideas y profundizar en temas."},
    {"contra": "Muchos dicen que las reglas escolares son demasiado estrictas.",
     "modelo": "Aunque puedan parecer rígidas, garantizan orden, respeto y seguridad para todos."},
    {"contra": "Algunos sostienen que leer poesía es una actividad anticuada.",
     "modelo": "No obstante, la poesía estimula sensibilidad, lenguaje figurado y reflexión estética."},
    {"contra": "Se dice que el diseño gráfico no es una materia seria.",
     "modelo": "Aunque sea visual, involucra comunicación efectiva, análisis cultural y pensamiento estratégico."},
    {"contra": "Hay quien piensa que escribir a mano ya no tiene valor.",
     "modelo": "Sin embargo, fortalece la memoria, la motricidad y el estilo personal de comunicación."},
    {"contra": "Algunos afirman que la ortografía no importa si se entiende el mensaje.",
     "modelo": "No obstante, escribir correctamente muestra respeto, claridad y mejora la credibilidad."},
    {"contra": "Se cree que los proyectos creativos no ayudan a mejorar el aprendizaje.",
     "modelo": "Aunque parezcan informales, fomentan autonomía, exploración y conexión entre saberes."}
]

elogios = [
    "✅ Refutación clara y argumentada.",
    "🎯 Buen uso de conectores opositores.",
    "🌟 Tu idea refuerza tu postura con lógica.",
    "👏 Bien razonado, respuesta precisa y respetuosa.",
    "🧠 Contraargumento respondido con evidencia."
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CONTRAARGUMENTO + REFUTACIÓN:")
    for ej in ejemplos:
        print(f"🗣️ Contraargumento: {ej['contra']}")
        print(f"🧠 Refutación: {ej['refutacion']}\n")

# 📝 20 ejercicios evaluados
def practicar_20():
    print("\n📝 PRACTICA LOS 20 EJERCICIOS CON RETROALIMENTACIÓN:\n")
    total = 0
    for i, ej in enumerate(ejercicios, 1):
        print(f"{str(i).zfill(2)}. Contraargumento:")
        print(f"🗣️ {ej['contra']}")
        print(f"💡 Ejemplo de refutación: {ej['modelo']}")
        respuesta = input("👉 Tu refutación: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in ["sin embargo", "aunque", "no obstante"]):
            puntos += 1
        if len(respuesta.split()) >= 8:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)\n")
        total += puntos
    print(f"\n📊 PUNTAJE FINAL: {total}/60")
    if total >= 50:
        print("🏅 ¡Nivel argumentativo avanzado! Refutas con lógica y profundidad.")
    elif total >= 35:
        print("👍 Buen nivel. Puedes afinar más tus ideas.")
    else:
        print("📘 Practica más el uso de conectores y profundidad argumentativa.")

# ✍️ Crear refutaciones propias
def crear_propias():
    print("\n✍️ CREA 3 REFUTACIONES PROPIAS:")
    total = 0
    for i in range(1, 4):
        contra = input(f"\n🗣️ Contraargumento {i}: ").strip()
        refuta = input("🧠 Refutación: ").strip().lower()
        puntos = 0
        if any(c in refuta for c in ["sin embargo", "aunque", "no obstante"]):
            puntos += 1
        if len(refuta.split()) >= 8:
            puntos += 1
        if "." in refuta or "," in refuta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)\n")
        total += puntos
    print(f"🏅 Total creativo: {total}/9")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Grado("\n📝 PRACTICA LOS 20 EJERCICIOS CON RETROALIMENTACIÓN:\n")
    total = 0
    for i, ej in enumerate(ejercicios, 1):
        print(f"{str(i).zfill(2)}. Contraargumento:")
        print(f"🗣️ {ej['contra']}")
        print(f"💡 Ejemplo de refutación: {ej['modelo']}")
        respuesta = input("👉 Tu refutación: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in ["sin embargo", "aunque", "no obstante"]):
            puntos += 1
        if len(respuesta.split()) >= 8:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)\n")
        total += puntos
    print(f"\n📊 PUNTAJE FINAL: {total}/60")
    if total >= 50:
        print("🏅 ¡Nivel argumentativo avanzado! Refutas con lógica y profundidad.")
    elif total >= 35:
        print("👍 Buen nivel. Puedes afinar más tus ideas.")
    else:
        print("📘 Practica más el uso de conectores y profundidad argumentativa.")

# ✍️ Crear refutaciones propias
def crear_propias():
    print("\n✍️ CREA 3 REFUTACIONES PROPIAS:")
    total = 0
    for i in range(1, 4):
        contra = input(f"\n🗣️ Contraargumento {i}: ").strip()
        refuta = input("🧠 Refutación: ").strip().lower()
        puntos = 0
        if any(c in refuta for c in ["sin embargo", "aunque", "no obstante"]):
            puntos += 1
        if len(refuta.split()) >= 8:
            puntos += 1
        if "." in refuta or "," in refuta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntaje: {puntos}/3)\n")
        total += puntos
    print(f"🏅 Total creativo: {total}/9")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Grado
