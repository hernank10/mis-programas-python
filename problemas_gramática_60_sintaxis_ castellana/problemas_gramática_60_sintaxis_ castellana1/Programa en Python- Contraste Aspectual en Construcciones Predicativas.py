def mostrar_teoria():
    print("""
    ====================================================
    TEORÍA: CONTRASTE ASPECTUAL EN CONSTRUCCIONES PREDICATIVAS
    ====================================================

    En español, los verbos de percepción (como 'ver', 'oír', 'sentir') pueden combinarse con tres formas no finitas:
    1. Infinitivo: Ej. 'Lo vi atracar'.
    2. Gerundio: Ej. 'Lo vi atracando'.
    3. Participio: Ej. 'Lo vi atracado'.

    Cada una de estas formas aporta un valor aspectual distinto:

    - INFINITIVO: Presenta el evento como una totalidad delimitada, con un valor aspectual perfectivo.
      Ejemplo: 'Lo vi atracar' (el evento se percibe como un todo, sin focalizar en sus fases internas).

    - GERUNDIO: Presenta el evento en su desarrollo, con un valor aspectual imperfectivo.
      Ejemplo: 'Lo vi atracando' (el evento se percibe en progreso, sin referencia a su inicio o final).

    - PARTICIPIO: Presenta el evento como culminado, con un valor aspectual perfectivo o perfecto.
      Ejemplo: 'Lo vi atracado' (el evento se percibe como terminado, con un estado resultante).

    ====================================================
    """)

def ejercicio_1():
    print("""
    EJERCICIO 1: IDENTIFICAR EL VALOR ASPECTUAL
    -------------------------------------------
    A continuación, se te presentarán oraciones con verbos de percepción. Debes identificar si el predicado secundario es un infinitivo, gerundio o participio, y explicar su valor aspectual.
    """)

    oraciones = [
        "La escuché cantar en el escenario.",
        "Los vi corriendo por el parque.",
        "Encontré el libro perdido."
    ]

    respuestas_correctas = [
        "Infinitivo: 'cantar' presenta el evento como una totalidad delimitada (perfectivo).",
        "Gerundio: 'corriendo' presenta el evento en su desarrollo (imperfectivo).",
        "Participio: 'perdido' presenta el evento como culminado (perfectivo o perfecto)."
    ]

    for i, oracion in enumerate(orasiones):
        print(f"\nOración {i+1}: {oracion}")
        respuesta = input("¿Qué forma no finita aparece y qué valor aspectual tiene? ")
        print(f"Respuesta correcta: {respuestas_correctas[i]}")

def ejercicio_2():
    print("""
    EJERCICIO 2: COMPLETAR LAS ORACIONES
    ------------------------------------
    Completa las siguientes oraciones con la forma no finita correcta (infinitivo, gerundio o participio) según el valor aspectual indicado.
    """)

    ejercicios = [
        ("Vi al niño _________ (jugar/jugando/jugado) en el parque. (imperfectivo)", "jugando"),
        ("Oí a la banda _________ (tocar/tocando/tocado) mi canción favorita. (perfectivo)", "tocar"),
        ("Encontré la puerta _________ (abrir/abriendo/abierta). (perfectivo o perfecto)", "abierta")
    ]

    for i, (enunciado, respuesta) in enumerate(ejercicios):
        print(f"\nEjercicio {i+1}: {enunciado}")
        respuesta_usuario = input("Respuesta: ")
        if respuesta_usuario.lower() == respuesta:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta}'.")

def ejercicio_3():
    print("""
    EJERCICIO 3: EXPLICAR EL CONTRASTE ASPECTUAL
    --------------------------------------------
    Explica el contraste aspectual entre las siguientes oraciones:
    """)

    oraciones = [
        "Lo vi correr.",
        "Lo vi corriendo.",
        "Lo vi corrido."
    ]

    for i, oracion in enumerate(orasiones):
        print(f"\nOración {i+1}: {oracion}")
        explicacion = input("Explica el valor aspectual: ")
        print(f"Respuesta sugerida: {['Infinitivo: evento como totalidad (perfectivo).', 'Gerundio: evento en progreso (imperfectivo).', 'Participio: evento culminado (perfectivo o perfecto).'][i]}")

def main():
    print("Bienvenido al programa de teoría y ejercicios sobre el contraste aspectual en construcciones predicativas.")
    mostrar_teoria()

    while True:
        print("\nMenú de ejercicios:")
        print("1. Identificar el valor aspectual.")
        print("2. Completar las oraciones.")
        print("3. Explicar el contraste aspectual.")
        print("4. Salir.")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
