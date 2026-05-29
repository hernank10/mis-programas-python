import spacy

nlp = spacy.load("es_core_news_md")

def identificar_diptongos_triptongos(texto):
  doc = nlp(texto)
  for token in doc:
    if token.pos_ == "VERB":
      # Obtener la forma de lema del verbo
      lema = token.lemma_
      # Buscar diptongos y triptongos en la forma de lema
      for i in range(len(lema) - 2):
        if lema[i] in "aeiou" and lema[i + 1] in "iuy" and lema[i + 2] in "aeiou":
          print(f"Triptongo encontrado: {lema[i]}{lema[i + 1]}{lema[i + 2]}")
        elif lema[i] in "iuy" and lema[i + 1] in "aeiou" and lema[i + 2] in "aeiou":
          print(f"Triptongo encontrado: {lema[i]}{lema[i + 1]}{lema[i + 2]}")
        elif lema[i] in "aeiou" and lema[i + 1] in "iuy":
          print(f"Diptongo encontrado: {lema[i]}{lema[i + 1]}")
        elif lema[i] in "iuy" and lema[i + 1] in "aeiou":
          print(f"Diptongo encontrado: {lema[i]}{lema[i + 1]}")

texto = "El cielo está azul y brillante."
identificar_diptongos_triptongos(texto)
