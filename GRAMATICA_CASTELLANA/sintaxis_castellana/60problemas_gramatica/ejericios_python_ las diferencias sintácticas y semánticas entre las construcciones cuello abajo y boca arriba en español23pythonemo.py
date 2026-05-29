import json
import random

PROGRESO_FILE = "progreso.json"
EJEMPLOS_FILE = "ejemplos.json"

def cargar_ejemplos():
    try:
        with open(EJEMPLOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"locativa": "Las lágrimas caían cuello abajo. 😭⬇️", "manera": "Lo acostaron boca arriba. 😴⬆️"}
        ]

def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_FILE, "w") as file:
        json.dump(ejemplos, file, indent=4)

def cargar_progreso():
    try:
        with open(PROGRESO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_progreso(progreso):
    with open(PROGRESO_FILE, "w") as file:
        json.dump(progreso, file, indent=4)

def mostrar_introduccion():
    print("📖 ¡Bienvenido al estudio de construcciones gramaticales! 📝")
    print("Exploramos construcciones como 'cuello abajo' y 'boca arriba' en español. 🤔📚")

def mostrar_teoria():
    print("🧐 Las construcciones pueden indicar una ubicación 📍 o la manera en que ocurre una acción 🚶‍♂️💨.")

def mostrar_ejemplos():
    print("🔍 Ejemplos de construcciones:")
    ejemplos = cargar_ejemplos()
    for ej in ejemplos:
        print(f"📌 Locativa: {ej['locativa']} | 🎭 Manera: {ej['manera']}")

def agregar_ejemplo():
    locativa = input("✍️ Ingrese un ejemplo de locativa: ") + " ⬇️"
    manera = input("✍️ Ingrese un ejemplo de manera: ") + " ⬆️"
    ejemplos = cargar_ejemplos()
    ejemplos.append({"locativa": locativa, "manera": manera})
    guardar_ejemplos(ejemplos)
    print("✅ Ejemplo agregado correctamente. 🎉")

def ejercicios_escritura():
    ejercicios = [
        "✍️ Escribe una oración con una construcción locativa.",
        "🔄 Transforma 'Las gotas caían por la cara' en una construcción locativa.",
        "✍️ Escribe una oración con 'boca arriba'.",
        "🔄 Convierte 'Se deslizaba por la espalda' en una construcción locativa.",
        "❓ Explica la diferencia entre 'cuello abajo' y 'boca arriba'.",
        "📝 Corrige la oración: 'El agua resbalaba abajo la espalda'.",
        "✍️ Crea una oración donde 'arriba' indique manera.",
        "🔄 Transforma 'Caminaba con pasos pesados' en una oración con construcción de manera.",
        "📝 Completa la oración: 'Las hojas caían ______' (locativa).",
        "✍️ Escribe una oración con 'cabeza abajo'.",
        "🔄 Reescribe 'Se acostó en la cama con la cara hacia el techo' usando una construcción de manera.",
        "📝 Corrige: 'El perro durmió barriga en el suelo'.",
        "✍️ Crea una oración usando 'espalda abajo'.",
        "🔄 Transforma 'Lo llevaban de lado' en una construcción más precisa.",
        "❓ Explica cuándo usar 'boca abajo' y cuándo 'de cabeza'."
    ]
    progreso = cargar_progreso()
    
    for i, ej in enumerate(ejercicios):
        print(f"{i+1}. {ej} ✍️")
        respuesta = input("Tu respuesta: ")
        progreso[str(i)] = respuesta
        guardar_progreso(progreso)
        print("✅ Respuesta guardada. 📁")

def ver_progreso():
    progreso = cargar_progreso()
    if not progreso:
        print("😢 Aún no has registrado respuestas.")
    else:
        print("📊 Progreso guardado:")
        for i, respuesta in progreso.items():
            print(f"📌 Ejercicio {int(i) + 1}: {respuesta}")

def juego():
    niveles = ["🐣 Básico", "📖 Intermedio", "🚀 Avanzado"]
    nivel = random.choice(niveles)
    print(f"🎮 Nivel seleccionado: {nivel}")
    
    if nivel == "🐣 Básico":
        respuesta = input("🎲 Juego - Nivel Básico: ¿Es locativa o de manera? Escribe tu respuesta: ")
    elif nivel == "📖 Intermedio":
        respuesta = input("🎲 Juego - Nivel Intermedio: Completa la oración: 'Las lágrimas caían ______'. ✍️")
    else:
        respuesta = input("🎲 Juego - Nivel Avanzado: Reescribe la oración cambiando la estructura: 'Lo acostaron boca arriba'. ✍️")
    
    print(f"👏 Escribiste: {respuesta} 🎉")

def menu():
    while True:
        print("\n📜 Menú de estudio:")
        print("1️⃣ Introducción 📖")
        print("2️⃣ Teoría 📚")
        print("3️⃣ Ejemplos 🔍")
        print("4️⃣ Agregar Ejemplo ✍️")
        print("5️⃣ Ejercicios de Escritura 📝")
        print("6️⃣ Ver Progreso 📊")
        print("7️⃣ Juego 🎮")
        print("8️⃣ Salir 🚪")
        
        opcion = input("👉 Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            mostrar_teoria()
        elif opcion == "3":
            mostrar_ejemplos()
        elif opcion == "4":
            agregar_ejemplo()
        elif opcion == "5":
            ejercicios_escritura()
        elif opcion == "6":
            ver_progreso()
        elif opcion == "7":
            juego()
        elif opcion == "8":
            print("👋 Saliendo del programa. ¡Hasta la próxima! 🏁")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo. 🔄")

if __name__ == "__main__":
    menu()
