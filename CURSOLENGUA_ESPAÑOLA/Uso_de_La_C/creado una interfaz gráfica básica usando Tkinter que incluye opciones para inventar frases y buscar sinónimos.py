import tkinter as tk
import random

# Lista de palabras y sus sinónimos (puedes expandir esta lista)
palabras = {
    "rápido": ["veloz", "ligero", "presto"],
    "feliz": ["contento", "alegre", "gozoso"],
    "grande": ["enorme", "gigante", "colosal"],
    "pequeño": ["minúsculo", "diminuto", "chico"],
    "inteligente": ["sabio", "ingenioso", "listo"]
}

# Función para inventar frases
def inventar_frases():
    palabra = random.choice(list(palabras.keys()))
    frase = input(f"Inventa una frase con la palabra '{palabra}': ")
    print(f"Tu frase: {frase}")

# Función para buscar sinónimos
def buscar_sinonimos():
    palabra = random.choice(list(palabras.keys()))
    print(f"Palabra: {palabra}")
    print("Sinónimos:")
    for sinonimo in palabras[palabra]:
        print(f"  - {sinonimo}")

# Función para crear interfaz gráfica con Tkinter
def crear_interfaz():
    root = tk.Tk()
    root.title("Juego de Palabras")
    
    label = tk.Label(root, text="Bienvenido al Juego de Palabras", font=("Helvetica", 16))
    label.pack(pady=20)
    
    btn_frases = tk.Button(root, text="Inventa Frases", command=inventar_frases)
    btn_frases.pack(pady=10)
    
    btn_sinonimos = tk.Button(root, text="Buscar Sinónimos", command=buscar_sinonimos)
    btn_sinonimos.pack(pady=10)
    
    btn_jugar = tk.Button(root, text="Jugar con Palabras", command=jugar_con_palabras)
    btn_jugar.pack(pady=10)
    
    root.mainloop()

# Función para jugar con palabras
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

# Ejecutar la interfaz gráfica
crear_interfaz()
