import random

# Lista de reglas y sus respuestas
reglas = {
    "Antes de 'e' e 'i', generalmente se escribe 'g':": "geografía, germen, ginecología",
    "Antes de 'a', 'o' y 'u', generalmente se escribe 'g':": "gato, goma, gusto",
    "Al inicio de palabra o después de consonante, se escribe 'j':": "jarrón, lejos, caja",
    # Agrega más reglas aquí
}

def jugar():
    while True:
        # Seleccionar una regla al azar
        regla, respuesta = random.choice(list(reglas.items()))

        print(regla)
        respuesta_usuario = input("Escribe ejemplos: ")

        if respuesta_usuario.lower() == respuesta.lower():
            print("¡Correcto! ¡Muy bien!")
        else:
            print("No es correcto. La respuesta correcta es:", respuesta)

        # Preguntar si quiere continuar
        continuar = input("¿Quieres seguir practicando? (si/no): ")
        if continuar.lower() != 'si':
            break

if __name__ == "__main__":
    jugar()
