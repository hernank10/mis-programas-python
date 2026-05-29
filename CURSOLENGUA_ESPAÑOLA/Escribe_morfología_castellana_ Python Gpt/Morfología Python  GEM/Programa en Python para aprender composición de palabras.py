import random

# Diccionario con las reglas de composición (puedes agregar más)
reglas_composicion = {
    "sustantivo+sustantivo": "Se unen dos sustantivos para formar uno nuevo (bocacalle, girasol).",
    "adjetivo+sustantivo": "Se une un adjetivo y un sustantivo (verdemar, agridulce).",
    "verbo+sustantivo": "Se une un verbo y un sustantivo (abrelatas, quitaesmalte).",
    # Agrega aquí más reglas de composición
}

def preguntar_regla(regla):
    print(f"Escribe la regla de {regla}:")
    respuesta = input()
    if respuesta.lower() == reglas_composicion[regla].lower():
        print("¡Correcto! ¡Muy bien!")
    else:
        print(f"Incorrecto. La regla correcta es: {reglas_composicion[regla]}")

def iniciar_aprendizaje():
    while True:
        regla = random.choice(list(reglas_composicion.keys()))
        preguntar_regla(regla)

        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    print("¡Bienvenido al tutor de reglas de composición en español!")
    iniciar_aprendizaje()
