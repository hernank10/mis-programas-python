def silabas():
    texto = input("Escribe un fragmento de texto: ")
    palabras = texto.split()
    monosilabas = []
    bisilabas = []
    trisilabas = []
    tetrasilabas = []
    for palabra in palabras:
        if len(palabra) == 1:
            monosilabas.append(palabra)
        elif len(palabra) == 2:
            bisilabas.append(palabra)
        elif len(palabra) == 3:
            trisilabas.append(palabra)
        elif len(palabra) == 4:
            tetrasilabas.append(palabra)
    print("Las palabras que contienen una sílaba son:")
    for palabra in monosilabas:
        print(palabra)
    print("Las palabras que contienen dos sílabas son:")
    for palabra in bisilabas:
        print(palabra)
    print("Las palabras que contienen tres sílabas son:")
    for palabra in trisilabas:
        print(palabra)
    print("Las palabras que contienen cuatro sílabas son:")
    for palabra in tetrasilabas:
        print(palabra)
