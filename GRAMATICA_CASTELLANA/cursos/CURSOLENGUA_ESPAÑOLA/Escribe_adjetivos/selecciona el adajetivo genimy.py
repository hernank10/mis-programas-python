# Lista de oraciones
oraciones = [
    "El cielo es azul.",
    "Compré una camisa nueva.",
    "El perro es muy inteligente.",
    "La casa está ubicada en una zona tranquila.",
    "Ella es una persona muy amable."
]

# Lista de adjetivos
adjetivos = [
    "azul",
    "nueva",
    "inteligente",
    "tranquila",
    "amable"
]

# Función para identificar el adjetivo en una oración
def identificar_adjetivo(oracion):
    for adjetivo in adjetivos:
        if adjetivo in oracion:
            return adjetivo
    return None

# Función para verificar si la oración reescrita es correcta
def verificar_oracion(oracion_original, adjetivo, oracion_reescrita):
    if adjetivo in oracion_reescrita:
        return True
    else:
        return False

# Bucle para recorrer las oraciones y solicitar al usuario que identifique el adjetivo
for oracion, adjetivo in zip(oraciones, adjetivos):
    print(f"Oración: {oracion}")
    adjetivo_usuario = input("¿Cuál es el adjetivo en la oración?: ")
    if adjetivo_usuario == adjetivo:
        print("¡Correcto! El adjetivo en la oración es", adjetivo)
        nueva_oracion = input("Reescribe la oración utilizando el adjetivo: ")
        if verificar_oracion(oracion, adjetivo, nueva_oracion):
            print("¡Felicidades! La oración reescrita es correcta:", nueva_oracion)
        else:
            print("Incorrecto. La oración reescrita no es correcta.")
    else:
        print("Incorrecto. El adjetivo en la oración es", adjetivo)

# Mensaje de felicitaciones al final
print("¡Felicidades! Has completado todas las oraciones.")
