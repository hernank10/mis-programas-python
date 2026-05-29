import random

# Lista de palabras para usar en las frases
palabras = ["gato", "sol", "risa", "aventura", "amigo", "chocolate"]

def obtener_sinonimo(palabra):
    # Aquí podrías usar un diccionario o una API de sinónimos para obtener sinónimos
    # Por simplicidad, elegiré sinónimos aleatorios de una lista predefinida
    sinonimos = {
        "gato": ["felino", "minino", "michino"],
        "sol": ["astro", "luminoso", "brillante"],
        "risa": ["carcajada", "risotada", "sonrisa"],
        "aventura": ["viaje", "excursión", "odisea"],
        "amigo": ["compañero", "camarada", "aliado"],
        "chocolate": ["dulce", "cacao", "bombón"]
    }
    return random.choice(sinonimos.get(palabra, [palabra]))

def main():
    print("¡Inventa frases divertidas y originales!")
    while True:
        palabra_elegida = random.choice(palabras)
        sinonimo = obtener_sinonimo(palabra_elegida)
        frase = input(f"Inventa una frase con la palabra '{palabra_elegida}' (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            break
        frase_con_sinonimo = frase.replace(palabra_elegida, sinonimo)
        print(f"¡Buena elección! Tu frase con un sinónimo es: '{frase_con_sinonimo}'")

if __name__ == "__main__":
    main()
