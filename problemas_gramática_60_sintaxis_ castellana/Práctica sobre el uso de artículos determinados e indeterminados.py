def mostrar_menu():
    print("\nPráctica sobre el uso de artículos determinados e indeterminados")
    print("1. Explicación del tema")
    print("2. Ver ejemplos")
    print("3. Realizar ejercicios")
    print("4. Escribir tus propios ejemplos")
    print("5. Salir")


def explicacion():
    print("\nExplicación:")
    print("Los artículos determinados (el, la, los, las) y los indeterminados (un, una, unos, unas) tienen funciones específicas.")
    print("Por ejemplo, 'el amigo de Pedro' sugiere que conocemos a la persona, mientras que 'un amigo de Pedro' no especifica quién es.")
    print("Sin embargo, en ciertas expresiones, como 'votó el ochenta por ciento' y 'votó un ochenta por ciento', la diferencia se neutraliza.")


def ver_ejemplos():
    ejemplos = [
        ("Compré un coche nuevo.", "Compré el coche que quería."),
        ("Votó una minoría.", "Votó la mayoría."),
        ("Encontré un problema en el código.", "Encontré el problema en el código."),
    ]
    print("\nEjemplos de uso:")
    for ind, (indeterminado, determinado) in enumerate(ejemplos, 1):
        print(f"{ind}. {indeterminado} | {determinado}")


def realizar_ejercicios():
    print("\nEjercicios: Completa las frases con el artículo adecuado (determinado o indeterminado)")
    ejercicios = [
        ("___ gobierno anunció nuevas medidas.", "El"),
        ("Necesito ___ consejo sobre este tema.", "un"),
        ("___ treinta por ciento de los alumnos aprobaron el examen.", "El"),
    ]
    for frase, respuesta in ejercicios:
        usuario = input(frase + " ")
        if usuario.lower() == respuesta.lower():
            print("✔ Correcto!")
        else:
            print(f"✘ Incorrecto. La respuesta correcta es: {respuesta}")


def escribir_ejemplos():
    print("\nEscribe tus propias frases usando artículos determinados e indeterminados.")
    while True:
        ejemplo = input("Escribe una oración (o escribe 'salir' para volver al menú): ")
        if ejemplo.lower() == "salir":
            break
        print("Gracias por tu ejemplo!")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            ver_ejemplos()
        elif opcion == "3":
            realizar_ejercicios()
        elif opcion == "4":
            escribir_ejemplos()
        elif opcion == "5":
            print("Gracias por practicar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
