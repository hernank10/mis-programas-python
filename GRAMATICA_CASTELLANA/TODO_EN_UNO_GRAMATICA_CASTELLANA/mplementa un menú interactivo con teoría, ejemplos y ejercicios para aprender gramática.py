def menu_gramatica():
    while True:
        print("\n===🏛 Aprende Gramática Castellana 🏛===")
        print("1. 🌟 Teoría 🌟")
        print("2. 🌟 Ejemplos 🌟")
        print("3. 🌟 Ejercicios 🌟")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            realizar_ejercicios()
        elif opcion == "4":
            print("¡Gracias por aprender con nosotros! 😊")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def mostrar_teoria():
    print("\n📚 Teoría: Tipos de oraciones 📚")
    print("1. Declarativas: Informan un hecho. Ejemplo: 'Hoy es lunes.'")
    print("2. Interrogativas: Plantean preguntas. Ejemplo: '¿Cómo estás?' 🤔")
    print("3. Exclamativas: Expresan emoción. Ejemplo: '¡Qué alegría verte!' 😃")

def mostrar_ejemplos():
    print("\n✏️ Ejemplos:")
    print("Oración declarativa: 'El sol brilla por la mañana.' 🌞")
    print("Oración interrogativa: '¿Vendrás mañana?' 🤔")
    print("Oración exclamativa: '¡Qué hermoso día!' 😍")

def realizar_ejercicios():
    print("\n🎯 Ejercicio: Identifica el tipo de oración 🎯")
    oraciones = [
        ("¡Qué sorpresa tan agradable!", "exclamativa"),
        ("¿Dónde está mi libro?", "interrogativa"),
        ("Mañana es sábado.", "declarativa"),
    ]
    puntaje = 0

    for oracion, tipo_correcto in oraciones:
        print(f"\nOración: {oracion}")
        respuesta = input("¿Qué tipo de oración es? (declarativa/interrogativa/exclamativa): ").lower()
        if respuesta == tipo_correcto:
            print("✅ ¡Correcto! 🌟")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {tipo_correcto}.")

    print(f"\nTu puntaje final: {puntaje}/{len(oraciones)}")
    if puntaje == len(oraciones):
        print("🏆 ¡Perfecto! ¡Eres un experto en gramática! 🏆")
    elif puntaje > 0:
        print("😊 ¡Buen trabajo! Sigue practicando. 😊")
    else:
        print("😔 Sigue intentándolo. ¡No te rindas! 💪")

# Ejecutar el programa
menu_gramatica()
