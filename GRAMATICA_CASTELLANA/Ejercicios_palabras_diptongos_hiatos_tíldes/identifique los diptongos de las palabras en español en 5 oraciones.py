def identificar_diptongos(oracion):
    vocales_fuertes = "aeo"
    vocales_suaves = "iu"
    diptongos = ["ai", "ei", "oi", "ui", "au", "eu", "iu", "ay", "ey", "oy", "uy", "aí", "eí", "oí"]

    palabras = oracion.split()

    print(f"\nOración: {oracion}")
    print("Diptongos encontrados:")

    for palabra in palabras:
        for diptongo in diptongos:
            if diptongo in palabra.lower():
                print(f"{diptongo.capitalize()} en la palabra '{palabra}'")

def main():
    oraciones = [
        "La lluvia cae suavemente sobre el tejado.",
        "Esa melodía me hace recordar tiempos pasados.",
        "Las aves vuelan alto en el cielo azul.",
        "El río serpentea entre las colinas verdes.",
        "Tú y yo compartimos momentos inolvidables."
    ]

    for oracion in oraciones:
        identificar_diptongos(oracion)

if __name__ == "__main__":
    main()
