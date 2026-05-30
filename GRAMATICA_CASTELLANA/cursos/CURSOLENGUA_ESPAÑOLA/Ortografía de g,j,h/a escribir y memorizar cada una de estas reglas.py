import time

# Lista de reglas con ejemplos
rules = [
    {
        "rule": "La letra g se usa antes de las vocales e e i.",
        "examples": ["gente", "gesto", "girar", "gigante"]
    },
    {
        "rule": "Terminaciones -gen, -gélico, -gético, -genario.",
        "examples": ["origen", "angélico", "energético", "sexagenario"]
    },
    {
        "rule": "Terminaciones -gia, -gio, -gión.",
        "examples": ["magia", "litigio", "religión"]
    },
    {
        "rule": "Sufijos -logía y -gógico.",
        "examples": ["biología", "pedagógico"]
    },
    {
        "rule": "Palabras que empiezan con geo-, gest-, gen-.",
        "examples": ["geografía", "gestión", "general"]
    },
    {
        "rule": "La letra j se usa antes de las vocales a, o, u.",
        "examples": ["jamón", "joven", "jugar"]
    },
    {
        "rule": "Terminaciones -aje, -eje.",
        "examples": ["traje", "viaje", "coraje", "releje"]
    },
    {
        "rule": "Verbos terminados en -jar, -jear.",
        "examples": ["trabajar", "teclear"]
    },
    {
        "rule": "Formas verbales que terminan en -je, -ja, -jo, -ju.",
        "examples": ["dije", "dijiste", "trajeron", "condujeron"]
    },
    {
        "rule": "Palabras que empiezan con eje-, aje-, adje-.",
        "examples": ["ejemplo", "ajeno", "adjetivo"]
    }
]

def main():
    print("Bienvenido al programa para memorizar las reglas del uso de la G y la J en español.")
    time.sleep(1)

    for idx, rule in enumerate(rules):
        print(f"\nRegla {idx + 1}: {rule['rule']}")
        time.sleep(1)
        
        user_input = input("Escribe la regla que acabas de leer: ").strip()
        
        if user_input.lower() == rule['rule'].lower():
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La regla correcta es: {rule['rule']}")
        
        print("Ejemplos:", ", ".join(rule['examples']))
        time.sleep(2)

if __name__ == "__main__":
    main()
