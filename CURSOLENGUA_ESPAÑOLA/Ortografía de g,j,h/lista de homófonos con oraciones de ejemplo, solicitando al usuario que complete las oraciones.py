import random

homophones = {
    ("gira", "jira"): [
        "La Tierra ____ alrededor del Sol.",
        "Nos fuimos de ____ al campo."
    ],
    ("ingerir", "injerir"): [
        "El médico le indicó que ____ más frutas y verduras.",
        "El jardinero ____ nuevas ramas en el árbol."
    ],
    # Agrega más pares de homófonos y sus oraciones aquí
}

def jugar():
    print("¡Bienvenido a la práctica de homófonos con 'g' y 'j'!")

    for homophone_pair, sentences in homophones.items():
        print(f"\nHomófonos: {', '.join(homophone_pair)}")
        for sentence in sentences:
            print(sentence)
            user_answer = input("Escribe la palabra correcta: ")

            correct_answer = homophone_pair[0] if sentence.find(homophone_pair[0]) > -1 else homophone_pair[1]
            if user_answer.lower() == correct_answer.lower():
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La palabra correcta es: {correct_answer}")

if __name__ == "__main__":
    jugar()
