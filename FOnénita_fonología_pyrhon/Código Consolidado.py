import pyttsx3
from playsound import playsound
import random
import os

# Configuración del lector de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de voz
engine.setProperty('volume', 0.9)  # Volumen

# Rutas para archivos de audio de fonemas
audio_folder = "./audios_fonemas"  # Carpeta donde están almacenados los audios de los fonemas

# Diccionario con fonemas y sus descripciones (español e inglés)
fonemas_es = {
    "/a/": "Vocal abierta, anterior, como en 'amar'.",
    "/e/": "Vocal cerrada, anterior, como en 'peso'.",
}
fonemas_en = {
    "/æ/": "Vocal abierta, como en 'cat'.",
    "/i:/": "Vocal larga, como en 'see'.",
}

# Función para leer texto en voz alta
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Menú principal consolidado
def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Estudiar Sistema Fonético y Fonológico")
        print("2. Cuestionarios Interactivos (Fonética y Fonología)")
        print("3. Ejercicios de Gramática Castellana")
        print("4. Ensayo Contrastivo de Programas")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            menu_fonetico()
        elif opcion == "2":
            cuestionarios_interactivos()
        elif opcion == "3":
            ejercicios_gramatica()
        elif opcion == "4":
            mostrar_ensayo()
        elif opcion == "5":
            print("¡Gracias por usar el programa! Hasta pronto.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Submenú para estudiar sistema fonético y fonológico
def menu_fonetico():
    while True:
        print("\n--- Estudio del Sistema Fonético y Fonológico ---")
        print("1. Teoría (Español)")
        print("2. Teoría (Inglés)")
        print("3. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            teoria_fonetica(fonemas_es, "Español")
        elif opcion == "2":
            teoria_fonetica(fonemas_en, "Inglés")
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Teoría fonética con reproducción de voz y audio
def teoria_fonetica(fonemas, idioma):
    print(f"\n--- Teoría Fonética ({idioma}) ---")
    speak(f"Teoría Fonética en {idioma}.")
    
    for fonema, descripcion in fonemas.items():
        print(f"{fonema}: {descripcion}")
        speak(f"Fonema {fonema}: {descripcion}")
        play_audio(fonema)
    input("Presiona Enter para regresar al menú anterior.")

# Cuestionarios interactivos
def cuestionarios_interactivos():
    print("\n--- Cuestionarios Interactivos ---")
    while True:
        fonema, descripcion = random.choice(list(fonemas_es.items()))
        print(f"¿Qué fonema corresponde a la descripción? {descripcion}")
        respuesta = input("Tu respuesta: ").strip()
        
        if respuesta == fonema:
            print("¡Correcto!")
            speak("Correcto.")
        else:
            print(f"Incorrecto. La respuesta era {fonema}.")
            speak(f"Incorrecto. La respuesta correcta era {fonema}.")
        
        seguir = input("¿Deseas continuar? (s/n): ").strip().lower()
        if seguir != "s":
            break

# Ejercicios de gramática
def ejercicios_gramatica():
    print("\n--- Ejercicios de Gramática Castellana ---")
    print("Sección en construcción...")
    input("Presiona Enter para regresar al menú principal.")

# Mostrar el ensayo contrastivo
def mostrar_ensayo():
    ensayo = """
    Los programas desarrollados ofrecen una variedad de enfoques para estudiar la fonética,
    fonología y gramática del español e inglés. Cada herramienta está diseñada para 
    combinar teoría, práctica interactiva y retroalimentación, haciendo énfasis en:
    
    - **Sistema Fonético**: Audios de fonemas y explicaciones detalladas.
    - **Gramática**: Ejercicios estructurados y adaptados a las necesidades del usuario.
    - **Interactividad**: Cuestionarios y retroalimentación para un aprendizaje dinámico.
    
    Al consolidar estas herramientas en un solo programa, se logra una experiencia educativa completa.
    """
    print("\n--- Ensayo Contrastivo ---")
    print(ensayo)
    speak("Mostrando ensayo contrastivo.")
    input("Presiona Enter para regresar al menú principal.")

# Reproducir audios pregrabados
def play_audio(fonema):
    filepath = os.path.join(audio_folder, f"{fonema}.mp3")
    if os.path.exists(filepath):
        playsound(filepath)
    else:
        print(f"Audio para {fonema} no encontrado.")
        speak(f"Audio for {fonema} not found.")

# Ejecutar el programa
menu_principal()
