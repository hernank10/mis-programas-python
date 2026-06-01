import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO EXPRESAMOS IDEAS GENERALES SIN DECIR 'YO'?

Una oración impersonal no menciona a ninguna persona específica.
Usamos expresiones como:

🔹 se dice que...
🔹 es importante...
🔹 es posible que...
🔹 no se permite...
🔹 se cree que...

🎯 Estas estructuras permiten dar opiniones, instrucciones o afirmaciones con estilo más formal.

📝 Ejemplo:
"Yo pienso que leer es bueno." → "Se dice que leer mejora la mente."
"Yo creo que debemos ayudar." → "Es importante ayudar a los demás."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"personal": "Yo pienso que el deporte es bueno.", "impersonal": "Se cree que el deporte es beneficioso."},
    {"personal": "Nosotros sabemos que la lectura ayuda.", "impersonal": "Se dice que la lectura mejora el pensamiento."},
    {"personal": "Yo creo que debemos respetar las normas.", "impersonal": "Es importante respetar las normas."},
    {"personal": "Yo pienso que la tecnología es útil.", "impersonal": "Es posible que la tecnología facilite la vida."},
    {"personal": "Todos saben que dormir bien es necesario.", "impersonal": "Se reconoce que el descanso es fundamental."}
]

# 📝 20 ejercicios de transformación
ejercicios = [
    {"personal": "Yo creo que el reciclaje ayuda al planeta.", "impersonal": "Se dice que el reciclaje ayuda al planeta."},
    {"personal": "Nosotros pensamos que la comida sana es buena.", "impersonal": "Se recomienda consumir comida sana."},
    {"personal": "Yo sé que el respeto es importante.", "impersonal": "Es importante respetar a los demás."},
    {"personal": "Yo pienso que el arte es necesario.", "impersonal": "Se valora la importancia del arte."},
    {"personal": "Nosotros creemos que el trabajo en equipo funciona.", "impersonal": "Se reconoce que el trabajo en equipo da buenos resultados."}
]

elogios = [
    "🎩 ¡Estilo formal logrado!",
    "🧠 ¡Buena transformación a impersonal!",
    "✅ ¡Redacción clara sin ‘yo’!",
    "👏 ¡Muy bien, eso suena profesional!",
    "🌟 ¡Excelente uso de estructuras neutras!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TRANSFORMACIÓN:")
    for ej in ejemplos:
        print(f"👤 Personal: {ej['personal']}")
        print(f"🤖 Impersonal: {ej['impersonal']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 TRANSFORMA LAS FRASES A IMPERSONAL:")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Frase personal: {ej['personal']}")
        respuesta = input("👉 Redacción impersonal: ").strip().lower()
        if respuesta == ej['impersonal'].lower():
            print(random.choice(elogios))
        else:
            print(f"⚠️ Una forma posible sería: '{ej['impersonal']}'")

# ✍️ Crear oraciones impersonales propias
def escribir_propias():
    print("\n✍️ ESCRIBE 5 FRASES IMPERSONALES:")
    frases = []
    for i in range(1, 6):
        frase = input(f"👉 Oración impersonal {i}: ").strip()
        frases.append(frase)

    print("\n📘 Tus frases en estilo formal:")
    for idx, f in enumerate(frases, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Muy bien! Tu escritura ahora suena informativa y profesional.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 8.º Grado – Lección 7: Oraciones Impersonales")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir frases propias ✍️")
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
            print("👋 ¡Gracias por transformar tu estilo hacia lo formal y reflexivo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
