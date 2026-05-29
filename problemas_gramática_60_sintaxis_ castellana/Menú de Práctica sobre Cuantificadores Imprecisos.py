def mostrar_menu():
    print("\nMenú de Práctica sobre Cuantificadores Imprecisos")
    print("1. Explicación del tema")
    print("2. Completar oraciones")
    print("3. Seleccionar el cuantificador correcto")
    print("4. Salir")

def explicacion():
    print("\nExplicación: En español, ciertos cuantificadores pueden aparecer antes o después de 'otro', ")
    print("como 'muchos otros' y 'otros muchos'. Sin embargo, otros como 'bastantes' o 'demasiados' ")
    print("sólo pueden preceder a 'otro'.")

def completar_oraciones():
    ejercicios = [
        ("He recibido _____ otros regalos.", ["muchos", "bastantes"]),
        ("Me quedan ya _____ otras cosas.", ["pocas", "muchas"]),
        ("He visto ya otras _____ desgracias.", ["demasiadas", "bastantes"])
    ]
    for oracion, respuestas in ejercicios:
        print(f"\n{oracion}")
        respuesta = input("Ingrese su respuesta: ")
        if respuesta in respuestas:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. Respuestas posibles: {', '.join(respuestas)}")

def seleccionar_cuantificador():
    opciones = {
        "1": ("¿Cuál es la forma correcta? 'otros demasiados' o 'demasiados otros'?", "demasiados otros"),
        "2": ("¿Cuál es la forma correcta? 'otros bastantes' o 'bastantes otros'?", "bastantes otros"),
        "3": ("¿Cuál es la forma correcta? 'otros muchos' o 'muchos otros'?", "ambas")
    }
    for key, (pregunta, respuesta_correcta) in opciones.items():
        print(f"\n{pregunta}")
        respuesta = input("Ingrese su respuesta: ")
        if respuesta.lower() == respuesta_correcta.lower():
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            completar_oraciones()
        elif opcion == "3":
            seleccionar_cuantificador()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
