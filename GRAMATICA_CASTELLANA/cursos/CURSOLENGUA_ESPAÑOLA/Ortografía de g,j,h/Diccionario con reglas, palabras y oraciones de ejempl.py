import random

# Diccionario con reglas, palabras y oraciones de ejemplo
reglas = {
    "Antes de 'e' e 'i', generalmente se escribe 'g':": [
        ("La **geografía** es la ciencia que estudia la Tierra.", "geografía"),
        ("El **germen** de la idea surgió en una reunión.", "germen"),
        # ... y así sucesivamente para las demás palabras
    ],
    # ... y las demás reglas con sus respectivas oraciones y palabras
}

def jugar():
    while True:
        regla, preguntas = random.choice(list(reglas.items()))

        print(regla)

        # Mezclar las preguntas para variar el orden
        random.shuffle(preguntas)

        for pregunta, respuesta in preguntas:
            print(pregunta)
            respuesta_usuario = input("Escribe la palabra correcta: ")
            if respuesta_usuario.lower() == respuesta.lower():
                print("¡Correcto!")
            else:
                print("Incorrecto. La palabra correcta es:", respuesta)

        # Preguntar si quiere continuar
        continuar = input("¿Quieres seguir practicando? (si/no): ")
        if continuar.lower() != 'si':
            break

if __name__ == "__main__":
    jugar()
