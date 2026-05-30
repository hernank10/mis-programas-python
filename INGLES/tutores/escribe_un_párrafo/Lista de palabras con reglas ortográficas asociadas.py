# Lista de palabras con reglas ortográficas asociadas
palabras_reglas = {
    "acción": "Las palabras terminadas en -ción que derivan de verbos terminados en -ar, se escriben con 'c'.",
    "canción": "Las palabras terminadas en -ción derivadas de verbos, como 'cantar', se escriben con 'c'.",
    "excepción": "Las palabras terminadas en -ción que provienen de verbos en -er o -ir, como 'excepcionar', se escriben con 'c'.",
    "suficiente": "Las palabras que terminan en -ente, suelen escribirse con 'c' cuando se refiere a adjetivos o sustantivos relacionados con acciones.",
    "prohibir": "Los verbos terminados en -bir, como 'prohibir', se escriben con 'b'.",
    "conducir": "Los verbos terminados en -ducir, como 'conducir', se escriben con 'c'.",
    "diferencia": "Las palabras que terminan en -cia, como 'diferencia', se escriben con 'c'.",
}

# Función para mostrar las palabras y reglas
def mostrar_palabras():
    print("A continuación, se muestran algunas palabras con sus reglas ortográficas.")
    for palabra, regla in palabras_reglas.items():
        print(f"\nPalabra: {palabra}\nRegla: {regla}")

# Función para evaluar la ortografía del usuario
def evaluar_ortografia():
    errores = 0
    print("\nAhora escribe correctamente las palabras que se te mostraron anteriormente.")
    
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
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar palabras y reglas ortográficas")
        print("2. Evaluar ortografía")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == "1":
            mostrar_palabras()
        elif opcion == "2":
            evaluar_ortografia()
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
