import random
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Praticar palabras polisémicas")
    print("2. Praticar sinónimos")
    print("3. Praticar antónimos")
    print("4. Praticar homónimos")
    print("5. Praticar palabras con múltiples significados")
    print("6. Salir")

def practicar_polisemias():
    print("\n--- Palabras Polisémicas ---")
    palabras = {
        "banco": ["Asiento para varias personas", "Institución financiera"],
        "carta": ["Documento escrito", "Carta de baralho"],
        "corte": ["Acción de cortar", "Tribunal de justicia"]
    }
    for palabra, significados in palabras.items():
        print(f"\nPalabra: {palabra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")

def practicar_sinonimos():
    print("\n--- Sinónimos ---")
    palabras = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for palabra, sinonimos in palabras.items():
        print(f"\nPalabra: {palavra}")
        print(f"Sinónimos: {', '.join(sinonimos)}")

def practicar_antonimos():
    print("\n--- Antónimos ---")
    palabras = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for palabra, antonimos in palabras.items():
        print(f"\nPalabra: {palavra}")
        print(f"Antónimos: {', '.join(antonimos)}")

def practicar_homonimos():
    print("\n--- Homónimos ---")
    palabras = {
        "vino": ["Bebida alcohólica", "Pasado del verbo 'venir'"],
        "llama": ["Animal sudamericano", "Fuego", "Forma del verbo 'llamar'"],
        "banco": ["Asiento", "Institución financiera"]
    }
    for palabra, significados in palabras.items():
        print(f"\nPalabra: {palavra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")

def practicar_multiples_significados():
    print("\n--- Palabras con Múltiples Significados ---")
    palabras = {
        "cabeza": ["Parte superior del cuerpo", "Líder de un grupo"],
        "lengua": ["Órgano muscular en la boca", "Idioma"],
        "ojo": ["Órgano de la visión", "Ojo de una aguja"]
    }
    for palabra, significados in palabras.items():
        print(f"\nPalabra: {palavra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == "1":
            practicar_polisemias()
        elif opcion == "2":
            practicar_sinonimos()
        elif opcion == "3":
            practicar_antonimos()
        elif opcion == "4":
            practicar_homonimos()
        elif opcion == "5":
            practicar_multiples_significados()
        elif opcion == "6":
            print("\n¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
