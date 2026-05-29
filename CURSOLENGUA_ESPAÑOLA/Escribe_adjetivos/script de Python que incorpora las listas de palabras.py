import random

# Diccionario con reglas y listas de palabras de ejemplo
reglas = {
    "Antes de 'e' e 'i', generalmente se escribe 'g':": ["geografía", "geología", "geometría", "génesis", "magia", "región", "legítimo", "legión", "legislador", "ingeniero"],
    "Antes de 'a', 'o' y 'u', generalmente se escribe 'g':": ["gato", "goma", "gusto", "agua", "aguja", "ángulo", "gato", "goma", "gusto", "agua"],
    "Al inicio de palabra o después de consonante, se escribe 'j':": ["jarrón", "jefe", "jaula", "caja", "lejos", "rojo", "tarjeta", "sujetador", "reloj", "ajeno"],
    "J en algunos verbos (-jar, -jer, -jir):": ["cajar", "trabajar", "jugar", "tejer", "ejercer", "crujir", "cojear", "bujía", "trazar", "rozar"],
    "J en algunos adjetivos y sustantivos (-jero, -jera, -jería):": ["panadero", "cartero", "librero", "lechera", "costurera", "joyería", "ferretería", "carnicería", "cerrajero", "relojería"]
}

def jugar():
    while True:
        regla, palabras = random.choice(list(reglas.items()))

        print(regla)

        # Mezclar las palabras para variar el orden
        random.shuffle(palabras)

        print("Escribe 5 palabras de ejemplo:")

        correctas = 0
        for i in range(5):
            respuesta_usuario = input(f"{i+1}. ")
            if respuesta_usuario.lower() in palabras:
                print("¡Correcto!")
                correctas += 1
            else:
                print("Incorrecto. Intenta otra vez.")

        print(f"Has acertado {correctas} de 5 palabras.")

        # Preguntar si quiere continuar
        continuar = input("¿Quieres seguir practicando? (si/no): ")
        if continuar.lower() != 'si':
            break

if __name__ == "__main__":
    jugar()
