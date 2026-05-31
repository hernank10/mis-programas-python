def menu_principal():
    print("\n*** Bienvenido al Juego de Gramática Estelar ***")
    print("Capitán Orion: ¡Prepárate para una aventura gramatical entre las estrellas!")
    print("Elige una opción:")
    print("1. Aprender sobre las partes de la gramática")
    print("2. Ejercicios de nivel básico")
    print("3. Ejercicios de nivel intermedio")
    print("4. Ejercicios de nivel avanzado")
    print("5. Agregar nuevos niveles y reglas gramaticales")
    print("0. Salir del juego")
    
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
        print("Capitán Orion: ¡Hasta la próxima, cadete!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        menu_principal()

def menu_aprender_gramatica():
    print("\n*** Menú: Aprender sobre las partes de la gramática ***")
    print("1. Sustantivos")
    print("2. Verbos")
    print("3. Adjetivos")
    print("4. Pronombres")
    print("0. Volver al menú principal")
    
    opcion = input("Selecciona un número: ")
    if opcion == '1':
        print("\nProfesora Vega: Los sustantivos son palabras que usamos para nombrar cosas, personas o lugares.")
    elif opcion == '2':
        print("\nAstra: ¡Los verbos indican acción! Por ejemplo, correr, saltar, volar...")
    elif opcion == '3':
        print("\nCapitán Orion: Los adjetivos describen a los sustantivos, como 'rápido' o 'brillante'.")
    elif opcion == '4':
        print("\nProfesora Vega: Los pronombres sustituyen a los sustantivos, como 'él', 'ella', 'eso'.")
    elif opcion == '0':
        menu_principal()
    else:
        print("Opción no válida, por favor elige de nuevo.")
        menu_aprender_gramatica()
    menu_aprender_gramatica()

def nivel_basico():
    print("\n*** Ejercicios de Nivel Básico ***")
    print("Capitán Orion: ¡Cadete, identifiquemos los sustantivos en esta frase!")
    print("Frase: 'El astronauta explora la luna con su nave.'")
    respuesta = input("¿Cuál es el sustantivo principal?: ")
    if respuesta.lower() == "astronauta" or respuesta.lower() == "luna" or respuesta.lower() == "nave":
        print("Astra: ¡Correcto! Has identificado un sustantivo y ganaste una insignia de explorador galáctico.")
    else:
        print("Profesora Vega: Lo siento, la respuesta correcta era 'astronauta', 'luna' o 'nave'.")
    menu_principal()

def nivel_intermedio():
    print("\n*** Ejercicios de Nivel Intermedio ***")
    print("Capitán Orion: Ahora, encuentra el verbo en esta frase.")
    print("Frase: 'La nave espacial viaja por el espacio a gran velocidad.'")
    respuesta = input("¿Cuál es el verbo principal?: ")
    if respuesta.lower() == "viaja":
        print("Astra: ¡Bien hecho! Has acertado y ganado la medalla de piloto estelar.")
    else:
        print("Profesora Vega: La respuesta correcta era 'viaja'. Sigue practicando, cadete.")
    menu_principal()

def nivel_avanzado():
    print("\n*** Ejercicios de Nivel Avanzado ***")
    print("Profesora Vega: En este nivel, debes separar las sílabas de una palabra.")
    palabra = "astronave"
    respuesta = input(f"¿Cómo se separan las sílabas de la palabra '{palabra}'?: ")
    if respuesta.lower() == "as-tro-na-ve":
        print("Capitán Orion: ¡Excelente! Has completado el desafío avanzado y obtenido el título de Experto Lingüístico.")
    else:
        print("Astra: No es correcto. La respuesta correcta era 'as-tro-na-ve'.")
    menu_principal()

def agregar_nivel():
    print("\n*** Agregar Nuevos Niveles ***")
    print("Capitán Orion: Puedes agregar nuevos temas y ejercicios en futuras versiones del juego.")
    print("Profesora Vega: Por ahora, sigue explorando y aprendiendo con los niveles actuales.")
    menu_principal()

# Inicia el juego
menu_principal()
