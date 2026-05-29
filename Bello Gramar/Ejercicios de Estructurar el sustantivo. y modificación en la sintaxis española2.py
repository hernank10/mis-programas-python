import random

# Base de datos mejorada con ejemplos iniciales
ejemplos = [
    {
        "oracion": "El niño curioso preguntó sobre las estrellas.",
        "tipo": "adjetivo",
        "modificador": "curioso",
        "oracion_parcial": "El niño [  ] preguntó sobre las estrellas."
    },
    {
        "oracion": "Las hojas del otoño cubrían el suelo.",
        "tipo": "complemento",
        "modificador": "del otoño",
        "oracion_parcial": "Las hojas [  ] cubrían el suelo."
    },
    {
        "oracion": "El hombre que vive en la colina es misterioso.",
        "tipo": "proposicion",
        "modificador": "que vive en la colina",
        "oracion_parcial": "El hombre [  ] es misterioso."
    }
]

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Clasificar modificación")
    print("2. Reescribir oración")
    print("3. Crear nuevas oraciones")
    print("4. Ver ejemplos (categorías/paginados)")
    print("5. Cuestionario completar espacios")
    print("6. Cuestionario opción múltiple")
    print("7. Salir")
    return input("Seleccione una opción (1-7): ")

def ver_ejemplos():
    print("\n--- Visualización de ejemplos ---")
    print("1. Ver por categorías\n2. Ver paginados")
    choice = input("Opción: ")
    
    if choice == "1":
        categorias = {}
        for ej in ejemplos:
            key = ej["tipo"].capitalize()
            if key not in categorias:
                categorias[key] = []
            categorias[key].append(ej["oracion"])
        
        for tipo, lista in categorias.items():
            print(f"\n=== {tipo} ===")
            for i, oracion in enumerate(lista, 1):
                print(f"{i}. {oracion}")
    
    elif choice == "2":
        pagina = 0
        while True:
            inicio = pagina * 10
            fin = inicio + 10
            actual = ejemplos[inicio:fin]
            
            if not actual:
                print("Fin del listado")
                break
                
            print(f"\n--- Página {pagina + 1} ---")
            for i, ej in enumerate(actual, inicio + 1):
                print(f"{i}. {ej['oracion']}")
                
            if fin < len(ejemplos):
                input("\nEnter para siguiente página...")
                pagina += 1
            else:
                break

def cuestionario_completar():
    disponibles = [e for e in ejemplos if "modificador" in e]
    
    if not disponibles:
        print("¡Primero crea algunas oraciones!")
        return
    
    ejemplo = random.choice(disponibles)
    print(f"\nCompleta el espacio en blanco:")
    print(ejemplo["oracion_parcial"])
    respuesta = input("Tu respuesta: ").strip()
    
    if respuesta.lower() == ejemplo["modificador"].lower():
        print("¡Correcto! ✔️")
    else:
        print(f"Incorrecto. Respuesta correcta: {ejemplo['modificador']} ❌")

def cuestionario_opcion_multiple():
    if not ejemplos:
        print("¡No hay ejemplos disponibles!")
        return
    
    ejemplo = random.choice(ejemplos)
    opciones = ["adjetivo", "complemento", "proposicion"]
    random.shuffle(opciones)
    
    print(f"\nOración: {ejemplo['oracion']}")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion.capitalize()}")
    
    try:
        respuesta = int(input("Opción correcta (1-3): ")) - 1
        if opciones[respuesta] == ejemplo["tipo"]:
            print("¡Correcto! ✔️")
        else:
            print(f"Incorrecto. La respuesta era: {ejemplo['tipo'].capitalize()} ❌")
    except:
        print("Entrada inválida ❌")

def crear_oraciones():
    if len(ejemplos) >= 100:
        print("¡Base de datos llena (máximo 100 ejemplos)!")
        return
    
    print("\nFormato requerido:")
    print("Adjetivo: 'El pájaro colorido' → Modificador: 'colorido'")
    print("Complemento: 'El camino hacia el bosque' → Modificador: 'hacia el bosque'")
    print("Proposición: 'La casa donde nací' → Modificador: 'donde nací'\n")
    
    tipo = input("Tipo (adjetivo/complemento/proposicion): ").lower()
    if tipo not in ["adjetivo", "complemento", "proposicion"]:
        print("Tipo inválido")
        return
    
    oracion = input("Oración completa: ")
    modificador = input("Modificador utilizado: ")
    
    # Crear oración con espacio en blanco
    oracion_parcial = oracion.replace(modificador, "[  ]", 1)
    
    ejemplos.append({
        "oracion": oracion,
        "tipo": tipo,
        "modificador": modificador,
        "oracion_parcial": oracion_parcial
    })
    print("¡Oración añadida exitosamente!")

# Resto de funciones anteriores (clasificar_modificacion, reescribir_oracion) permanecen igual

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
        ver_ejemplos()
    elif opcion == "5":
        cuestionario_completar()
    elif opcion == "6":
        cuestionario_opcion_multiple()
    elif opcion == "7":
        print("¡Hasta luego! 👋")
        break
    else:
        print("Opción inválida")
    
    input("\nPresione Enter para continuar...")
