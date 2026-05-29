# -*- coding: utf-8 -*-
def main():
    niveles = {
        "semántico": {
            "ejemplo": "Sustantivo que nombre un fenómeno natural",
            "traduccion": "Noun that names a natural phenomenon",
            "respuesta_correcta": "tormenta",
            "análisis": "Los sustantivos designan entidades. 'Tormenta' nombra un fenómeno atmosférico."
        },
        "morfológico": {
            "ejemplo": "Deriva un adjetivo de 'oscuridad'",
            "traduccion": "Derive an adjective from 'oscuridad' (darkness)",
            "respuesta_correcta": "oscuro",
            "análisis": "Se elimina el sufijo '-idad' y se añade '-o' para formar el adjetivo."
        },
        "sintáctico": {
            "ejemplo": "Identifica el complemento directo: 'El chef preparó una cena'",
            "traduccion": "Identify the direct object: 'El chef preparó una cena' (The chef prepared a dinner)",
            "respuesta_correcta": "una cena",
            "análisis": "'Una cena' es el objeto directo de la acción 'preparó'."
        },
        "fonológico": {
            "ejemplo": "¿Cuántos fonemas tiene 'chocolate'? (solo número)",
            "traduccion": "How many phonemes does 'chocolate' have? (number only)",
            "respuesta_correcta": "7",
            "análisis": "/ch/o/c/o/l/a/te/ → 7 fonemas (en español, 'ch' es un solo fonema)."
        }
    }

    print("¡Bienvenido al Practicador Lingüístico Bilingüe! 🌍")
    print("Niveles disponibles: semántico, morfológico, sintáctico, fonológico\n")

    while True:
        nivel = input("Elige un nivel o escribe 'salir': ").lower()
        
        if nivel == "salir":
            print("¡Hasta luego! 😊")
            break
        
        if nivel not in niveles:
            print("❌ Nivel no válido. Intenta de nuevo.\n")
            continue
        
        data = niveles[nivel]
        print(f"\n*** Nivel {nivel.capitalize()} / Level: {nivel.capitalize()} ***")
        print(f"Ejercicio: {data['ejemplo']}")
        print(f"Translation: {data['traduccion']}\n")
        respuesta = input("Tu respuesta / Your answer: ").strip()
        
        if respuesta.lower() == data["respuesta_correcta"].lower():
            print("✅ ¡Correcto! / Correct!")
        else:
            print(f"❌ Incorrecto. La respuesta esperada era: {data['respuesta_correcta']}")
            print(f"❌ Incorrect. Expected answer: {data['respuesta_correcta']}")
        
        print(f"\nAnálisis / Analysis: {data['análisis']}\n")

if __name__ == "__main__":
    main()
