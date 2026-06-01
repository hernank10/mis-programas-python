import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO FORTALECEMOS NUESTRA IDEA EN UN PÁRRAFO?

Un buen párrafo argumentativo incluye:

1. 🔸 Tesis → idea principal clara y debatible  
2. 🔹 Desarrollo → razón o ejemplo que la apoya  
3. 🔸 Contraargumento → opinión contraria con respeto  
4. 🔹 Refutación → respuesta lógica que defiende la tesis

🎯 Ejemplo:
"Los jóvenes deben participar en debates escolares.
Algunos creen que no tienen suficiente madurez.
Sin embargo, al hacerlo desarrollan respeto, pensamiento crítico y confianza."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La lectura crítica debería enseñarse desde primaria.\nAlgunos dicen que es demasiado compleja a esa edad.\nSin embargo, si se adapta con ejemplos sencillos, se puede fomentar la reflexión desde temprano.",
    "Los trabajos en grupo mejoran el aprendizaje.\nAlgunos opinan que generan conflictos y desorden.\nPero en realidad, enseñan a colaborar, negociar y respetar opiniones distintas.",
    "La educación artística debe tener más horas en la semana.\nMuchos creen que no es tan importante como las matemáticas.\nEn cambio, el arte desarrolla creatividad, sensibilidad y pensamiento lateral.",
]

# 📝 20 temas base con contraargumento
temas = [
    {
        "tesis": "Las redes sociales pueden ser herramientas educativas.",
        "contra": "Algunos piensan que solo distraen y generan pérdida de tiempo."
    },
    {
        "tesis": "Los jóvenes deberían votar desde los 16 años.",
        "contra": "Muchos opinan que no tienen suficiente conocimiento político."
    },
    {
        "tesis": "El deporte escolar debe practicarse todos los días.",
        "contra": "Algunos creen que quita tiempo a asignaturas más académicas."
    },
    {
        "tesis": "Escribir diarios personales mejora la salud emocional.",
        "contra": "Hay quienes creen que es una actividad inútil y privada."
    },
    {
        "tesis": "Los debates en clase fortalecen la expresión oral.",
        "contra": "Algunos sostienen que generan tensión y discusiones entre compañeros."
    },
    {
        "tesis": "El uso de videojuegos puede mejorar el pensamiento estratégico.",
        "contra": "Muchos creen que solo promueven violencia o evasión."
    },
    {
        "tesis": "Las excursiones pedagógicas enriquecen el aprendizaje.",
        "contra": "Algunos opinan que son una pérdida de tiempo fuera del aula."
    },
    {
        "tesis": "Aprender a programar debe ser parte del currículo escolar.",
        "contra": "Muchos consideran que es una habilidad muy técnica y limitada."
    },
    {
        "tesis": "La poesía debe incluirse como lectura obligatoria.",
        "contra": "Algunos creen que los estudiantes no la entienden ni la disfrutan."
    },
    {
        "tesis": "Los adolescentes deben tener voz en decisiones escolares.",
        "contra": "Hay quienes piensan que no tienen criterio suficiente."
    },
    {
        "tesis": "Estudiar filosofía estimula el pensamiento crítico.",
        "contra": "Algunos dicen que no tiene aplicación práctica en la vida diaria."
    },
    {
        "tesis": "Las películas pueden ser usadas como recurso educativo.",
        "contra": "Muchos sostienen que solo entretienen y no enseñan."
    },
    {
        "tesis": "La educación sexual debe comenzar desde la primaria.",
        "contra": "Hay quien considera que esos temas deben postergarse hasta la adolescencia."
    },
    {
        "tesis": "Los exámenes escritos no deberían ser la única forma de evaluar.",
        "contra": "Algunos creen que son la forma más objetiva de medir conocimiento."
    },
    {
        "tesis": "Los adolescentes deben tener horarios flexibles para estudiar.",
        "contra": "Muchos piensan que esto lleva a desorden y falta de disciplina."
    },
    {
        "tesis": "La lectura digital es tan valiosa como la impresa.",
        "contra": "Hay quienes opinan que leer en pantalla es superficial."
    },
    {
        "tesis": "La alimentación escolar debe ser variada y saludable.",
        "contra": "Algunos sostienen que eso implica costos que no se pueden cubrir."
    },
    {
        "tesis": "La escritura creativa debería practicarse en todas las áreas.",
        "contra": "Muchos piensan que solo tiene valor en clases de lengua."
    },
    {
        "tesis": "Los estudiantes pueden enseñar entre ellos como método de repaso.",
        "contra": "Algunos creen que solo el maestro tiene el conocimiento adecuado."
    },
    {
        "tesis": "El humor en el aula mejora el ambiente de aprendizaje.",
        "contra": "Hay quienes opinan que puede hacer perder el respeto o la concentración."
    },
]

elogios = [
    "🌟 ¡Tu refutación fortalece la idea principal!",
    "✅ ¡Muy bien! Usaste lógica y respeto.",
    "👏 ¡La estructura del párrafo está completa!",
    "🧠 ¡Excelente pensamiento argumentativo!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE PÁRRAFOS COMPLETOS:")
    for ej in ejemplos:
        print(f"📝 {ej}\n")

# 📝 Practicar 20 párrafos
def practicar_parrafos():
    print("\n📝 AGREGA UNA REFUTACIÓN A CADA TEMA:")
    total = 0
    for i, tema in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tema['tesis']}")
        print(f"   Contraargumento: {tema['contra']}")
        refuta = input("👉 Tu refutación (máximo 3 líneas): ").strip().lower()
        puntos = 0
        if any(c in refuta for c in ["sin embargo", "aunque", "no obstante", "en cambio", "pero", "a pesar de"]):
            puntos += 1
        if len(refuta.split()) >= 10:
            puntos += 1
        if "." in refuta or "," in refuta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Excelente dominio de estructura argumentativa!")
    elif total >= 35:
        print("👍 Buen trabajo. Puedes afinar tus refutaciones.")
    else:
        print("📘 Practica más cómo responder con lógica y cortesía.")

# ✍️ Redacción libre
def redactar_completo():
    print("\n✍️ ESCRIBE UN PÁRRAFO COMPLETO:")
    tesis = input("📝 Tesis: ").strip()
    desarrollo = input("👉 Desarrollo o ejemplo: ").strip()
    contra = input("👉 Contraargumento: ").strip()
    refutacion = input("👉 Refutación: ").strip()
    texto = f"{tesis} {desarrollo} {contra} {refutacion}"
    puntos = 0
    if any(c in refutacion.lower() for c in ["sin embargo", "aunque", "no obstante", "en cambio", "pero", "a pesar de"]):
        puntos += 1
    if len(texto.split()) >= 40:
        puntos += 1
    if "." in texto and "," in texto:
        puntos += 1
    print(f"\n🎯 Tu puntuación: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu párrafo tiene profundidad y claridad!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes afinar la estructura.")
    else:
        print("📘 Intenta organizar mejor tus ideas.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 8.º Grado – Lección 8: Párrafos argumentativos completos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 refutaciones 📝")
        print("4. Escribir tu propio párrafo ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_parrafos()
        elif opcion == "4":
            redactar_completo()
        elif opcion == "5":
            print("👋 ¡Gracias por pensar con claridad y respeto al escribir!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
