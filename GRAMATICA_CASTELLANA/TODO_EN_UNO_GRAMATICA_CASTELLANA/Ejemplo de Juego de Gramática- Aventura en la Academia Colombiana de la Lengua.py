def menu_principal():
    print("\n*** 🏛️ Bienvenido a la Academia Colombiana de la Lengua 🏛️ ***")
    print("Tomson📜️🕵️✏: ¡Te damos la bienvenida🎶 a un lugar donde se protege y estudia la lengua castellana!")
    print("Elige una opción para comenzar:")
    print("1. 🌟📌Aprender sobre las partes de la gramática")
    print("2. 🌟📌Ejercicios de nivel básico")
    print("3. 🌟📌Ejercicios de nivel intermedio")
    print("4. 🌟📌Ejercicios de nivel avanzado")
    print("5. 🌟📌Agregar nuevos niveles y reglas gramaticales")
    print("0. 🌟📌Salir de la academia")
    
    opcion = input("Selecciona un número: ")
    if opcion == '1':
        menu_aprender_gramatica()
    elif opcion == '2':
        nivel_basico()
    elif opcion == '3':
        nivel_intermedio()
    elif opcion == '4':
        nivel_avanzado()
    elif opcion == '5':
        agregar_nivel()
    elif opcion == '0':
        print("Tomson: ¡Vuelve pronto! La lengua castellana siempre tiene algo nuevo que enseñarte.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        menu_principal()

def menu_aprender_gramatica():
    print("\n***🏛 Sala de Aprendizaje de la Gramática 🏛***")
    print("Profesora Laurent: Aquí desentrañamos los secretos de la gramática española.")
    print("1. 🌟📌Sustantivos y su clasificación")
    print("2. 🌟📌Verbos y conjugaciones")
    print("3. 🌟📌Reglas de acentuación")
    print("4. 🌟📌Diptongos y triptongos")
    print("0. 🌟📌Volver al menú principal")
    
    opcion = input("Selecciona un número: ")
    if opcion == '1':
        print("\nTomson: Los sustantivos son palabras que nombran seres, cosas, lugares e ideas. Ejemplo: 'la academia'.")
    elif opcion == '2':
        print("\nKoko: Los verbos indican acciones o estados. Conjuga 'aprender' en tiempo presente.")
    elif opcion == '3':
        print("\nProfesora Laurent: La acentuación es esencial para escribir correctamente. ¿Sabías que 'café' lleva tilde?")
    elif opcion == '4':
        print("\nTomson: Los diptongos y triptongos son combinaciones de vocales. Ejemplo de diptongo: 'paisaje'.")
    elif opcion == '0':
        menu_principal()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        menu_aprender_gramatica()
    menu_aprender_gramatica()

def nivel_basico():
    print("\n***🏛 Salón de los Primeros Desafíos 🏛***")
    print("Tomson📜️🕵: ¡Empieza con una prueba sencilla! Encuentra los sustantivos en la siguiente oración.")
    print("Frase: 'El profesor enseña la historia de la lengua en la academia.'")
    respuesta = input("¿Cuáles son los sustantivos?: ")
    if "profesor" in respuesta.lower() and "historia" in respuesta.lower() and "lengua" in respuesta.lower() and "academia" in respuesta.lower():
        print("Koko: ¡Correcto! Has recibido una insignia de Explorador de la Lengua.")
    else:
        print("Profesora Laurent: No es correcto. Los sustantivos eran 'profesor', 'historia', 'lengua' y 'academia'.")
    menu_principal()

def nivel_intermedio():
    print("\n***🏛 Sala de Conjugaciones y Acentuación 🏛***")
    print("Profesora Laurent👋: Encuentra el verbo y su tiempo verbal en la siguiente frase.")
    print("Frase👋: 'El aprendiz estudia con dedicación cada lección.'")
    respuesta = input("¿Cuál es el verbo y en qué tiempo verbal está?: ")
    if respuesta.lower() == "estudia presente":
        print("Tomson📜️🕵: ¡Bien hecho! Has ganado el título de Maestro de las Conjugaciones.")
    else:
        print("Koko: No es correcto, la respuesta era 'estudia presente'.")
    menu_principal()

def nivel_avanzado():
    print("\n***🏛 Desafíos de Acentuación y Fonética 🏛***")
    print("Profesora Laurent👋: Identifica si la siguiente palabra contiene un diptongo, un triptongo o ninguna de las dos.")
    palabra = "uruguay"
    respuesta = input(f"¿La palabra '{palabra}' contiene un diptongo, un triptongo o ninguna?: ")
    if respuesta.lower() == "triptongo":
        print("Koko: ¡Magnífico! Has alcanzado el rango de Sabio Fonético.")
    else:
        print("Profesora Laurent👋: Incorrecto. La respuesta correcta era 'triptongo'.")
    menu_principal()

def agregar_nivel():
    print("\n***🏛 Agregar Nuevas Reglas y Desafíos 🏛***")
    print("Profesora Laurent: Puedes incluir nuevas reglas y niveles, como la separación de sílabas o más sobre la acentuación.")
    print("Tomson: ¡Explora los manuscritos y crea tu propio camino de aprendizaje!")
    menu_principal()

# Inicia el juego
menu_principal()
