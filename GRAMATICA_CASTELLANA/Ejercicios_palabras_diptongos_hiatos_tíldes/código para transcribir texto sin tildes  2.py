# Importamos las bibliotecas para el manejo de archivos y el procesamiento de texto
import random
import re

# Definimos una función para generar un fragmento de texto sin tildes
def generar_fragmento_de_texto_sin_tildes():
    # Declaramos una lista para almacenar las palabras
    palabras = []

    # Generamos 10 palabras
    for _ in range(100):
        # Generamos una palabra aleatoria
        palabra = random.choice([
            "el", "la", "los", "las",
            "que", "quien", "donde", "cuando",
            "como", "porque", "si", "no",
            "hoy", "ayer", "mañana",
            "bien", "mal", "muy",
            "solo", "junto", "lejos",
            "arriba", "abajo",
            "dentro", "fuera",
            "aquí", "allá",
            "ahora", "luego",
            "antes", "después",
            "primero", "segundo",
            "tercero",
            "cuarto", "quinto",
            "sexto", "septimo",
            "octavo", "noveno",
            "decimo"
        ])
        palabras.append(palabra)

    # Generamos el fragmento de texto
    fragmento_de_texto = " ".join(palabras)

    return fragmento_de_texto

# Generamos un fragmento de texto sin tildes
fragmento_de_texto_sin_tildes = generar_fragmento_de_texto_sin_tildes()

# Imprimimos el fragmento de texto sin tildes
print("El fragmento de texto sin tildes es:")
print(fragmento_de_texto_sin_tildes)

# Solicitamos al usuario que transcriba el fragmento de texto
fragmento_de_texto_con_tildes = input("Transcriba el fragmento de texto con tildes: ")

# Verificamos las respuestas
respuestas_correctas = []
for palabra in fragmento_de_texto_sin_tildes.split():
    palabra_con_tildes = palabra + " "
    if palabra_con_tildes in fragmento_de_texto_con_tildes:
        respuestas_correctas.append(palabra)

# Imprimimos las respuestas correctas
print("Las respuestas correctas son:")
print(respuestas_correctas)

# Imprimimos las respuestas incorrectas
respuestas_incorrectas = fragmento_de_texto_con_tildes.split()
for respuesta in respuestas_incorrectas:
    if respuesta not in respuestas_correctas:
        print("La respuesta incorrecta es:", respuesta)
