def practicar_reglas():
    reglas = [
        ("g", "gente"),
        ("g", "gigante"),
        ("g", "guerra"),
        ("j", "cruje"),
        ("j", "trabaja"),
        ("j", "cajita"),
    ]

    print("¡Bienvenido! Vamos a practicar las reglas de la 'g' y la 'j'.")
    print("Escribe la palabra correcta según la regla indicada:")

    for regla, palabra in reglas:
        respuesta = input(f"Regla: Palabras con '{regla}': {palabra.capitalize()}: ")
        if respuesta.lower() == palabra.lower():
            print("¡Correcto! ¡Sigue así!")
        else:
            print(f"La palabra correcta era '{palabra}'. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    practicar_reglas()
