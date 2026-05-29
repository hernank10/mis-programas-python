def mostrar_menu():
    print("\n--- Menú de Práctica de Ser y Estar con Complementos ---")
    print("1. Practicar adjetivos con complementos (estar)")
    print("2. Practicar adjetivos sin complementos (ser)")
    print("3. Practicar ambos (mezclados)")
    print("4. Salir")

def practicar_estar():
    print("\n--- Practicando Adjetivos con Complementos (estar) ---")
    oraciones = [
        ("Juan ___ casado (con María).", "está"),
        ("María ___ contenta (con su regalo).", "está"),
        ("El niño ___ aburrido (con la película).", "está"),
        ("La comida ___ fría (al tocarla).", "está"),
        ("El clima ___ nublado (en la montaña).", "está")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (ser/estar)"))
        respuesta = input("Elige el verbo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_ser():
    print("\n--- Practicando Adjetivos sin Complementos (ser) ---")
    oraciones = [
        ("Juan ___ casado (*con María).", "es"),
        ("María ___ morena (*por el sol).", "es"),
        ("El libro ___ interesante (*para mí).", "es"),
        ("La casa ___ grande (*para una familia).", "es"),
        ("El perro ___ juguetón (*con los niños).", "es")
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
    print("\n--- Practicando Ambos Tipos de Adjetivos ---")
    oraciones = [
        ("Juan ___ casado (con María).", "está", "con complemento"),
        ("María ___ morena (*por el sol).", "es", "sin complemento"),
        ("El niño ___ aburrido (con la película).", "está", "con complemento"),
        ("La casa ___ grande (*para una familia).", "es", "sin complemento"),
        ("El clima ___ nublado (en la montaña).", "está", "con complemento")
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
            practicar_estar()
        elif opcion == "2":
            practicar_ser()
        elif opcion == "3":
            practicar_ambos()
        elif opcion == "4":
            print("¡Gracias por practicar! Hasta luego. 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
