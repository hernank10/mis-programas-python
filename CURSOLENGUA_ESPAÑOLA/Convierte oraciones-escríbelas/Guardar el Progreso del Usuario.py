import json

def guardar_progreso(nombre_usuario, texto_corregido, intentos):
    progreso = {
        "nombre_usuario": nombre_usuario,
        "texto_corregido": texto_corregido,
        "intentos": intentos
    }
    with open(f"{nombre_usuario}_progreso.json", "w") as file:
        json.dump(progreso, file)

nombre_usuario = input("Introduce tu nombre: ")
intentos = 1

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

# Verificar la corrección
while not ("feliz" in texto_corregido and "conoce" in texto_corregido and "parecer" in texto_corregido and "conocer" in texto_corregido):
    print("Hay errores en tu corrección. Por favor, inténtalo de nuevo.")
    texto_corregido = input("Texto corregido: ")
    intentos += 1

print("¡Correcto! Aquí tienes tu recompensa:")
say("¡Correcto! Aquí tienes tu recompensa:")
audio_recompensa = "¡Muy bien hecho! Has corregido todos los errores."
say(audio_recompensa)

# Guardar el progreso
guardar_progreso(nombre_usuario, texto_corregido, intentos)
