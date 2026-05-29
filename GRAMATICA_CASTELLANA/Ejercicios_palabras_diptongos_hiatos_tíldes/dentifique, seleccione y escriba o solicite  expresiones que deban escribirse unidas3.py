def expresiones_unidas():
    texto = input("Escribe un fragmento de texto: ")
    palabras = texto.split()
    expresiones = []
    while len(expresiones) < 15:
        expresion = input("Escribe una expresión que deba escribirse unida: ")
        if expresion in palabras:
            expresiones.append(expresion)
    print("Las expresiones que deben escribirse unidas son:")
    for expresion in expresiones:
        print(expresion)
