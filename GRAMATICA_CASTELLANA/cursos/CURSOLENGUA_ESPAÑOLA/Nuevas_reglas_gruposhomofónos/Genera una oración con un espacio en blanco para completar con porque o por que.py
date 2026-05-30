import random

def generar_oracion():
    """Genera una oración con un espacio en blanco para completar con "porque" o "por que".

    Returns:
        str: La oración a completar.
    """

    # Lista de oraciones base con un espacio en blanco
    oraciones = [
        "No fui a la fiesta _____ estaba cansado.",
        "La razón _____ no contestó el teléfono es desconocida.",
        "Me gusta el helado de chocolate _____ es delicioso.",
        "El camino _____ llegamos a la casa estaba lleno de baches.",
        "El libro _____ estoy leyendo es muy interesante.",
    ]

    # Seleccionar una oración aleatoria y devolverla
    return random.choice(oraciones)

def corregir_respuesta(oracion, respuesta_usuario):
    """Compara la respuesta del usuario con la respuesta correcta.

    Args:
        oracion (str): La oración a completar.
        respuesta_usuario (str): La respuesta del usuario.

    Returns:
        bool: True si la respuesta es correcta, False si no.
    """

    # Aquí se definiría la lógica para determinar la respuesta correcta 
    # basándose en el contexto de la oración.

    # Ejemplo simplificado:
    if "razón" in oracion:
        respuesta_correcta = "por que"
    else:
        respuesta_correcta = "porque"

    return respuesta_usuario == respuesta_correcta

def jugar():
    """Función principal del juego."""

    puntaje = 0
    num_preguntas = 5

    for _ in range(num_preguntas):
        oracion = generar_oracion()
        print(oracion)
        respuesta = input("Completa la oración con 'porque' o 'por que': ")

        if corregir_respuesta(oracion, respuesta):
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto. La respuesta correcta era:", respuesta_correcta)

    print("Tu puntaje final es:", puntaje)

if __name__ == "__main__":
    jugar()
