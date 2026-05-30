import time
import random

# Lista de preguntas de práctica
preguntas = [
    {
        "tipo": "seleccion",
        "pregunta": "¿Cuál es una frase comparativa correcta?",
        "opciones": [
            "El coche es tan rápido como un avión.",
            "El coche es tan rápido un avión.",
            "El coche como un avión es rápido."
        ],
        "respuesta": 1
    },
    {
        "tipo": "completar",
        "pregunta": "Completa: La cosa fue más deprisa de lo ___ yo esperaba.",
        "respuesta": "que"
    },
    {
        "tipo": "seleccion",
        "pregunta": "¿Qué tipo de comparación es: 'Tiene un hijo de la misma edad que el tuyo'?",
        "opciones": [
            "Comparación de sujetos",
            "Comparación de atributos o complementos",
            "Comparación de verbos"
        ],
        "respuesta": 2
    },
    {
        "tipo": "completar",
        "pregunta": "Completa: El forro es de distinto color ___ la tela.",
        "respuesta": "que"
    }
]

historial_frases = []

def modo_practica():
    print("\n🧪 MODO PRÁCTICA\n")
    random.shuffle(preguntas)
    for p in preguntas:
        if p["tipo"] == "seleccion":
            print(p["pregunta"])
            for idx, op in enumerate(p["opciones"], 1):
                print(f"{idx}. {op}")
            intento = int(input("Elige una opción: "))
            if intento == p["respuesta"]:
                print("✅ ¡Correcto!")
                historial_frases.append(p["opciones"][p["respuesta"] - 1])
            else:
                print("❌ Incorrecto.")
                print(f"La respuesta correcta era: {p['opciones'][p['respuesta'] - 1]}")
        elif p["tipo"] == "completar":
            print(p["pregunta"])
            respuesta = input("Tu respuesta: ").strip().lower()
            if respuesta == p["respuesta"]:
                print("✅ ¡Correcto!")
                frase_completa = p["pregunta"].replace("___", respuesta)
                historial_frases.append(frase_completa)
            else:
                print(f"❌ Incorrecto. La respuesta correcta es: '{p['respuesta']}'")

def modo_examen():
    print("\n📝 MODO EXAMEN (3 preguntas, 60 segundos)\n")
    start_time = time.time()
    puntos = 0
    seleccionadas = random.sample(preguntas, 3)
    for p in seleccionadas:
        if time.time() - start_time > 60:
            print("⏰ ¡Tiempo agotado!")
            break
        if p["tipo"] == "seleccion":
            print(p["pregunta"])
            for idx, op in enumerate(p["opciones"], 1):
                print(f"{idx}. {op}")
            intento = int(input("Elige una opción: "))
            if intento == p["respuesta"]:
                puntos += 1
        elif p["tipo"] == "completar":
            print(p["pregunta"])
            respuesta = input("Tu respuesta: ").strip().lower()
            if respuesta == p["respuesta"]:
                puntos += 1
    print(f"\n🎯 Puntaje final: {puntos}/3")

def revisar_historial():
    if not historial_frases:
        print("❌ No has registrado frases todavía.")
        return
    print("\n📚 Frases correctas que has completado o identificado:\n")
    for i, frase in enumerate(historial_frases[:50], 1):
        print(f"{i}. {frase}")

    repetir = input("\n¿Quieres volver a escribirlas para memorizar? (s/n): ")
    if repetir.lower() == "s":
        correctas = 0
        for i, frase in enumerate(historial_frases[:50], 1):
            print(f"\nReescribe la frase #{i}:")
            entrada = input("→ ").strip()
            if entrada.lower() == frase.lower():
                print("✅ Correcto.")
                correctas += 1
            else:
                print(f"❌ Incorrecto. Era: {frase}")
        print(f"\n💡 Acertaste {correctas}/{len(historial_frases[:50])} frases.")

def menu_principal():
    while True:
        print("\n📘 PRÁCTICA DE CONSTRUCCIÓN COMPARATIVA")
        print("1. Modo práctica")
        print("2. Modo examen (con tiempo)")
        print("3. Revisar frases y reescribir")
        print("4. Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == "1":
            modo_practica()
        elif eleccion == "2":
            modo_examen()
        elif eleccion == "3":
            revisar_historial()
        elif eleccion == "4":
            print("¡Hasta pronto! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
