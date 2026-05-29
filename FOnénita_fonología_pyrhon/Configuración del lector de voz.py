import pyttsx3
from playsound import playsound
import random
import os

# Configuración del lector de voz
# Esta sección inicializa el motor de voz para leer texto en voz alta.
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de voz
engine.setProperty('volume', 0.9)  # Volumen

# Carpeta para archivos de audio de fonemas
# Crea una carpeta llamada "audios_fonemas" en el mismo directorio donde se ejecutará este script.
audio_folder = "./audios_fonemas"  # Cambia la ruta si necesitas una ubicación diferente.

# Diccionario con fonemas y sus descripciones (español e inglés)
# Aquí defines los fonemas y su descripción. Puedes agregar más fonemas según tus necesidades.
fonemas_es = {
    "/a/": "Vocal abierta, anterior, como en 'amar'.",
    "/e/": "Vocal cerrada, anterior, como en 'peso'.",
}
fonemas_en = {
    "/æ/": "Vocal abierta, como en 'cat'.",
    "/i:/": "Vocal larga, como en 'see'.",
}

# Función para leer texto en voz alta
# Usa esta función para cualquier texto que desees que el programa lea en voz alta.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Menú principal consolidado
# Este es el menú principal que centraliza todas las funcionalidades del programa.
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
            menu_fonetico()  # Llama al submenú para estudiar fonética y fonología
        elif opcion == "2":
            cuestionarios_interactivos()  # Acceso a los cuestionarios interactivos
        elif opcion == "3":
            ejercicios_gramatica()  # Abre ejercicios de gramática
        elif opcion == "4":
            mostrar_ensayo()  # Muestra el ensayo contrastivo
        elif opcion == "5":
            print("¡Gracias por usar el programa! Hasta pronto.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Submenú para estudiar sistema fonético y fonológico
# Aquí defines un menú específico para explorar la teoría del sistema fonético en español e inglés.
def menu_fonetico():
    while True:
        print("\n--- Estudio del Sistema Fonético y Fonológico ---")
        print("1. Teoría (Español)")
        print("2. Teoría (Inglés)")
        print("3. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            teoria_fonetica(fonemas_es, "Español")  # Accede a la teoría del español
        elif opcion == "2":
            teoria_fonetica(fonemas_en, "Inglés")  # Accede a la teoría del inglés
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Teoría fonética con reproducción de voz y audio
# Aquí se muestra cada fonema con su descripción y se reproduce el audio asociado si está disponible.
def teoria_fonetica(fonemas, idioma):
    print(f"\n--- Teoría Fonética ({idioma}) ---")
    speak(f"Teoría Fonética en {idioma}.")  # Lee en voz alta el idioma seleccionado
    
    for fonema, descripcion in fonemas.items():
        print(f"{fonema}: {descripcion}")
        speak(f"Fonema {fonema}: {descripcion}")  # Lee en voz alta el fonema y su descripción
        play_audio(fonema)  # Reproduce el audio del fonema
    input("Presiona Enter para regresar al menú anterior.")

# Cuestionarios interactivos
# Un juego de preguntas y respuestas basado en los fonemas.
def cuestionarios_interactivos():
    print("\n--- Cuestionarios Interactivos ---")
    while True:
        fonema, descripcion = random.choice(list(fonemas_es.items()))  # Selecciona un fonema aleatorio
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
# Aquí puedes añadir ejercicios relacionados con gramática castellana.
def ejercicios_gramatica():
    print("\n--- Ejercicios de Gramática Castellana ---")
    print("Sección en construcción...")
    input("Presiona Enter para regresar al menú principal.")

# Mostrar el ensayo contrastivo
# Esta sección muestra un texto analítico sobre los programas desarrollados.
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
# Asegúrate de que los archivos de audio tengan el mismo nombre que el fonema, con extensión .mp3.
def play_audio(fonema):
    filepath = os.path.join(audio_folder, f"{fonema}.mp3")
    if os.path.exists(filepath):
        playsound(filepath)  # Reproduce el audio si existe
    else:
        print(f"Audio para {fonema} no encontrado.")
        speak(f"Audio for {fonema} not found.")

# Ejecutar el programa
# Este es el punto de entrada del programa.
menu_principal()
