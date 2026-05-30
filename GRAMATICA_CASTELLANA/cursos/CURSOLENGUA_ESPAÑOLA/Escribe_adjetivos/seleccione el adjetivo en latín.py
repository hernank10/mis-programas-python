# Lista de oraciones con adjetivos en latín
oraciones = [
    "Bonus puer currit per viam.",
    "Puella pulchra in horto sedet.",
    "Magnus rex regnum tenet.",
    "Ferox leo in silva habitat.",
    "Dulce mel in cupa est.",
    "Levis aqua per rivum fluit.",
    "Bona puella amica mea est.",
    "Malus servus dominum timet.",
    "Multae stellae in caelo fulgent.",
    "Pauper agricola in villa laborat.",
    "Grauis lapis in via iacet.",
    "Audax miles in proelio pugnat.",
    "Difficilis via ad montem ducit.",
    "Opulentus mercator multas merces habet.",
    "Intelligens magister discipulos docet.",
    "Felix dies nobis venit.",
    "Pulchrum templum in urbe est.",
    "Leve onus facile porto.",
    "Acer equus velociter currit.",
    "Interessante fabula me delectat.",
    "Magnus imperator multos milites ducit."
    # ... Agrega más oraciones aquí ...
]

# Función para identificar el adjetivo en una oración
def identificar_adjetivo(oracion):
    palabras = oracion.split()
    for palabra in palabras:
        if palabra.lower() in adjetivos:
            return palabra.lower()
    return None

# Lista de adjetivos en latín
adjetivos = [
    "bonus", "malus", "magnus", "ferox", "dulce",
    "levis", "bona", "multae", "pauper", "graue",
    "audax", "difficilis", "opulentus", "intelligens", "felix",
    "pulchrum", "leve", "acer", "interessante", "magnus"
    # ... Agrega más adjetivos aquí ...
]

# Procesamiento de cada oración
for i, oracion in enumerate(oraciones, 1):
    print(f"Oración {i}: {oracion}")
    adjetivo_correcto = identificar_adjetivo(oracion)
    if adjetivo_correcto:
        respuesta_usuario = input("Identifica el adjetivo en la oración: ")
        if respuesta_usuario.lower() == adjetivo_correcto:
            print("¡Correcto! Reescribe la oración en latín:")
            nueva_oracion = input()
            print(f"Oración reescrita: {nueva_oracion}\n")
        else:
            print(f"El adjetivo correcto era '{adjetivo_correcto}'. Inténtalo de nuevo.\n")
    else:
        print("No se encontró un adjetivo en esta oración.\n")

print("¡Has completado todas las oraciones! ¡Bien hecho!")
