import spacy

def analizar_partes_oracion(oracion):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(oracion)

    partes_seleccionadas = {
        "Sustantivos": [token.text for token in doc if token.pos_ == "NOUN"],
        "Verbos": [token.text for token in doc if token.pos_ == "VERB"],
        "Adjetivos": [token.text for token in doc if token.pos_ == "ADJ"],
        "Pronombres": [token.text for token in doc if token.pos_ == "PRON"],
        "Adverbios": [token.text for token in doc if token.pos_ == "ADV"],
        "Preposiciones": [token.text for token in doc if token.pos_ == "ADP"],
        "Conjunciones": [token.text for token in doc if token.pos_ == "CONJ"],
    }

    return partes_seleccionadas

# Pedir al usuario que ingrese una oración
oracion_usuario = input("Ingresa una oración para analizar sus partes: ")

# Analizar las partes de la oración
resultado_analisis = analizar_partes_oracion(oracion_usuario)

# Mostrar el resultado
print("\nResultado del análisis:")
for categoria, partes in resultado_analisis.items():
    print(f"{categoria}: {', '.join(partes)}")
