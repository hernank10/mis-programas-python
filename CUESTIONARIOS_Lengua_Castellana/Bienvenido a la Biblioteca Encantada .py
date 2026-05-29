import time

def bienvenida():
    print("\n🌟 Bienvenido a la Biblioteca Encantada 🌟")
    print("Aquí, las reglas de la lengua están atrapadas en libros mágicos.")
    print("Tu misión es resolver desafíos gramaticales y liberar estos conocimientos.")
    print("Prepárate para aprender, resolver y triunfar. ¡Buena suerte!\n")

def menu_principal():
    print("\n📚 Menú Principal:")
    print("1. Explorar la biblioteca")
    print("2. Resolver acertijos gramaticales")
    print("3. Ver logros")
    print("4. Salir del juego")
    return input("Elige una opción (1-4): ")

def explorar_biblioteca():
    print("\n✨ Te encuentras en un salón lleno de libros mágicos. Algunos están sellados por acertijos.")
    print("Cada libro contiene un fragmento del conocimiento gramatical.")
    print("Descubre los secretos respondiendo correctamente a los desafíos.\n")

def resolver_acertijos(logros):
    print("\n🧐 Resuelve los siguientes acertijos para liberar los libros:")
    preguntas = [
        {
            "pregunta": "¿Cuál es el sujeto en la oración: 'El gato persigue al ratón'?",
            "opciones": ["1. El gato", "2. Persigue", "3. Al ratón"],
            "respuesta": "1"
        },
        {
            "pregunta": "¿Qué tipo de palabra es 'rápidamente'?",
            "opciones": ["1. Sustantivo", "2. Adverbio", "3. Verbo"],
            "respuesta": "2"
        },
        {
            "pregunta": "¿Cuál es el plural de 'luz'?",
            "opciones": ["1. Luces", "2. Luzes", "3. Luzs"],
            "respuesta": "1"
        }
    ]

    for i, q in enumerate(preguntas):
        print(f"\n📖 Libro {i+1}: {q['pregunta']}")
        for opcion in q['opciones']:
            print(opcion)
        respuesta = input("Escribe el número de la respuesta correcta: ")
        if respuesta == q["respuesta"]:
            print("✅ ¡Correcto! El libro se ha liberado.")
            logros.append(f"Libro {i+1}: {q['pregunta']}")
        else:
            print("❌ Incorrecto. Intenta con el siguiente libro.")
    return logros

def ver_logros(logros):
    if logros:
        print("\n🏆 Logros obtenidos:")
        for logro in logros:
            print(f"- {logro}")
    else:
        print("\n⚠️ No tienes logros aún. Resuelve acertijos para ganar libros.")

def despedida():
    print("\n📚 Gracias por visitar la Biblioteca Encantada. ¡Hasta la próxima!")

def juego():
    bienvenida()
    logros = []
    while True:
        opcion = menu_principal()
        if opcion == "1":
            explorar_biblioteca()
        elif opcion == "2":
            logros = resolver_acertijos(logros)
        elif opcion == "3":
            ver_logros(logros)
        elif opcion == "4":
            despedida()
            break
        else:
            print("⚠️ Opción no válida. Inténtalo nuevamente.")
        time.sleep(1)

# Inicia el juego
juego()
