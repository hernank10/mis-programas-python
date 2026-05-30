def practicar_reglas():
    reglas = {
        "g": "Se utiliza cuando está seguida de las vocales 'e' o 'i'. Ejemplos: gato, gorra, guacamole, grabar, gigante, general, gemelo, germen, gesto, gimnasio.",
        "j": "Representa el sonido de una 'j' en inglés. Ejemplos: jabalí, sonrojo, ajuste, juicio, jardín, jirafa, jota, juez, jaula, jengibre."
    }

    while True:
        letra = input("Ingresa una letra ('g' o 'j'): ").lower()

        if letra in reglas:
            print(f"Regla para '{letra}': {reglas[letra]}")
            respuesta = input("¿Escribiste correctamente? (s/n): ").lower()
            if respuesta == "s":
                print("¡Correcto! ¡Sigue practicando!")
            else:
                print(f"La respuesta correcta es: {reglas[letra]}")
        else:
            print("Ingresa una letra válida ('g' o 'j').")

        continuar = input("¿Quieres seguir practicando? (s/n): ").lower()
        if continuar != "s":
            break

practicar_reglas()
