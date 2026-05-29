import random

palabras = ["el", "mas", "mi", "si", "tu", "mas", "te", "ya", "de", "se"]

acentos = {"el": "él", "mas": "más", "mi": "mí", "si": "sí", "tu": "tú", "te": "té", "ya": "yá", "de": "dé", "se": "sé"}

print("Identifica la palabra homónima o polisémica en cada oración:")

for i in range(10):
    palabra = random.choice(palabras)
    print(f"{i+1}. La palabra {palabra} es {palabra.upper()}.")

respuestas = []
for i in range(10):
    respuesta = input(f"{i+1}. Escribe la palabra homónima o polisémica: ")
    if respuesta.lower() == acentos[palabras[i]].lower():
        print("¡Correcto!")
        respuestas.append(True)
    else:
        print("Incorrecto.")
        respuestas.append(False)

print("Retroalimentación:")
for i in range(10):
    if respuestas[i]:
        print(f"{i+1}. La palabra {palabras[i]} es {palabras[i].upper()}: Correcto")
    else:
        print(f"{i+1}. La palabra {palabras[i]} es {palabras[i].upper()}: Incorrecto")
