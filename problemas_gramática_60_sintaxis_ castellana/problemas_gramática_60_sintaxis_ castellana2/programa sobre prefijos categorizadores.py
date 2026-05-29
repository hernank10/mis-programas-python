import random

def ocultar_letras(palabra, num_ocultas=2):
    """Oculta aleatoriamente algunas letras de la palabra con guiones bajos."""
    indices = random.sample(range(len(palabra)), num_ocultas)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def juego_practica():
    palabras = [
        "polisilabo", "policromatico", "polifacetico", "politecnico", "poligonal", "polimorfico", "polilingue", "polimetrico", "polifonico", "polivalente",
        "poliglota", "polimolecular", "politonal", "polideportivo", "poliestrategico", "politetico", "polidimensional", "polineuronal", "polifuncional", "polimaterial",
        "policefalo", "poligrafia", "polimerico", "multicolor", "multiforme", "multilingue", "multilateral", "multimodal", "multinacional", "multirracial", "multiorganico",
        "multigrado", "multiproposito", "multimillonario", "multirregional", "multiescalar", "multifacetico", "multiconsciente", "multitematico", "multidimensional", "multivariado",
        "multigeneracional", "multilateralista", "multitarea", "multifuncion", "multiangular", "multicausal", "multimotor"
    ]
    
    palabra = random.choice(palabras)
    palabra_oculta = ocultar_letras(palabra)
    
    print("Escribe la palabra correctamente completando las letras ocultas:")
    print(palabra_oculta)
    
    intento = input("Tu respuesta: ").strip().lower()
    
    if intento == palabra:
        print("¡Correcto! Has escrito la palabra correctamente.")
    else:
        print(f"Incorrecto. La respuesta correcta era: {palabra}")

if __name__ == "__main__":
    juego_practica()
