import random

def mostrar_teoria():
    print("\n=== Teoría sobre la incompatibilidad entre 'ser' y adjetivos con complemento ===")
    print("Ciertos adjetivos pueden combinarse con 'ser' y 'estar', pero solo 'estar' permite complementos.")
    print("Ejemplo:")
    print(" - Es casado (*con María).  → INCORRECTO")
    print(" - Está casado (con María). → CORRECTO\n")

def mostrar_ejemplos():
    ejemplos = [
        ("Es feliz (*de su éxito).", "Está feliz (de su éxito)."),
        ("Es consciente (*del problema).", "Está consciente (del problema)."),
        ("Es orgulloso (*de su hijo).", "Está orgulloso (de su hijo)."),
        ("Es seguro (*de sí mismo).", "Está seguro (de sí mismo).")
    ]
    print("\n=== Ejemplos ===")
    for incorrecto, correcto in ejemplos:
        print(f"❌ {incorrecto}\n✔️ {correcto}\n")

def verificar_ejercicio():
    print("\n=== Práctica ===")
    oraciones = [
        ("(ser) feliz de su éxito", "estar feliz de su éxito"),
        ("(ser) consciente del problema", "estar consciente del problema"),
        ("(ser) seguro de sí mismo", "estar seguro de sí mismo"),
    ]
    random.shuffle(oraciones)

    for incorrecta, correcta in oraciones:
        respuesta = input(f"Corrige la siguiente oración: '{incorrecta}': ").strip().lower()
        if respuesta == correcta:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: '{correcta}'")

def menu():
    while True:
        print("\n=== Menú ===")
        print("1. Leer teoría")
        print("2. Ver ejemplos")
        print("3. Practicar ejercicios")
        print("4. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            verificar_ejercicio()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
