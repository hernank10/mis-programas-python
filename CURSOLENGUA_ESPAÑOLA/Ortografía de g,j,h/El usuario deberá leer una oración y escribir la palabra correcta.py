def practicar_homofonos():
    homofonos = [
        ("Agito", "batir algo"),
        ("Ajito", "diminutivo de la planta de ajo"),
        ("Gira", "girar un objeto"),
        ("Jira", "excursión campestre"),
        ("Giron", "gallo de un color giro"),
        ("Jirón", "jalón de tela"),
        ("Gigote", "guisado de carne picada rehogada en manteca"),
        ("Jigote", "pierna de cordero guisada"),
    ]

    print("¡Bienvenido! Vamos a practicar los homófonos con 'g' y 'j'.")
    print("Lee la oración y escribe la palabra correcta según el contexto:")

    for palabra, definicion in homofonos:
        oracion = input(f"Oración: {definicion}: ")
        if oracion.lower() == palabra.lower():
            print("¡Correcto! ¡Sigue así!")
        else:
            print(f"La palabra correcta era '{palabra}'. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    practicar_homofonos()
