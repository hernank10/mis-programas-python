# Función para que el usuario ingrese 50 palabras con sus reglas ortográficas
def ingresar_palabras():
    palabras_reglas_usuario = {}
    
    print("Ingresa 50 palabras con sus respectivas reglas ortográficas:")
    for i in range(1, 51):
        palabra = input(f"\nPalabra {i}: ").strip().lower()
        regla = input(f"Regla para la palabra '{palabra}': ").strip()
        palabras_reglas_usuario[palabra] = regla

    return palabras_reglas_usuario

# Función para mostrar las palabras y reglas ingresadas por el usuario
def mostrar_palabras(palabras_reglas):
    print("\nA continuación, se muestran las palabras ingresadas con sus reglas ortográficas:")
    for palabra, regla in palabras_reglas.items():
        print(f"\nPalabra: {palabra}\nRegla: {regla}")

# Función para evaluar la ortografía del usuario con las palabras ingresadas
def evaluar_ortografia(palabras_reglas):
    errores = 0
    print("\nAhora escribe correctamente las palabras que ingresaste anteriormente según las reglas.")
    
    for palabra in palabras_reglas.keys():
        respuesta = input(f"Escribe la palabra correcta para la regla: '{palabras_reglas[palabra]}': ").strip().lower()
        
        if respuesta == palabra:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {palabra}")
            errores += 1
    
    # Mostrar resultado final
    total_palabras = len(palabras_reglas)
    aciertos = total_palabras - errores
    print(f"\nResultado final: Aciertos: {aciertos} / {total_palabras}")
    print(f"Errores: {errores}")

    if errores == 0:
        print("¡Excelente trabajo! No has cometido ningún error.")
    elif errores <= total_palabras / 2:
        print("Buen trabajo, pero podrías mejorar.")
    else:
        print("Necesitas practicar más. ¡Sigue intentándolo!")

# Menú interactivo
def menu():
    palabras_reglas_usuario = {}

    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar palabras y reglas ortográficas")
        print("2. Mostrar palabras y reglas ingresadas")
        print("3. Evaluar ortografía")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")
        
        if opcion == "1":
            palabras_reglas_usuario = ingresar_palabras()
        elif opcion == "2":
            if palabras_reglas_usuario:
                mostrar_palabras(palabras_reglas_usuario)
            else:
                print("Primero debes ingresar palabras y reglas ortográficas.")
        elif opcion == "3":
            if palabras_reglas_usuario:
                evaluar_ortografia(palabras_reglas_usuario)
            else:
                print("Primero debes ingresar palabras y reglas ortográficas.")
        elif opcion == "4":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
