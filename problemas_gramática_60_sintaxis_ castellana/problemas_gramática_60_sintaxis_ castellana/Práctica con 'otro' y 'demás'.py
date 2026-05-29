def mostrar_menu():
    print("\n--- Práctica con 'otro' y 'demás' ---")
    print("1. Ver explicación")
    print("2. Realizar ejercicios")
    print("3. Escribir ejemplos propios")
    print("4. Salir")
    
def mostrar_explicacion():
    print("\nExplicación:")
    print("'Otro' se usa para referirse a algo adicional o diferente dentro de un conjunto.")
    print("'Demás' se usa para referirse al resto de un grupo.")
    print("Ejemplo: 'Compré otro libro.' vs. 'Los demás libros estaban en oferta.'")
    
def realizar_ejercicios():
    print("\nEjercicio: Completa las siguientes oraciones con 'otro' o 'demás'.")
    ejercicios = [
        ("Fui a la tienda y compré ___ pantalón porque me gustó el color.", "otro"),
        ("Pedro llegó temprano, pero los ___ estudiantes llegaron tarde.", "demás"),
        ("¿Tienes ___ pregunta o ya terminaste?", "otra"),
        ("Los ___ invitados están en el salón principal.", "demás")
    ]
    
    for oracion, respuesta in ejercicios:
        respuesta_usuario = input(oracion + " ")
        if respuesta_usuario.lower() == respuesta:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es '{respuesta}'.")
    
def escribir_ejemplos():
    print("\nEscribe tus propios ejemplos usando 'otro' y 'demás'.")
    oracion1 = input("Ejemplo con 'otro': ")
    oracion2 = input("Ejemplo con 'demás': ")
    print("Gracias por participar. Aquí están tus ejemplos:")
    print("-", oracion1)
    print("-", oracion2)
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_explicacion()
        elif opcion == "2":
            realizar_ejercicios()
        elif opcion == "3":
            escribir_ejemplos()
        elif opcion == "4":
            print("Gracias por practicar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
