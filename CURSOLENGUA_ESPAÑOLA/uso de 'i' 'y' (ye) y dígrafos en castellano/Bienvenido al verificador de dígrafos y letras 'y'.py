def verificar_digrafo(palabra):
    """
    Verifica si la palabra contiene los dígrafos "ll" o "y".
    """
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para evitar errores de caso
    if "ll" in palabra:
        return "Contiene el dígrafo 'll'."
    elif "y" in palabra:
        return "Contiene la letra 'y'."
    else:
        return "No contiene 'll' ni 'y'."

def main():
    print("Bienvenido al verificador de dígrafos y letras 'y'.")

    while True:
        palabra = input("Introduce una palabra (o 'salir' para terminar): ")
        if palabra.lower() == "salir":
            print("¡Hasta luego!")
            break
        else:
            resultado = verificar_digrafo(palabra)
            print(resultado)

if __name__ == "__main__":
    main()
