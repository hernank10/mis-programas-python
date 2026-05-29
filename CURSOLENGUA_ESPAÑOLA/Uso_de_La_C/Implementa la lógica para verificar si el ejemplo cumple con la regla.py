def main():
    print("Bienvenido al ejercicio de reglas de la letra C en español.")
    print("Lee las siguientes reglas y escribe ejemplos utilizando palabras con 'C'.")
    print("Cuando estés listo, escribe 'salir' para terminar.")

    while True:
        regla = input("\nRegla: ")
        if regla.lower() == "salir":
            break

        print("\nEscribe un ejemplo que cumpla con la regla:")
        ejemplo = input("Ejemplo: ")

        # Verificar si el ejemplo cumple con la regla
        if regla_valida(ejemplo, regla):
            print("¡Correcto! Sigue practicando.")
        else:
            print("Ese ejemplo no cumple con la regla. Inténtalo de nuevo.")

def regla_valida(ejemplo, regla):
    # Implementa la lógica para verificar si el ejemplo cumple con la regla
    # Puedes usar expresiones regulares o comparaciones de cadenas

    # Ejemplo: Verificar si la palabra contiene 'C' y cumple con la regla
    return 'c' in ejemplo.lower()

if __name__ == "__main__":
    main()
