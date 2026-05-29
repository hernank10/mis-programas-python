import random

# Diccionario con las reglas de flexión (puedes agregar más)
reglas_flexion = {
    "género": "Los sustantivos pueden ser masculinos o femeninos.",
    "número": "Los sustantivos y adjetivos pueden ser singulares o plurales.",
    "tiempo_presente": "El presente de indicativo se utiliza para acciones que ocurren en el momento de hablar.",
    # Agrega aquí más reglas de flexión
}

def preguntar_regla(regla):
    print(f"Escribe la regla de {regla}:")
    respuesta = input()
    if respuesta.lower() == reglas_flexion[regla].lower():
        print("¡Correcto! ¡Muy bien!")
    else:
        print(f"Incorrecto. La regla correcta es: {reglas_flexion[regla]}")

def iniciar_aprendizaje():
    while True:
        regla = random.choice(list(reglas_flexion.keys()))
        preguntar_regla(regla)

        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    print("¡Bienvenido al tutor de reglas de flexión!")
    iniciar_aprendizaje()
