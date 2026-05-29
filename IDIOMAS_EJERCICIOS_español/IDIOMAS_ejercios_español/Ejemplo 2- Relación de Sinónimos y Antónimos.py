import random
sinonimos = {"feliz": "alegre", "rápido": "veloz"}
antonimos = {"feliz": "triste", "rápido": "lento"}
def sinonimos_antonimos():
    palabra = random.choice(list(sinonimos.keys()))
    print(f"Escribe un sinónimo o antónimo de '{palabra}':")
    respuesta = input().strip()
    if respuesta in (sinonimos[palabra], antonimos[palabra]):
        print("Correcto!")
    else:
        print(f"Incorrecto. Un sinónimo sería '{sinonimos[palabra]}' y un antónimo '{antonimos[palabra]}'")

sinonimos_antonimos()
