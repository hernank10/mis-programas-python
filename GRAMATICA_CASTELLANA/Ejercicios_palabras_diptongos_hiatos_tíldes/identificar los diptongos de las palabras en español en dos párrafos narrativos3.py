def diptongo():
    parrafos = ["El sol brillaba en el cielo y el viento soplaba suavemente. Los pájaros cantaban y las flores florecían. Era un día hermoso y perfecto para salir a caminar.", "La noche era oscura y silenciosa. La luna brillaba en el cielo y las estrellas parpadeaban. El viento soplaba frío y la nieve caía suavemente. Era una noche tranquila y pacífica."]
    diptongos = []
    for parrafo in parrafos:
        palabras = parrafo.split()
        for palabra in palabras:
            if any([palabra.count(vocal) > 0 for vocal in "aeiouAEIOU"]) and any([palabra.count(dipt) > 0 for dipt in ["ai", "ei", "oi", "au", "eu", "iu", "ua", "ue", "uo"]]):
                diptongos.append(palabra)
    print("Las palabras que contienen diptongo son:")
    for palabra in diptongos:
        print(palabra)
