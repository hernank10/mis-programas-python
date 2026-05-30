def verificar_uso(texto):
    if "porqué" in texto and "el porqué" in texto:
        return "Correcto: Has usado 'porqué' como un sustantivo."
    elif "por qué" in texto and "por qué" in texto:
        return "Correcto: Has usado 'por qué' en una pregunta o exclamación."
    else:
        return "Incorrecto: Revisa el uso de 'porqué' y 'por qué'."

def main():
    print("Programa para practicar el uso de 'porqué' y 'por qué'")
    print("Escribe una oración usando 'porqué' como un sustantivo:")
    oracion_1 = input("Oración 1: ")
    feedback_1 = verificar_uso(oracion_1)
    
    print("Escribe una oración usando 'por qué' en una pregunta o exclamación:")
    oracion_2 = input("Oración 2: ")
    feedback_2 = verificar_uso(oracion_2)
    
    print("\nRetroalimentación:")
    print(f"Oración 1: {feedback_1}")
    print(f"Oración 2: {feedback_2}")

if __name__ == "__main__":
    main()
