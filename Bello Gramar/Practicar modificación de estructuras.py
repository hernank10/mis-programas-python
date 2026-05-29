import json
import os

# Datos iniciales
estructuras = {
    "Adjetivo modificado": {
        "definicion": "El adjetivo puede ser modificado por adverbios, complementos o proposiciones",
        "ejemplos": [
            {"texto": "muy prudente", "modificador": "muy", "tipo": "adverbio"},
            {"texto": "abundante de frutos", "modificador": "de frutos", "tipo": "complemento"},
            {"texto": "severó en sus costumbres, como lo habían sido sus padres", "modificador": "como lo habían sido sus padres", "tipo": "proposición"}
        ]
    },
    "Adverbio modificado": {
        "definicion": "El adverbio puede ser modificado por otros adverbios, complementos o proposiciones",
        "ejemplos": [
            {"texto": "muy bien", "modificador": "muy", "tipo": "adverbio"},
            {"texto": "cerca del río", "modificador": "del río", "tipo": "complemento"},
            {"texto": "allí solo florecen las artes, donde se les proponen recompensas", "modificador": "donde se les proponen recompensas", "tipo": "proposición"}
        ]
    },
    "Complementos modificados": {
        "definicion": "Los complementos pueden ser modificados por adverbios o proposiciones",
        "ejemplos": [
            {"texto": "muy a propósito", "modificador": "muy", "tipo": "adverbio"},
            {"texto": "sin luz como estaba el aposento", "modificador": "como estaba el aposento", "tipo": "proposición"}
        ]
    },
    "Verbo modificado": {
        "definicion": "El verbo puede ser modificado por predicados, adverbios, complementos o proposiciones",
        "ejemplos": [
            {"texto": "es virtuosa", "modificador": "virtuosa", "tipo": "predicado"},
            {"texto": "habla bien", "modificador": "bien", "tipo": "adverbio"},
            {"texto": "va al campo", "modificador": "al campo", "tipo": "complemento"},
            {"texto": "cuando el cuadrillero tal oyó, túvole por hombre falto de juicio", "modificador": "cuando el cuadrillero tal oyó", "tipo": "proposición"}
        ]
    }
}

ARCHIVO_EJEMPLOS = "ejemplos_guardados.json"

def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, 'r') as f:
            return json.load(f)
    return {}

def guardar_ejemplos(datos):
    with open(ARCHIVO_EJEMPLOS, 'w') as f:
        json.dump(datos, f, indent=2)

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Practicar modificación de estructuras")
    print("2. Identificar palabras modificadas")
    print("3. Crear/Ver/Guardar ejemplos")
    print("4. Salir")
    return input("Seleccione una opción: ")

def practicar_reescritura():
    print("\n=== PRÁCTICA DE MODIFICACIÓN ===")
    for categoria, datos in estructuras.items():
        print(f"\nCategoría: {categoria}")
        print(f"Definición: {datos['definicion']}")
        for ejemplo in datos['ejemplos']:
            print(f"\nEjemplo: {ejemplo['texto']}")
            user_input = input("Reescribe el ejemplo subrayando el modificador (usa ** para subrayar): ")
            if user_input.replace("**", "") == ejemplo['texto']:
                print(f"¡Correcto! Modificador: {ejemplo['modificador']}")
            else:
                print(f"Inténtalo de nuevo. El modificador correcto era: {ejemplo['modificador']}")

def identificar_palabra_modificada():
    print("\n=== IDENTIFICAR PALABRA MODIFICADA ===")
    ejemplos_mezclados = []
    for categoria, datos in estructuras.items():
        for ejemplo in datos['ejemplos']:
            ejemplos_mezclados.append((ejemplo['texto'], categoria.split()[0].lower()))
    
    for texto, tipo in ejemplos_mezclados:
        print(f"\nEjemplo: {texto}")
        print("Opciones:")
        print("1. Adjetivo\n2. Adverbio\n3. Complemento\n4. Verbo")
        respuesta = input("¿Qué tipo de palabra está siendo modificada? (1-4): ")
        opciones = {1: "adjetivo", 2: "adverbio", 3: "complemento", 4: "verbo"}
        if opciones.get(int(respuesta), "") == tipo:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: {tipo.capitalize()}")

def gestionar_ejemplos():
    ejemplos_guardados = cargar_ejemplos()
    
    while True:
        print("\n=== GESTIÓN DE EJEMPLOS ===")
        print("1. Crear nuevo ejemplo")
        print("2. Ver ejemplos guardados")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            categoria = input("Categoría (Adjetivo/Adverbio/Complemento/Verbo): ").capitalize()
            texto = input("Ingrese el ejemplo: ")
            modificador = input("Ingrese el modificador: ")
            tipo = input("Tipo de modificador (adverbio/complemento/proposición/predicado): ")
            
            if categoria not in ejemplos_guardados:
                ejemplos_guardados[categoria] = []
            ejemplos_guardados[categoria].append({
                "texto": texto,
                "modificador": modificador,
                "tipo": tipo
            })
            guardar_ejemplos(ejemplos_guardados)
            print("¡Ejemplo guardado exitosamente!")
        
        elif opcion == "2":
            if not ejemplos_guardados:
                print("No hay ejemplos guardados.")
                continue
            for categoria, ejemplos in ejemplos_guardados.items():
                print(f"\nCategoría: {categoria}")
                for i, ejemplo in enumerate(ejemplos, 1):
                    print(f"{i}. {ejemplo['texto']} - Modificador: {ejemplo['modificador']}")
        
        elif opcion == "3":
            break

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            practicar_reescritura()
        elif opcion == "2":
            identificar_palabra_modificada()
        elif opcion == "3":
            gestionar_ejemplos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
