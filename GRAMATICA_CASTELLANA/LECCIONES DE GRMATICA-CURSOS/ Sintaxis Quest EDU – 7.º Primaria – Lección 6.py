import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – CONECTORES LÓGICOS

Los conectores lógicos unen oraciones y muestran la relación entre ideas.

🔹 TIPOS DE CONECTORES:

1. CAUSA: explican el motivo
   Ej: porque, ya que, debido a que

2. CONSECUENCIA: muestran el resultado
   Ej: por eso, entonces, así que

3. CONTRASTE: indican diferencia u oposición
   Ej: pero, aunque, sin embargo

4. CONDICIÓN: expresan una situación hipotética
   Ej: si, a menos que, en caso de que
"""

# 📚 Ejemplos explicados
ejemplos = [
    {"oracion": "Estudié mucho porque tenía examen.", "conector": "porque", "tipo": "causa"},
    {"oracion": "No entendí el tema, por eso pregunté.", "conector": "por eso", "tipo": "consecuencia"},
    {"oracion": "Quería salir, pero empezó a llover.", "conector": "pero", "tipo": "contraste"},
    {"oracion": "Si llueve, no saldremos.", "conector": "si", "tipo": "condición"},
    {"oracion": "Aunque estaba cansado, terminó la tarea.", "conector": "aunque", "tipo": "contraste"}
]

# 📝 20 ejercicios
ejercicios = [
    {"oracion": "No traje mi cuaderno porque lo olvidé.", "conector": "porque", "tipo": "causa"},
    {"oracion": "Estaba enfermo, así que no fue a clase.", "conector": "así que", "tipo": "consecuencia"},
    {"oracion": "Quiero ir, pero no tengo permiso.", "conector": "pero", "tipo": "contraste"},
    {"oracion": "Si practicas más, mejorarás.", "conector": "si", "tipo": "condición"},
    {"oracion": "Llovía, entonces usamos paraguas.", "conector": "entonces", "tipo": "consecuencia"},
    {"oracion": "Voy a estudiar porque mañana hay prueba.", "conector": "porque", "tipo": "causa"},
    {"oracion": "A menos que llueva, saldremos.", "conector": "a menos que", "tipo": "condición"},
    {"oracion": "Ella quería ayudar, pero no sabía cómo.", "conector": "pero", "tipo": "contraste"},
    {"oracion": "Estaba nervioso, por eso no habló.", "conector": "por eso", "tipo": "consecuencia"},
    {"oracion": "En caso de que no vengas, avisaré.", "conector": "en caso de que", "tipo": "condición"},
    {"oracion": "No comí desayuno, así que tengo hambre.", "conector": "así que", "tipo": "consecuencia"},
    {"oracion": "Salí temprano porque tenía una cita.", "conector": "porque", "tipo": "causa"},
    {"oracion": "No le gusta correr, aunque es rápido.", "conector": "aunque", "tipo": "contraste"},
    {"oracion": "Si no estudias, reprobarás.", "conector": "si", "tipo": "condición"},
    {"oracion": "Le dolía la cabeza, entonces descansó.", "conector": "entonces", "tipo": "consecuencia"},
    {"oracion": "Jugamos en casa porque llovía.", "conector": "porque", "tipo": "causa"},
    {"oracion": "Quiso ir, pero se quedó dormido.", "conector": "pero", "tipo": "contraste"},
    {"oracion": "Aunque está cansado, sigue trabajando.", "conector": "aunque", "tipo": "contraste"},
    {"oracion": "Si llueve, cancelan el partido.", "conector": "si", "tipo": "condición"},
    {"oracion": "No entendió la tarea, por eso no la hizo.", "conector": "por eso", "tipo": "consecuencia"}
]

elogios = [
    "🧠 ¡Muy bien!",
    "🌟 ¡Conector lógico detectado!",
    "👏 ¡Buen análisis sintáctico!",
    "🎉 ¡Correcto!",
    "⭐ ¡Excelente pensamiento lógico!"
]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Conector: {ej['conector']} | Tipo: {ej['tipo'].capitalize()}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['oracion']}")
        respuesta = input("👉 ¿Cuál es el conector lógico?: ").strip().lower()
        tipo = input("👉 ¿Qué tipo es? (causa, consecuencia, contraste, condición): ").strip().lower()
        if respuesta == ej["conector"] and tipo == ej["tipo"]:
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: Conector: '{ej['conector']}' | Tipo: '{ej['tipo']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Maestro del Enlace Lógico! 🧠🔗")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES CON CONECTORES")
    print("Escribe 20 oraciones usando conectores lógicos (ej. 'No fui porque llovía.'):\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo con enlaces lógicos!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 7.º Primaria – Lección 6")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
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
            print("👋 ¡Gracias por conectar ideas con lógica!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
