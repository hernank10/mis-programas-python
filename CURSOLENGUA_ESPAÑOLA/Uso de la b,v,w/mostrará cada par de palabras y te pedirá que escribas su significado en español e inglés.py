def main():
    homophones = [
        ("Baca", "Vaca"),
        # ... otros pares de palabras homófonas
    ]

    for b_word, v_word in homophones:
        print(f"¿Cuál es el significado de '{b_word}' en español e inglés?")
        b_meaning_es = input("Significado en español: ")
        b_meaning_en = input("Significado en inglés: ")

        if b_meaning_es.lower() == b_word.lower() and b_meaning_en.lower() == v_word.lower():
            print("¡Correcto! Sigue con el siguiente par.")
        else:
            print(f"Incorrecto. La respuesta correcta era: '{b_word}' significa '{v_word}'.")

if __name__ == "__main__":
    main()
