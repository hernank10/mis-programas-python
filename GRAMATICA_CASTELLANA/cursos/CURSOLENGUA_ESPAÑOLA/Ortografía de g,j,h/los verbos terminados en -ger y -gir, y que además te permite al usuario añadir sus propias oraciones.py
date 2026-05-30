import string
import itertools

# Definimos las sustituciones permitidas para cada letra
replacements = """
s=$ s=5 s=S c=( c=[ c={ c=< c=C r=R i=I i=| i=1 i=!
"""

# Creamos un diccionario que mapea cada letra a sus sustituciones
d = {c: [c] for c in string.printable}
for line in replacements.strip().split("\n"):
    c, replacement = line.split("=")
    d[c].append(replacement)

# Palabra original
word = "script"

# Generamos todas las combinaciones posibles
for letters in itertools.product(*[d[c] for c in word]):
    print("".join(letters))
