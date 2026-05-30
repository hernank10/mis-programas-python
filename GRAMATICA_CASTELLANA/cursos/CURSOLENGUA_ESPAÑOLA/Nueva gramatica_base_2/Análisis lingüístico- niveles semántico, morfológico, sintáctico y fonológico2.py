# -*- coding: utf-8 -*-
import json
import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import eng_to_ipa as ipa
import time

# Configuración de directorios
AUDIO_DIR = "audio_samples"
os.makedirs(AUDIO_DIR, exist_ok=True)

niveles = {
    "semántico": {"ejemplos": [], "max": 100},
    "morfológico": {"ejemplos": [], "max": 100},
    "sintáctico": {"ejemplos": [], "max": 100},
    "fonológico": {"ejemplos": [], "max": 100}
}

def generar_tts(texto, idioma='es'):
    tts = gTTS(text=texto, lang=idioma)
    filename = os.path.join(AUDIO_DIR, f"tts_{int(time.time())}.mp3")
    tts.save(filename)
    return filename

def grabar_audio(duracion=5, fs=44100):
    print(f"Grabando durante {duracion} segundos...")
    grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=2)
    sd.wait()
    filename = os.path.join(AUDIO_DIR, f"user_{int(time.time())}.wav")
    write(filename, fs, grabacion)
    return filename

def mostrar_ipa(texto, idioma='es'):
    try:
        if idioma == 'en':
            return ipa.convert(texto)
        # Implementación básica para español
        equivalencias = {
            'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
            'b': 'b', 'c': 'k', 'ch': 'ʧ', 'd': 'd', 'f': 'f',
            'g': 'g', 'h': '', 'j': 'x', 'k': 'k', 'l': 'l',
            'll': 'ʎ', 'm': 'm', 'n': 'n', 'ñ': 'ɲ', 'p': 'p',
            'q': 'k', 'r': 'ɾ', 'rr': 'r', 's': 's', 't': 't',
            'v': 'b', 'w': 'w', 'x': 'ks', 'y': 'ʝ', 'z': 'θ'
        }
        transcription = []
        for letra in texto.lower():
            transcription.append(equivalencias.get(letra, letra))
        return ''.join(transcription)
    except:
        return "Transcripción no disponible"

def crear_ejemplo(nivel):
    if len(niveles[nivel]["ejemplos"]) >= niveles[nivel]["max"]:
        print("Límite alcanzado")
        return

    print("\nNuevo ejemplo:")
    ejemplo_es = input("Texto en español: ")
    ejemplo_en = input("Texto en inglés: ")
    respuesta = input("Respuesta correcta: ")
    
    # Generar TTS
    tts_es = generar_tts(ejemplo_es, 'es')
    tts_en = generar_tts(ejemplo_en, 'en')
    
    # Grabar usuario
    print("\nGraba tu lectura (5 segundos):")
    user_audio = grabar_audio()
    
    # Generar AFI
    afi_es = mostrar_ipa(ejemplo_es, 'es')
    afi_en = ipa.convert(ejemplo_en)
    
    nuevo_ejemplo = {
        "texto": {"es": ejemplo_es, "en": ejemplo_en},
        "audio": {"tts_es": tts_es, "tts_en": tts_en, "usuario": user_audio},
        "afi": {"es": afi_es, "en": afi_en},
        "respuesta": respuesta
    }
    
    niveles[nivel]["ejemplos"].append(nuevo_ejemplo)
    print("✅ Ejemplo guardado con audio y AFI!")

def reproducir_audio(filename):
    if filename.endswith('.mp3'):
        os.system(f"start {filename}" if os.name == 'nt' else f"afplay {filename}")
    else:
        os.system(f"start {filename}" if os.name == 'nt' else f"aplay {filename}")

def menu_audio(ejemplo):
    while True:
        print("\nOpciones de audio:")
        print("1. Escuchar TTS español")
        print("2. Escuchar TTS inglés")
        print("3. Escuchar grabación usuario")
        print("4. Regresar")
        
        opcion = input("Selección: ")
        audios = ejemplo["audio"]
        
        if opcion == "1":
            reproducir_audio(audios["tts_es"])
        elif opcion == "2":
            reproducir_audio(audios["tts_en"])
        elif opcion == "3":
            reproducir_audio(audios["usuario"])
        elif opcion == "4":
            break

def ver_ejemplos(nivel):
    for idx, ejemplo in enumerate(niveles[nivel]["ejemplos"]):
        print(f"\nEjemplo #{idx + 1}")
        print(f"ES: {ejemplo['texto']['es']}")
        print(f"EN: {ejemplo['texto']['en']}")
        print(f"AFI Español: {ejemplo['afi']['es']}")
        print(f"AFI Inglés: {ejemplo['afi']['en']}")
        menu_audio(ejemplo)

def guardar_cargar_datos(accion):
    filename = "datos_linguisticos.json"
    try:
        if accion == "guardar":
            with open(filename, 'w') as f:
                json.dump(niveles, f)
            print("Datos guardados")
        elif accion == "cargar":
            with open(filename, 'r') as f:
                niveles.update(json.load(f))
            print("Datos cargados")
    except Exception as e:
        print(f"Error: {str(e)}")

def main_menu():
    while True:
        print("\nLINGUISTIC ANALYSIS SUITE")
        print("1. Crear ejemplo (con voz)")
        print("2. Ver ejemplos")
        print("3. Guardar/Cargar datos")
        print("4. Salir")
        
        opcion = input("Selección: ")
        
        if opcion == "1":
            nivel = input("Nivel (semántico/morfológico/sintáctico/fonológico): ")
            if nivel in niveles:
                crear_ejemplo(nivel)
        
        elif opcion == "2":
            nivel = input("Nivel a ver: ")
            if nivel in niveles:
                ver_ejemplos(nivel)
        
        elif opcion == "3":
            accion = input("¿Guardar o cargar? ")
            guardar_cargar_datos(accion.lower())
        
        elif opcion == "4":
            break

if __name__ == "__main__":
    main_menu()
