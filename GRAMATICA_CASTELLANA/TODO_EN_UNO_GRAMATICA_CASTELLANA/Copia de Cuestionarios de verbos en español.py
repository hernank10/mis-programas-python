# Función para mostrar una pregunta
def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3/4): "))
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            return True
        else:
            print(f"Incorrecto. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")
        return False

# Cuestionarios de verbos en español
def cuestionario_verbos_espanol():
    return [
        ("¿Cuál es un verbo transitivo?", ["Correr", "Leer", "Dormir", "Estar"], 2),
        ("Selecciona el verbo reflexivo:", ["Lavarse", "Caminar", "Ver", "Ser"], 1),
        ("¿Cuál es un verbo intransitivo?", ["Cantar", "Cocinar", "Abrir", "Tener"], 1),
        ("¿Cuál es un verbo auxiliar?", ["Haber", "Cantar", "Comer", "Dormir"], 1),
        ("¿Cuál es un verbo regular?", ["Correr", "Ser", "Ir", "Hacer"], 1),
    ]

# Cuestionarios de verbos en inglés
def cuestionario_verbos_ingles():
    return [
        ("Which of the following is a modal verb?", ["Can", "Eat", "Run", "Be"], 1),
        ("Choose the irregular verb:", ["Walk", "Write", "Play", "Talk"], 2),
        ("Which is a transitive verb?", ["Read", "Sleep", "Jump", "Smile"], 1),
        ("Choose the auxiliary verb:", ["Have", "Dance", "Sing", "Cook"], 1),
        ("Which is a reflexive verb?", ["Wash yourself", "Read", "Play", "Eat"], 1),
    ]

# Guardar progreso
def guardar_progreso(usuario, idioma, tipo, puntuacion, total):
    with open("progreso_verbos.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Idioma: {idioma}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas, idioma):
    print(f"\n--- Cuestionario de Verbos: {tipo} ({idioma}) ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} ({idioma}) es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Verbos en Español e Inglés!")
    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Verbos en Español")
        print("2. Verbos en Inglés")
        print("3. Salir")
        idioma = input("Elige una opción (1-3): ")

        if idioma == "1":
            while True:
                print("\n--- Verbos en Español ---")
                print("1. Verbos Transitivos/Intransitivos")
                print("2. Verbos Reflexivos")
                print("3. Verbos Auxiliares")
                print("4. Verbos Regulares/Irregulares")
                print("5. Volver al Menú Principal")
                opcion = input("Elige una opción (1-5): ")

                if opcion == "1":
                    preguntas = [
                        ("¿Cuál es un verbo transitivo?", ["Correr", "Leer", "Dormir", "Estar"], 2),
                        ("Selecciona el verbo intransitivo:", ["Cantar", "Cocinar", "Abrir", "Tener"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Transitivos/Intransitivos", preguntas, "Español")
                elif opcion == "2":
                    preguntas = [
                        ("Selecciona el verbo reflexivo:", ["Lavarse", "Caminar", "Ver", "Ser"], 1),
                        ("Selecciona otro verbo reflexivo:", ["Vestirse", "Abrir", "Cerrar", "Dormir"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Reflexivos", preguntas, "Español")
                elif opcion == "3":
                    preguntas = [
                        ("¿Cuál es un verbo auxiliar?", ["Haber", "Cantar", "Comer", "Dormir"], 1),
                        ("Selecciona otro verbo auxiliar:", ["Ser", "Estar", "Haber", "Ir"], 3),
                    ]
                    puntuacion, total = iniciar_cuestionario("Auxiliares", preguntas, "Español")
                elif opcion == "4":
                    preguntas = [
                        ("¿Cuál es un verbo regular?", ["Correr", "Ser", "Ir", "Hacer"], 1),
                        ("Selecciona el verbo irregular:", ["Decir", "Cantar", "Mirar", "Lavar"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Regulares/Irregulares", preguntas, "Español")
                elif opcion == "5":
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    continue

                guardar_progreso(usuario, "Español", opcion, puntuacion, total)

        elif idioma == "2":
            while True:
                print("\n--- Verbos en Inglés ---")
                print("1. Modal Verbs")
                print("2. Irregular Verbs")
                print("3. Reflexive Verbs")
                print("4. Auxiliary Verbs")
                print("5. Volver al Menú Principal")
                opcion = input("Elige una opción (1-5): ")

                if opcion == "1":
                    preguntas = [
                        ("Which of the following is a modal verb?", ["Can", "Eat", "Run", "Be"], 1),
                        ("Choose another modal verb:", ["May", "Cook", "Sleep", "Dance"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Modal Verbs", preguntas, "Inglés")
                elif opcion == "2":
                    preguntas = [
                        ("Choose the irregular verb:", ["Walk", "Write", "Play", "Talk"], 2),
                        ("Select another irregular verb:", ["Go", "Wash", "Cook", "Jump"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Irregular Verbs", preguntas, "Inglés")
                elif opcion == "3":
                    preguntas = [
                        ("Which is a reflexive verb?", ["Wash yourself", "Read", "Play", "Eat"], 1),
                        ("Select another reflexive verb:", ["Dress yourself", "Cook", "Run", "Jump"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Reflexive Verbs", preguntas, "Inglés")
                elif opcion == "4":
                    preguntas = [
                        ("Choose the auxiliary verb:", ["Have", "Dance", "Sing", "Cook"], 1),
                        ("Select another auxiliary verb:", ["Be", "Play", "Cook", "Run"], 1),
                    ]
                    puntuacion, total = iniciar_cuestionario("Auxiliary Verbs", preguntas, "Inglés")
                elif opcion == "5":
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    continue

                guardar_progreso(usuario, "Inglés", opcion, puntuacion, total)

        elif idioma == "3":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

# Ejecutar el programa
menu_principal()
