# Lista de oraciones para traducir (Español - Inglés)
oraciones_para_traducir = [
    ("La casa es grande.", "The house is big."),
    ("El perro corre rápido.", "The dog runs fast."),
    ("Nosotros estamos felices.", "We are happy."),
    ("Ella estudia todos los días.", "She studies every day."),
    ("El cielo está azul.", "The sky is blue."),
    ("¿Dónde está el baño?", "Where is the bathroom?"),
    ("Yo tengo un libro nuevo.", "I have a new book."),
    ("Ellos viven en Londres.", "They live in London."),
    ("Él juega al fútbol los fines de semana.", "He plays soccer on weekends."),
    ("Nos gusta viajar.", "We like to travel.")
]

# Función para mostrar una oración y verificar la traducción
def traducir_oracion(oracion, traduccion_correcta):
    print("\nTraduce la siguiente oración:")
    print(oracion)
    respuesta_usuario = input("Escribe tu traducción: ").strip()
    if respuesta_usuario.lower() == traduccion_correcta.lower():
        print("¡Correcto!")
        return True
    else:
        print(f"Incorrecto. La traducción correcta es: {traduccion_correcta}")
        return False

# Cuestionario de traducción
def cuestionario_traduccion():
    print("\n--- Cuestionario de Traducción ---")
    print("1. Español a Inglés")
    print("2. Inglés a Español")
    try:
        opcion = int(input("Elige el tipo de traducción (1/2): "))
        if opcion == 1:
            print("\n--- Traducción: Español a Inglés ---")
            puntuacion = 0
            for oracion, traduccion in oraciones_para_traducir:
                if traducir_oracion(oracion, traduccion):
                    puntuacion += 1
            print(f"\nTu puntuación final: {puntuacion}/{len(oraciones_para_traducir)}")
        elif opcion == 2:
            print("\n--- Traducción: Inglés a Español ---")
            puntuacion = 0
            for oracion, traduccion in oraciones_para_traducir:
                if traducir_oracion(traduccion, oracion):
                    puntuacion += 1
            print(f"\nTu puntuación final: {puntuacion}/{len(oraciones_para_traducir)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")

# Función para practicar gramática (Ejemplo de sustantivos)
def practica_sustantivos():
    print("\n--- Cuestionario de Sustantivos ---")
    preguntas_sustantivos = [
        ("¿Cuál es el sustantivo en la oración 'El perro corre rápido'?", "perro"),
        ("¿Cuál es el sustantivo en la oración 'La casa es grande'?", "casa"),
        ("¿Cuál es el sustantivo en la oración 'Ellos tienen un coche nuevo'?", "coche"),
    ]
    puntuacion = 0
    for pregunta, respuesta_correcta in preguntas_sustantivos:
        print(pregunta)
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
    print(f"\nTu puntuación final: {puntuacion}/{len(preguntas_sustantivos)}")

# Función para practicar verbos
def practica_verbos():
    print("\n--- Cuestionario de Verbos ---")
    preguntas_verbos = [
        ("¿Cuál es el verbo en la oración 'Ella corre todos los días'?", "corre"),
        ("¿Cuál es el verbo en la oración 'Nosotros estudiamos mucho'?", "estudiamos"),
        ("¿Cuál es el verbo en la oración 'Yo voy al cine'?", "voy"),
    ]
    puntuacion = 0
    for pregunta, respuesta_correcta in preguntas_verbos:
        print(pregunta)
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
    print(f"\nTu puntuación final: {puntuacion}/{len(preguntas_verbos)}")

# Función para practicar complementos directos
def practica_complemento_directo():
    print("\n--- Cuestionario de Complemento Directo ---")
    preguntas_complemento = [
        ("En la oración 'Vimos la película', ¿cuál es el complemento directo?", "la película"),
        ("En la oración 'Compré un libro', ¿cuál es el complemento directo?", "un libro"),
    ]
    puntuacion = 0
    for pregunta, respuesta_correcta in preguntas_complemento:
        print(pregunta)
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
    print(f"\nTu puntuación final: {puntuacion}/{len(preguntas_complemento)}")

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario Interactivo de Gramática y Traducción!")
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Traducir Oraciones")
        print("2. Practicar Sustantivos")
        print("3. Practicar Verbos")
        print("4. Practicar Complemento Directo")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            cuestionario_traduccion()
        elif opcion == "2":
            practica_sustantivos()
        elif opcion == "3":
            practica_verbos()
        elif opcion == "4":
            practica_complemento_directo()
        elif opcion == "5":
            print(f"\n¡Gracias por participar, {nombre_usuario}! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
menu_principal()
