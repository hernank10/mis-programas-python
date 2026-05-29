def completar_el_o_el():
    print("\nCompleta con el artículo 'el' o con el pronombre personal 'él':\n")
    oraciones = [
        "___ libro que me diste es muy interesante.",
        "___ está leyendo una novela de misterio.",
        "Hoy fui a ___ mercado a comprar frutas.",
        "No sé si ___ vendrá a la reunión esta tarde.",
        "Dejé ___ documento en la mesa de la oficina.",
    ]
    respuestas = ["el", "él", "el", "él", "el"]
    for i, oracion in enumerate(oraciones, start=1):
        respuesta = input(f"{i}. {oracion}\nTu respuesta: ").strip()
        if respuesta == respuestas[i - 1]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuestas[i - 1]}'")
    print("\n¡Terminaste la práctica!\n")


def formular_preguntas():
    print("\nFormula preguntas adecuadas con los pronombres interrogativos:\n")
    datos = [
        ("Tengo 18 años", "¿Cuántos años tienes?"),
        ("Trabajo como secretaria en una empresa de cosméticos", "¿En qué trabajas?"),
        ("Estudio Filosofía en la facultad de Salamanca", "¿Qué estudias?"),
        ("El próximo verano voy a Chile", "¿Cuándo vas a Chile?"),
        ("Aquellos chicos de camisa roja son Juan y Alfredo", "¿Quiénes son aquellos chicos?"),
        ("Raúl viene de un pueblo que está al sur de Mérida", "¿De dónde viene Raúl?"),
        ("Voy al centro de compras en metro", "¿Cómo vas al centro de compras?"),
        ("Voy a la playa el próximo martes", "¿Cuándo vas a la playa?"),
        ("Mi nombre es Mercedes", "¿Cuál es tu nombre?"),
        ("Me llamo Manuel", "¿Cómo te llamas?"),
    ]
    for i, (respuesta, pregunta) in enumerate(datos, start=1):
        print(f"\nRespuesta: {respuesta}")
        user_pregunta = input("Tu pregunta: ").strip()
        if user_pregunta.lower() == pregunta.lower():
            print("¡Correcto!")
        else:
            print(f"Incorrecto. Una pregunta adecuada sería: '{pregunta}'")
    print("\n¡Terminaste la práctica!\n")


def menu_principal():
    while True:
        print("Menú:")
        print("1. Completar con 'el' o 'él'")
        print("2. Formular preguntas con pronombres interrogativos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            completar_el_o_el()
        elif opcion == "2":
            formular_preguntas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.\n")


if __name__ == "__main__":
    menu_principal()
