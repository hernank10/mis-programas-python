import time

# Lista de reglas con ejemplos
rules = [
    {
        "rule": "La letra g se usa antes de las vocales e e i.",
        "examples": ["gente", "gesto", "girar", "gigante", "germen", "general", "género", "geografía", "geometría", "gimnasia"]
    },
    {
        "rule": "Terminaciones -gen, -gélico, -gético, -genario.",
        "examples": ["origen", "imagen", "oxígeno", "vigésimo", "energúmeno", "diabético", "angélico", "energético", "sexagenario", "octogenario"]
    },
    {
        "rule": "Terminaciones -gia, -gio, -gión.",
        "examples": ["magia", "geología", "teología", "energía", "liturgia", "litigo", "prestigio", "religión", "región", "legislador"]
    },
    {
        "rule": "Sufijos -logía y -gógico.",
        "examples": ["biología", "psicología", "tecnología", "arqueología", "ecología", "dermatología", "pedagógico", "demagógico", "teológico", "filosófico"]
    },
    {
        "rule": "Palabras que empiezan con geo-, gest-, gen-.",
        "examples": ["geografía", "geometría", "geología", "gestión", "gesticular", "gesto", "general", "generación", "genético", "gentil"]
    },
    {
        "rule": "La letra j se usa antes de las vocales a, o, u.",
        "examples": ["jamón", "jarra", "jarrón", "joven", "jornada", "jugar", "júbilo", "juicio", "juntar", "justicia"]
    },
    {
        "rule": "Terminaciones -aje, -eje.",
        "examples": ["viaje", "traje", "lenguaje", "coraje", "drenaje", "mensaje", "garaje", "personaje", "paisaje", "pasaje"]
    },
    {
        "rule": "Verbos terminados en -jar, -jear.",
        "examples": ["trabajar", "teclear", "dibujar", "viajar", "empujar", "dejar", "alojar", "manejar", "reflejar", "festejar"]
    },
    {
        "rule": "Formas verbales que terminan en -je, -ja, -jo, -ju.",
        "examples": ["dije", "trajiste", "condujo", "dejé", "reflejé", "empujé", "corregí", "fijé", "tejer", "dibujó"]
    },
    {
        "rule": "Palabras que empiezan con eje-, aje-, adje-.",
        "examples": ["ejemplo", "ejercer", "ejecución", "ajeno", "ajedrez", "ajedrecista", "ajustar", "ajuste", "adjetivo", "adjetivar"]
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
