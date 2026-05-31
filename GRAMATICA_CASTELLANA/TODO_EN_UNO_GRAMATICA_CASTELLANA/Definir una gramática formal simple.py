#pip install nltk
import nltk
from nltk import CFG

# Descargar recursos necesarios (si es la primera vez)
nltk.download('punkt')

# Definir una gramática formal simple
gramatica = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'el' | 'la' | 'un' | 'una'
    N -> 'niño' | 'niña' | 'perro' | 'parque'
    V -> 'corre' | 've' | 'camina'
    P -> 'en' | 'con'
""")

# Crear un analizador sintáctico
parser = nltk.ChartParser(gramatica)

# Oración para analizar
oracion = "el niño corre en el parque"
tokens = nltk.word_tokenize(oracion)

# Analizar y mostrar el análisis sintáctico
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
