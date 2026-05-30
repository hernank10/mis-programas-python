import random

# Diccionario con las reglas de derivación (puedes agregar más)
reglas_derivacion = {
    "prefijos": "Los prefijos se añaden al principio de una palabra para modificar su significado.",
    "sufijos": "Los sufijos se añaden al final de una palabra para cambiar su categoría gramatical.",
    "prefijos_negativos": "Los prefijos como 'in-', 'des-', 'im-' suelen expresar negación.",
    "sufijos_sustantivos": "Los sufijos como '-dad', '-ción', '-miento' forman sustantivos.",
    # Agrega aquí más reglas de derivación
}

def preguntar_regla(regla):
    print(f"Escribe la regla de {regla}:")
    respuesta = input()
    if respuesta.lower() == reglas_derivacion[regla].lower():
        print("¡Correcto! ¡Muy bien!")
    else:
        print(f"Incorrecto. La regla correcta es: {reglas_derivacion[regla]}")

def iniciar_aprendizaje():
    while True:
        regla = random.choice(list(reglas_derivacion.keys()))
        preguntar_regla(regla)

        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    print("¡Bienvenido al tutor de reglas de derivación en español!")
    iniciar_aprendizaje()
