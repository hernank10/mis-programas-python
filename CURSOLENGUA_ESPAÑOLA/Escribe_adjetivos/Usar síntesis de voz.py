import json
import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Función para reproducir un mensaje de voz
def say(text):
    engine.say(text)
    engine.runAndWait()

# Función para cargar el diccionario
def cargar_diccionario(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

# Función para guardar el diccionario
def guardar_diccionario(diccionario, archivo):
    with open(archivo, 'w') as file:
        json.dump(diccionario, file, indent=4)

# Función para agregar palabras al diccionario
def agregar_palabra(diccionario, archivo):
    palabra = input("Introduce la nueva palabra: ")
    tipo = input("Introduce el tipo de palabra (verbo, adjetivo, etc.): ")
    diccionario[palabra] = tipo
    guardar_diccionario(diccionario, archivo)
    print(f"La palabra '{palabra}' ha sido añadida al diccionario.")

# Función para mostrar las reglas ortográficas
def mostrar_reglas(reglas):
    print("Reglas ortográficas:")
    for clave, descripcion in reglas.items():
        print(f"- {descripcion}")
    say("Por favor, presta atención a las siguientes reglas ortográficas.")
    for descripcion in reglas.values():
        say(descripcion)

# Función para verificar palabras en el diccionario
def verificar_palabra(palabra, diccionario):
    return palabra in diccionario

# Función para verificar las reglas ortográficas en el texto
def verificar_reglas(texto):
    errores = []
    # Verificar regla de verbos terminados en -cer y -cir
    if any(palabra for palabra in texto.split() if palabra.endswith('ser') or palabra.endswith('sir')):
        errores.append("Verbos terminados en -cer y -cir deben escribirse con c.")
    
    # Verificar regla de plural de palabras terminadas en -z
    if any(palabra for palabra in texto.split() if palabra.endswith('zes')):
        errores.append("Las palabras que terminan en -z cambian la z por c al formar el plural.")
    
    # Verificar regla de uso de b y v
    if any(palabra for palabra in texto.split() if palabra.endswith('vir') or palabra.endswith('vuir')):
        errores.append("Se escriben con b todas las formas de los verbos acabados en -bir, -buir y de sus derivados.")
    
    return errores

# Función para guardar el progreso del usuario
def guardar_progreso(nombre_usuario, texto_corregido, intentos):
    progreso = {
        "nombre_usuario": nombre_usuario,
        "texto_corregido": texto_corregido,
        "intentos": intentos
    }
    with open(f"{nombre_usuario}_progreso.json", "w") as file:
        json.dump(progreso, file)

# Diccionario inicial en español
diccionario_espanol = {
    "feliz": "adjetivo",
    "conoce": "verbo",
    "parecer": "verbo",
    "conocer": "verbo"
}

# Guardar el diccionario en un archivo JSON
archivo_diccionario = 'diccionario_espanol.json'
guardar_diccionario(diccionario_espanol, archivo_diccionario)

# Cargar el diccionario
diccionario_espanol = cargar_diccionario(archivo_diccionario)

# Reglas ortográficas
reglas_ortograficas = {
    "verbos_cer_cir": "Los verbos terminados en -cer y -cir se escriben con c.",
    "plural_terminacion_z": "Las palabras que terminan en -z cambian la z por c al formar el plural.",
    "uso_b_v": "Se escriben con b todas las formas de los verbos acabados en -bir, -buir y de sus derivados."
}

# Mostrar las reglas
mostrar_reglas(reglas_ortograficas)

# Solicitar el nombre del usuario
nombre_usuario = input("Introduce tu nombre: ")
intentos = 1

# Texto con errores ortográficos en español
texto_erroneo = """
El niño se pone felís cuando conose nuevos amigos. 
Al pareser, le gusta mucho conoser personas y establecer nuevas relaciones.
"""
print("Texto con errores ortográficos:")
print(texto_erroneo)
say("Texto con errores ortográficos:")
say(texto_erroneo)

# Solicitar corrección del texto
print("Por favor, corrige los errores ortográficos del texto anterior:")
texto_corregido = input("Texto corregido: ")

# Verificar las reglas ortográficas y las palabras en el diccionario
errores = verificar_reglas(texto_corregido)
palabras = texto_corregido.split()
errores.extend([f"La palabra '{palabra}' no está en el diccionario." for palabra in palabras if not verificar_palabra(palabra, diccionario_espanol)])

# Mostrar resultados y solicitar nuevas correcciones hasta que no haya errores
while errores:
    print("Hay errores en tu corrección:")
    for error in errores:
        print(f"- {error}")
        say(error)
    texto_corregido = input("Texto corregido: ")
    errores = verificar_reglas(texto_corregido)
    palabras = texto_corregido.split()
    errores.extend([f"La palabra '{palabra}' no está en el diccionario." for palabra in palabras if not verificar_palabra(palabra, diccionario_espanol)])
    intentos += 1

print("¡Correcto! Aquí tienes tu recompensa:")
say("¡Correcto! Aquí tienes tu recompensa:")
audio_recompensa = "¡Muy bien hecho! Has corregido todos los errores."
say(audio_recompensa)

# Guardar el progreso
guardar_progreso(nombre_usuario, texto_corregido, intentos)

# Agregar una nueva palabra al diccionario
agregar_palabra(diccionario_espanol, archivo_diccionario)
