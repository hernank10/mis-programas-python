import spacy

def analizar_concordancia_adjetivo_sustantivo(oracion):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(oracion)

    concordancia_correcta = True

    for token in doc:
        if token.pos_ == "ADJ" and token.head.pos_ == "NOUN":
            if token.morph.get("Gender", None) != token.head.morph.get("Gender", None) or \
               token.morph.get("Number", None) != token.head.morph.get("Number", None):
                concordancia_correcta = False

    return concordancia_correcta

# Pedir al usuario que ingrese una oración
oracion_usuario = input("Ingresa una oración para analizar la concordancia entre el adjetivo y el sustantivo: ")

# Analizar la concordancia entre el adjetivo y el sustantivo en la oración
concordancia_correcta = analizar_concordancia_adjetivo_sustantivo(oracion_usuario)

# Mostrar el resultado
if concordancia_correcta:
    print("La concordancia entre el adjetivo y el sustantivo es correcta.")
else:
    print("La concordancia entre el adjetivo y el sustantivo es incorrecta.")
