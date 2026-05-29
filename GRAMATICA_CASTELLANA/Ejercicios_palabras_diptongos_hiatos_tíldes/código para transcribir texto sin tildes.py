def quitar_tildes(texto):
    # Función para quitar tildes de un texto
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    return ''.join(tildes.get(char, char) for char in texto)

def verificar_respuestas(texto_original, respuestas_usuario):
    texto_original_sin_tildes = quitar_tildes(texto_original.lower())
    respuestas_usuario_sin_tildes = quitar_tildes(respuestas_usuario.lower())
    return texto_original_sin_tildes == respuestas_usuario_sin_tildes

# Fragmento de texto con palabras compuestas en mayúsculas y sin tilde
fragmento_texto = """
En este fragmento, verás **ARMARIO** sin tilde, pero deberías escribirlo correctamente con tilde. Además, encontrarás **RELOJERO** sin tilde. Espero que puedas transcribirlo adecuadamente.
"""

# Mostrar el fragmento de texto al usuario
print("Lee el siguiente fragmento de texto y transcribe correctamente las palabras con tilde:\n")
print(fragmento_texto)

# Solicitar respuesta al usuario
respuesta_usuario = input("Tu respuesta: ")

# Verificar respuesta y proporcionar retroalimentación
if verificar_respuestas(fragmento_texto, respuesta_usuario):
    print("\n¡Correcto! Has transcritos correctamente las palabras con tilde.")
else:
    print("\nIncorrecto. Algunas palabras no han sido transcritas correctamente. Recuerda agregar tildes donde corresponda.")

