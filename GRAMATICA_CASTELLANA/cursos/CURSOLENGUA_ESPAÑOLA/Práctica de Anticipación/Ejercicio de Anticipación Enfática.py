import random

adjetivo_absoluto = [
    "Libros, tiene miles.",
    "Amigos, conserva pocos.",
    "Ideas, le sobran.",
    "Problemas, ha enfrentado bastantes.",
    "Sueños, mantiene vivos muchos.",
    "Errores, cometió incontables.",
    "Metas, ha alcanzado numerosas.",
    "Historias, conoce muchas.",
    "Pasiones, ha tenido muchas.",
    "Vacaciones, ha disfrutado espléndidas."
]

pronombre_retoma = [
    "Libros, los guarda con celo.",
    "Amigos, los valora muchísimo.",
    "Ideas, las organiza con cuidado.",
    "Problemas, los enfrenta con valentía.",
    "Sueños, los persigue sin cesar.",
    "Errores, los repasa para aprender.",
    "Metas, las cumple con disciplina.",
    "Historias, las relata con pasión.",
    "Pasiones, las alimenta a diario.",
    "Vacaciones, las planea con entusiasmo."
]

def mostrar_menu():
    print("\n--- Ejercicio de Anticipación Enfática ---")
    print("1. Ver ejemplos por categoría")
    print("2. Escribir una oración y clasificarla")
    print("3. Salir")

def ver_ejemplos():
    print("\nEjemplos con adjetivo absoluto:")
    for oracion in random.sample(adjetivo_absoluto, 5):
        print(" →", oracion)

    print("\nEjemplos con pronombre que retoma el sustantivo:")
    for oracion in random.sample(pronombre_retoma, 5):
        print(" →", oracion)

def clasificar_oracion(oracion):
    if any(pron in oracion for pron in ["los ", "las ", "lo ", "la "]):
        return "Pronombre que retoma el sustantivo"
    elif any(adj in oracion for adj in ["muchos", "pocos", "varios", "numerosas", "incontables", "bastantes"]):
        return "Adjetivo absoluto"
    else:
        return "No se pudo clasificar con certeza"

def escribir_y_clasificar():
    oracion = input("\nEscribe tu oración con anticipación enfática:\n→ ")
    categoria = clasificar_oracion(oracion)
    print(f"Clasificación tentativa: {categoria}")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-3): ")

        if opcion == "1":
            ver_ejemplos()
        elif opcion == "2":
            escribir_y_clasificar()
        elif opcion == "3":
            print("¡Hasta luego! Sigue practicando 😊")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
