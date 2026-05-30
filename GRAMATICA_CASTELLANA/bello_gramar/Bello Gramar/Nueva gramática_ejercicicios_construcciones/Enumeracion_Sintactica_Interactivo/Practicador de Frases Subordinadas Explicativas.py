import random

# Base de datos de ejemplos organizados por categorías
ejemplos = {
    "que": [
        {
            "principal": "El nuevo parque de la ciudad fue inaugurado ayer",
            "subordinada": "que cuenta con áreas verdes y un lago artificial",
            "antecedente": "parque"
        },
        # ... (más ejemplos de "que")
    ],
    "quien": [
        {
            "principal": "La actriz principal recibió una ovación",
            "subordinada": "quien interpretó un papel desgarrador",
            "antecedente": "actriz"
        },
        # ... (más ejemplos de "quien")
    ],
    "cuyo": [
        {
            "principal": "La universidad pública anunció una huelga",
            "subordinada": "cuyos estudiantes exigen mayor presupuesto",
            "antecedente": "universidad"
        },
        # ... (más ejemplos de "cuyo")
    ],
    "nominal": [
        {
            "principal": "Los agricultores cosecharon café",
            "subordinada": "producto que representa el 30% de las exportaciones",
            "antecedente": "café"
        },
        # ... (más ejemplos nominales)
    ]
}

# Cuestionario conceptual
def cuestionario_conceptual():
    preguntas = [
        {
            "pregunta": "¿A qué elemento de la frase principal debe referirse la subordinada explicativa?",
            "opciones": ["Al verbo", "Al primer sustantivo", "Al último sustantivo"],
            "respuesta": 2
        },
        {
            "pregunta": "¿Cómo se separa la subordinada explicativa de la principal?",
            "opciones": ["Con punto", "Con comas", "Sin signos"],
            "respuesta": 1
        }
    ]
    
    print("¡Cuestionario Conceptual! Responde las siguientes preguntas:")
    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {pregunta['pregunta']}")
        for j, opcion in enumerate(pregunta['opciones']):
            print(f"{j+1}. {opcion}")
        respuesta = int(input("Tu respuesta (número): ")) - 1
        if respuesta == pregunta['respuesta']:
            print("✅ Correcto")
        else:
            print(f"❌ Incorrecto. La respuesta es: {pregunta['opciones'][pregunta['respuesta']]}")

# Ejercicio práctico
def practica_subordinadas():
    print("\n¡Ejercicio Práctico! Completa la frase con una subordinada explicativa.")
    categoria = random.choice(list(ejemplos.keys()))
    ejemplo = random.choice(ejemplos[categoria])
    
    print(f"\nFrase principal: {ejemplo['principal']}")
    subordinada = input("Escribe la subordinada explicativa (incluye comas si es necesario): ").strip()
    
    # Validar comas
    if not (subordinada.startswith(", ") and subordinada.endswith(".")):
        print("⚠️ Recuerda: La subordinada debe empezar con coma y terminar con punto. Ej: ', que...'")
    
    # Validar antecedente
    if ejemplo['antecedente'].lower() not in subordinada.lower():
        print(f"⚠️ El antecedente debe ser '{ejemplo['antecedente']}'. Revisa tu subordinada.")
    
    # Validar conector
    if categoria not in subordinada.lower():
        print(f"⚠️ Usa un conector de la categoría '{categoria}' (ej: {ejemplo['subordinada'].split()[0]})")
    
    # Mostrar respuesta correcta
    print(f"\nRespuesta sugerida: {ejemplo['principal']}, {ejemplo['subordinada']}.")

# Función principal
def main():
    print("""
    ¡Bienvenido al Practicador de Frases Subordinadas Explicativas!
    ------------------------------------------------------------
    1. Cuestionario conceptual
    2. Practicar con ejemplos
    3. Salir
    """)
    
    while True:
        opcion = input("Elige una opción (1-3): ")
        if opcion == "1":
            cuestionario_conceptual()
        elif opcion == "2":
            practica_subordinadas()
        elif opcion == "3":
            print("¡Hasta luego! 😊")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
