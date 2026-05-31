# Programa educativo para aprender reglas ortográficas

import json

# Lista de 100 reglas ortográficas
rules = [
    "1. Se escriben con 'b' los verbos terminados en 'bir', excepto hervir, servir y vivir.",
    "2. Se escriben con 'c' los diminutivos terminados en 'cito' y 'ecito', excepto si la palabra base contiene 's'.",
    "3. Se escribe 'g' delante de 'e' o 'i' en palabras como 'genio' o 'girar'.",
    # Agregar las 97 reglas restantes...
]

# Función para mostrar el menú principal
def show_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Leer📖 las reglas ortográficas😊📖")
    print("2. Practicar las reglas 📝(escribir y verificar)")
    print("3. Escribir traducción al inglés⏳🕵")
    print("4. Revisar progreso🤔")
    print("5. Salir")

# Función para mostrar las reglas
def display_rules():
    print("\n--- Reglas Ortográficas ---")
    for i, rule in enumerate(rules, 1):
        print(f"{i}. {rule}")

# Función para practicar las reglas
def practice_rules():
    print("\n--- Práctica de Reglas Ortográficas ---")
    correct = 0
    for i, rule in enumerate(rules, 1):
        print(f"\nRegla {i}:")
        print(rule)
        user_input = input("Escribe la regla: ")
        if user_input.strip() == rule.strip():
            print("¡Correcto!")
            correct += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {rule}")
    print(f"\nTu puntaje: {correct}/{len(rules)}")

# Función para escribir traducciones al inglés
def translate_rules():
    print("\n--- Traducción de Reglas Ortográficas ---")
    translations = {}
    for i, rule in enumerate(rules, 1):
        print(f"\nRegla {i}: {rule}")
        translation = input("Escribe la traducción al inglés: ")
        translations[rule] = translation
    # Guardar traducciones en un archivo
    with open("translations.json", "w", encoding="utf-8") as file:
        json.dump(translations, file, ensure_ascii=False, indent=4)
    print("Traducciones guardadas exitosamente.")

# Función para revisar el progreso
def review_progress():
    try:
        with open("translations.json", "r", encoding="utf-8") as file:
            translations = json.load(file)
        print("\n--- Progreso en Traducciones ---")
        for rule, translation in translations.items():
            print(f"Regla: {rule}")
            print(f"Traducción: {translation}\n")
    except FileNotFoundError:
        print("\nNo hay progreso registrado. Comienza practicando o traduciendo las reglas.")

# Programa principal
def main():
    while True:
        show_menu()
        choice = input("\nSelecciona una opción: ")
        if choice == "1":
            display_rules()
        elif choice == "2":
            practice_rules()
        elif choice == "3":
            translate_rules()
        elif choice == "4":
            review_progress()
        elif choice == "5":
            print("¡Gracias por usar el programa! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
