def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Corrección de Textos")
        print("2. Aprender Vocabulario")
        print("3. Práctica de Gramática")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_correccion()
        elif opcion == "2":
            menu_vocabulario()
        elif opcion == "3":
            menu_gramatica()
        elif opcion == "4":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_correccion():
    while True:
        print("\n--- Menú Corrección de Textos ---")
        print("1. Corregir texto")
        print("2. Ver ejemplos de corrección")
        print("3. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            correccion_texto()
        elif opcion == "2":
            ejemplos_correccion()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_vocabulario():
    while True:
        print("\n--- Menú Vocabulario ---")
        print("1. Ver palabras nuevas")
        print("2. Ejercicios interactivos")
        print("3. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_palabras()
        elif opcion == "2":
            ejercicios_vocabulario()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_gramatica():
    while True:
        print("\n--- Menú Gramática ---")
        print("1. Ejercicios básicos")
        print("2. Ejercicios avanzados")
        print("3. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicios_basicos()
        elif opcion == "2":
            ejercicios_avanzados()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Funciones adicionales para las opciones
def correccion_texto():
    print("Función de corrección de texto activada.")

def ejemplos_correccion():
    print("Mostrando ejemplos de corrección...")

def mostrar_palabras():
    print("Lista de palabras nuevas...")

def ejercicios_vocabulario():
    print("Ejercicios interactivos de vocabulario activados.")

def ejercicios_basicos():
    print("Ejercicios básicos de gramática...")

def ejercicios_avanzados():
    print("Ejercicios avanzados de gramática activados.")

# Ejecutar el programa
menu_principal()
