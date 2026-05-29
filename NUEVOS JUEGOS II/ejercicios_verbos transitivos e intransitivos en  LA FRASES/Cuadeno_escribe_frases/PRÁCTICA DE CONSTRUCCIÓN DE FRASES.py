import random

# Base de datos de frases (español + inglés)
frases = [
    {
        "español": "El gobierno entregó a los agricultores un paquete de subsidios para mejorar la producción de cultivos regionales.",
        "componentes": {
            "quien": "El gobierno",
            "verbo": "entregó",
            "a_quien": "a los agricultores",
            "que": "un paquete de subsidios para mejorar la producción de cultivos regionales"
        },
        "ingles": "The government gave farmers a subsidy package to improve regional crop production."
    },
    # ... (Agrega aquí los otros 49 ejemplos en el mismo formato)
]

def practicar_orden():
    """Modo: Ordenar correctamente los componentes de la frase."""
    frase = random.choice(frases)
    componentes = [
        frase["componentes"]["quien"],
        frase["componentes"]["verbo"],
        frase["componentes"]["a_quien"],
        frase["componentes"]["que"]
    ]
    print("\n== Ordena los siguientes componentes ==")
    print(f"- Quién: {componentes[0]}")
    print(f"- Verbo: {componentes[1]}")
    print(f"- A quién: {componentes[2]}")
    print(f"- Qué: {componentes[3]}")
    
    respuesta = input("\nEscribe la frase ordenada (A QUIÉN corto primero): ")
    correcta = f'{componentes[0]} {componentes[1]} {componentes[2]} {componentes[3]}.'
    
    if respuesta.strip().lower() == correcta.lower():
        print("✅ ¡Correcto! Frase clara y bien estructurada.")
    else:
        print(f"❌ Mejor opción: {correcta}")

def traducir_frase():
    """Modo: Traducir la frase al inglés respetando el orden."""
    frase = random.choice(frases)
    print("\n== Traduce al inglés ==")
    print(f"ESPAÑOL: {frase['español']}")
    
    respuesta = input("INGLÉS: ")
    if respuesta.strip().lower() == frase['ingles'].lower():
        print("✅ ¡Traducción precisa!")
    else:
        print(f"❌ Traducción sugerida: {frase['ingles']}")

def reescribir_frase():
    """Modo: Corregir frases con orden incorrecto."""
    frase = random.choice(frases)
    componentes = [
        frase["componentes"]["quien"],
        frase["componentes"]["verbo"],
        frase["componentes"]["que"],  # Incorrecto: QUÉ primero
        frase["componentes"]["a_quien"]
    ]
    frase_desordenada = f'{componentes[0]} {componentes[1]} {componentes[2]} {componentes[3]}.'
    
    print("\n== Reescribe la frase con el orden correcto ==")
    print(f"Frase desordenada: {frase_desordenada}")
    
    respuesta = input("Tu corrección: ")
    correcta = f'{frase["componentes"]["quien"]} {frase["componentes"]["verbo"]} {frase["componentes"]["a_quien"]} {frase["componentes"]["que"]}.'
    
    if respuesta.strip().lower() == correcta.lower():
        print("✅ ¡Orden optimizado!")
    else:
        print(f"❌ Versión clara: {correcta}")

def menu():
    while True:
        print("\n=== PRÁCTICA DE CONSTRUCCIÓN DE FRASES ===")
        print("1. Ordenar componentes (A QUIÉN corto primero)")
        print("2. Traducir al inglés (Mantener brevedad primero)")
        print("3. Reescribir frases desordenadas")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        if opcion == "1":
            practicar_orden()
        elif opcion == "2":
            traducir_frase()
        elif opcion == "3":
            reescribir_frase()
        elif opcion == "4":
            print("¡Hasta luego! Sigue practicando ✍️")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
