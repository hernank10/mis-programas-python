import random

def mostrar_menu():
    print("\nMenú de práctica de oraciones:")
    print("1. Teoría sobre oraciones simples y compuestas")
    print("2. Ver ejemplos de oraciones")
    print("3. Convertir una oración compuesta en simple")
    print("4. Convertir una oración simple en compuesta")
    print("5. Completar una oración")
    print("6. Redactar una oración y guardarla")
    print("7. Ver ejemplos guardados")
    print("8. Salir")

def mostrar_teoria():
    print("\nTEORÍA: ORACIONES SIMPLES Y COMPUESTAS")
    print("Las oraciones simples contienen un solo verbo conjugado, mientras que las oraciones compuestas")
    print("poseen dos o más verbos conjugados, usualmente unidos por conjunciones.")
    print("Ejemplo:")
    print("- Simple: La bomba cayó en el campo de batalla.")
    print("- Compuesta: La bomba cayó en el campo de batalla y destruyó todo a su paso.\n")

def mostrar_ejemplos():
    ejemplos = [
        "El imperio cayó tras años de crisis, pero su legado aún perdura.",
        "Juan cayó enfermo después de la tormenta, así que no pudo ir a trabajar.",
        "La noche cayó rápidamente sobre la ciudad, aunque las luces la mantuvieron iluminada.",
        "El telón cayó al finalizar la obra y el público aplaudió con entusiasmo."
    ]
    print("\nEJEMPLOS DE ORACIONES COMPUESAS:")
    for ejemplo in ejemplos:
        print(f"- {ejemplo}")

def obtener_oracion_compuesta():
    oraciones = [
        "La bomba cayó en el campo de batalla y destruyó todo a su paso.",
        "El imperio cayó tras años de crisis, pero su legado aún perdura.",
        "Juan cayó enfermo después de la tormenta, así que no pudo ir a trabajar.",
        "La noche cayó rápidamente sobre la ciudad, aunque las luces la mantuvieron iluminada.",
        "El telón cayó al finalizar la obra y el público aplaudió con entusiasmo."
    ]
    return random.choice(oraciones)

def obtener_oracion_simple():
    oraciones = [
        "La bomba cayó en el campo de batalla.",
        "El imperio cayó tras años de crisis.",
        "Juan cayó enfermo después de la tormenta.",
        "La noche cayó rápidamente sobre la ciudad.",
        "El telón cayó al finalizar la obra."
    ]
    return random.choice(oraciones)

def obtener_oracion_incompleta():
    oraciones = [
        "El barco ____ las velas antes de zarpar.",
        "La lluvia hizo que el nivel del agua ____.",
        "El atleta ____ la copa con orgullo tras ganar.",
        "El telón ____ al finalizar la función y el público aplaudió.",
        "Los precios ____ debido a la inflación del mercado."
    ]
    return random.choice(oraciones)

ejemplos_guardados = []

def practicar_conversion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == "1":
            mostrar_teoria()
        
        elif opcion == "2":
            mostrar_ejemplos()
        
        elif opcion == "3":
            oracion = obtener_oracion_compuesta()
            print(f"Oración compuesta: {oracion}")
            respuesta = input("Conviértela en una oración simple: ")
            print("Tu respuesta ha sido registrada. Continúa practicando.")
        
        elif opcion == "4":
            oracion = obtener_oracion_simple()
            print(f"Oración simple: {oracion}")
            respuesta = input("Conviértela en una oración compuesta: ")
            print("Tu respuesta ha sido registrada. Continúa practicando.")
        
        elif opcion == "5":
            oracion = obtener_oracion_incompleta()
            print(f"Completa la oración: {oracion}")
            respuesta = input("Tu respuesta: ")
            print("Tu respuesta ha sido registrada. Continúa practicando.")
        
        elif opcion == "6":
            if len(ejemplos_guardados) < 100:
                ejemplo = input("Escribe una oración para guardar: ")
                ejemplos_guardados.append(ejemplo)
                print("Ejemplo guardado correctamente.")
            else:
                print("Se ha alcanzado el límite de 100 ejemplos guardados.")
        
        elif opcion == "7":
            if ejemplos_guardados:
                print("\nEjemplos guardados:")
                for idx, ejemplo in enumerate(ejemplos_guardados, 1):
                    print(f"{idx}. {ejemplo}")
            else:
                print("No hay ejemplos guardados aún.")
        
        elif opcion == "8":
            print("Gracias por practicar. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    practicar_conversion()
