import re

def es_verbo_reflexivo(palabra):
    # Verificar si la palabra termina en "se" para identificar verbos reflexivos
    if re.search(r'se$', palabra):
        return True
    return False

texto = "Él se levantó temprano y se lavó las manos."
palabras = texto.split()

for palabra in palabras:
    if es_verbo_reflexivo(palabra):
        print(f"La palabra '{palabra}' es un verbo reflexivo.")
