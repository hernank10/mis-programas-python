from textblob import TextBlob

def verificar_ortografia_textblob(palabra):
    blob = TextBlob(palabra)
    return blob.correct()

palabra = "cnidario"
correccion = verificar_ortografia_textblob(palabra)
print(f"Palabra original: {palabra}")
print(f"Corrección sugerida: {correccion}")
