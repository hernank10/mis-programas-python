def mostrar_menu():
    print("\n--- Menú de Práctica de Demostrativos ---")
    print("1. Practicar demostrativos prenominales")
    print("2. Practicar demostrativos posnominales")
    print("3. Practicar ambos (mezclados)")
    print("4. Salir")

def practicar_prenominal():
    print("\n--- Practicando Demostrativos Prenominales ---")
    oraciones = [
        ("___ libro es muy interesante.", "este"),
        ("___ casa es grande.", "aquella"),
        ("___ coche es rápido.", "ese"),
        ("___ flores son hermosas.", "estas"),
        ("___ perro es juguetón.", "aquel")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (este/ese/aquel)"))
        respuesta = input("Elige el demostrativo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_posnominal():
    print("\n--- Practicando Demostrativos Posnominales ---")
    oraciones = [
        ("El libro ___ es muy interesante.", "este"),
        ("La casa ___ es grande.", "aquella"),
        ("El coche ___ es rápido.", "ese"),
        ("Las flores ___ son hermosas.", "estas"),
        ("El perro ___ es juguetón.", "aquel")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (este/ese/aquel)"))
        respuesta = input("Elige el demostrativo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_ambos():
    print("\n--- Practicando Ambos Tipos de Demostrativos ---")
    oraciones = [
        ("___ libro es muy interesante.", "este", "prenominal"),
        ("El libro ___ es muy interesante.", "este", "posnominal"),
        ("___ casa es grande.", "aquella", "prenominal"),
        ("La casa ___ es grande.", "aquella", "posnominal"),
        ("___ coche es rápido.", "ese", "prenominal"),
        ("El coche ___ es rápido.", "ese", "posnominal")
    ]
    for oracion, correcto, tipo in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (este/ese/aquel)"))
        respuesta = input("Elige el demostrativo correcto: ").strip().lower()
        if respuesta == correcto:
            print(f"¡Correcto! 👍 (Tipo: {tipo})")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎 (Tipo: {tipo})")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            practicar_prenominal()
        elif opcion == "2":
            practicar_posnominal()
        elif opcion == "3":
            practicar_ambos()
        elif opcion == "4":
            print("¡Gracias por practicar! Hasta luego. 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
