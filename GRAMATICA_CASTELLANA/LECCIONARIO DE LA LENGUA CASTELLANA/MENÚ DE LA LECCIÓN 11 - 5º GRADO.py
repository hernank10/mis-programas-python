def mostrar_teoria():
    print("\n--- TEORÍA ---")
    print("1. El sujeto es quien realiza la acción.")
    print("2. El predicado es lo que se dice del sujeto.")
    print("3. Las oraciones compuestas tienen más de un verbo.")
    print("4. Pueden estar unidas por nexos: y, o, pero (coordinadas), o depender una de la otra (subordinadas).\n")

def mostrar_ejemplos():
    print("\n--- EJEMPLOS ---")
    print("Ejemplo 1: Luis y Pedro juegan fútbol y comen helado.")
    print("Sujeto: Luis y Pedro | Predicado: juegan fútbol y comen helado")
    print("Ejemplo 2: El perro ladra cuando alguien pasa por la calle.")
    print("Oración principal: El perro ladra | Oración subordinada: cuando alguien pasa por la calle\n")

def crear_cuento():
    print("\n--- CREA TU CUENTO CORTO ---")
    cuento = input("Escribe un pequeño cuento de 2-3 oraciones: ")
    print("\nGracias. Ahora intenta identificar los sujetos y predicados en tu cuento.\n")

def juego_roles():
    print("\n--- JUEGO DE ROLES ---")
    print("Inventa una oración con sujeto implícito (por ejemplo: 'Salí temprano.')")
    print("Ahora, representa esa oración con gestos o dramatización frente al grupo.\n")

def lectura_comprensiva():
    texto = """
    Clara miraba el cielo mientras su hermano preparaba la mochila.
    Luego, ambos salieron al parque y jugaron hasta que anocheció.
    """
    print("\n--- LECTURA COMPRENSIVA ---")
    print("Texto:")
    print(texto)
    print("\nSubraya (mentalmente o en tu cuaderno):")
    print("1. Los sujetos.")
    print("2. Los predicados.")
    print("3. Distingue oraciones coordinadas y subordinadas.\n")

def menu():
    while True:
        print("=== MENÚ DE LA LECCIÓN 11 - 5º GRADO ===")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Escribir cuento corto y analizarlo")
        print("4. Juego de roles con sujeto implícito")
        print("5. Lectura comprensiva con subrayado gramatical")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            crear_cuento()
        elif opcion == "4":
            juego_roles()
        elif opcion == "5":
            lectura_comprensiva()
        elif opcion == "6":
            print("¡Hasta la próxima lección!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
