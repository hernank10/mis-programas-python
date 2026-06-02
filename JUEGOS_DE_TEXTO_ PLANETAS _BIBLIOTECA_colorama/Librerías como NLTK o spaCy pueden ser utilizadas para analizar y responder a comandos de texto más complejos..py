import nltk
from nltk.tokenize import word_tokenize

# Asegúrate de descargar los recursos necesarios
# nltk.download('punkt')

def procesar_comando(comando):
    tokens = word_tokenize(comando.lower())
    if "hola" in tokens:
        return "¡Hola! ¿Cómo puedo ayudarte?"
    elif "adios" in tokens:
        return "¡Hasta luego!"
    else:
        return "No entiendo ese comando."

while True:
    comando = input(">> ")
    respuesta = procesar_comando(comando)
    print(respuesta)
    if "adios" in comando.lower():
        break
