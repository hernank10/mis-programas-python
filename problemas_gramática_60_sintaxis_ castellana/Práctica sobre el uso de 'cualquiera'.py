def mostrar_menu():
    print("\nPráctica sobre el uso de 'cualquiera'")
    print("1. Explicación sobre 'cualquiera'")
    print("2. Ejercicios de completar oraciones")
    print("3. Escribir tus propios ejemplos")
    print("4. Salir")

def explicacion():
    print("\nExplicación:")
    print("La palabra 'cualquiera' puede usarse de dos formas principales en español:")
    print("1. Como determinante prenominal: 'Puedes consultar a cualquier médico.'")
    print("2. Como adjetivo posnominal: 'Puedes consultar a un médico cualquiera.'")
    print("En el primer caso, indica libre elección entre varios elementos; en el segundo, enfatiza indiferencia.")

def ejercicio_completar():
    oraciones = [
        ("Puedes hablar con ____ profesor sobre el tema.", "cualquier"),
        ("No confíes en ____ persona desconocida.", "cualquier"),
        ("Era un amigo ____ que no tenía mucho que ver con la conversación.", "cualquiera"),
        ("Aceptaron a un candidato ____ sin revisar su experiencia.", "cualquiera")
    ]
    
    print("\nEjercicios de completar oraciones con 'cualquiera'")
    correctas = 0
    for oracion, respuesta in oraciones:
        usuario = input(oracion + " ").strip().lower()
        if usuario == respuesta:
            print("Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta}'")
    print(f"Has acertado {correctas} de {len(oraciones)}.")

def escribir_ejemplos():
    print("\nEscribe tus propios ejemplos con 'cualquiera'.")
    ejemplos = []
    for i in range(3):
        ejemplo = input(f"Ejemplo {i+1}: ")
        ejemplos.append(ejemplo)
    print("Gracias por escribir tus ejemplos. Revísalos para asegurarte de que reflejan bien el uso de 'cualquiera'.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            ejercicio_completar()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
