import random

def mostrar_teoria():
    print("\n--- Teoría sobre los demostrativos en español ---")
    print("Los demostrativos en español pueden aparecer en posición prenominal (antes del sustantivo) ")
    print("y en posición posnominal (después del sustantivo), sin cambiar su significado.")
    print("Ejemplo: \n - Este libro (prenominal)\n - El libro este (posnominal)")
    print("\nEn posición posnominal, el demostrativo requiere un determinante, por ejemplo: 'el libro este'.")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "Completa la frase: 'Me gusta ____ coche rojo'", "respuesta": "este"},
        {"pregunta": "Completa la frase: 'No entiendo por qué compraste ____ zapatos'", "respuesta": "esos"},
        {"pregunta": "Transforma en posnominal: 'Esa casa'", "respuesta": "la casa esa"},
        {"pregunta": "Transforma en prenominal: 'El perro aquel'", "respuesta": "aquel perro"}
    ]
    random.shuffle(ejercicios)
    
    for ejercicio in ejercicios:
        respuesta_usuario = input(f"{ejercicio['pregunta']}\nTu respuesta: ").strip().lower()
        if respuesta_usuario == ejercicio['respuesta']:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")

def menu():
    while True:
        print("\n--- Menú de Práctica ---")
        print("1. Leer teoría sobre demostrativos")
        print("2. Realizar ejercicios")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
