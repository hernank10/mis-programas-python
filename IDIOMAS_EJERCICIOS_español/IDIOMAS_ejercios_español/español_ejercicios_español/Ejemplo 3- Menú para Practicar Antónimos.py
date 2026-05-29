def mostrar_menu():
    print("1. Practicar antónimos")
    print("2. Salir")

def practicar_antonimos():
    palabras = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for palabra, antonimos in palabras.items():
        print(f"Palabra: {palabra}")
        print(f"Antónimos: {', '.join(antonimos)}")
        print()

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            practicar_antonimos()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
