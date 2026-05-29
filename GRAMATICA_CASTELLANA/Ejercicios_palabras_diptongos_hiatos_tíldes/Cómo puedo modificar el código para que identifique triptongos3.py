def diptongo():
    diptongos = []
    while len(diptongos) < 15:
        palabra = input("Escribe una palabra que contenga diptongo o triptongo: ")
        if any([palabra.count(vocal) > 0 for vocal in "aeiouAEIOU"]) and any([palabra.count(dipt) > 0 for dipt in ["ai", "ei", "oi", "au", "eu", "iu", "ua", "ue", "uo", "iai", "iei", "uai", "uei", "uau", "ueu", "iou", "ioi", "iei", "uei", "uoi", "iau", "iéi", "iói", "uái", "uói", "uée", "iái", "iéi", "iói", "uái", "uée", "uói", "iéu", "iéi", "iúa", "iúe", "iúo", "uía", "uío", "uúa", "uúe", "uúo"]]):
            diptongos.append(palabra)
    print("Las palabras que contienen diptongo o triptongo son:")
    for palabra in diptongos:
        print(palabra)

