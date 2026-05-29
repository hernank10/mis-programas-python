def mostrar_menu():
    print("\n--- Práctica de Alternancias Locativas ---")
    print("1. Ver ejemplos de alternancia LOC y MAT")
    print("2. Escribir un ejercicio y recibir retroalimentación")
    print("3. Salir")

def ejemplos():
    print("\nEjemplos de Alternancia Locativa:")
    print("1. Los operarios cargaron el camión con el heno. (LOC)")
    print("2. Los operarios cargaron el heno en el camión. (MAT)")
    print("3. Los operarios llenaron el camión con el heno. (LOC, permitido)")
    print("4. *Los operarios llenaron el heno en el camión. (MAT, no permitido)")
    print("5. *Los operarios colocaron el camión con el heno. (LOC, no permitido)")
    print("6. Los operarios colocaron el heno en el camión. (MAT, permitido)")

def evaluar_ejercicio(oracion):
    locativos_correctos = ["cargaron el camión con", "llenaron el camión con"]
    materiales_correctos = ["cargaron el heno en", "colocaron el heno en"]
    
    if any(frase in oracion for frase in locativos_correctos):
        print("Correcto: Alternancia LOC válida.")
    elif any(frase in oracion for frase in materiales_correctos):
        print("Correcto: Alternancia MAT válida.")
    else:
        print("Posible error: La estructura puede no ser gramaticalmente válida.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ejemplos()
        elif opcion == "2":
            oracion = input("Escriba su oración con alternancia LOC o MAT: ")
            evaluar_ejercicio(oracion)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
