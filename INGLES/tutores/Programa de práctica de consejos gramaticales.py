# Programa de práctica de consejos gramaticales
# Adjetivos, Pronombres y Preposiciones
# Versión interactiva con menú y retroalimentación

consejos_es = [
    # Solo muestro algunos como ejemplo, deberás completar los 100 en español
    "Coloca siempre los adjetivos antes de los sustantivos en inglés.",
    "Aprende el orden común de los adjetivos: opinión, tamaño, edad, forma, color, origen, material, propósito.",
    "Ejemplo: una hermosa mesa grande, redonda, roja, italiana, de madera para comer.",
    "Usa adjetivos comparativos para comparar dos cosas: más grande, más pequeño, más interesante.",
    "Usa adjetivos superlativos para comparar más de dos cosas: el más grande, el más interesante.",
]

consejos_en = [
    # Solo muestro algunos como ejemplo, deberás completar los 100 en inglés
    "Always place adjectives before nouns in English.",
    "Learn common adjective order: opinion, size, age, shape, color, origin, material, purpose.",
    "Example: a beautiful big old round red Italian wooden dining table.",
    "Use comparative adjectives to compare two things: bigger, smaller, more interesting.",
    "Use superlative adjectives to compare more than two things: the biggest, the most interesting.",
]

def practicar(consejos):
    puntuacion = 0
    for i, consejo in enumerate(consejos, start=1):
        print(f"\nConsejo {i}:")
        respuesta = input("Escribe este consejo exactamente como aparece:\n> ")
        if respuesta.strip() == consejo:
            print("✅ Correcto")
            puntuacion += 1
        else:
            print("❌ Incorrecto")
            print(f"El consejo correcto era:\n{consejo}")
    print(f"\nTu puntuación final: {puntuacion}/{len(consejos)}")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Practicar consejos en español")
        print("2. Practicar consejos en inglés")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            practicar(consejos_es)
        elif opcion == "2":
            practicar(consejos_en)
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
