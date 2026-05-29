def mostrar_menu():
    print("\nMenú de práctica sobre la posición del sujeto en predicados seleccionados por verbos de conjetura")
    print("1. Leer explicación teórica")
    print("2. Ver ejemplos")
    print("3. Escribir y analizar una oración")
    print("4. Salir")

def explicacion_teorica():
    print("\nExplicación teórica:")
    print("Los verbos de conjetura, como 'conjeturar', 'adivinar' o 'sospechar', suelen seleccionar cláusulas completas.")
    print("Sin embargo, a diferencia de verbos como 'considerar', no permiten una estructura reducida sin cópula.")
    print("Por ejemplo, 'Considero eso interesante' es posible, pero '*Conjeturábamos eso perdido' no lo es.")

def ejemplos():
    print("\nEjemplos:")
    print("1. Considero que esa teoría es interesante. (Correcto)")
    print("2. Considero esa teoría interesante. (Correcto)")
    print("3. Conjeturábamos que el dato estaba perdido. (Correcto)")
    print("4. *Conjeturábamos el dato perdido. (Incorrecto)")

def analizar_oracion():
    oracion = input("\nEscribe una oración para analizar: ")
    if "considero" in oracion or "consideramos" in oracion:
        print("Tu oración sigue un patrón permitido con cláusulas reducidas.")
    elif "conjeturo" in oracion or "conjeturamos" in oracion:
        print("Recuerda que los verbos de conjetura no aceptan cláusulas reducidas sin cópula.")
    else:
        print("Interesante oración. Verifica si sigue las reglas de los verbos de conjetura.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            explicacion_teorica()
        elif opcion == "2":
            ejemplos()
        elif opcion == "3":
            analizar_oracion()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
