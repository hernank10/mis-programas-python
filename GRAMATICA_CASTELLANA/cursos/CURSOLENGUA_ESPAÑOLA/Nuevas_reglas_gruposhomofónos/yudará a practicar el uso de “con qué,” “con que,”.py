def practica_con_expresiones():
    print("¡Vamos a practicar!")
    print("1. ¿Con qué argumentos defendiste tu posición en la reunión?")
    respuesta_1 = input("Respuesta: ")
    if respuesta_1.lower() == "con qué":
        print("¡Correcto! 😊")
    else:
        print("Incorrecto. La respuesta correcta es 'con qué'.")

    print("\n2. El libro con que aprendí a programar es muy completo.")
    respuesta_2 = input("Respuesta: ")
    if respuesta_2.lower() == "con que":
        print("¡Exacto! 🚀")
    else:
        print("Incorrecto. La respuesta correcta es 'con que'.")

    print("\n3. Conque no te gustan los deportes extremos, ¿verdad?")
    respuesta_3 = input("Respuesta: ")
    if respuesta_3.lower() == "conque":
        print("¡Muy bien! 👍")
    else:
        print("Incorrecto. La respuesta correcta es 'conque'.")

# Ejecutamos la función para practicar
practica_con_expresiones()
