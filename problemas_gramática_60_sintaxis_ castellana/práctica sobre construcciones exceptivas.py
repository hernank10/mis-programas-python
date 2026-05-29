def mostrar_menu():
    print("\nMenú de práctica sobre construcciones exceptivas")
    print("1. Leer explicación sobre construcciones exceptivas")
    print("2. Completar ejercicios de frases")
    print("3. Escribir ejemplos propios")
    print("4. Salir")


def explicar_exceptivas():
    print("\nLas construcciones exceptivas sirven para indicar una exclusión dentro de un grupo. ")
    print("Ejemplos:")
    print("- Bailé con todos, excepto Juan.")
    print("- Excepto con Juan, bailé con todos.")
    print("- Eso supone un cambio para todos los niños, salvo él.")
    print("Recuerda que algunas estructuras exceptivas pueden ir al inicio y otras no.")


def completar_ejercicios():
    ejercicios = [
        ("Bailé con todos, _____ Juan.", ["excepto", "salvo", "menos"]),
        ("_____ con Marta, fui con todos a la fiesta.", ["Excepto", "Salvo", "Menos"]),
        ("Todos aprobaron el examen, _____ Pedro.", ["excepto", "salvo", "menos"]),
    ]
    
    for i, (frase, opciones) in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {frase}")
        respuesta = input("Completa la frase con 'excepto', 'salvo' o 'menos': ").strip()
        if respuesta in opciones:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. Respuestas posibles: {', '.join(opciones)}")


def escribir_ejemplos():
    print("\nEscribe una oración con una construcción exceptiva:")
    ejemplo = input("Tu oración: ")
    print("Gracias por tu ejemplo. Sigue practicando.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            explicar_exceptivas()
        elif opcion == "2":
            completar_ejercicios()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
