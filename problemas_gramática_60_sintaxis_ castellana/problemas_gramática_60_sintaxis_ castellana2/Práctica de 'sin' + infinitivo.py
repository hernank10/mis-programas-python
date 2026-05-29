import random

ejemplos = [
    "Sin comprender la situación.", "Sin decir una palabra.", "Sin saber la respuesta.", "Sin mirar atrás.",
    "Sin pensar en las consecuencias.", "Sin dudarlo un segundo.", "Sin explicar el motivo.", "Sin aprender la lección.",
    "Sin escuchar atentamente.", "Sin reconocer el error.", "Sin trabajar en equipo.", "Sin esforzarse lo suficiente.",
    "Sin escribir correctamente.", "Sin leer las instrucciones.", "Sin calcular los riesgos.", "Sin preguntar antes.",
    "Sin planear el viaje.", "Sin hacer ruido.", "Sin seguir las normas.", "Sin estudiar para el examen.",
    "Sin esperar demasiado.", "Sin pagar la cuenta.", "Sin atender la llamada.", "Sin corregir los errores.",
    "Sin mirar el reloj.", "Sin probar la comida.", "Sin cuidar los detalles.", "Sin avisar a tiempo.",
    "Sin analizar los datos.", "Sin justificar la decisión.", "Sin aceptar la realidad.", "Sin recordar la fecha.",
    "Sin cumplir la promesa.", "Sin creer en sí mismo.", "Sin compartir la información.", "Sin corregir la ortografía.",
    "Sin esperar su turno.", "Sin tomar precauciones.", "Sin controlar sus emociones.", "Sin entender el problema.",
    "Sin permitir interrupciones.", "Sin admitir su culpa.", "Sin asumir responsabilidades.", "Sin cambiar de opinión.",
    "Sin detenerse a pensar.", "Sin apreciar el esfuerzo ajeno.", "Sin respetar el turno de los demás.",
    "Sin escribir con claridad.", "Sin advertir el peligro.", "Sin seguir las indicaciones."
]

usuario_ejemplos = []

def teoria():
    print("\n--- Teoría sobre 'sin' + infinitivo ---")
    print("El uso de 'sin' seguido de un verbo en infinitivo indica ausencia de una acción. Puede funcionar como prefijo ")
    print("(con una interpretación léxica) o como preposición (con una interpretación sintáctica). La elección depende del ")
    print("contexto y de las variaciones aspectuales.")
    print("Ejemplo:")
    print(" - Sin saber la verdad, no podemos tomar decisiones correctas.")
    print(" - Sin escolarizar a los niños, la educación no avanza.\n")

def practicar_memoria():
    oracion = random.choice(ejemplos)
    print("Escribe nuevamente esta oración de memoria:")
    print(oracion)
    input("Presiona Enter para continuar...")
    print("\nAhora intenta escribirla sin verla.")
    respuesta = input("Tu respuesta: ")
    if respuesta.strip() == oracion:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta era: {oracion}")

def crear_oracion():
    verbo = input("Escribe un verbo en infinitivo: ")
    complemento = input("Escribe un complemento para la oración: ")
    simple = f"Sin {verbo} {complemento}."
    compuesta = f"Sin {verbo} {complemento}, la situación no cambiará."
    print("Oración simple:", simple)
    print("Oración compuesta:", compuesta)
    if len(usuario_ejemplos) < 100:
        usuario_ejemplos.append(simple)
        usuario_ejemplos.append(compuesta)
        print("Oraciones guardadas.")
    else:
        print("Has alcanzado el límite de 100 ejemplos guardados.")

def completar_oracion():
    base = "Sin ___ la situación, no podemos actuar correctamente."
    print("\n--- Completa la oración ---")
    print(base)
    respuesta = input("Ingresa un verbo en infinitivo: ")
    print(f"Oración completa: Sin {respuesta} la situación, no podemos actuar correctamente.")

def menu():
    while True:
        print("\n--- Práctica de 'sin' + infinitivo ---")
        print("1. Leer teoría")
        print("2. Practicar la escritura de memoria")
        print("3. Crear nuevas oraciones simples y compuestas")
        print("4. Completar una oración")
        print("5. Ver mis ejemplos guardados")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            teoria()
        elif opcion == "2":
            practicar_memoria()
        elif opcion == "3":
            crear_oracion()
        elif opcion == "4":
            completar_oracion()
        elif opcion == "5":
            print("\nTus ejemplos guardados:")
            for i, oracion in enumerate(usuario_ejemplos, 1):
                print(f"{i}. {oracion}")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
