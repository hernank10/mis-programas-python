def mostrar_menu():
    print("1. Practicar palabras con múltiples significados")
    print("2. Salir")

def practicar_multiples_significados():
    palabras = {
        "cabeza": ["Parte superior del cuerpo", "Líder de un grupo"],
        "lengua": ["Órgano muscular en la boca", "Idioma"],
        "ojo": ["Órgano de la visión", "Abertura en una aguja"]
    }
    for palabra, significados in palabras.items():
        print(f"Palabra: {palabra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")
        print()

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            practicar_multiples_significados()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
