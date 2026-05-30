def mostrar_instrucciones():
    print("Practiquemos el uso de 'porque' y 'por que'.")
    print("1. 'Porque' es una conjunción causal que indica la razón de lo que se dice anteriormente.")
    print("   Ejemplos:")
    print("   - Nos vamos porque se está haciendo tarde.")
    print("   - No te acompaño porque tengo mucho trabajo.")
    print("2. 'Por que' está constituido por la preposición 'por' y la palabra átona 'que' (pronombre relativo o conjunción).")
    print("   Ejemplos:")
    print("   - La razón por que no ha escrito no está clara.")
    print("   - Que obtenga el puesto pasa por que demuestre su valía.")
    print()

def solicitar_ejemplo(tipo):
    if tipo == "porque":
        return input("Escribe un ejemplo utilizando 'porque': ")
    elif tipo == "por que":
        return input("Escribe un ejemplo utilizando 'por que': ")

def verificar_ejemplo(ejemplo, tipo):
    if tipo == "porque":
        if "porque" in ejemplo:
            print("¡Correcto! Has utilizado 'porque' correctamente.")
        else:
            print("Parece que no has utilizado 'porque' correctamente. Intenta nuevamente.")
    elif tipo == "por que":
        if "por que" in ejemplo:
            print("¡Correcto! Has utilizado 'por que' correctamente.")
        else:
            print("Parece que no has utilizado 'por que' correctamente. Intenta nuevamente.")

def main():
    mostrar_instrucciones()

    while True:
        print("Elige el tipo de ejemplo que quieres practicar:")
        print("1. Porque")
        print("2. Por que")
        print("3. Salir")

        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            ejemplo = solicitar_ejemplo("porque")
            verificar_ejemplo(ejemplo, "porque")
        elif opcion == "2":
            ejemplo = solicitar_ejemplo("por que")
            verificar_ejemplo(ejemplo, "por que")
        elif opcion == "3":
            print("¡Gracias por practicar! Hasta la próxima.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
