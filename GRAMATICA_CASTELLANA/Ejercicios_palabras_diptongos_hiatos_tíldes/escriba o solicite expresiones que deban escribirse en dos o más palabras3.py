def expresiones_separadas():
    texto = input("Escribe un fragmento de texto: ")
    palabras = texto.split()
    expresiones = []
    while len(expresiones) < 15:
        expresion = input("Escribe una expresión que deba escribirse en dos o más palabras: ")
        if " " in expresion and expresion in palabras:
            expresiones.append(expresion)
    print("Las expresiones que deben escribirse en dos o más palabras son:")
    for expresion in expresiones:
        print(expresion)
