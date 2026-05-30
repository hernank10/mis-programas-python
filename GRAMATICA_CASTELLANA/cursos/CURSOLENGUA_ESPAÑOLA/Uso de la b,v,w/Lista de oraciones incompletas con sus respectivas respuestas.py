import random

# Lista de oraciones incompletas con sus respectivas respuestas
homofonos_oraciones = [
    ("El niño _____ la pelota muy lejos.", "botar"),
    # ... (agrega el resto de las oraciones)
]

def practicar_homofonos():
    """Función para practicar las parejas de homófonos."""
    puntaje = 0
    total_preguntas = len(homofonos_oraciones)

    print("¡Vamos a practicar homófonos! Escribe la palabra que complete la oración.")

    while homofonos_oraciones:
        oracion, respuesta_correcta = random.choice(homofonos_oraciones)
        respuesta_usuario = input(oracion + " ")
        if respuesta_usuario.lower() == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        homofonos_oraciones.remove((oracion, respuesta_correcta))

    print(f"¡Has terminado! Tu puntaje es: {puntaje}/{total_preguntas}")

if __name__ == "__main__":
    practicar_homofonos()
