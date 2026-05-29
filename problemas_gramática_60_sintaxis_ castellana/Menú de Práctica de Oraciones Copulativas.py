def mostrar_menu():
    print("\n--- Menú de Práctica de Oraciones Copulativas ---")
    print("1. Practicar atributos estáticos (ser)")
    print("2. Practicar atributos dinámicos (estar)")
    print("3. Practicar ambos (mezclados)")
    print("4. Salir")

def practicar_estaticos():
    print("\n--- Practicando Atributos Estáticos (ser) ---")
    oraciones = [
        ("Juan ___ alto.", "es"),
        ("María ___ morena.", "es"),
        ("El libro ___ interesante.", "es"),
        ("La casa ___ grande.", "es"),
        ("El perro ___ juguetón.", "es")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (ser/estar)"))
        respuesta = input("Elige el verbo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_dinamicos():
    print("\n--- Practicando Atributos Dinámicos (estar) ---")
    oraciones = [
        ("Juan ___ cansado.", "está"),
        ("María ___ contenta.", "está"),
        ("El niño ___ aburrido.", "está"),
        ("La comida ___ fría.", "está"),
        ("El clima ___ nublado.", "está")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (ser/estar)"))
        respuesta = input("Elige el verbo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_ambos():
    print("\n--- Practicando Ambos Tipos de Atributos ---")
    oraciones = [
        ("Juan ___ alto.", "es", "estático"),
        ("María ___ contenta.", "está", "dinámico"),
        ("El libro ___ interesante.", "es", "estático"),
        ("El niño ___ aburrido.", "está", "dinámico"),
        ("La casa ___ grande.", "es", "estático")
    ]
    for oracion, correcto, tipo in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (ser/estar)"))
        respuesta = input("Elige el verbo correcto: ").strip().lower()
        if respuesta == correcto:
            print(f"¡Correcto! 👍 (Tipo: {tipo})")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎 (Tipo: {tipo})")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            practicar_estaticos()
        elif opcion == "2":
            practicar_dinamicos()
        elif opcion == "3":
            practicar_ambos()
        elif opcion == "4":
            print("¡Gracias por practicar! Hasta luego. 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
