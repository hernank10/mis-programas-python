def obtener_fragmento_texto():
    fragmento_texto = (
        "La mañana despertó con un sol radiante. "
        "Los pájaros cantaban mientras el río fluía "
        "serpenteando por el valle."
    )
    return fragmento_texto

def identificar_palabras_con_prefijos(fragmento_texto):
    palabras = fragmento_texto.split()
    prefijos = ["des", "radi", "can", "flu", "serp"]

    print("\nFragmento de texto:")
    print(fragmento_texto)

    print("\nIdentifica palabras que contengan los siguientes prefijos:")

    for i in range(5):
        palabra_usuario = input(f"Palabra que contiene '{prefijos[i]}': ").strip().lower()

        palabras_con_prefijo = [palabra for palabra in palabras if prefijos[i] in palabra.lower()]

        if palabra_usuario in palabras_con_prefijo:
            print(f"¡Correcto! La palabra '{palabra_usuario}' contiene el prefijo '{prefijos[i]}'.")
        else:
            print(f"Incorrecto. La palabra '{palabra_usuario}' no contiene el prefijo '{prefijos[i]}'.")

def main_prefijos():
    fragmento_texto = obtener_fragmento_texto()
    identificar_palabras_con_prefijos(fragmento_texto)

if __name__ == "__main__":
    main_prefijos()
