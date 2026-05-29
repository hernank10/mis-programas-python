def identificar_diptongos(parrafo):
    vocales_fuertes = "aeo"
    vocales_suaves = "iu"
    diptongos = ["ai", "ei", "oi", "ui", "au", "eu", "iu", "ay", "ey", "oy", "uy", "aí", "eí", "oí"]

    palabras = parrafo.split()

    print(f"\nParrafo: {parrafo}")
    print("Diptongos encontrados:")

    for palabra in palabras:
        for diptongo in diptongos:
            if diptongo in palabra.lower():
                print(f"{diptongo.capitalize()} en la palabra '{palabra}'")

def main():
    parrafo1 = "Era un día soleado en la playa. Las olas rompían suavemente en la orilla, mientras los niños jugaban en la arena."
    parrafo2 = "La música resonaba en el viejo teatro. La actriz recitaba sus líneas con emoción, mientras el público permanecía atento."

    identificar_diptongos(parrafo1)
    identificar_diptongos(parrafo2)

if __name__ == "__main__":
    main()
