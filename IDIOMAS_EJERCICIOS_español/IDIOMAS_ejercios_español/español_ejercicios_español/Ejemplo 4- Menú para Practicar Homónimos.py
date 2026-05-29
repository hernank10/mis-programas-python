def mostrar_menu():
    print("1. Practicar homónimos")
    print("2. Salir")

def practicar_homonimos():
    palabras = {
        "vino": ["Bebida alcohólica", "Pasado del verbo venir"],
        "llama": ["Animal sudamericano", "Fuego", "Forma del verbo llamar"],
        "banco": ["Asiento", "Institución financiera"]
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
            practicar_homonimos()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
