import json

# Diccionario inicial en español
diccionario_espanol = {
    "feliz": "adjetivo",
    "conoce": "verbo",
    "parecer": "verbo",
    "conocer": "verbo"
}

# Guardar el diccionario en un archivo JSON
with open('diccionario_espanol.json', 'w') as file:
    json.dump(diccionario_espanol, file)

