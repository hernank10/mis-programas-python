import random

# Reglas didácticas
reglas = """
REGLAS DE LA PRIMERA DECLINACIÓN DEL INGLÉS (SUSTANTIVOS REGULARES):

1. La mayoría de los sustantivos forman el plural añadiendo -s:
   - cat → cats
   - book → books

2. Los sustantivos terminados en -s, -sh, -ch, -x o -z forman el plural añadiendo -es:
   - bus → buses
   - box → boxes

3. Los sustantivos terminados en consonante + y cambian la -y por -ies:
   - city → cities
   - baby → babies

4. El posesivo se forma añadiendo 's (singular) o solo ' (plural terminado en -s):
   - the girl's book (el libro de la niña)
   - the girls' books (los libros de las niñas)
"""

# Lista de sustantivos para practicar
sustantivos = [
    "cat", "dog", "book", "bus", "box", "church", "city", "baby", "car", "house"
]

def generar_ejercicio():
    palabra = random.choice(sustantivos)
    tipo = random.choice(["plural", "posesivo"])
    
    if tipo == "plural":
        respuesta = formar_plural(palabra)
        print(f"Forma el PLURAL de: {palabra}")
    else:
        respuesta = formar_posesivo(palabra)
        print(f"Forma el POSESIVO de: {palabra}")
    
    return respuesta

def formar_plural(palabra):
    if palabra.endswith(("s", "sh", "ch", "x", "z")):
        return palabra + "es"
    elif palabra.endswith("y") and palabra[-2] not in "aeiou":
        return palabra[:-1] + "ies"
    else:
        return palabra + "s"

def formar_posesivo(palabra):
    plural = formar_plural(palabra)
    if plural.endswith("s"):
        return plural + "'"
    else:
        return palabra + "'s"

# Programa principal
print("=== ENTRENADOR DE LA 'PRIMERA DECLINACIÓN' DEL INGLÉS ===")
print(reglas)

puntaje = 0
for i in range(5):
    respuesta_correcta = generar_ejercicio()
    respuesta_usuario = input("Tu respuesta: ").strip()
    
    if respuesta_usuario == respuesta_correcta:
        print("✅ Correcto")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. Respuesta correcta: {respuesta_correcta}")
    print()

print(f"Tu puntaje final: {puntaje}/5")
