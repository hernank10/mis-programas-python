def mostrar_menu():
    print("\nPráctica sobre el uso de 'ojalá'")
    print("1. Leer una explicación sobre 'ojalá'")
    print("2. Resolver ejercicios de completado")
    print("3. Escribir ejemplos propios")
    print("4. Salir")

def explicacion():
    print("\n'Ojalá' es un adverbio modal que se usa para expresar deseos o esperanzas.")
    print("Siempre va seguido de un verbo en subjuntivo.")
    print("Ejemplo: Ojalá mañana haga buen tiempo.")

def ejercicios():
    ejercicios = [
        ("______ (hacer) sol mañana para ir a la playa.", "Ojalá haga"),
        ("______ (aprobar) el examen sin problemas.", "Ojalá apruebe"),
        ("______ (venir) pronto mis amigos.", "Ojalá vengan")
    ]
    
    for enunciado, respuesta in ejercicios:
        usuario = input(f"{enunciado}\nCompleta la oración: ")
        if usuario.strip().lower() == respuesta.lower():
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta}\n")

def escribir_ejemplos():
    print("\nEscribe tus propios ejemplos usando 'ojalá':")
    ejemplos = []
    while True:
        ejemplo = input("Escribe una oración o presiona Enter para volver al menú: ")
        if not ejemplo:
            break
        ejemplos.append(ejemplo)
    
    print("\nTus ejemplos:")
    for e in ejemplos:
        print(f"- {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            ejercicios()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
