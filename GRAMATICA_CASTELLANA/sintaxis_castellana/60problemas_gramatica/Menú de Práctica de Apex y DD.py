import random

def completar_apex():
    frase = "Gabriel García Márquez, ____________, escribió *Cien años de soledad*."
    respuesta = input(f"Completa la aposición explicativa: {frase}\nRespuesta: ")
    print(f"Frase completada: Gabriel García Márquez, {respuesta}, escribió *Cien años de soledad*.\n")

def completar_dd():
    frase = "La vi en el concierto, ____________."
    respuesta = input(f"Completa la dislocación a la derecha: {frase}\nRespuesta: ")
    print(f"Frase completada: La vi en el concierto, {respuesta}.\n")

def combinar_apex_dd():
    frase = "En la reunión estaba él, ____________, ____________."
    respuesta1 = input("Completa la primera aposición explicativa: ")
    respuesta2 = input("Completa la dislocación a la derecha: ")
    print(f"Frase completada: En la reunión estaba él, {respuesta1}, {respuesta2}.\n")

def reescribir_dd():
    frase_original = "El chef preparó el plato más exquisito."
    respuesta = input(f"Reescribe con dislocación a la derecha: {frase_original}\nRespuesta: ")
    print(f"Frase reescrita: {respuesta}, el chef preparó el plato más exquisito.\n")

def crear_apex():
    frase = "El Taj Mahal, ____________, es una maravilla arquitectónica."
    respuesta = input(f"Completa la aposición explicativa: {frase}\nRespuesta: ")
    print(f"Frase completada: El Taj Mahal, {respuesta}, es una maravilla arquitectónica.\n")

def menu():
    while True:
        print("\nMenú de Práctica de Apex y DD")
        print("1. Completar una Aposición Explicativa")
        print("2. Completar una Dislocación a la Derecha")
        print("3. Combinar Apex y DD en una oración")
        print("4. Reescribir una frase con DD")
        print("5. Crear una Aposición Explicativa")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            completar_apex()
        elif opcion == "2":
            completar_dd()
        elif opcion == "3":
            combinar_apex_dd()
        elif opcion == "4":
            reescribir_dd()
        elif opcion == "5":
            crear_apex()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
