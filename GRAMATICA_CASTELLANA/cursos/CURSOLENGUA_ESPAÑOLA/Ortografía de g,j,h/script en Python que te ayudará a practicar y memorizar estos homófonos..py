import time

# Lista de homófonos con ejemplos
homophones = [
    {
        "words": ["gira", "jira"],
        "examples": {
            "gira": "La tierra gira alrededor del sol.",
            "jira": "Durante la jira, visitamos varios pueblos."
        }
    },
    {
        "words": ["gesto", "jesto"],
        "examples": {
            "gesto": "Hizo un gesto de aprobación.",
            "jesto": "El jesto del rey fue recordado."
        }
    },
    {
        "words": ["genio", "jenio"],
        "examples": {
            "genio": "Einstein era un genio de la física.",
            "jenio": "Jenio fue un sabio en la antigüedad."
        }
    },
    {
        "words": ["gente", "jente"],
        "examples": {
            "gente": "La gente está esperando.",
            "jente": "Jente era una palabra usada en documentos antiguos."
        }
    },
    {
        "words": ["gestión", "jestión"],
        "examples": {
            "gestión": "La gestión del proyecto fue excelente.",
            "jestión": "En textos antiguos, se encuentra la palabra jestión."
        }
    },
    {
        "words": ["genero", "jenero"],
        "examples": {
            "genero": "Genero electricidad con paneles solares.",
            "jenero": "Jenero es una ortografía incorrecta."
        }
    },
    {
        "words": ["general", "jeneral"],
        "examples": {
            "general": "El general dirigió la operación.",
            "jeneral": "Jeneral es una ortografía incorrecta."
        }
    },
    {
        "words": ["gentil", "jentil"],
        "examples": {
            "gentil": "El anfitrión fue muy gentil.",
            "jentil": "Jentil es una ortografía incorrecta."
        }
    }
]

def main():
    print("Bienvenido al programa para memorizar homófonos con G y J en español.")
    time.sleep(1)

    for pair in homophones:
        for word, sentence in pair['examples'].items():
            print(f"\nOración: {sentence}")
            user_input = input("Escribe la palabra correcta o la oración completa: ").strip()
            
            if user_input.lower() == word.lower() or user_input.lower() == sentence.lower():
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La palabra correcta es: {word}")
                print(f"La oración correcta es: {sentence}")

        time.sleep(2)

if __name__ == "__main__":
    main()
