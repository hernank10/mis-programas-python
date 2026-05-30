import random

# Diccionario de alfabetos con equivalencia en español e inglés
alphabets = {
    "Hindi": [
        ("अ", "a", "a"), ("आ", "aa", "aa"), ("इ", "i", "i"), ("ई", "ii", "ii"), ("उ", "u", "u")
    ],
    "Chino": [
        ("你", "ni", "you"), ("好", "hao", "good"), ("是", "shi", "is/are"), ("我", "wo", "I/me"), ("的", "de", "of")
    ],
    "Coreano": [
        ("ㄱ", "giyeok", "g/k"), ("ㄴ", "nieun", "n"), ("ㄷ", "digeut", "d/t"), ("ㄹ", "rieul", "r/l"), ("ㅁ", "mieum", "m")
    ],
    "Árabe": [
        ("ا", "alif", "a"), ("ب", "baa", "b"), ("ت", "taa", "t"), ("ث", "thaa", "th"), ("ج", "jeem", "j")
    ],
    "Japonés": [
        ("あ", "a", "a"), ("い", "i", "i"), ("う", "u", "u"), ("え", "e", "e"), ("お", "o", "o")
    ]
}

# Función para reproducir la pronunciación
def pronounce_character(character, language):
    engine.setProperty('rate', 150)
    engine.say(character)
    engine.runAndWait()

# Función para practicar un alfabeto
def practice_alphabet(language):
    alphabet = alphabets[language]
    random.shuffle(alphabet)
    correct_answers = 0

    print(f"\n--- Practicando el alfabeto: {language} ---")
    print("Escribe el carácter que corresponda a la transliteración.")

    for char, translit_es, translit_en in alphabet:
        print(f"\nTransliteración (Español): {translit_es}")
        print(f"Transliteración (Inglés): {translit_en}")
        pronounce_character(char, language)

        user_input = input("Escribe el carácter: ").strip()
        if user_input == char:
            print("¡Correcto! 🎉")
            correct_answers += 1
        else:
            print(f"Incorrecto. El carácter correcto es: {char}")

    print(f"\n¡Ejercicio completado! Respuestas correctas: {correct_answers}/{len(alphabet)}\n")

# Función principal para mostrar el menú de idiomas
def main():
    print("Bienvenido a la práctica de alfabetos multilingües")
    print("Idiomas disponibles:")
    languages = list(alphabets.keys())
    for idx, lang in enumerate(languages, start=1):
        print(f"{idx}. {lang}")

    choice = input("Selecciona un idioma ingresando su número: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(languages):
        selected_language = languages[int(choice) - 1]
        practice_alphabet(selected_language)
    else:
        print("Selección inválida. Inténtalo nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
