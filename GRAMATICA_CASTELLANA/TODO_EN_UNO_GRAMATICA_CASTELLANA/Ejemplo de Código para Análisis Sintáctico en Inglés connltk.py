##pip install nltk
import nltk
from nltk import CFG

# Definición de una gramática simple en inglés
gramatica_ingles = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | N
    VP -> V NP | V NP PP | V
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'cat' | 'park'
    V -> 'saw' | 'walked' | 'ate'
    P -> 'in' | 'on' | 'with'
""")

# Crear un analizador sintáctico utilizando la gramática definida
parser = nltk.ChartParser(gramatica_ingles)

# Oración de ejemplo para analizar
oracion = "the man saw the dog in the park"
tokens = oracion.split()

# Analizar y mostrar el análisis sintáctico
print("Análisis sintáctico en inglés:")
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
