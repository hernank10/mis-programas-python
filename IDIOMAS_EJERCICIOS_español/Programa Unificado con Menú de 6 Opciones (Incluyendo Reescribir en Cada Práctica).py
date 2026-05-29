def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Practicar palabras polisémicas")
    print("2. Practicar sinónimos")
    print("3. Practicar antónimos")
    print("4. Practicar homónimos")
    print("5. Practicar palabras con múltiples significados")
    print("6. Salir")

def reescribir_ejemplo(palabra, significado):
    print(f"\nPalabra: {palabra}")
    print(f"Significado original: {significado}")
    respuesta = input("Reescribe el significado con tus propias palabras: ")
    
    # Comparación simple (puede mejorarse con NLP en el futuro)
    if respuesta.lower() == significado.lower():
        print("¡Correcto! Has reescrito el significado perfectamente.")
    else:
        print(f"Tu respuesta: {respuesta}")
        print(f"Significado original: {significado}")
        print("¡Buen intento! Sigue practicando.")

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
        
        # Opción para reescribir
        reescribir = input("\n¿Quieres reescribir uno de los significados? (s/n): ").lower()
        if reescribir == "s":
            num_significado = int(input("Elige el número del significado que quieres reescribir (1 o 2): "))
            if 1 <= num_significado <= len(significados):
                reescribir_ejemplo(palabra, significados[num_significado - 1])
            else:
                print("Número no válido.")

def practicar_sinonimos():
    print("\n--- Sinónimos ---")
    palabras = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for palabra, sinonimos in palabras.items():
        print(f"\nPalabra: {palabra}")
        print(f"Sinónimos: {', '.join(sinonimos)}")
        
        # Opción para reescribir
        reescribir = input("\n¿Quieres reescribir uno de los sinónimos? (s/n): ").lower()
        if reescribir == "s":
            num_sinonimo = int(input("Elige el número del sinónimo que quieres reescribir (1, 2 o 3): "))
            if 1 <= num_sinonimo <= len(sinonimos):
                reescribir_ejemplo(palabra, sinonimos[num_sinonimo - 1])
            else:
                print("Número no válido.")

def practicar_antonimos():
    print("\n--- Antónimos ---")
    palabras = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for palabra, antonimos in palabras.items():
        print(f"\nPalabra: {palabra}")
        print(f"Antónimos: {', '.join(antonimos)}")
        
        # Opción para reescribir
        reescribir = input("\n¿Quieres reescribir uno de los antónimos? (s/n): ").lower()
        if reescribir == "s":
            num_antonimo = int(input("Elige el número del antónimo que quieres reescribir (1, 2 o 3): "))
            if 1 <= num_antonimo <= len(antonimos):
                reescribir_ejemplo(palabra, antonimos[num_antonimo - 1])
            else:
                print("Número no válido.")

def practicar_homonimos():
    print("\n--- Homónimos ---")
    palabras = {
        "vino": ["Bebida alcohólica", "Pasado del verbo 'venir'"],
        "llama": ["Animal sudamericano", "Fuego", "Forma del verbo 'llamar'"],
        "banco": ["Asiento", "Institución financiera"]
    }
    for palabra, significados in palabras.items():
        print(f"\nPalabra: {palabra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")
        
        # Opción para reescribir
        reescribir = input("\n¿Quieres reescribir uno de los significados? (s/n): ").lower()
        if reescribir == "s":
            num_significado = int(input("Elige el número del significado que quieres reescribir (1 o 2): "))
            if 1 <= num_significado <= len(significados):
                reescribir_ejemplo(palabra, significados[num_significado - 1])
            else:
                print("Número no válido.")

def practicar_multiples_significados():
    print("\n--- Palabras con Múltiples Significados ---")
    palabras = {
        "cabeza": ["Parte superior del cuerpo", "Líder de un grupo"],
        "lengua": ["Órgano muscular en la boca", "Idioma"],
        "ojo": ["Órgano de la visión", "Ojo de una aguja"]
    }
    for palabra, significados in palabras.items():
        print(f"\nPalabra: {palabra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")
        
        # Opción para reescribir
        reescribir = input("\n¿Quieres reescribir uno de los significados? (s/n): ").lower()
        if reescribir == "s":
            num_significado = int(input("Elige el número del significado que quieres reescribir (1 o 2): "))
            if 1 <= num_significado <= len(significados):
                reescribir_ejemplo(palabra, significados[num_significado - 1])
            else:
                print("Número no válido.")

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
