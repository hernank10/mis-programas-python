import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – ORACIONES ARGUMENTATIVAS

Una oración argumentativa presenta una opinión personal acompañada de una razón que la respalde
y opcionalmente un refuerzo que la profundice o ejemplifique.

🔹 ESTRUCTURA:
1. Tesis → ¿Qué pienso?
2. Razón → ¿Por qué lo pienso?
3. Refuerzo → ¿Qué ejemplo, consecuencia o ampliación lo sostiene?

🎯 Ejemplo:
"Tesis: Creo que el reciclaje debe enseñarse en la escuela.
 Razón: Porque ayuda a formar conciencia ambiental.
 Refuerzo: Además, los estudiantes pueden aplicar estas prácticas en casa."
"""

# 📚 Ejemplos explicados
ejemplos = [
    {
        "oracion": "Creo que leer diariamente mejora la mente porque desarrolla el vocabulario. Además, fomenta la imaginación.",
        "tesis": "leer diariamente mejora la mente",
        "razon": "desarrolla el vocabulario",
        "refuerzo": "fomenta la imaginación"
    },
    {
        "oracion": "Pienso que cuidar el planeta es responsabilidad de todos porque vivimos en él. Por eso, debemos actuar con urgencia.",
        "tesis": "cuidar el planeta es responsabilidad de todos",
        "razon": "vivimos en él",
        "refuerzo": "debemos actuar con urgencia"
    },
    {
        "oracion": "Afirmo que el deporte fortalece el carácter porque enseña disciplina. Además, mejora la salud.",
        "tesis": "el deporte fortalece el carácter",
        "razon": "enseña disciplina",
        "refuerzo": "mejora la salud"
    }
]

# 📝 20 ejercicios
ejercicios = [
    {
        "oracion": "Considero que ayudar en casa fortalece la familia porque todos colaboran. Además, genera respeto mutuo.",
        "tesis": "ayudar en casa fortalece la familia",
        "razon": "todos colaboran"
    },
    {
        "oracion": "Pienso que estudiar historia nos permite entender el presente porque revela nuestras raíces.",
        "tesis": "estudiar historia nos permite entender el presente",
        "razon": "revela nuestras raíces"
    },
    {
        "oracion": "Creo que ser puntual refleja respeto porque valora el tiempo de los demás.",
        "tesis": "ser puntual refleja respeto",
        "razon": "valora el tiempo de los demás"
    },
    {
        "oracion": "Opino que practicar arte estimula la creatividad porque da libertad de expresión.",
        "tesis": "practicar arte estimula la creatividad",
        "razon": "da libertad de expresión"
    },
    {
        "oracion": "Afirmo que cuidar animales enseña empatía porque sentimos lo que ellos sienten.",
        "tesis": "cuidar animales enseña empatía",
        "razon": "sentimos lo que ellos sienten"
    },
    {
        "oracion": "Considero que expresar gratitud mejora las relaciones porque muestra aprecio.",
        "tesis": "expresar gratitud mejora las relaciones",
        "razon": "muestra aprecio"
    },
    {
        "oracion": "Pienso que aprender idiomas abre oportunidades porque permite comunicarse con más personas.",
        "tesis": "aprender idiomas abre oportunidades",
        "razon": "permite comunicarse con más personas"
    },
    {
        "oracion": "Creo que cuidar la salud mental es esencial porque impacta nuestras emociones.",
        "tesis": "cuidar la salud mental es esencial",
        "razon": "impacta nuestras emociones"
    },
    {
        "oracion": "Opino que escuchar música mejora el ánimo porque nos conecta con emociones positivas.",
        "tesis": "escuchar música mejora el ánimo",
        "razon": "nos conecta con emociones positivas"
    },
    {
        "oracion": "Afirmo que aprender a programar prepara para el futuro porque muchas profesiones lo requieren.",
        "tesis": "aprender a programar prepara para el futuro",
        "razon": "muchas profesiones lo requieren"
    },
    {
        "oracion": "Pienso que la lectura diaria forma pensamiento crítico porque expone ideas diversas.",
        "tesis": "la lectura diaria forma pensamiento crítico",
        "razon": "expone ideas diversas"
    },
    {
        "oracion": "Creo que jugar en equipo enseña valores porque exige colaboración.",
        "tesis": "jugar en equipo enseña valores",
        "razon": "exige colaboración"
    },
    {
        "oracion": "Opino que respetar las reglas escolares mejora la convivencia porque evita conflictos.",
        "tesis": "respetar las reglas escolares mejora la convivencia",
        "razon": "evita conflictos"
    },
    {
        "oracion": "Afirmo que tener metas claras impulsa el esfuerzo porque dan dirección.",
        "tesis": "tener metas claras impulsa el esfuerzo",
        "razon": "dan dirección"
    },
    {
        "oracion": "Considero que la educación ambiental es urgente porque el planeta está en riesgo.",
        "tesis": "la educación ambiental es urgente",
        "razon": "el planeta está en riesgo"
    },
    {
        "oracion": "Creo que usar internet con responsabilidad es vital porque afecta nuestra reputación.",
        "tesis": "usar internet con responsabilidad es vital",
        "razon": "afecta nuestra reputación"
    },
    {
        "oracion": "Pienso que trabajar con otros desarrolla habilidades sociales porque obliga a comunicarse.",
        "tesis": "trabajar con otros desarrolla habilidades sociales",
        "razon": "obliga a comunicarse"
    },
    {
        "oracion": "Opino que organizar el tiempo mejora el rendimiento escolar porque permite cumplir tareas.",
        "tesis": "organizar el tiempo mejora el rendimiento escolar",
        "razon": "permite cumplir tareas"
    },
    {
        "oracion": "Afirmo que participar en debates mejora la expresión porque obliga a defender ideas.",
        "tesis": "participar en debates mejora la expresión",
        "razon": "obliga a defender ideas"
    },
    {
        "oracion": "Considero que conocer historia local fortalece la identidad porque revela el origen cultural.",
        "tesis": "conocer historia local fortalece la identidad",
        "razon": "revela el origen cultural"
    }
]

elogios = [
    "🧠 ¡Tesis clara y bien defendida!",
    "🌟 ¡Gran argumento!",
    "👏 ¡Análisis excelente!",
    "🎉 ¡Buena conexión lógica!",
    "⭐ ¡Excelente razonamiento!"
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
        print("🏅 ¡Insignia ganada: Constructor de Opiniones Claras! 🎯")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES ARGUMENTATIVAS")
    print("Escribe 20 frases siguiendo la estructura: Tesis + Razón + Refuerzo\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Gran trabajo con ideas bien defendidas!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 8.º Primaria – Lección 6: Oraciones Argumentativas")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar con 10 ejercicios 📝")
        print("4. Escribir 20 oraciones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            crear_ejemplos_usuario()
        elif opcion == "5":
            print("👋 ¡Gracias por defender tus ideas con estructura y convicción!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")
