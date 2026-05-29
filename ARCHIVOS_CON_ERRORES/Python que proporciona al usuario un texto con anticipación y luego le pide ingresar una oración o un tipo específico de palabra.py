import spacy

def analizar_estructura_oracion(oracion):
    # Cargar el modelo de SpaCy para el español
    nlp = spacy.load("es_core_news_sm")

    # Procesar la oración con SpaCy
    doc = nlp(oracion)

    # Mostrar el árbol de dependencias
    print("\nÁrbol de dependencias:")
    for token in doc:
        print(f"{token.text} <--{token.dep_}-- {token.head.text}")

    # Pedir al usuario que ingrese un tipo de palabra específico
    tipo_palabra = input("\nIngresa un tipo de palabra (sustantivo, verbo, adjetivo, etc.) para resaltar en la oración: ")

    # Mostrar palabras específicas del tipo proporcionado por el usuario
    palabras_seleccionadas = [token.text for token in doc if token.pos_ == tipo_palabra]
    print(f"\n{tipo_palabra.capitalize()}s en la oración: {palabras_seleccionadas}")

# Texto con anticipación
texto_anticipado = "La niña juega feliz en el parque. El sol brilla en el cielo azul."

# Entregar el texto al usuario
print("Aquí hay un texto para analizar:")
print(texto_anticipado)

# Pedir al usuario que ingrese una oración
or
