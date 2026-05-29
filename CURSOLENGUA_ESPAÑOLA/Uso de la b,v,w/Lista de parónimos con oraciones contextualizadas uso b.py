import random

# Lista de parónimos con oraciones contextualizadas
paronimos = [
    ("El juez decidió **absolver** al acusado.", "absolver", "absorber"),
    ("Trata de **eludir** el tema cuando le preguntas sobre su pasado.", "eludir", "aludir"),
    # ... (agrega el resto de las oraciones con sus respectivos parónimos)
]

def practicar_paronimos():
    """Función para practicar pares de parónimos."""
    puntaje = 0
    total_preguntas = len(paronimos)

    print("¡Vamos a practicar parónimos! Elige la palabra correcta para completar la oración.")

    while paronimos:
        oracion, respuesta_correcta, alternativa = random.choice(paronimos)
        print(oracion)
        respuesta_usuario = input(f"Elige la palabra correcta: {respuesta_correcta} o {alternativa}? ")
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La palabra correcta era: {respuesta_correcta}")
            print(f"**{respuesta_correcta}** significa {obtener_definicion(respuesta_correcta)} y **{alternativa}** significa {obtener_definicion(alternativa)}.")
        paronimos.remove((oracion, respuesta_correcta, alternativa))

    print(f"¡Has terminado! Tu puntaje es: {puntaje}/{total_preguntas}")

def obtener_definicion(palabra):
    # Aquí puedes implementar una función para buscar la definición en un diccionario
    # o en una base de datos. Por ahora, puedes agregar las definiciones manualmente.
    # Ejemplo:
    definiciones = {
        "absolver": "perdonar",
        "absorber": "asimilar",
        # ... (agrega más definiciones)
    }
    return definiciones.get(palabra, "No se encontró la definición.")

if __name__ == "__main__":
    practicar_paronimos()
