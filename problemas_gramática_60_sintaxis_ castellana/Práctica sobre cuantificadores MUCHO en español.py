import random

def mostrar_menu():
    print("\nPráctica sobre cuantificadores en español")
    print("1. Ver ejemplos y analizar")
    print("2. Escribir oraciones con cuantificadores")
    print("3. Explicación teórica")
    print("4. Salir")

def ejemplos_cuantificadores():
    ejemplos = [
        ("María ha sufrido mucho en su vida.", "Significa 'intensamente'."),
        ("Antonio piensa mucho en ella.", "Puede significar 'con mucha frecuencia' o 'durante mucho tiempo'."),
        ("Ha comido mucho.", "Aquí indica una cantidad elevada."),
        ("Ana viene mucho de familia aristocrática.", "Esta construcción no es gramatical."),
    ]
    ejemplo, explicacion = random.choice(ejemplos)
    print(f"Ejemplo: {ejemplo}")
    input("Presiona Enter para ver la explicación...")
    print(f"Explicación: {explicacion}")

def escribir_oraciones():
    print("Escribe una oración usando 'mucho' o un cuantificador afín y su significado será evaluado.")
    oracion = input("Tu oración: ")
    print("Gracias por tu aporte. Intenta analizar qué interpretación tiene tu oración.")

def explicacion_teorica():
    print("\nExplicación sobre los cuantificadores:")
    print("El cuantificador 'mucho' puede tomar distintos significados dependiendo del verbo que acompaña.")
    print("1. Con verbos de acción, indica cantidad (Ej. 'Ha comido mucho').")
    print("2. Con verbos de estado o actividad mental, indica duración o frecuencia (Ej. 'Antonio piensa mucho en ella').")
    print("3. En algunos contextos, puede indicar intensidad (Ej. 'María ha sufrido mucho').")
    print("4. Sin embargo, no siempre es compatible con cualquier verbo o construcción sintáctica.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            ejemplos_cuantificadores()
        elif opcion == "2":
            escribir_oraciones()
        elif opcion == "3":
            explicacion_teorica()
        elif opcion == "4":
            print("¡Gracias por participar!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
