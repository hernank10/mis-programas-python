import random
import json

# Base de datos de fonemas
fonemas = {
    "vocales": {
        "a": "Vocal abierta y central",
        "e": "Vocal semiabierta y anterior",
        "i": "Vocal cerrada y anterior",
        "o": "Vocal semiabierta y posterior",
        "u": "Vocal cerrada y posterior",
    },
    "consonantes": {
        "p": "Consonante bilabial oclusiva sorda",
        "b": "Consonante bilabial oclusiva sonora",
        "m": "Consonante bilabial nasal sonora",
        "t": "Consonante dental oclusiva sorda",
        "d": "Consonante dental oclusiva sonora",
        "s": "Consonante alveolar fricativa sorda",
    },
    "diptongos": {
        "ai": "Diptongo creciente: vocal cerrada + vocal abierta",
        "eu": "Diptongo decreciente: vocal abierta + vocal cerrada",
        "ie": "Diptongo creciente: vocal cerrada + vocal abierta",
    },
}

# Introducción
def mostrar_introduccion():
    print("\n🎓 Bienvenido al Estudio del Sistema Fonético Castellano 🎓")
    print(
        "Este programa te ayudará a aprender y practicar fonemas en español.\n"
        "Incluye teoría, cuestionarios interactivos, y ejercicios prácticos.\n"
    )

# Guardar progreso
def guardar_progreso(progreso):
    with open("progreso.json", "w") as archivo:
        json.dump(progreso, archivo)
    print("📂 Progreso guardado exitosamente.")

# Cargar progreso
def cargar_progreso():
    try:
        with open("progreso.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"correctas": 0, "incorrectas": 0}

# Menú principal
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Teoría")
    print("2. Cuestionario Interactivo")
    print("3. Ejercicios Prácticos")
    print("4. Ver progreso")
    print("5. Salir")

# Teoría
def mostrar_teoria():
    print("\n--- Sección de Teoría ---")
    for categoria, sonidos in fonemas.items():
        print(f"\n📘 {categoria.capitalize()}:")
        for fonema, descripcion in sonidos.items():
            print(f"  - {fonema}: {descripcion}")

# Cuestionario interactivo
def cuestionario(progreso):
    print("\n--- Cuestionario Interactivo ---")
    preguntas = []
    for categoria, sonidos in fonemas.items():
        preguntas.extend([(fonema, descripcion, categoria) for fonema, descripcion in sonidos.items()])
    random.shuffle(preguntas)
    
    for fonema, descripcion, categoria in preguntas[:5]:
        print(f"\n💡 Fonema: {fonema}")
        print(f"Pregunta: ¿A qué categoría pertenece este fonema? (vocales, consonantes, diptongos)")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == categoria:
            print("✅ ¡Correcto! 😄")
            progreso["correctas"] += 1
        else:
            print(f"❌ Incorrecto. Es un fonema de la categoría '{categoria}'.")
            progreso["incorrectas"] += 1

# Ejercicios prácticos
def ejercicios(practica):
    print("\n--- Ejercicios Prácticos ---")
    categoria = random.choice(list(fonemas.keys()))
    fonema, descripcion = random.choice(list(fonemas[categoria].items()))
    print(f"🖍 Fonema: {fonema}")
    print("Pregunta: Describe este fonema basándote en sus características.")
    respuesta = input("Tu respuesta: ").strip()
    if respuesta.lower() in descripcion.lower():
        print("✅ ¡Bien hecho! 👍")
        practica["correctas"] += 1
    else:
        print(f"❌ No es correcto. La descripción es: {descripcion}")
        practica["incorrectas"] += 1

# Mostrar progreso
def ver_progreso(progreso):
    print("\n--- Progreso ---")
    print(f"Respuestas correctas: {progreso['correctas']} 🎉")
    print(f"Respuestas incorrectas: {progreso['incorrectas']} 💡")

# Programa principal
def main():
    mostrar_introduccion()
    progreso = cargar_progreso()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            cuestionario(progreso)
        elif opcion == "3":
            ejercicios(progreso)
        elif opcion == "4":
            ver_progreso(progreso)
        elif opcion == "5":
            guardar_progreso(progreso)
            print("¡Gracias por usar el programa! 😊")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    main()
