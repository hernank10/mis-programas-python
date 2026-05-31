#pip install nltk
import nltk
from nltk import CFG

# Descargar recursos necesarios de nltk
nltk.download('punkt')

# Definición de la gramática formal
gramatica = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP | V
    PP -> P NP
    Det -> 'el' | 'la' | 'un' | 'una'
    N -> 'niño' | 'niña' | 'perro' | 'parque' | 'jardín'
    V -> 'corre' | 've' | 'camina' | 'juega'
    P -> 'en' | 'con' | 'por' | 'sobre'
""")

# Crear un analizador sintáctico utilizando la gramática definida
parser = nltk.ChartParser(gramatica)

# Oración de ejemplo para analizar
oracion = "el niño corre en el parque"
tokens = nltk.word_tokenize(oracion)

# Analizar y mostrar el análisis sintáctico
print("Análisis sintáctico:")
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
