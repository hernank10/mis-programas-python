import random

def solicitar_frases(palabras):
    print("Inventa frases: Utiliza las siguientes palabras para crear frases divertidas y originales:")
    for palabra in palabras:
        frase = input(f"Usa la palabra '{palabra}' en una frase: ")
        print(f"Tu frase: {frase}")
    print("\n¡Gracias por tus frases!")

def buscar_sinonimos(palabras):
    sinonimos = {
        "acción": ["movimiento", "actividad", "operación"],
        "canción": ["melodía", "tema", "composición"],
        "naciente": ["emergente", "incipiente", "inicial"],
        "cercar": ["rodear", "acotar", "encerrar"],
        "circulo": ["anillo", "aro", "círculo"]
    }
    print("Busca sinónimos: Encuentra palabras que tengan un significado similar a las que ya conoces.")
    for palabra in palabras:
        if palabra in sinonimos:
            print(f"Palabra: {palabra}")
            for sinonimo in sinonimos[palabra]:
                print(f"  - Sinónimo: {sinonimo}")
    print("\n¡Eso es todo con los sinónimos!")

def jugar_con_palabras():
    trabalenguas = [
        "Tres tristes tigres tragaban trigo en un trigal.",
        "Pablito clavó un clavito en la calva de un calvito.",
        "El cielo está enladrillado, ¿quién lo desenladrillará?"
    ]
    rimas = [
        "El gato en el tejado, con su maullido se ha expresado.",
        "La luna brilla en el cielo, iluminando todo el suelo.",
        "La lluvia cae sin cesar, refrescando el lugar."
    ]
    adivinanzas = [
        "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera. (La pera)",
        "Oro parece, plata no es. ¿Qué es? (El plátano)",
        "Me pelo para que no me puedan pelar. (El plátano)"
    ]

    print("Juega con las palabras:")
    print("Trabalinguas:")
    print(random.choice(trabalenguas))
    
    print("\nRimas:")
    print(random.choice(rimas))
    
    print("\nAdivinanzas:")
    print(random.choice(adivinanzas))
    print("\n¡Diviértete jugando con las palabras!")

# Lista de palabras que siguen las reglas del uso de la letra C
palabras_lista = ["acción", "canción", "naciente", "cercar", "circulo"]

# Ejecutar las funciones
solicitar_frases(palabras_lista)
buscar_sinonimos(palabras_lista)
jugar_con_palabras()
