def mostrar_menu():
    print("1. Practicar palabras polisémicas")
    print("2. Salir")

def practicar_polisemias():
    palabras = {
        "banco": ["Asiento para varias personas", "Institución financiera"],
        "carta": ["Documento escrito", "Cada uno de los naipes"],
        "corte": ["Acción de cortar", "Tribunal de justicia"]
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
            practicar_polisemias()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
