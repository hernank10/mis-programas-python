import random

# Base de datos de ejemplos y sus tipos de modificación
ejemplos = [
    # Adjetivos (A)
    {"oracion": "El niño curioso preguntó sobre las estrellas.", "tipo": "adjetivo"},
    {"oracion": "La montaña nevada brillaba bajo el sol.", "tipo": "adjetivo"},
    # ... Agregar aquí el resto de los 50 ejemplos originales
    # Complementos (B)
    {"oracion": "Las hojas del otoño cubrían el suelo.", "tipo": "complemento"},
    {"oracion": "El sabor a vainilla del postre era delicioso.", "tipo": "complemento"},
    # Proposiciones (C)
    {"oracion": "El hombre que vive en la colina es misterioso.", "tipo": "proposicion"},
    {"oracion": "La película que vimos anoche fue impactante.", "tipo": "proposicion"}
]

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Clasificar modificación en oración aleatoria")
    print("2. Reescribir oración con diferente modificación")
    print("3. Crear nuevas oraciones")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def clasificar_modificacion():
    ejemplo = random.choice(ejemplos)
    print(f"\nOración: {ejemplo['oracion']}")
    respuesta = input("¿Qué tipo de modificación es? (adjetivo/complemento/proposicion): ").lower()
    
    if respuesta == ejemplo['tipo']:
        print("¡Correcto! ✔️")
    else:
        print(f"Incorrecto. La respuesta correcta era: {ejemplo['tipo'].capitalize()} ❌")

def reescribir_oracion():
    ejemplo = random.choice(ejemplos)
    print(f"\nOración original: {ejemplo['oracion']}")
    print("Ejemplo de reescritura:")
    
    if ejemplo['tipo'] == "adjetivo":
        print("Cambiar adjetivo por complemento: 'El hombre honrado' → 'El hombre con principios'")
    elif ejemplo['tipo'] == "complemento":
        print("Cambiar complemento por proposición: 'Las hojas del otoño' → 'Las hojas que caen en octubre'")
    else:
        print("Cambiar proposición por adjetivo: 'El libro que compré ayer' → 'El libro nuevo'")
    
    input("\nPresiona Enter para escribir tu propia versión...")
    nueva_version = input("Escribe tu versión modificada: ")
    print("\n¡Versión guardada! Tu creación:")
    print(f"Original: {ejemplo['oracion']}")
    print(f"Modificada: {nueva_version}")

def crear_oraciones():
    print("\nCrea oraciones según los modelos:")
    tipos = {
        "adjetivo": "Ej: 'El pájaro colorido'",
        "complemento": "Ej: 'El camino hacia el bosque'",
        "proposicion": "Ej: 'La casa donde nací'"
    }
    
    for tipo, ejemplo in tipos.items():
        print(f"\nTipo: {tipo.capitalize()} ({ejemplo})")
        oracion = input("Escribe tu oración: ")
        ejemplos.append({"oracion": oracion, "tipo": tipo})
    
    print("\n¡Tus nuevas oraciones se han añadido a la base de datos!")

# Programa principal
while True:
    opcion = menu_principal()
    
    if opcion == "1":
        clasificar_modificacion()
    elif opcion == "2":
        reescribir_oracion()
    elif opcion == "3":
        crear_oraciones()
    elif opcion == "4":
        print("¡Hasta luego! 👋")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    input("\nPresiona Enter para continuar...")
