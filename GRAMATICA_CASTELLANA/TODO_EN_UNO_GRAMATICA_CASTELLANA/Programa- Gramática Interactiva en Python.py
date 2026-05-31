def mostrar_menu_principal():
    print("\n---🏛️ MENÚ PRINCIPAL 🏛️---")
    print("1. 🌟Teoría de Gramática😊📖")
    print("2. 🌟Ejercicios Prácticos🧭⚡")
    print("3. 🌟Resultados y Retroalimentación📝")
    print("4. Salir")

def mostrar_submenu_teoria():
    print("\n---🏛️ TEORÍA DE GRAMÁTICA 🏛️---")
    print("1. 🌟Partes de la oración😊📝")
    print("2. 🌟Reglas de puntuación")
    print("3. 🌟Uso correcto de 'B' y 'V'")
    print("4. Volver al menú principal")

def mostrar_submenu_ejercicios():
    print("\n---🏛️ EJERCICIOS PRÁCTICOS 🏛️---")
    print("1. 🌟Identificar el sujeto y el predicado😊📝")
    print("2. 🌟Completar oraciones con puntuación correcta🧭⚡")
    print("3. 🌟Identificar errores ortográficos")
    print("4. Volver al menú principal")

# Variables para almacenar resultados
resultados = {"correctos": 0, "incorrectos": 0}

def teoria(opcion):
    if opcion == "1":
        print("\n📝Las partes de la oración incluyen sujeto, predicado y complementos. Ejemplo:")
        print("Oración: 'El gato duerme en la cama.'")
        print("- Sujeto: 'El gato'")
        print("- Predicado: 'duerme en la cama'")
    elif opcion == "2":
        print("\nReglas de puntuación: El punto y coma (;) se usa para separar ideas afines.")
    elif opcion == "3":
        print("\nUso correcto de 'B' y 'V':")
        print("- Se usa 'B' después de la letra 'M'. Ejemplo: 'también'")
        print("- Se usa 'V' después de 'N'. Ejemplo: 'invierno'")
    elif opcion == "4":
        return

def ejercicios(opcion):
    global resultados
    if opcion == "1":
        print("\nEjercicio: 📝Identifica el sujeto en la siguiente oración🌟:")
        print("'El perro juega con la pelota.'")
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == "el perro":
            print("¡Correcto! 😊")
            resultados["correctos"] += 1
        else:
            print("Incorrecto. La respuesta correcta es: 'El perro'. 😔")
            resultados["incorrectos"] += 1
    elif opcion == "2":
        print("\nEjercicio: 📝Completa la oración con la puntuación correcta🌟:")
        print("'Me gustan las frutas tropicales como el mango la papaya y el coco'")
        respuesta = input("Tu respuesta: ")
        if respuesta == "Me gustan las frutas tropicales, como el mango, la papaya y el coco.":
            print("¡Correcto! 🎉")
            resultados["correctos"] += 1
        else:
            print("Incorrecto. La respuesta correcta es:")
            print("'Me gustan las frutas tropicales, como el mango, la papaya y el coco.'")
            resultados["incorrectos"] += 1
    elif opcion == "3":
        print("\nEjercicio: Encuentra el error ortográfico en esta oración:")
        print("'Los niños invitan a sus buelos al almuerzo.'")
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == "vuelos":
            print("¡Correcto! 😄🌟")
            resultados["correctos"] += 1
        else:
            print("Incorrecto. La respuesta correcta es: 'vuelos'.")
            resultados["incorrectos"] += 1
    elif opcion == "4":
        return

def mostrar_resultados():
    print("\n--- RESULTADOS ---")
    print(f"Respuestas correctas: {resultados['correctos']}")
    print(f"Respuestas incorrectas: {resultados['incorrectos']}")
    print("¡Sigue practicando para mejorar! 🌟")

# Programa principal
while True:
    mostrar_menu_principal()
    opcion_principal = input("Selecciona una opción: ")

    if opcion_principal == "1":
        while True:
            mostrar_submenu_teoria()
            opcion_teoria = input("Selecciona una opción: ")
            if opcion_teoria == "4":
                break
            teoria(opcion_teoria)
    elif opcion_principal == "2":
        while True:
            mostrar_submenu_ejercicios()
            opcion_ejercicios = input("Selecciona una opción: ")
            if opcion_ejercicios == "4":
                break
            ejercicios(opcion_ejercicios)
    elif opcion_principal == "3":
        mostrar_resultados()
    elif opcion_principal == "4":
        print("Gracias por usar el programa. ¡Hasta pronto! 🌟")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
