def aprender_reglas_c():
    """Función para enseñar las reglas del uso de la letra C en español."""

    reglas = [
        "La C se pronuncia como K antes de A, O y U.",
        "La C se pronuncia como S antes de E e I.",
        "Hay excepciones a estas reglas, como en las palabras 'ciudad' y 'cima'.",
        "La C se utiliza en muchas terminaciones de palabras, como -cito, -cita, -cillo, -cilla.",
        # Agrega más reglas aquí
    ]

    print("¡Vamos a aprender sobre el uso de la letra C en español!")
    for regla in reglas:
        print(regla)
        input("Presiona Enter para continuar o escribe 'repetir' para volver a leer la regla: ")
        while True:
            respuesta = input("¿Quieres repetir la regla? (sí/no): ").lower()
            if respuesta == "sí":
                print(regla)
            elif respuesta == "no":
                break
            else:
                print("Por favor, responde 'sí' o 'no'.")

# Llama a la función para iniciar el programa
aprender_reglas_c()
