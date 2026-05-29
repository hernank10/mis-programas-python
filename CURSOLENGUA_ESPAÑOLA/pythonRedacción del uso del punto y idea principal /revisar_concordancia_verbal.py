import spacy

# Cargar el modelo de lenguaje español
nlp = spacy.load("es_core_web_sm")

def revisar_concordancia_verbal(texto):
    # Procesar el texto con el modelo de lenguaje
    doc = nlp(texto)

    # Identificar errores de concordancia verbal
    errores = []
    for token in doc:
        if token.pos_ == "VERB":
            # Verificar la concordancia entre el sujeto y el verbo
            if token.number != token.head.number:
                errores.append((token.idx, "Error de concordancia verbal: " + str(token)))

    return errores

# Ejemplo de uso
texto = "Los niño juegan en el parque."
errores = revisar_concordancia_verbal(texto)

if errores:
    print("Se encontraron errores de concordancia verbal:")
    for error in errores:
        print(error)
else:
    print("No se encontraron errores de concordancia verbal.")
