import random

# Lista de ejemplos clasificados
ejemplos = [
    ("El niño travieso juega en el parque.", "adjetivo"),
    ("La ciudad antigua guarda muchos secretos.", "adjetivo"),
    ("La dama elegante caminaba por el salón.", "adjetivo"),
    ("La sin par Dulcinea", "complemento"),
    ("Las orillas del Maipo estaban cubiertas de flores.", "complemento"),
    ("El cuadro de Goya se exhibe en el museo.", "complemento"),
    ("Aquel gran bulto que allí se ve", "proposición"),
    ("La persona a quien vimos ayer en el paseo", "proposición"),
    ("La campiña por donde transitábamos", "proposición"),
]

# Función principal
def juego_de_sintaxis():
    print("\n🧠 Bienvenido al juego de la sintaxis del sustantivo.")
    print("Clasifica, transforma y crea oraciones con adjetivos, complementos y proposiciones.")
    
    while True:
        # Mostrar ejemplo aleatorio
        oracion, tipo = random.choice(ejemplos)
        print(f"\n🔸 Oración: {oracion}")
        
        # Clasificación
        clasificacion = input("👉 ¿Qué tipo de modificación tiene esta oración? (adjetivo / complemento / proposición): ").strip().lower()
        if clasificacion == tipo:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {tipo}")
        
        # Reescritura
        nueva = input("✍️ Reescribe esta oración cambiando el tipo de modificador (por ejemplo, adjetivo → complemento):\n> ")
        print(f"📝 Nueva versión registrada: {nueva}")
        
        # Creación
        print("\n🎨 Ahora crea tus propias oraciones con los tres tipos de modificación.")
        or1 = input("1. Con adjetivo: ")
        or2 = input("2. Con complemento (como 'de', 'con', etc.): ")
        or3 = input("3. Con proposición subordinada: ")
        print("\n✅ Tus oraciones:")
        print(f"   - Adjetivo: {or1}")
        print(f"   - Complemento: {or2}")
        print(f"   - Proposición: {or3}")
        
        continuar = input("\n¿Quieres practicar con otra oración? (s/n): ").strip().lower()
        if continuar != 's':
            print("👋 ¡Gracias por practicar sintaxis! Hasta la próxima.")
            break

# Ejecutar el programa
juego_de_sintaxis()
