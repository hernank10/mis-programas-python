def mostrar_menu():
    print("\n=== Práctica sobre Determinantes Indefinidos en Estructuras Partitivas ===")
    print("1. Leer explicación sobre estructuras partitivas")
    print("2. Realizar ejercicios de selección")
    print("3. Escribir tus propios ejemplos")
    print("4. Salir")

def explicacion():
    print("\n--- Explicación ---")
    print("Una construcción partitiva está encabezada por un determinante indefinido que extrae un subconjunto de un conjunto definido.")
    print("Ejemplo válido: Algunas de esas propuestas fueron aprobadas.")
    print("Ejemplo incorrecto: *Ciertas de esas propuestas fueron aprobadas.")
    print("Los determinantes indefinidos que pueden funcionar en estructuras partitivas incluyen: algunas, dos, demasiadas, más, etc.")

def ejercicios():
    print("\n--- Ejercicios ---")
    print("Selecciona la opción correcta para completar la oración:")
    preguntas = [
        ("__ de esas ideas fueron descartadas.", ["Algunas", "Ciertas", "Distintas", "Diversas"], 0),
        ("__ de los documentos estaban incompletos.", ["Dos", "Determinadas", "Varias", "Unas"], 0),
        ("__ de los casos fueron aprobados.", ["Más", "Diferentes", "Ciertos", "Otras"], 0)
    ]
    
    for i, (pregunta, opciones, respuesta_correcta) in enumerate(preguntas, 1):
        print(f"{i}. {pregunta}")
        for j, opcion in enumerate(opciones, 1):
            print(f"  {j}. {opcion}")
        respuesta = int(input("Selecciona la opción correcta (1-4): ")) - 1
        if respuesta == respuesta_correcta:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: {opciones[respuesta_correcta]}")

def escribir_ejemplos():
    print("\n--- Escribe tus propios ejemplos ---")
    ejemplo = input("Escribe una oración con una estructura partitiva: ")
    print("Gracias por tu contribución. Puedes revisar tu ejemplo con la explicación dada.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            explicacion()
        elif opcion == "2":
            ejercicios()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
