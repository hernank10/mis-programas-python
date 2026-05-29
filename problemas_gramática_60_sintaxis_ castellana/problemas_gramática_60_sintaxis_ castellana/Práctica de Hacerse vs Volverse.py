def mostrar_menu():
    print("\n--- Práctica de Hacerse vs. Volverse ---")
    print("1. Explicación sobre los verbos")
    print("2. Ver ejemplos")
    print("3. Escribir tus propios ejemplos")
    print("4. Salir")


def explicacion():
    print("\nLos verbos 'hacerse' y 'volverse' expresan cambios de estado, pero con matices diferentes:")
    print("- 'Hacerse': Cambio progresivo, intencionado o relacionado con una evolución.")
    print("  Ejemplo: 'Se hizo médico después de años de estudio.'")
    print("- 'Volverse': Cambio brusco, involuntario o inesperado.")
    print("  Ejemplo: 'Después del accidente, se volvió muy reservado.'")
    print("\nCuando hay un pronombre dativo (me, te, le, etc.), 'hacerse' es más natural que 'volverse'.")


def ver_ejemplos():
    print("\nEjemplos de uso:")
    print("1. Este culebrón se está haciendo cada vez más aburrido. (Cambio progresivo)")
    print("2. Este culebrón se está volviendo cada vez más aburrido. (Cambio repentino)")
    print("3. Este culebrón se me está haciendo cada vez más aburrido. (Aceptado)")
    print("4. ?? Este culebrón se me está volviendo cada vez más aburrido. (Menos aceptado)")


def escribir_ejemplos():
    print("\nEscribe una oración con 'hacerse' o 'volverse':")
    oracion = input("➡ ")
    print(f"Has escrito: {oracion}")
    print("Intenta identificar si usaste el verbo correctamente y si podrías reformularla.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            ver_ejemplos()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Gracias por practicar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
