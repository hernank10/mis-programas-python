def mostrar_menu():
    print("\n--- Menú de Práctica de Nominalizaciones Deadjetivales ---")
    print("1. Practicar construcciones con 'lo'")
    print("2. Practicar construcciones con sustantivos abstractos")
    print("3. Practicar ambos (mezclados)")
    print("4. Salir")

def practicar_lo():
    print("\n--- Practicando Construcciones con 'lo' ---")
    oraciones = [
        ("___ bueno de Juan es su generosidad.", "lo"),
        ("___ interesante de la película es su trama.", "lo"),
        ("___ malo de la situación es que no tiene solución.", "lo"),
        ("___ importante de este proyecto es su impacto social.", "lo"),
        ("___ curioso de este fenómeno es su frecuencia.", "lo")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (lo/la)"))
        respuesta = input("Elige la opción correcta: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_sustantivos():
    print("\n--- Practicando Construcciones con Sustantivos Abstractos ---")
    oraciones = [
        ("La ___ de Juan es admirable.", "bondad"),
        ("La ___ de los políticos es cuestionable.", "honestidad"),
        ("La ___ de la película es impresionante.", "complejidad"),
        ("La ___ de la situación es preocupante.", "gravedad"),
        ("La ___ de este proyecto es notable.", "importancia")
    ]
    for oracion, correcto in oraciones:
        print("\nCompleta la oración:")
        print(oracion.replace("___", "___ (bondad/honestidad/complejidad/gravedad/importancia)"))
        respuesta = input("Elige el sustantivo correcto: ").strip().lower()
        if respuesta == correcto:
            print("¡Correcto! 👍")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")

def practicar_ambos():
    print("\n--- Practicando Ambos Tipos de Construcciones ---")
    oraciones = [
        ("___ bueno de Juan es su generosidad.", "lo", "con 'lo'"),
        ("La ___ de Juan es admirable.", "bondad", "sustantivo abstracto"),
        ("___ interesante de la película es su trama.", "lo", "con 'lo'"),
        ("La ___ de los políticos es cuestionable.", "honestidad", "sustantivo abstracto"),
        ("___ malo de la situación es que no tiene solución.", "lo", "con 'lo'")
    ]
    for oracion, correcto, tipo in oraciones:
        print("\nCompleta la oración:")
        if tipo == "con 'lo'":
            print(oracion.replace("___", "___ (lo/la)"))
        else:
            print(oracion.replace("___", "___ (bondad/honestidad/complejidad/gravedad/importancia)"))
        respuesta = input("Elige la opción correcta: ").strip().lower()
        if respuesta == correcto:
            print(f"¡Correcto! 👍 (Tipo: {tipo})")
        else:
            print(f"Incorrecto. La respuesta correcta es '{correcto}'. 👎 (Tipo: {tipo})")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            practicar_lo()
        elif opcion == "2":
            practicar_sustantivos()
        elif opcion == "3":
            practicar_ambos()
        elif opcion == "4":
            print("¡Gracias por practicar! Hasta luego. 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
