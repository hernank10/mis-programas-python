import random
import speech_recognition as sr

# Ejercicio 1: Asociación de imágenes con palabras en inglés
def asociacion_imagenes_palabras():
    print("\n--- Exercise 1: Picture-Word Association ---")
    imagenes_palabras = {
        "apple": "🍎",
        "dog": "🐕",
        "sun": "☀️",
        "house": "🏠",
        "tree": "🌳"
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"What word corresponds to this image? {imagen}")
        respuesta = input("Write the word: ").strip().lower()
        if respuesta == palabra:
            print("Correct! 🎉\n")
        else:
            print(f"Incorrect. The correct answer is: {palabra}\n")

# Ejercicio 2: Dictado Interactivo en inglés
def dictado_interactivo():
    print("\n--- Exercise 2: Interactive Dictation ---")
    oraciones = [
        "The sun shines in the sky.",
        "The dog plays in the park.",
        "The apple is red and sweet.",
        "The house has a big garden.",
        "The tree provides shade in summer."
    ]
    oracion = random.choice(oraciones)
    print(f"Write the following sentence: '{oracion}'")
    respuesta = input("Your answer: ").strip()
    
    if respuesta == oracion:
        print("Perfect! No errors. 🎉\n")
    else:
        print(f"There were some errors. The correct sentence is: {oracion}\n")

# Ejercicio 3: Ordenar Palabras en inglés
def ordenar_palabras():
    print("\n--- Exercise 3: Word Order ---")
    oraciones_desordenadas = [
        ["plays", "the", "park", "in", "dog", "the"],
        ["shines", "sky", "the", "in", "sun", "the"],
        ["red", "is", "and", "sweet", "apple", "the"],
        ["big", "garden", "a", "has", "house", "the"],
        ["shade", "provides", "tree", "summer", "the", "in"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Order the following words to form a sentence: {', '.join(palabras)}")
    respuesta = input("Your answer: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta.lower() == oracion_correcta.lower():
        print("Correct! The sentence is well ordered. 🎉\n")
    else:
        print(f"Incorrect. The correct sentence is: {oracion_correcta}\n")

# Ejercicio 4: Rellenar Espacios en Blanco en inglés
def rellenar_espacios():
    print("\n--- Exercise 4: Fill in the Blanks ---")
    oraciones = [
        "The ___ shines in the sky.",
        "The dog plays in the ___.",
        "The apple is ___ and sweet.",
        "The house has a ___ garden.",
        "The tree provides ___ in summer."
    ]
    respuestas_correctas = ["sun", "park", "red", "big", "shade"]
    
    oracion = random.choice(oraciones)
    print(f"Complete the sentence: {oracion}")
    respuesta = input("Your answer: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Correct! 🎉\n")
    else:
        print(f"Incorrect. The correct answer is: {respuestas_correctas[indice]}\n")

# Ejercicio 5: Lectura en Voz Alta en inglés
def lectura_voz_alta():
    print("\n--- Exercise 5: Read Aloud ---")
    oraciones = [
        "The sun shines in the sky.",
        "The dog plays in the park.",
        "The apple is red and sweet.",
        "The house has a big garden.",
        "The tree provides shade in summer."
    ]
    oracion = random.choice(oraciones)
    print(f"Read the following sentence aloud: '{oracion}'")
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            texto_reconocido = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {texto_reconocido}")
            if texto_reconocido.lower() == oracion.lower():
                print("Perfect! You read it correctly. 🎉\n")
            else:
                print(f"There were some errors. The correct sentence is: {oracion}\n")
        except sr.UnknownValueError:
            print("Could not understand what you said. Try again.\n")
        except sr.RequestError:
            print("Error in the speech recognition service.\n")

# Menú principal
def main():
    while True:
        print("Welcome to the English Learning Application")
        print("1. Picture-Word Association")
        print("2. Interactive Dictation")
        print("3. Word Order")
        print("4. Fill in the Blanks")
        print("5. Read Aloud")
        print("6. Exit")
        opcion = input("Choose an option (1-6): ").strip()
        
        if opcion == "1":
            asociacion_imagenes_palabras()
        elif opcion == "2":
            dictado_interactivo()
        elif opcion == "3":
            ordenar_palabras()
        elif opcion == "4":
            rellenar_espacios()
        elif opcion == "5":
            lectura_voz_alta()
        elif opcion == "6":
            print("Thank you for using the application! See you soon. 👋")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
