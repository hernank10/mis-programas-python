import json

# Diccionario para almacenar las reglas y ejemplos
reglas = []

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Identificar base y afijo")
    print("2. Distinguir patrón productivo")
    print("3. Registrar variación diatópica/diacrónica")
    print("4. Añadir caso prototípico o excepción")
    print("5. Redactar regla completa")
    print("6. Ver todas las reglas")
    print("7. Guardar reglas en archivo")
    print("8. Salir")

def identificar_base_afijo():
    verbo = input("Introduce un verbo derivado: ")
    base = input("¿Cuál es la base léxica?: ")
    afijo = input("¿Cuál es el afijo derivativo?: ")
    reglas.append({"verbo": verbo, "base": base, "afijo": afijo})

def distinguir_patron():
    patron = input("Describe el patrón morfológico (ej. N-izar, A-ecer): ")
    descripcion = input("Explica brevemente su productividad: ")
    reglas[-1]["patron"] = patron
    reglas[-1]["descripcion_patron"] = descripcion

def registrar_variacion():
    tipo = input("¿Qué tipo de variación? (diatópica o diacrónica): ")
    detalle = input("Explica el detalle de esta variación: ")
    reglas[-1]["variacion"] = {"tipo": tipo, "detalle": detalle}

def añadir_caso():
    tipo = input("¿Es caso prototípico o excepción?: ")
    ejemplo = input("Introduce un ejemplo ilustrativo: ")
    reglas[-1]["caso"] = {"tipo": tipo, "ejemplo": ejemplo}

def redactar_regla():
    regla = input("Redacta la regla de derivación verbal completa: ")
    reglas[-1]["regla_redactada"] = regla

def ver_reglas():
    if not reglas:
        print("No hay reglas registradas aún.")
        return
    for i, r in enumerate(reglas):
        print(f"\n[{i+1}] Verbo: {r.get('verbo')}")
        print(f"  Base: {r.get('base')} | Afijo: {r.get('afijo')}")
        print(f"  Patrón: {r.get('patron')} ({r.get('descripcion_patron')})")
        print(f"  Variación: {r.get('variacion', {}).get('tipo')} - {r.get('variacion', {}).get('detalle')}")
        print(f"  Caso: {r.get('caso', {}).get('tipo')} - {r.get('caso', {}).get('ejemplo')}")
        print(f"  Regla redactada: {r.get('regla_redactada')}")

def guardar_reglas():
    with open("reglas_derivacion.json", "w", encoding="utf-8") as f:
        json.dump(reglas, f, indent=4, ensure_ascii=False)
    print("Reglas guardadas en 'reglas_derivacion.json'.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-8): ")
    
    if opcion == "1":
        identificar_base_afijo()
    elif opcion == "2":
        distinguir_patron()
    elif opcion == "3":
        registrar_variacion()
    elif opcion == "4":
        añadir_caso()
    elif opcion == "5":
        redactar_regla()
    elif opcion == "6":
        ver_reglas()
    elif opcion == "7":
        guardar_reglas()
    elif opcion == "8":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
