#adaptar el programa para que funcione con español
#usando las librerías pyttsx3 para síntesis de voz y speech_recognition para reconocimiento de voz
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

# Adaptar las Funciones para Cargar y Guardar el Diccionario

def cargar_diccionario(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

def guardar_diccionario(diccionario, archivo):
    with open(archivo, 'w') as file:
        json.dump(diccionario, file, indent=4)
        
# Verificar las Palabras contra el Diccionario

def verificar_palabra(palabra, diccionario):
    return palabra in diccionario

# Cargar el diccionario en español
diccionario_espanol = cargar_diccionario('diccionario_espanol.json')

# Texto de Ejemplo en Español y Verificación

# Texto con errores ortográficos en español
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
errores = [palabra for palabra in palabras if not verificar_palabra(palabra, diccionario_espanol)]

# Verificar la corrección
if not errores:
    print("¡Correcto! Aquí tienes tu recompensa:")
    # Recompensa de audio
    audio_recompensa = "¡Muy bien hecho! Has corregido todos los errores."
    engine.say(audio_recompensa)
    engine.runAndWait()
else:
    print(f"Hay errores en tu corrección: {', '.join(errores)}. Por favor, inténtalo de nuevo.")
    engine.say("Hay errores en tu corrección. Por favor, inténtalo de nuevo.")
    engine.runAndWait()

# Adaptar la Síntesis de Voz y el Reconocimiento de Voz

import pyttsx3
import speech_recognition as sr

# Inicializar el motor de síntesis de voz en español
engine = pyttsx3.init()
engine.setProperty('voice', 'spanish')  # Asegúrate de tener una voz en español instalada

# Función para reproducir un mensaje de voz
def say(text):
    engine.say(text)
    engine.runAndWait()

# Reconocimiento de voz en español
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Di algo en español:")
    audio = recognizer.listen(source)
    try:
        texto_reconocido = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {texto_reconocido}")
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
    except sr.RequestError:
        print("Error al conectar con el servicio de reconocimiento de voz.")


# import pyttsx3
import speech_recognition as sr

# Inicializar el motor de síntesis de voz en español
engine = pyttsx3.init()
engine.setProperty('voice', 'spanish')  # Asegúrate de tener una voz en español instalada

# Función para reproducir un mensaje de voz
def say(text):
    engine.say(text)
    engine.runAndWait()

