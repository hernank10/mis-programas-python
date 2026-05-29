import random
import json

# Base de datos de fonemas y fonología (Español e Inglés)
fonemas_es = {
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

fonemas_en = {
    "vocales": {
        "ɪ": "Vocal cerrada anterior no redondeada (bit)",
        "i:": "Vocal cerrada anterior no redondeada larga (bead)",
        "ʊ": "Vocal cerrada posterior redondeada (book)",
        "u:": "Vocal cerrada posterior redondeada larga (food)",
        "æ": "Vocal semiabierta anterior no redondeada (cat)",
    },
    "consonantes": {
        "p": "Consonante bilabial oclusiva sorda",
        "b": "Consonante bilabial oclusiva sonora",
        "tʃ": "Consonante postalveolar africada sorda (ch)",
        "dʒ": "Consonante postalveolar africada sonora (j)",
        "θ": "Consonante interdental fricativa sorda (think)",
    },
    "diptongos": {
        "eɪ": "Diptongo (face)",
        "aɪ": "Diptongo (price)",
        "ɔɪ": "Diptongo (choice)",
        "aʊ": "Diptongo (mouth)",
        "əʊ": "Diptongo (goat)",
    },
}

fonologia = {
    "es": {
        "definicion": "El sistema fonológico del español está compuesto por los fonemas, que son las unidades mínimas de sonido que distinguen significado.",
        "clasificacion": {
            "vocales": "Son sonidos que se producen sin obstrucción del flujo de aire. En español hay cinco fonemas vocálicos: /a/, /e/, /i/, /o/, /u/.",
            "consonantes": "Son sonidos que implican algún tipo de obstrucción del flujo de aire. En español hay 19 fonemas consonánticos.",
        },
    },
    "en": {
        "definicion": "El sistema fonológico del inglés incluye 12 vocales monoftongas, 8 diptongos y 24 consonantes, con variaciones regionales.",
        "clasificacion": {
            "vocales": "Incluyen monoftongos cortos (ɪ, ʊ, æ) y largos (iː, uː).",
            "consonantes": "Incluyen sonidos específicos como fricativas interdentales (θ, ð).",
        },
    },
}

# Introducción
def mostrar_introduccion():
    print("\n🎓 Bienvenido al Estudio del Sistema Fonético y Fonológico 🎓")
    print("Incluye secciones para el español y el inglés, con teoría, cuestionarios y ejercicios prácticos.\n")

# Menú principal
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Teoría del Sistema Fonético (Español)")
    print("2. Cuestionario Interactivo (Fonética Española)")
    print("3. Teoría del Sistema Fonológico (Español)")
    print("4. Cuestionario Interactivo (Fonología Española)")
    print("5. Teoría del Sistema Fonético (Inglés)")
    print("6. Cuestionario Interactivo (Fonética Inglesa)")
    print("7. Teoría del Sistema Fonológico (Inglés)")
    print("8. Cuestionario Interactivo (Fonología Inglesa)")
    print("9. Ver progreso")
    print("10. Salir")

# Teoría fonética
def mostrar_teoria_fonetica(fonemas):
    print("\n--- Sección de Teoría: Sistema Fonético ---")
    for categoria, sonidos in fonemas.items():
        print(f"\n📘 {categoria.capitalize()}:")
        for fonema, descripcion in sonidos.items():
            print(f"  - {fonema}: {descripcion}")

# Teoría fonológica
def mostrar_teoria_fonologica(fonologia, idioma):
    print("\n--- Sección de Teoría: Sistema Fonológico ---")
    print(f"📖 Definición: {fonologia[idioma]['definicion']}\n")
    for clave, descripcion in fonologia[idioma]["clasificacion"].items():
        print(f"📘 {clave.capitalize()}: {descripcion}")

# Cuestionarios
def cuestionario_interactivo(fonemas, progreso):
    print("\n--- Cuestionario Interactivo ---")
    preguntas = []
    for categoria, sonidos in fonemas.items():
        preguntas.extend([(fonema, categoria) for fonema in sonidos])
    random.shuffle(preguntas)

    for fonema, categoria in preguntas[:5]:
        print(f"\n💡 Fonema: {fonema}")
        print("Pregunta: ¿A qué categoría pertenece este fonema? (vocales, consonantes, diptongos)")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == categoria:
            print("✅ ¡Correcto! 😄")
            progreso["correctas"] += 1
        else:
            print(f"❌ Incorrecto. Es un fonema de la categoría '{categoria}'.")
            progreso["incorrectas"] += 1

# Ver progreso
def ver_progreso(progreso):
    print("\n--- Progreso ---")
    print(f"Respuestas correctas: {progreso['correctas']} 🎉")
    print(f"Respuestas incorrectas: {progreso['incorrectas']} 💡")

# Programa principal
def main():
    mostrar_introduccion()
    progreso = {"correctas": 0, "incorrectas": 0}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-10): ").strip()
        if opcion == "1":
            mostrar_teoria_fonetica(fonemas_es)
        elif opcion == "2":
            cuestionario_interactivo(fonemas_es, progreso)
        elif opcion == "3":
            mostrar_teoria_fonologica(fonologia, "es")
        elif opcion == "4":
            cuestionario_interactivo(fonemas_es, progreso)
        elif opcion == "5":
            mostrar_teoria_fonetica(fonemas_en)
        elif opcion == "6":
            cuestionario_interactivo(fonemas_en, progreso)
        elif opcion == "7":
            mostrar_teoria_fonologica(fonologia, "en")
        elif opcion == "8":
            cuestionario_interactivo(fonemas_en, progreso)
        elif opcion == "9":
            ver_progreso(progreso)
        elif opcion == "10":
            print("¡Gracias por usar el programa! 😊")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
