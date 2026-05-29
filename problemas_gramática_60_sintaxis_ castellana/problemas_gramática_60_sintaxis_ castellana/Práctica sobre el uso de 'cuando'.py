def mostrar_menu():
    print("\n=== Práctica sobre el uso de 'cuando' ===")
    print("1. Explicación sobre 'cuando'")
    print("2. Completar oraciones")
    print("3. Escribir oraciones con 'cuando'")
    print("4. Salir")

def explicacion():
    print("\n'Cuando' puede ser un adverbio relativo de tiempo o una conjunción subordinante.")
    print("Ejemplo como adverbio relativo: 'Recuerdo el día cuando nos conocimos.'")
    print("Ejemplo como conjunción subordinante: 'Cuando llegué, ya habías salido.'")

def completar_oraciones():
    ejercicios = [
        ("Recuerdo el día ___ nos conocimos.", "cuando"),
        ("___ llegué a casa, ya era de noche.", "Cuando"),
        ("No sé ___ será el evento.", "cuándo")
    ]
    
    print("\nCompleta las siguientes oraciones con 'cuando' o 'cuándo':")
    
    for i, (oracion, respuesta) in enumerate(ejercicios, 1):
        usuario = input(f"{i}. {oracion} ")
        if usuario.strip().lower() == respuesta.lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {respuesta}")

def escribir_oraciones():
    print("\nEscribe una oración con 'cuando' y presiona Enter:")
    oracion = input("➡ ")
    print(f"Tu oración: {oracion}")
    print("¡Bien! Sigue practicando.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            completar_oraciones()
        elif opcion == "3":
            escribir_oraciones()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
