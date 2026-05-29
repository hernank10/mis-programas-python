# Programa de consola para practicar consejos de gramática inglés-español

# Lista de consejos (ejemplo con pocos, tú puedes ampliarla hasta 200)
consejos = [
    ("Use adjectives before nouns. / Usa los adjetivos antes de los sustantivos.",
     "Use adjectives before nouns.",
     "Usa los adjetivos antes de los sustantivos."),
    ("Pronouns replace nouns. / Los pronombres reemplazan a los sustantivos.",
     "Pronouns replace nouns.",
     "Los pronombres reemplazan a los sustantivos."),
    ("Prepositions show relationships. / Las preposiciones muestran relaciones.",
     "Prepositions show relationships.",
     "Las preposiciones muestran relaciones."),
]

def mostrar_menu():
    print("\n=== MENÚ DE CONSEJOS ===")
    print("1. Ver un consejo aleatorio")
    print("2. Escribir un consejo nuevamente (práctica)")
    print("3. Salir")

def ver_consejo():
    import random
    consejo = random.choice(consejos)
    print("\n--- CONSEJO ---")
    print(consejo[0])

def practicar_consejo():
    import random
    consejo = random.choice(consejos)
    print("\n--- PRÁCTICA ---")
    print("Consejo a memorizar:\n")
    print(consejo[0])

    # Solicitar reescritura en inglés
    user_eng = input("\nEscribe el consejo en INGLÉS exactamente: ")
    if user_eng.strip() == consejo[1]:
        print("✅ Correcto en inglés.")
    else:
        print(f"❌ Incorrecto. La versión correcta es:\n{consejo[1]}")

    # Solicitar reescritura en español
    user_esp = input("\nEscribe el consejo en ESPAÑOL exactamente: ")
    if user_esp.strip() == consejo[2]:
        print("✅ Correcto en español.")
    else:
        print(f"❌ Incorrecto. La versión correcta es:\n{consejo[2]}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_consejo()
        elif opcion == "2":
            practicar_consejo()
        elif opcion == "3":
            print("¡Hasta pronto! Sigue practicando.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
