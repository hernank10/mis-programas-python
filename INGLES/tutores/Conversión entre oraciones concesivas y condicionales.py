# Programa: Conversión entre oraciones concesivas y condicionales
# Autor: Hernán + ChatGPT

concesivas = [
    "Por más que no quieras, sí puedes intentarlo",
    "Aunque lo intentes, no lo lograrás fácilmente",
    "Aun cuando estés cansado, puedes terminarlo"
]

condicionales = [
    "Tan si quieras no puedes intentarlo",
    "Tan aunque lo intentes, no lo lograrás fácilmente",
    "Tan si estés cansado, no puedes terminarlo"
]

def mostrar_reglas():
    print("\n=== Reglas RAE ===")
    print("1. Las oraciones concesivas expresan dificultad u oposición (aunque, por más que, aun cuando).")
    print("2. Las condicionales expresan condición (si, siempre que, con tal de que).")
    print("3. Convertir una en otra cambia la perspectiva:")
    print("   - Concesiva → mantiene la posibilidad.")
    print("   - Condicional negativa → enfatiza la imposibilidad.\n")

def practicar_conversion():
    for i, frase in enumerate(concesivas):
        print(f"\nFrase concesiva {i+1}: {frase}")
        respuesta = input("Convierte a condicional negativa: ")
        print(f"Posible transformación: {condicionales[i]}")

    for i, frase in enumerate(condicionales):
        print(f"\nFrase condicional {i+1}: {frase}")
        respuesta = input("Convierte a concesiva: ")
        print(f"Posible transformación: {concesivas[i]}")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver reglas RAE")
        print("2. Practicar conversiones")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_reglas()
        elif opcion == "2":
            practicar_conversion()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
