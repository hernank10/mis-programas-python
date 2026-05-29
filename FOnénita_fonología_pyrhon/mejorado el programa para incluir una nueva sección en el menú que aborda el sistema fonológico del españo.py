import random
import json

# Base de datos de fonemas y fonología
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

fonologia = {
    "teoria": {
        "definicion": "El sistema fonológico del español está compuesto por los fonemas, que son las unidades mínimas de sonido que distinguen significado.",
        "clasificacion": {
            "vocales": "Son sonidos que se producen sin obstrucción del flujo de aire. En español hay cinco fonemas vocálicos: /a/, /e/, /i/, /o/, /u/.",
            "consonantes": "Son sonidos que implican algún tipo de obstrucción del flujo de aire. En español hay 19 fonemas consonánticos.",
        },
        "rasgos": {
            "punto_de_articulacion": "Describe dónde se produce el sonido (bilabial, dental, velar, etc.).",
            "modo_de_articulacion": "Indica cómo se produce el sonido (oclusivo, fricativo, nasal, etc.).",
            "sonoridad": "Se refiere a la vibración de las cuerdas vocales: sonidos sonoros y sordos.",
        },
    }
}

# Introducción
def mostrar_introduccion():
    print("\n🎓 Bienvenido al Estudio del Sistema Fonético y Fonológico del Español 🎓")
    print(
        "Este programa incluye teoría, cuestionarios y ejercicios prácticos basados en las normas de la RAE y la Academia Colombiana de la Lengua.\n"
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
    print("1. Teoría del Sistema Fonético")
    print("2. Cuestionario Interactivo (Fonética)")
    print("3. Ejercicios Prácticos")
    print("4. Teoría del Sistema Fonológico (RAE)")
    print("5. Cuestionario Interactivo (Fonología)")
    print("6. Ver progreso")
    print("7. Salir")

# Teoría fonética
def mostrar_teoria_fonetica():
    print("\n--- Sección de Teoría: Sistema Fonético ---")
    for categoria, sonidos in fonemas.items():
        print(f"\n📘 {categoria.capitalize()}:")
        for fonema, descripcion in sonidos.items():
            print(f"  - {fonema}: {descripcion}")

# Teoría fonológica
def mostrar_teoria_fonologica():
    print("\n--- Sección de Teoría: Sistema Fonológico ---")
    print(f"📖 Definición: {fonologia['teoria']['definicion']}\n")
    for clave, descripcion in fonologia["teoria"].items():
        if isinstance(descripcion, str):
            continue
        print(f"📘 {clave.capitalize().replace('_', ' ')}:")
        for subclave, subdescripcion in descripcion.items():
            print(f"  - {subclave.replace('_', ' ').capitalize()}: {subdescripcion}")

# Cuestionario fonético
def cuestionario_fonetico(progreso):
    print("\n--- Cuestionario Interactivo: Fonética ---")
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

# Cuestionario fonológico
def cuestionario_fonologico(progreso):
    print("\n--- Cuestionario Interactivo: Fonología ---")
    preguntas = [
        ("¿Cuántos fonemas vocálicos tiene el español?", "5"),
        ("¿Cuántos fonemas consonánticos tiene el español?", "19"),
        ("¿Qué describe el punto de articulación?", "Dónde se produce el sonido"),
        ("¿Qué indica el modo de articulación?", "Cómo se produce el sonido"),
        ("¿Qué diferencia los sonidos sonoros de los sordos?", "La vibración de las cuerdas vocales"),
    ]
    random.shuffle(preguntas)

    for pregunta, respuesta_correcta in preguntas[:5]:
        print(f"\n💡 {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() in respuesta_correcta.lower():
            print("✅ ¡Correcto! 😄")
            progreso["correctas"] += 1
        else:
            print(f"❌ Incorrecto. La respuesta es: {respuesta_correcta}.")
            progreso["incorrectas"] += 1

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
        opcion = input("Selecciona una opción (1-7): ").strip()
        if opcion == "1":
            mostrar_teoria_fonetica()
        elif opcion == "2":
            cuestionario_fonetico(progreso)
        elif opcion == "3":
            print("Ejercicios prácticos próximamente. ¡Permanece atento!")
        elif opcion == "4":
            mostrar_teoria_fonologica()
        elif opcion == "5":
            cuestionario_fonologico(progreso)
        elif opcion == "6":
            ver_progreso(progreso)
        elif opcion == "7":
            guardar_progreso(progreso)
            print("¡Gracias por usar el programa! 😊")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    main()
