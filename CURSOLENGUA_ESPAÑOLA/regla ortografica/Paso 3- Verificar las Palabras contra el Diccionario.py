import json

def cargar_diccionario():
    with open('diccionario.json', 'r') as file:
        return json.load(file)

def verificar_palabra(palabra, diccionario):
    return palabra in diccionario

# Cargar el diccionario
diccionario = cargar_diccionario()

# Texto con errores ortográficos
texto_erroneo = """
El niño se pone felís cuando conose nuevos amigos. 
Al pareser, le gusta mucho conoser personas y establecer nuevas relaciones.
"""
print("Texto con errores ortográficos:")
print(texto_erroneo)

# Solicitar corrección del texto
print("Por favor, corrige los errores ortográficos del texto anterior:")
texto_corregido = input("Texto corregido: ")

# Dividir el texto en palabras y verificar cada una
palabras = texto_corregido.split()
errores = [palabra for palabra in palabras if not verificar_palabra(palabra, diccionario)]

# Verificar la corrección
if not errores:
    print("¡Correcto! Aquí tienes tu recompensa:")
    say("¡Correcto! Aquí tienes tu recompensa:")
    audio_recompensa = "¡Muy bien hecho! Has corregido todos los errores."
    say(audio_recompensa)
else:
    print(f"Hay errores en tu corrección: {', '.join(errores)}. Por favor, inténtalo de nuevo.")
    say("Hay errores en tu corrección. Por favor, inténtalo de nuevo.")
