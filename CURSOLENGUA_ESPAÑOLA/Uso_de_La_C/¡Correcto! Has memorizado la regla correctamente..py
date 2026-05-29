def mostrar_reglas():
    reglas = [
        "1. Se escriben con 'C' los sustantivos que terminan en '-cia' y '-cio': experiencia, servicio.",
        "2. Se escriben con 'C' los adjetivos que terminan en '-civo' y '-civa': nocivo, pasiva.",
        "3. Se escriben con 'C' los sustantivos que terminan en '-ancia' y '-encio': constancia, silencio.",
        "4. Se escriben con 'C' los verbos terminados en '-cer' y '-cir', excepto 'hacer', 'decir' y sus compuestos: conocer, traducir.",
        "5. Se escriben con 'C' las palabras que comienzan con 'ce-' o 'ci-' seguidas de vocal: cemento, ciento.",
    ]
    for regla in reglas:
        print(regla)

def practicar_reglas():
    reglas = [
        "1. Se escriben con 'C' los sustantivos que terminan en '-cia' y '-cio': experiencia, servicio.",
        "2. Se escriben con 'C' los adjetivos que terminan en '-civo' y '-civa': nocivo, pasiva.",
        "3. Se escriben con 'C' los sustantivos que terminan en '-ancia' y '-encio': constancia, silencio.",
        "4. Se escriben con 'C' los verbos terminados en '-cer' y '-cir', excepto 'hacer', 'decir' y sus compuestos: conocer, traducir.",
        "5. Se escriben con 'C' las palabras que comienzan con 'ce-' o 'ci-' seguidas de vocal: cemento, ciento.",
    ]
    for i, regla in enumerate(reglas, 1):
        print(f"\nRegla {i}: {regla}")
        input("Presiona Enter cuando hayas leído y entendido la regla.")
        respuesta = input(f"Escribe la Regla {i}: ")
        if respuesta.strip().lower() == regla.lower():
            print("¡Correcto! Has memorizado la regla correctamente.")
        else:
            print("Incorrecto. Vuelve a intentarlo.")
            respuesta = input(f"Escribe la Regla {i} nuevamente: ")
            if respuesta.strip().lower() == regla.lower():
                print("¡Correcto! Has memorizado la regla correctamente.")
            else:
                print("Incorrecto. Sigue practicando.")

def main():
    print("Bienvenido al programa para memorizar las reglas del uso de la 'C' en español.")
    mostrar_reglas()
    input("\nPresiona Enter para comenzar a practicar.")
    practicar_reglas()
    print("\n¡Buen trabajo! Has completado la práctica de las reglas.")

if __name__ == "__main__":
    main()
