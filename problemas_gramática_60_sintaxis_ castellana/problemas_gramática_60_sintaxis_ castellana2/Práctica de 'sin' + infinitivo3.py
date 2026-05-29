import random
import os

FILENAME = "ejemplos_guardados.txt"

def cargar_ejemplos():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except OSError:
        print("Error al cargar ejemplos. Verifica el acceso al archivo.")
        return []

def guardar_ejemplos(nuevos_ejemplos):
    try:
        with open(FILENAME, "a", encoding="utf-8") as file:
            for ejemplo in nuevos_ejemplos:
                file.write(ejemplo + "\n")
    except OSError:
        print("Error al guardar ejemplos. Verifica el acceso al archivo.")

ejemplos = cargar_ejemplos()

def teoria():
    print("\n--- Teoría sobre 'sin' + infinitivo ---")
    print("El uso de 'sin' seguido de un verbo en infinitivo indica ausencia de una acción. Puede funcionar como prefijo ")
    print("(con una interpretación léxica) o como preposición (con una interpretación sintáctica). La elección depende del ")
    print("contexto y de las variaciones aspectuales.")
    print("Ejemplo:")
    print(" - Sin saber la verdad, no podemos tomar decisiones correctas.")
    print(" - Sin escolarizar a los niños, la educación no avanza.\n")

def practicar_memoria():
    if not ejemplos:
        print("No hay ejemplos guardados para practicar.")
        return
    oracion = random.choice(ejemplos)
    print("\nEscribe nuevamente esta oración de memoria:")
    print(oracion)
    input("Presiona Enter para continuar...")
    print("\nAhora intenta escribirla sin verla.")
    respuesta = input("Tu respuesta: ").strip()
    
    if respuesta == oracion:
        print("\u00a1Correcto!")
    else:
        print("Incorrecto. La respuesta correcta era: \"{}\"".format(oracion))

def crear_oracion():
    oraciones_creadas = []
    while True:
        verbo = input("Escribe un verbo en infinitivo (o 'fin' para terminar): ")
        if verbo.lower() == 'fin':
            break
        complemento = input("Escribe un complemento para la oración: ")
        simple = f"Sin {verbo} {complemento}."
        compuesta = f"Sin {verbo} {complemento}, la situación no cambiará."
        print("Oración simple:", simple)
        print("Oración compuesta:", compuesta)
        if len(ejemplos) < 100:
            ejemplos.extend([simple, compuesta])
            oraciones_creadas.extend([simple, compuesta])
            print("Oraciones guardadas.")
        else:
            print("Has alcanzado el límite de 100 ejemplos guardados.")
    
    guardar_ejemplos(oraciones_creadas)
    print("\nAhora escribe nuevamente todas las oraciones que creaste:")
    for oracion in oraciones_creadas:
        respuesta = input(f"Escríbela nuevamente: {oracion}\nTu respuesta: ")
        if respuesta.strip() == oracion:
            print("\u00a1Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: {oracion}")

def menu():
    while True:
        print("\n--- Práctica de 'sin' + infinitivo ---")
        print("1. Leer teoría")
        print("2. Practicar la escritura de memoria")
        print("3. Crear nuevas oraciones simples y compuestas")
        print("4. Salir")
        try:
            opcion = input("Elige una opción: ")
            if opcion == "1":
                teoria()
            elif opcion == "2":
                practicar_memoria()
            elif opcion == "3":
                crear_oracion()
            elif opcion == "4":
                print("\u00a1Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except OSError:
            print("Error en la entrada/salida. Verifica el entorno de ejecución.")

if __name__ == "__main__":
    menu()
