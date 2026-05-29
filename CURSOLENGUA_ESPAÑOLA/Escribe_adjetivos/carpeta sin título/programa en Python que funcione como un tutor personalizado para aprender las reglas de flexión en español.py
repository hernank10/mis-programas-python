import random

# Diccionario con las reglas de flexión (ejemplo)
reglas = {
    "género": "Los sustantivos pueden ser masculinos o femeninos.",
    "número": "Los sustantivos y adjetivos pueden ser singulares o plurales.",
    "tiempo_presente": "El presente de indicativo se utiliza para acciones que ocurren en el momento de hablar.",
    # ... agregar más reglas aquí
}

def preguntar_regla(regla):
    print(f"Escribe la regla de {regla}:")
    respuesta = input()
    if respuesta.lower() == reglas[regla].lower():
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La regla correcta es: {reglas[regla]}")

def iniciar_aprendizaje():
    while True:
        regla = random.choice(list(reglas.keys()))
        preguntar_regla(regla)

        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    print("¡Bienvenido al tutor de flexión en español!")
    iniciar_aprendizaje()
