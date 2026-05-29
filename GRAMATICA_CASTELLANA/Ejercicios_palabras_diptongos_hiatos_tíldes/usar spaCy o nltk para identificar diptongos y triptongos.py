import spacy

def identificar_diptongos_y_triptongos(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)

    print("Palabras con diptongos y triptongos:")
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "VERB":  # Consideramos sustantivos y verbos
            palabra = token.text.lower()
            if "a" in palabra or "e" in palabra or "o" in palabra:  # Filtramos palabras con 'a', 'e', o 'o'
                print(f"{palabra}: {'Diptongo' if 'a' in palabra and 'e' in palabra else 'Triptongo' if 'a' in palabra and 'e' in palabra and 'o' in palabra else 'No diptongo/triptongo'}")

def main():
    texto = "El río suena suavemente. La poesía de la vida nos envuelve con su magia."
    identificar_diptongos_y_triptongos(texto)

if __name__ == "__main__":
    main()
