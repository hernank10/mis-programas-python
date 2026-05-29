import random

sustantivos = {
    "niño": {"plural": "niños", "diminutivo": "niñito", "aumentativo": "niñote"},
    "taxi": {"plural": "taxis", "diminutivo": "taxicito", "aumentativo": "taxizote"},
    "menú": {"plural": "menús", "diminutivo": "menucito", "aumentativo": "menuzote"},
    "piedra": {"plural": "piedras", "diminutivo": "piedrita", "aumentativo": "piedrota"},
    "clase": {"plural": "clases", "diminutivo": "clasita", "aumentativo": "clasona"},
    "sofá": {"plural": "sofás", "diminutivo": "sofacito", "aumentativo": "sofazote"},
    "rubí": {"plural": "rubíes", "diminutivo": "rubicito", "aumentativo": "rubizote"},
    "café": {"plural": "cafés", "diminutivo": "cafecito", "aumentativo": "cafezote"},
    "mamá": {"plural": "mamás", "diminutivo": "mamita", "aumentativo": "mamacita"},
    "papá": {"plural": "papás", "diminutivo": "papito", "aumentativo": "papazote"},
    "pez": {"plural": "peces", "diminutivo": "pececillo", "aumentativo": "pezote"},
    "lápiz": {"plural": "lápices", "diminutivo": "lapicito", "aumentativo": "lapizote"},
    "cruz": {"plural": "cruces", "diminutivo": "crucecita", "aumentativo": "cruzota"},
    "juez": {"plural": "jueces", "diminutivo": "juececillo", "aumentativo": "juezote"},
    "nariz": {"plural": "narices", "diminutivo": "naricita", "aumentativo": "narizota"},
    "flor": {"plural": "flores", "diminutivo": "florecita", "aumentativo": "florzota"},
    "amor": {"plural": "amores", "diminutivo": "amorcito", "aumentativo": "amorzote"},
    "color": {"plural": "colores", "diminutivo": "colorcito", "aumentativo": "colozote"},
    "tambor": {"plural": "tambores", "diminutivo": "tamborcito", "aumentativo": "tamborzote"},
    "atlas": {"plural": "atlas", "diminutivo": "(sin diminutivo frecuente)", "aumentativo": "(sin aumentativo frecuente)"},
    "cosmos": {"plural": "cosmos", "diminutivo": "(sin diminutivo frecuente)", "aumentativo": "(sin aumentativo frecuente)"},
    "lunes": {"plural": "lunes", "diminutivo": "lunesito", "aumentativo": "lunesote"},
    "tesis": {"plural": "tesis", "diminutivo": "tesecita", "aumentativo": "tesisota"},
    "virus": {"plural": "virus", "diminutivo": "virucito", "aumentativo": "virusote"},
    "crisis": {"plural": "crisis", "diminutivo": "crisecita", "aumentativo": "crisisota"},
}

def practicar():
    vidas = 3
    puntaje = 0
    while vidas > 0:
        palabra = random.choice(list(sustantivos.keys()))
        categoria = random.choice(["plural", "diminutivo", "aumentativo"])
        respuesta_usuario = input(f"¿Cuál es el {categoria} de '{palabra}'? ").strip()
        respuesta_correcta = sustantivos[palabra][categoria]
        if respuesta_usuario.lower() == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            vidas -= 1
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}. Te quedan {vidas} vidas.")
    print(f"Tu puntaje final es: {puntaje}")

if __name__ == "__main__":
    practicar()
