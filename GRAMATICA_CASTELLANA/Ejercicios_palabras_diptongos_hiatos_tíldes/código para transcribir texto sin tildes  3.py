import re

palabras = ["casa", "camino", "pajaro", "lapiz", "telefono", "libro", "pelicula", "television", "computadora", "escuela", "jardin", "guitarra", "perro", "gato", "raton", "caballo", "elefante", "tigre", "leon", "cocodrilo", "serpiente", "aguila", "pajaro", "pez", "ballena"]

acentos = {"casa": "casa", "camino": "camino", "pajaro": "pájaro", "lapiz": "lápiz", "telefono": "teléfono", "libro": "libro", "pelicula": "película", "television": "televisión", "computadora": "computadora", "escuela": "escuela", "jardin": "jardín", "guitarra": "guitarra", "perro": "perro", "gato": "gato", "raton": "ratón", "caballo": "caballo", "elefante": "elefante", "tigre": "tigre", "leon": "león", "cocodrilo": "cocodrilo", "serpiente": "serpiente", "aguila": "águila", "pajaro": "pájaro", "pez": "pez", "ballena": "ballena"}

print("Lee el siguiente fragmento de texto sin tildes y transcribe correctamente las palabras con tilde:")

texto = "El telefono sonó y el pajaro salió volando por la ventana. El camino hacia la casa era largo y peligroso. El lapiz y el libro estaban sobre la mesa. La pelicula que vimos ayer en la television fue muy interesante. La computadora de la escuela es muy moderna. El jardin de la casa es muy bonito. La guitarra del músico sonaba muy bien. El perro y el gato jugaban con el raton. El caballo y el elefante estaban en el circo. El tigre y el leon son animales salvajes. El cocodrilo y la serpiente viven en el río. El águila y el pájaro vuelan muy alto. El pez y la ballena viven en el mar."

print(texto)

respuestas = []
for i in range(len(palabras)):
    respuesta = input(f"{i+1}. Escribe la palabra: ")
    if respuesta.lower() == acentos[palabras[i]].lower():
        print("¡Correcto!")
        respuestas.append(True)
    else:
        print("Incorrecto.")
        respuestas.append(False)

print("Retroalimentación:")
for i in range(len(palabras)):
    if respuestas[i]:
        print(f"{i+1}. {palabras[i]}: Correcto")
    else:
        print(f"{i+1}. {palabras[i]}: Incorrecto")
