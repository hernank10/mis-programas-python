def poema():
    print("Aquí te presento un poema:")
    print("")
    print("La luna vino a la fragua")
    print("con su polisón de nardos.")
    print("El niño la mira, mira.")
    print("El niño la está mirando.")
    print("")
    print("...")
    print("")
    print("Ahora, por favor, escribe 15 palabras que contengan diptongo:")
    diptongos = []
    while len(diptongos) < 15:
        palabra = input("Escribe una palabra que contenga diptongo: ")
        if any([palabra.count(vocal) > 0 for vocal in "aeiouAEIOU"]) and any([palabra.count(dipt) > 0 for dipt in ["ai", "ei", "oi", "au", "eu", "iu", "ua", "ue", "uo"]]):
            diptongos.append(palabra)
    print("Las palabras que contienen diptongo son:")
    for palabra in diptongos:
        print(palabra)
