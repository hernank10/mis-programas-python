def mostrar_menu_principal():
    print("\nBienvenido al Juego de Gramática")
    print("Elige una opción:")
    print("1. Aprender sobre las partes de la gramática")
    print("2. Ejercicios de nivel básico")
    print("3. Ejercicios de nivel intermedio")
    print("4. Ejercicios de nivel avanzado")
    print("5. Salir")

def mostrar_partes_gramatica():
    print("\nPartes de la gramática:")
    print("1. Sustantivos: palabras que nombran personas, lugares, cosas o ideas.")
    print("2. Verbos: palabras que expresan acciones o estados.")
    print("3. Adjetivos: palabras que describen a los sustantivos.")
    print("4. Adverbios: palabras que modifican verbos, adjetivos u otros adverbios.")
    print("5. Pronombres: palabras que reemplazan a los sustantivos.")
    print("6. Preposiciones: palabras que muestran la relación entre otras palabras en una oración.")

def ejercicios_basicos():
    print("\nEjercicios de nivel básico:")
    print("Completa la frase con un sustantivo adecuado: 'El ___ es muy alto.'")
    respuesta = input("Escribe tu respuesta: ").strip().lower()
    if respuesta == "árbol":
        print("¡Correcto!")
    else:
        print("Respuesta incorrecta. La respuesta podría ser 'árbol' u otro sustantivo similar.")

def ejercicios_intermedios():
    print("\nEjercicios de nivel intermedio:")
    print("Identifica la parte de la oración que está en mayúsculas: 'El perro CORRE rápidamente.'")
    respuesta = input("Escribe si es un sustantivo, verbo, adjetivo o adverbio: ").strip().lower()
    if respuesta == "verbo":
        print("¡Correcto!")
    else:
        print("Respuesta incorrecta. La parte en mayúsculas es un verbo.")

def ejercicios_avanzados():
    print("\nEjercicios de nivel avanzado:")
    print("Reemplaza el sustantivo en la oración con un pronombre: 'María y Juan fueron al parque.'")
    respuesta = input("Escribe tu respuesta: ").strip().lower()
    if respuesta == "ellos fueron al parque":
        print("¡Correcto!")
    else:
        print("Respuesta incorrecta. La respuesta correcta podría ser 'Ellos fueron al parque.'")

def juego_gramatica():
    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_partes_gramatica()
        elif opcion == "2":
            ejercicios_basicos()
        elif opcion == "3":
            ejercicios_intermedios()
        elif opcion == "4":
            ejercicios_avanzados()
        elif opcion == "5":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, por favor elige un número del 1 al 5.")

# Iniciar el juego de gramática
juego_gramatica()
