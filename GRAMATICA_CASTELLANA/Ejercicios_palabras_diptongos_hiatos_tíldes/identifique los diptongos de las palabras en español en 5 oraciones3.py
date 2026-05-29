def diptongo():
    oraciones = ["El hombre usa paraguas y boina siempre que llueve.", "Hay mucha nieve en las calles.", "El periodista se dirige hacia la zona del conflicto.", "Marcos se encuentra en una reunión para refinanciar su deuda con el banco.", "Fuimos al teatro a ver una obra excelente."]
    diptongos = []
    for oracion in oraciones:
        palabras = oracion.split()
        for palabra in palabras:
            if any([palabra.count(vocal) > 0 for vocal in "aeiouAEIOU"]) and any([palabra.count(dipt) > 0 for dipt in ["ai", "ei", "oi", "au", "eu", "iu", "ua", "ue", "uo"]]):
                diptongos.append(palabra)
    print("Las palabras que contienen diptongo son:")
    for palabra in diptongos:
        print(palabra)
