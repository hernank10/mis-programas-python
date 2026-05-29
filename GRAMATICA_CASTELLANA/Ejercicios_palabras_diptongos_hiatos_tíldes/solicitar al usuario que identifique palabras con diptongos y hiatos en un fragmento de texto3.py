def diptongo_hiatos():
    print("Por favor, ingresa un fragmento de texto:")
    texto = input()
    palabras = texto.split()
    diptongos = []
    hiatos = []
    for palabra in palabras:
        if any([palabra.count(vocal) > 0 for vocal in "aeiouAEIOU"]) and any([palabra.count(dipt) > 0 for dipt in ["ai", "ei", "oi", "au", "eu", "iu", "ua", "ue", "uo"]]):
            diptongos.append(palabra)
        elif any([palabra.count(vocal) > 1 for vocal in "aeiouAEIOU"]):
            hiatos.append(palabra)
    print("Las palabras que contienen diptongo son:")
    for palabra in diptongos:
        print(palabra)
    print("Las palabras que contienen hiato son:")
    for palabra in hiatos:
        print(palabra)
