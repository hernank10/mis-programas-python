# Programa para practicar 7 reglas de oraciones compuestas en inglés

rules = {
    1: {
        "title": "Evita el comma splice",
        "error": "I studied hard, I passed the test.",
        "correct": "I studied hard, and I passed the test."
    },
    2: {
        "title": "Usa la conjunción adecuada",
        "error": "I was hungry, and I didn’t eat anything.",
        "correct": "I was hungry, but I didn’t eat anything."
    },
    3: {
        "title": "Evita la traducción literal",
        "error": "I wanted to go, but that I was tired.",
        "correct": "I wanted to go, but I was tired."
    },
    4: {
        "title": "No hagas oraciones interminables",
        "error": "I went to the store and I bought milk and I met my friend and we talked.",
        "correct": "I went to the store and bought milk. Then I met my friend, and we talked."
    },
    5: {
        "title": "Revisa la puntuación",
        "error": "I like coffee, I don’t like tea.",
        "correct": "I like coffee; I don’t like tea."
    },
    6: {
        "title": "No omitas el sujeto o verbo",
        "error": "She likes pizza, and also likes pasta.",
        "correct": "She likes pizza, and she also likes pasta."
    },
    7: {
        "title": "Usa bien los conectores formales",
        "error": "I wanted to go, however I stayed home.",
        "correct": "I wanted to go; however, I stayed home."
    }
}

def mostrar_menu():
    print("\n=== MENÚ DE PRÁCTICA ===")
    for key, value in rules.items():
        print(f"{key}. {value['title']}")
    print("0. Salir")

def practicar_regla(opcion):
    regla = rules[opcion]
    print(f"\n📘 Regla: {regla['title']}")
    print(f"❌ Ejemplo con error: {regla['error']}")
    print(f"✅ Ejemplo corregido: {regla['correct']}")
    
    user_example = input("\nAhora escribe tu propio ejemplo con un sujeto o verbo diferente:\n> ")
    print(f"👍 Muy bien, escribiste: {user_example}")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una regla para practicar: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 0:
            print("¡Gracias por practicar! 👋")
            break
        elif opcion in rules:
            practicar_regla(opcion)
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    main()
