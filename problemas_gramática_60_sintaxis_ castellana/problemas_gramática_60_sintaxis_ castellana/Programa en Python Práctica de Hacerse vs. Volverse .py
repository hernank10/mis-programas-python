def mostrar_menu():
    print("\n--- Menú de Práctica de Hacerse y Volverse ---")
    print("1. Practicar sin pronombre dativo")
    print("2. Practicar con pronombre dativo")
    print("3. Practicar ambos (mezclados)")
    print("4. Salir")

def practicar_sin_dativo():
    print("\n--- Practicando sin Pronombre Dativo ---")
    oraciones = [
        ("Este culebrón se está {haciendo/volviendo} cada vez más aburrido.", "haciendo"),
        ("El clima se está {haciendo/volviendo} más frío.", "volviendo"),
        ("La situación se está {haciendo/volviendo} más complicada.", "haciendo"),
        ("El niño se está {haciendo/volviendo} más travieso.", "volviendo"),
        ("La película se está {haciendo/volviendo} más interesante.", "haciendo")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion)
        respuesta = input("Elige el verbo correcto (haciendo/volviendo): ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_con_dativo():
    print("\n--- Practicando con Pronombre Dativo ---")
    oraciones = [
        ("Este culebrón se me está {haciendo/volviendo} cada vez más aburrido.", "haciendo"),
        ("El clima se nos está {haciendo/volviendo} más frío.", "haciendo"),
        ("La situación se le está {haciendo/volviendo} más complicada.", "haciendo"),
        ("El niño se te está {haciendo/volviendo} más travieso.", "haciendo"),
        ("La película se les está {haciendo/volviendo} más interesante.", "haciendo")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion)
        respuesta = input("Elige el verbo correcto (haciendo/volviendo): ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_ambos():
    print("\n--- Practicando Ambos Tipos ---")
    oraciones = [
        ("Este culebrón se está {haciendo/volviendo} cada vez más aburrido.", "haciendo", "sin dativo"),
        ("Este culebrón se me está {haciendo/volviendo} cada vez más aburrido.", "haciendo", "con dativo"),
        ("El clima se está {haciendo/volviendo} más frío.", "volviendo", "sin dativo"),
        ("El clima se nos está {haciendo/volviendo} más frío.", "haciendo", "con dativo"),
        ("La situación se está {haciendo/volviendo} más complicada.", "haciendo", "sin dativo")
    ]
    for oracion, correcto, tipo in oraciones:
        print("\nCompleta la oración:")
        print(oracion)
        respuesta = input("Elige el verbo correcto (haciendo/volviendo): ").strip().lower()
        if respuesta == correcto:
            print(f"¡Correcto! 👍 (Tipo: {tipo})")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎 (Tipo: {tipo})")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            practicar_sin_dativo()
        elif opcion == "2":
            practicar_con_dativo()
        elif opcion == "3":
            practicar_ambos()
        elif opcion == "4":
            print("¡Gracias por practicar! Hasta luego. 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
