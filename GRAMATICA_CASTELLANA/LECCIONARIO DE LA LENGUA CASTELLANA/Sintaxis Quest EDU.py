import random

# 📘 Teoría explicada
teoria = """
📘 LECCIÓN 6 – ORACIONES ARGUMENTATIVAS

Una oración argumentativa presenta una opinión clara, una razón que la justifica, y opcionalmente una ampliación o refuerzo.

🔹 ESTRUCTURA:
- Tesis: la idea o posición personal
- Razón: motivo que la respalda
- Refuerzo: ejemplo, consecuencia o ampliación

🎯 Ejemplo:
"Tesis: Creo que deberíamos cuidar el planeta.
 Razón: Porque es nuestro hogar y está en peligro.
 Refuerzo: Además, pequeñas acciones diarias hacen gran diferencia."
"""

# 📚 Ejemplos explicados
ejemplos = [
    {
        "oracion": "Creo que el ejercicio regular es esencial porque mejora la salud. Además, reduce el estrés.",
        "tesis": "el ejercicio regular es esencial",
        "razon": "mejora la salud",
        "refuerzo": "reduce el estrés"
    },
    {
        "oracion": "Pienso que leer cada día es beneficioso porque enriquece el vocabulario. También fortalece la concentración.",
        "tesis": "leer cada día es beneficioso",
        "razon": "enriquece el vocabulario",
        "refuerzo": "fortalece la concentración"
    },
    {
        "oracion": "Considero que respetar a los demás es fundamental porque promueve la paz. Por eso, debemos practicar la empatía.",
        "tesis": "respetar a los demás es fundamental",
        "razon": "promueve la paz",
        "refuerzo": "debemos practicar la empatía"
    },
    {
        "oracion": "Afirmo que aprender idiomas abre oportunidades porque permite comunicarse con más personas. Así, se mejora la empleabilidad.",
        "tesis": "aprender idiomas abre oportunidades",
        "razon": "permite comunicarse con más personas",
        "refuerzo": "mejora la empleabilidad"
    },
    {
        "oracion": "Opino que cuidar a los animales es un deber porque son parte de la naturaleza. Además, enseñan valores como la responsabilidad.",
        "tesis": "cuidar a los animales es un deber",
        "razon": "son parte de la naturaleza",
        "refuerzo": "enseñan valores como la responsabilidad"
    }
]

# 📝 20 ejercicios argumentativos
ejercicios = [
    {"oracion": "Creo que estudiar historia es importante porque nos permite entender el presente. Además, nos enseña sobre nuestras raíces.", "tesis": "estudiar historia es importante", "razon": "entender el presente"},
    {"oracion": "Pienso que la puntualidad muestra respeto porque valora el tiempo de los demás. También ayuda a organizarse mejor.", "tesis": "la puntualidad muestra respeto", "razon": "valora el tiempo de los demás"},
    {"oracion": "Opino que practicar arte estimula la creatividad porque permite expresarnos libremente. Así, desarrollamos habilidades personales.", "tesis": "practicar arte estimula la creatividad", "razon": "permite expresarnos libremente"},
    {"oracion": "Considero que cuidar el medio ambiente es urgente porque el planeta está sufriendo. Por eso, debemos actuar ahora.", "tesis": "cuidar el medio ambiente es urgente", "razon": "el planeta está sufriendo"},
    {"oracion": "Afirmo que la lectura desarrolla el pensamiento crítico porque nos enfrenta a ideas diversas. Además, mejora la comprensión.", "tesis": "la lectura desarrolla el pensamiento crítico", "razon": "nos enfrenta a ideas diversas"},
    {"oracion": "Creo que comer sano mejora la calidad de vida porque da energía y previene enfermedades.", "tesis": "comer sano mejora la calidad de vida", "razon": "da energía y previene enfermedades"},
    {"oracion": "Opino que los deportes enseñan trabajo en equipo porque hay que colaborar para ganar.", "tesis": "los deportes enseñan trabajo en equipo", "razon": "hay que colaborar para ganar"},
    {"oracion": "Pienso que respetar las reglas escolares ayuda a la convivencia porque evita conflictos.", "tesis": "respetar las reglas escolares ayuda a la convivencia", "razon": "evita conflictos"},
    {"oracion": "Considero que cuidar nuestra salud mental es tan importante como la física porque afecta cómo vivimos.", "tesis": "cuidar nuestra salud mental es tan importante como la física", "razon": "afecta cómo vivimos"},
    {"oracion": "Afirmo que usar bien el internet es esencial porque influye en cómo aprendemos.", "tesis": "usar bien el internet es esencial", "razon": "influye en cómo aprendemos"},
    {"oracion": "Creo que expresar gratitud mejora las relaciones porque muestra aprecio y respeto.", "tesis": "expresar gratitud mejora las relaciones", "razon": "muestra aprecio y respeto"},
    {"oracion": "Opino que ayudar en casa fortalece la familia porque todos colaboran en armonía.", "tesis": "ayudar en casa fortalece la familia", "razon": "todos colaboran en armonía"},
    {"oracion": "Pienso que aprender programación abre nuevas posibilidades porque muchas profesiones lo requieren.", "tesis": "aprender programación abre nuevas posibilidades", "razon": "muchas profesiones lo requieren"},
    {"oracion": "Considero que hablar varios idiomas fomenta la tolerancia porque entendemos otras culturas.", "tesis": "hablar varios idiomas fomenta la tolerancia", "razon": "entendemos otras culturas"},
    {"oracion": "Afirmo que cuidar a los animales enseña empatía porque sentimos lo que ellos sienten.", "tesis": "cuidar a los animales enseña empatía", "razon": "sentimos lo que ellos sienten"},
    {"oracion": "Creo que tener amigos sinceros nos hace felices porque nos apoyan en todo momento.", "tesis": "tener amigos sinceros nos hace felices", "razon": "nos apoyan en todo momento"},
    {"oracion": "Opino que conocer historia local fortalece nuestra identidad porque sabemos de dónde venimos.", "tesis": "conocer historia local fortalece nuestra identidad", "razon": "sabemos de dónde venimos"},
    {"oracion": "Pienso que escuchar música mejora el ánimo porque influye en nuestras emociones.", "tesis": "escuchar música mejora el ánimo", "razon": "influye en nuestras emociones"},
    {"oracion": "Considero que escribir diariamente mejora la expresión porque organizamos nuestros pensamientos.", "tesis": "escribir diariamente mejora la expresión", "razon": "organizamos nuestros pensamientos"},
    {"oracion": "Afirmo que tener objetivos claros impulsa el esfuerzo porque nos da sentido en lo que hacemos.", "tesis": "tener objetivos claros impulsa el esfuerzo", "razon": "nos da sentido en lo que hacemos"}
]

elogios = [
    "🌟 ¡Muy bien estructurado!",
    "🧠 ¡Tesis clara y bien defendida!",
    "🎉 ¡Gran forma de argumentar!",
    "👏 ¡Pensamiento crítico en acción!",
    "⭐ ¡Excelente conexión entre ideas!"
]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración completa: {ej['oracion']}")
        print(f"👉 Tesis: {ej['tesis']}\n   Razón: {ej['razon']}\n   Refuerzo: {ej['refuerzo']}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['oracion']}")
        tesis = input("👉 ¿Cuál es la tesis?: ").strip().lower()
        razon = input("👉 ¿Cuál es la razón?: ").strip().lower()

        if tesis == ej["tesis"].lower() and razon == ej["razon"].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era:\n👉 Tesis: '{ej['tesis']}'\n👉 Razón: '{ej['razon']}'")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia: Constructor de Tesis Sólida! 🧱")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES ARGUMENTATIVAS")
    print("Escribe 20 oraciones con tesis, razón y refuerzo (ej. 'Creo que... porque... Además...'):\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {
