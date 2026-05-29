import os

def mostrar_teoria():
    teoria = """
    === TEORÍA: COORDINACIÓN Y SUBORDINACIÓN ===
    Los verbos transitivos como "decir" requieren un complemento. Ejemplos:
    - Proposiciones subordinadas sustantivas (Ej: "Juan dijo que vendría").
    - Oraciones coordinadas mediante conjunciones (Ej: "Juan dijo que vendría y que traería café").
    """
    print(teoria)
    input("\nPresiona Enter para continuar...")

def ejercicio_completacion():
    print("\n=== EJERCICIO DE COMPLETACIÓN ===")
    ejercicios = [
        ("María ____ que no tenía tiempo.", "dijo"),
        ("Pedro dijo que estudiaría ___ que se esforzaría más.", "y"),
        ("El maestro dijo que revisáramos la tarea ___ que la entregáramos.", "y"),
        ("Juan dijo que vendría temprano ___ que traería café.", "y"),
        ("Mi madre dijo que cocinó arroz ___ que preparó sopa.", "y")
    ]
    puntuacion = 0
    
    for i, (oracion, respuesta) in enumerate(ejercicios, 1):
        while True:
            user_resp = input(f"{i}. {oracion} ").strip().lower()
            if user_resp == respuesta:
                print("✅ Correcto!")
                puntuacion += 10
                break
            else:
                print("❌ Incorrecto. Inténtalo de nuevo.")
    
    print(f"\n🎯 Puntuación final: {puntuacion}/50")

def ejercicio_redaccion():
    print("\n=== EJERCICIO DE REDACCIÓN ===")
    user_input = input("Escribe una oración usando coordinación o subordinación: ")
    print("✅ Tu oración ha sido guardada: " + user_input)

def menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("\n=== MENÚ ===")
        print("1. Ver teoría")
        print("2. Ejercicios de completación")
        print("3. Ejercicio de redacción")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_completacion()
        elif opcion == "3":
            ejercicio_redaccion()
        elif opcion == "4":
            print("👋 Hasta luego!")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
