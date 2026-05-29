def main():
    fragmento = input("Ingresa un fragmento de texto: ")
    palabras = fragmento.split()

    expresiones_unidas = []

    for palabra in palabras:
        if "-" in palabra:
            expresiones_unidas.append(palabra)

    print("\nExpresiones unidas encontradas:")
    for exp in expresiones_unidas:
        print(exp)

if __name__ == "__main__":
    main()
