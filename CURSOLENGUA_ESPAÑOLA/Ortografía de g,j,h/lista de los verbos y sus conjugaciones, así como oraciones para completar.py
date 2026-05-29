import time

# Lista de oraciones con huecos para completar
sentences = [
    {"verb": "infringir", "sentence": "No debemos ____(infringir) las reglas del juego."},
    {"verb": "acoger", "sentence": "Ella me ____(acoger) en su casa con amabilidad."},
    {"verb": "afligir", "sentence": "La noticia me ____(afligir) profundamente."},
    {"verb": "escoger", "sentence": "¿Cuál libro vas a ____(escoger)?"},
    {"verb": "fingir", "sentence": "No es bueno ____(fingir) emociones."},
    {"verb": "encoger", "sentence": "El gato se ____(encoger) de miedo."},
    {"verb": "elegir", "sentence": "Debes ____(elegir) sabiamente."},
    {"verb": "dirigir", "sentence": "Yo ____(dirigir) el proyecto con mi equipo."},
    {"verb": "proteger", "sentence": "Es importante ____(proteger) el medio ambiente."},
    {"verb": "recoger", "sentence": "Vamos a ____(recoger) la basura del parque."}
]

# Función principal
def main():
    print("Bienvenido al programa para practicar la mutación ortográfica de verbos terminados en -ger y -gir.")
    time.sleep(1)

    for entry in sentences:
        sentence = entry["sentence"]
        correct_verb = entry["verb"]

        print(f"\nOración: {sentence}")
        user_input = input("Completa la oración con la forma correcta del verbo: ").strip()

        if correct_verb in user_input:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La forma correcta es: {correct_verb}.")

        time.sleep(1)

    print("\nAhora vamos a practicar la adición de g, gu, o gü en oraciones.")
    additional_practice = [
        "Voy a ____(jugar) al fútbol.",
        "Vamos a ____(seguir) adelante.",
        "Debes ____(guerrear) con valor.",
        "Voy a ____(pedir) un poco de agua.",
        "Tienes que ____(averiguar) la verdad.",
        "Vamos a ____(freír) el pescado.",
        "Voy a ____(pagar) la cuenta.",
        "El perro se ____(vagar) por el jardín.",
        "Necesitas ____(recoger) la ropa.",
        "Ella va a ____(colgar) el teléfono."
    ]

    for sentence in additional_practice:
        print(f"\nOración: {sentence}")
        user_input = input("Completa la oración con la forma correcta: ").strip()

        # No hay respuestas específicas correctas aquí, así que aceptamos cualquier entrada
        print("Gracias por completar la oración.")

        time.sleep(1)

if __name__ == "__main__":
    main()
