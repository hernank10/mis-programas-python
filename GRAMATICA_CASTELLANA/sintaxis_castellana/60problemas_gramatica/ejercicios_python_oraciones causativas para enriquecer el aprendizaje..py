def mostrar_teoria():
    print("\n--- TEORÍA SOBRE ORACIONES CAUSATIVAS ---")
    print("Las oraciones causativas expresan que una persona o circunstancia provoca que alguien más realice una acción.")
    print("El verbo más común en esta construcción es 'hacer', seguido de un infinitivo.")
    print("\nEjemplos de estructuras:")
    print("- [Sujeto] + hacer + [Complemento] + [Verbo en infinitivo]")
    print("- El maestro hizo escribir a los alumnos.")
    print("- El frío hizo temblar a los niños.")
    print("\n")

def mostrar_ejemplos():
    print("\n--- EJEMPLOS DE ORACIONES CAUSATIVAS ---")
    ejemplos = [
        "El profesor hizo estudiar a los alumnos.",
        "La tormenta hizo volar los techos de las casas.",
        "El jefe hizo trabajar más a sus empleados.",
        "El miedo hizo correr a los niños.",
        "El frío hizo encender las estufas.",
        "El entrenador hizo practicar más tiempo a los jugadores.",
        "La película hizo llorar a muchas personas.",
        "El alcalde hizo construir un puente.",
        "La noticia hizo reaccionar a la gente.",
        "El problema hizo pensar a los investigadores."
    ]
    for ejemplo in ejemplos:
        print(f"- {ejemplo}")
    print("\n")

def practicar_escritura():
    print("\n--- PRÁCTICA DE ESCRITURA ---")
    oracion = input("Escribe una oración con el verbo 'hacer' en su uso causativo: ")
    if "hacer" in oracion.lower():
        print("¡Bien! Has usado el verbo 'hacer' correctamente.")
    else:
        print("Recuerda que la oración debe contener el verbo 'hacer' seguido de un infinitivo.")
    print("\n")

def test_interactivo():
    print("\n--- TEST INTERACTIVO ---")
    preguntas = [
        {
            "pregunta": "¿Cuál de las siguientes es una oración causativa?",
            "opciones": [
                "A) Me gusta correr en la mañana.",
                "B) El profesor hizo leer el libro a los alumnos.",
                "C) María canta muy bonito."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué verbo se usa típicamente en oraciones causativas?",
            "opciones": [
                "A) Comer",
                "B) Hacer",
                "C) Bailar"
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Cuál de estas frases sigue la estructura de una oración causativa?",
            "opciones": [
                "A) El viento movió las hojas.",
                "B) La tormenta hizo caer los árboles.",
                "C) Juan está estudiando para el examen."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué característica define una oración causativa?",
            "opciones": [
                "A) Expresa una acción realizada directamente por el sujeto.",
                "B) Indica que alguien provoca que otro haga algo.",
                "C) Habla sobre una acción en el pasado."
            ],
            "respuesta": "B"
        },
        {
            "pregunta": "Completa la oración: 'El accidente hizo ____ la carretera.'",
            "opciones": [
                "A) cerrar",
                "B) cerró",
                "C) cerrando"
            ],
            "respuesta": "A"
        }
    ]

    puntaje = 0
    for pregunta in preguntas:
        print("\n" + pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta (A, B o C): ").strip().upper()
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto.")

    print(f"\nTu puntuación final: {puntaje}/{len(preguntas)}\n")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Practicar escritura")
        print("4. Realizar test")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_escritura()
        elif opcion == "4":
            test_interactivo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    menu()
