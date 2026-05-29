# -*- coding: utf-8 -*-
# Programa interactivo para aprender a escribir frases y transformarlas (RAE + ejemplos)

import random

# === Reglas básicas según la RAE (simplificadas para este ejercicio) ===
reglas_rae = {
    1: "La negación en español puede expresarse con 'no', 'nunca', 'jamás', etc.",
    2: "La doble negación en español es gramatical y refuerza el sentido negativo: 'No vino nadie'.",
    3: "Las construcciones concesivas usan 'aunque', 'por más que', 'si bien', etc.",
    4: "El adverbio 'sí' con tilde se emplea para la afirmación enfática: 'Sí quiero'.",
    5: "El contraste afirmación/negación da lugar a oposiciones expresivas: 'No puedes evitarlo, pero sí puedes intentarlo'."
}

# === Ejemplos categorizados ===
ejemplos = {
    "Negación": [
        "No puedo hacerlo.",
        "Nunca me lo dijiste.",
        "Tan si quieras no puedes intentarlo."
    ],
    "Afirmación": [
        "Sí lo puedo lograr.",
        "Por más que no quieras, sí puedes intentarlo.",
        "Claro que sí vendré mañana."
    ],
    "Concesivas": [
        "Aunque no quieras, debo decírtelo.",
        "Por más que intentes, no cambiarás mi decisión."
    ],
    "Dobles negaciones": [
        "No había nadie en la sala.",
        "No quiero que nadie se entere."
    ]
}

# === Conversor simple de frases negativas ↔ afirmativas ===
def convertir_frase(frase: str) -> str:
    # Diccionario de cambios básicos
    conversiones = {
        "no puedes": "sí puedes",
        "sí puedes": "no puedes",
        "tan si quieras": "por más que no quieras",
        "por más que no quieras": "tan si quieras"
    }
    for k, v in conversiones.items():
        if k in frase.lower():
            return frase.lower().replace(k, v)
    return "No encontré cómo convertir esta frase automáticamente."

# === Menú principal ===
def menu():
    while True:
        print("\n--- MENÚ DE APRENDIZAJE ---")
        print("1. Ver reglas de la RAE")
        print("2. Ver ejemplos por categoría")
        print("3. Practicar reescritura de frases")
        print("4. Convertir frase negativa ↔ afirmativa")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Reglas de la RAE ---")
            for num, regla in reglas_rae.items():
                print(f"{num}. {regla}")

        elif opcion == "2":
            print("\nCategorías disponibles:")
            for cat in ejemplos.keys():
                print(f"- {cat}")
            cat = input("Elige una categoría: ")
            if cat in ejemplos:
                print(f"\nEjemplos de {cat}:")
                for e in ejemplos[cat]:
                    print(f"- {e}")
            else:
                print("Categoría no encontrada.")

        elif opcion == "3":
            print("\n--- Práctica de reescritura ---")
            frase = random.choice(random.choice(list(ejemplos.values())))
            print(f"Frase original: {frase}")
            respuesta = input("Reescríbela cambiando su forma (afirmativa/negativa): ")
            print(f"Tu respuesta: {respuesta}")
            print(f"Posible transformación: {convertir_frase(frase)}")

        elif opcion == "4":
            frase = input("\nEscribe una frase para convertir: ")
            print(f"Conversión: {convertir_frase(frase)}")

        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

# === Ejecutar el programa ===
if __name__ == "__main__":
    menu()
