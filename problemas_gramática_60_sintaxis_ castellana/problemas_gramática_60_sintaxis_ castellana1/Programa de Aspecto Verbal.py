import random

def mostrar_teoria():
    teoria = """
    En español, los verbos de percepción pueden combinarse con infinitivos, gerundios y participios.
    - Infinitivo: Presenta el evento como un todo, sin enfatizar sus fases internas. Ejemplo: "Vi el barco atracar".
    - Gerundio: Enfoca el evento en su desarrollo. Ejemplo: "Vi el barco atracando".
    - Participio: Indica un evento concluido o su estado resultante. Ejemplo: "Vi el barco atracado".
    """
    print(teoria)

def ejercicio_identificacion():
    ejercicios = [
        ("Vi al niño correr en el parque.", "Infinitivo"),
        ("Vi a María estudiando en la biblioteca.", "Gerundio"),
        ("Vi el coche estacionado en la calle.", "Participio"),
        ("Observé a los pájaros volar sobre el lago.", "Infinitivo"),
        ("Miré la vela encendida sobre la mesa.", "Participio"),
        ("Escuché a los niños cantando en el aula.", "Gerundio")
    ]
    
    random.shuffle(ejercicios)
    
    puntaje = 0
    for oracion, respuesta_correcta in ejercicios:
        print(f"\nOración: {oracion}")
        print("Opciones: Infinitivo, Gerundio, Participio")
        respuesta_usuario = input("¿Qué forma verbal se usa aquí?: ").strip().capitalize()
        
        if respuesta_usuario == respuesta_correcta:
            print("Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
    
    print(f"\nTu puntaje final es: {puntaje}/{len(ejercicios)}")

def ejercicio_reescritura():
    oraciones = [
        "Oí a los perros ladrar.",
        "Vi a mi hermano pintar la pared.",
        "Observé a los niños jugar en el parque.",
        "Escuché a la profesora explicar la lección.",
        "Miré a mi amigo arreglando su bicicleta.",
        "Noté la puerta abierta.",
        "Percibí el aire frío entrando por la ventana.",
        "Vi a los alumnos trabajando en grupo.",
        "Observé el río fluyendo lentamente.",
        "Escuché la música resonando en el pasillo.",
        "Noté las luces encendidas en la casa.",
        "Vi a los gatos durmiendo bajo el árbol.",
        "Percibí el aroma del café recién hecho.",
        "Miré el papel arrugado sobre la mesa.",
        "Observé el fuego consumiendo la madera."
    ]
    
    print("\nEjercicio de reescritura: Convierte las siguientes oraciones utilizando una forma verbal distinta (infinitivo, gerundio o participio).")
    for oracion in oraciones:
        print(f"\nOración: {oracion}")
        input("Tu respuesta: ")
        print("\nComparación: Puedes revisar la teoría para verificar tu elección.")

def menu():
    while True:
        print("\n--- Programa de Aspecto Verbal ---")
        print("1. Ver teoría")
        print("2. Hacer ejercicios de identificación")
        print("3. Hacer ejercicios de reescritura")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_identificacion()
        elif opcion == "3":
            ejercicio_reescritura()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            
if __name__ == "__main__":
    menu()
