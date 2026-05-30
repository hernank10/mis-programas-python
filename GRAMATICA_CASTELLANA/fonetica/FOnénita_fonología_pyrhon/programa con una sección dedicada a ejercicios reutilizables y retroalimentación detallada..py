import random
import json
import os

# Base de datos de fonemas y fonología
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

# Base de datos de ejercicios
ejercicios = {
    "espanol": [
        {"pregunta": "¿Qué tipo de fonema es 'a'?", "respuesta": "vocal"},
        {"pregunta": "¿Qué tipo de fonema es 'p'?", "respuesta": "consonante"},
        {"pregunta": "¿Qué tipo de fonema es 'ai'?", "respuesta": "diptongo"},
    ],
    "ingles": [
        {"pregunta": "¿Qué tipo de fonema es 'ɪ'?", "respuesta": "vocal"},
        {"pregunta": "¿Qué tipo de fonema es 'θ'?", "respuesta": "consonante"},
        {"pregunta": "¿Qué tipo de fonema es 'eɪ'?", "respuesta": "diptongo"},
    ],
}

# Cargar y guardar ejercicios
def cargar_progreso(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    return {"correctas": 0, "incorrectas": 0, "historial": []}

def guardar_progreso(nombre_archivo, progreso):
    with open(nombre_archivo, "w") as archivo:
        json.dump(progreso, archivo)

# Retroalimentación
def retroalimentar(pregunta, respuesta_correcta):
    print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}.")
    if "vocal" in respuesta_correcta:
        print("💡 Las vocales son sonidos que no presentan obstrucción del flujo de aire.")
    elif "consonante" in respuesta_correcta:
        print("💡 Las consonantes se producen con una obstrucción parcial o total del flujo de aire.")
    elif "diptongo" in respuesta_correcta:
        print("💡 Los diptongos son combinaciones de dos vocales en una misma sílaba.")

# Cuestionario con ejercicios
def cuestionario_ejercicios(idioma, progreso):
    print(f"\n--- Cuestionario Interactivo ({idioma.capitalize()}) ---")
    ejercicios_idioma = ejercicios[idioma]
    random.shuffle(ejercicios_idioma)
    for ejercicio in ejercicios_idioma[:5]:
        print(f"\n💡 {ejercicio['pregunta']}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == ejercicio["respuesta"]:
            print("✅ ¡Correcto! 😄")
            progreso["correctas"] += 1
        else:
            retroalimentar(ejercicio["pregunta"], ejercicio["respuesta"])
            progreso["incorrectas"] += 1
        progreso["historial"].append({"pregunta": ejercicio["pregunta"], "respuesta": respuesta})

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

# Programa principal
def main():
    print("\n🎓 Bienvenido al Programa de Estudio del Sistema Fonético y Fonológico 🎓")
    progreso = cargar_progreso("progreso.json")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-10): ").strip()
        if opcion == "1":
            mostrar_teoria_fonetica(fonemas_es)
        elif opcion == "2":
            cuestionario_ejercicios("espanol", progreso)
        elif opcion == "3":
            mostrar_teoria_fonologica(fonologia, "es")
        elif opcion == "4":
            cuestionario_ejercicios("espanol", progreso)
        elif opcion == "5":
            mostrar_teoria_fonetica(fonemas_en)
        elif opcion == "6":
            cuestionario_ejercicios("ingles", progreso)
        elif opcion == "7":
            mostrar_teoria_fonologica(fonologia, "en")
        elif opcion == "8":
            cuestionario_ejercicios("ingles", progreso)
        elif opcion == "9":
            print(f"\nCorrectas: {progreso['correctas']}, Incorrectas: {progreso['incorrectas']}")
            print("Historial de respuestas:")
            for entrada in progreso["historial"][-5:]:
                print(f"- Pregunta: {entrada['pregunta']}, Respuesta: {entrada['respuesta']}")
        elif opcion == "10":
            guardar_progreso("progreso.json", progreso)
            print("¡Progreso guardado! Hasta la próxima. 😊")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
