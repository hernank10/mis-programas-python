def hacer_pregunta(regla):
    # Genera una pregunta basada en la regla
    # Por ejemplo, para la regla "La 'i' generalmente representa un sonido vocal cerrado anterior."
    pregunta = "¿Cuál es el sonido que generalmente representa la letra 'i'?"
    return pregunta

# ... (resto del código)

for regla in reglas:
    print(regla)
    respuesta = input(hacer_pregunta(regla))
    # Verificar si la respuesta es correcta
