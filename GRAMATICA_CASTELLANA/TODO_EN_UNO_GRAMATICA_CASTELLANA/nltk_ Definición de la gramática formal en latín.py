#pip install nltk
import nltk
from nltk import CFG

# Definición de la gramática formal en latín
gramatica_latin = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'ille' | 'illa' | 'hoc'
    N -> 'puer' | 'puella' | 'canis' | 'hortus'
    V -> 'currit' | 'videt' | 'amat' | 'ambulat'
""")

# Crear un analizador sintáctico utilizando la gramática definida
parser = nltk.ChartParser(gramatica_latin)

# Oración de ejemplo para analizar (en latín)
oracion = "puer currit"
tokens = oracion.split()

# Analizar y mostrar el análisis sintáctico
print("Análisis sintáctico en latín:")
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
