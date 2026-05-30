# Programa para practicar oraciones compuestas para cada letra del alfabeto con opciones adicionales

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ver ejemplo de una oración compuesta por letra")
    print("2. Introducir un ejemplo libre por letra con corrección ortográfica")
    print("3. Ver progreso guardado")
    print("4. Guardar progreso actual")
    print("5. Salir")

def ejemplos_oraciones():
    ejemplos = {
        "A": "Aunque estaba cansado, terminó el trabajo porque era urgente.",
        "B": "Buscó el libro que necesitaba, pero no lo encontró en la biblioteca.",
        "C": "Compró un regalo para su amigo porque era su cumpleaños.",
        # Agregar ejemplos para todas las letras...
    }
    return ejemplos

def mostrar_ejemplo(letra, ejemplos):
    print(f"Ejemplo para la letra {letra}: {ejemplos.get(letra.upper(), 'No hay ejemplo disponible para esta letra.')}")

def introducir_ejemplo_libre(letra):
    ejemplo = input(f"Introduce tu ejemplo para la letra {letra}: ")
    # Aquí se puede implementar una función de corrección ortográfica
    print(f"Ejemplo guardado para la letra {letra}: {ejemplo}")
    return letra, ejemplo

def guardar_progreso(progreso):
    with open("progreso.txt", "w") as file:
        for letra, ejemplo in progreso.items():
            file.write(f"{letra}: {ejemplo}\n")
    print("Progreso guardado exitosamente.")

def ver_progreso():
    try:
        with open("progreso.txt", "r") as file:
            print("\nProgreso guardado:")
            print(file.read())
    except FileNotFoundError:
        print("No hay progreso guardado aún.")

def main():
    ejemplos = ejemplos_oraciones()
    progreso = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            letra = input("Introduce la letra para ver el ejemplo: ")
            mostrar_ejemplo(letra, ejemplos)
        elif opcion == "2":
            letra = input("Introduce la letra para tu ejemplo: ")
            letra, ejemplo = introducir_ejemplo_libre(letra)
            progreso[letra] = ejemplo
        elif opcion == "3":
            ver_progreso()
        elif opcion == "4":
            guardar_progreso(progreso)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()
