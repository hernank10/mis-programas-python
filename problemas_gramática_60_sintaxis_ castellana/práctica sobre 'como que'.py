def mostrar_explicacion():
    print("\n--- Explicación sobre 'como que' ---")
    print("En español, la expresión 'como que' introduce una noción de aproximación o incertidumbre.")
    print("Por ejemplo, en la oración 'Todos estamos como que comiendo', se indica que la acción de 'comer' no es completamente asertiva, sino que tiene un matiz de indecisión.")
    print("\nEsta construcción es obligatoria en este contexto, ya que 'Todos estamos que comiendo' no es gramaticalmente aceptado.")
    input("\nPresiona Enter para volver al menú...")

def realizar_ejercicios():
    print("\n--- Ejercicios ---")
    print("Completa las siguientes oraciones con 'como que' cuando sea necesario.")
    ejercicios = [
        ("María ___ no quiere venir a la reunión.", "como que"),
        ("Me miró ___ extrañado, pero no dijo nada.", "como que"),
        ("___ está lloviendo, mejor llevemos paraguas.", "como que"),
        ("Todos estaban ___ nerviosos antes del examen.", "como que")
    ]
    
    puntaje = 0
    for i, (oracion, respuesta_correcta) in enumerate(ejercicios, 1):
        respuesta = input(f"{i}. {oracion}\nTu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("✔ Correcto!")
            puntaje += 1
        else:
            print(f"✘ Incorrecto. La respuesta correcta era: '{respuesta_correcta}'")
    
    print(f"\nTu puntaje final: {puntaje}/{len(ejercicios)}")
    input("\nPresiona Enter para volver al menú...")

def escribir_ejemplos():
    print("\n--- Escribe tus propios ejemplos ---")
    print("Escribe una oración usando 'como que'.")
    oracion = input("Tu oración: ")
    print("\nGracias por tu ejemplo. Practicar con ejemplos propios ayuda a mejorar tu comprensión.")
    input("\nPresiona Enter para volver al menú...")

def menu():
    while True:
        print("\n--- Menú de práctica sobre 'como que' ---")
        print("1. Leer explicación")
        print("2. Realizar ejercicios")
        print("3. Escribir ejemplos propios")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_explicacion()
        elif opcion == "2":
            realizar_ejercicios()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
