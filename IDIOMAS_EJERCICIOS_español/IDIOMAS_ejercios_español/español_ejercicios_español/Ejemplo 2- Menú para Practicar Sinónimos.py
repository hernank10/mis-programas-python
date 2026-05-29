def mostrar_menu():
    print("1. Practicar sinónimos")
    print("2. Salir")

def practicar_sinonimos():
    palabras = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for palabra, sinonimos in palabras.items():
        print(f"Palabra: {palabra}")
        print(f"Sinónimos: {', '.join(sinonimos)}")
        print()

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            practicar_sinonimos()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
