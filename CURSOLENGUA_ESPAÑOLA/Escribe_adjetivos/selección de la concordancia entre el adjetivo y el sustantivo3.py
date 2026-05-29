texto = input("Ingresa un texto: ")
palabras = texto.split()
adjetivos = []

for i in range(len(palabras)):
    if palabras[i].endswith("o") or palabras[i].endswith("a"):
        if i < len(palabras) - 1 and palabras[i+1].endswith("o") or palabras[i+1].endswith("a"):
            adjetivos.append(palabras[i] + " " + palabras[i+1])

if len(adjetivos) == 0:
    print("No hay concordancia entre adjetivo y sustantivo en el texto.")
elif len(adjetivos) == 1:
    print("La concordancia entre adjetivo y sustantivo es:")
    print(adjetivos[0])
else:
    print("Las concordancias entre adjetivo y sustantivo son:")
    for adjetivo in adjetivos:
        print(adjetivo)
