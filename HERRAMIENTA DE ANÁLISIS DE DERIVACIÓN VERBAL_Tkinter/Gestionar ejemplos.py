import json
import os

# Estructura de datos
DATA_FILE = "verbos.json"
CATEGORIAS = {
    1: "Epéntesis (Inserción consonántica)",
    2: "Síncopa y Epéntesis en Futuro/Condicional",
    3: "Alternancias Consonánticas/Vocálicas",
    4: "Pretéritos Fuertes",
    5: "Participios Irregulares",
    6: "Verbos de Conjugación Especial",
    7: "Verbos Defectivos"
}

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {str(k): [] for k in CATEGORIAS}

def guardar_datos(datos):
    with open(DATA_FILE, 'w') as f:
        json.dump(datos, f, indent=2)

def mostrar_progreso(datos):
    print("\n--- PROGRESO ---")
    total = 0
    for cat, ejemplos in datos.items():
        print(f"Categoría {cat} ({CATEGORIAS[int(cat)]}):")
        print(f"Ejemplos: {len(ejemplos)}/100 ({len(ejemplos)/100:.0%})")
        total += len(ejemplos)
    print(f"\nTOTAL: {total}/700 ({total/700:.0%})")

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar ejemplos")
        print("2. Ver progreso")
        print("3. Salir y guardar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            gestionar_ejemplos()
        elif opcion == '2':
            mostrar_progreso(cargar_datos())
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

def gestionar_ejemplos():
    datos = cargar_datos()
    while True:
        print("\n--- CATEGORÍAS ---")
        for k, v in CATEGORIAS.items():
            print(f"{k}. {v} ({len(datos[str(k)])}/100)")
        
        try:
            cat = input("\nSeleccione categoría (1-7) o '0' para volver: ")
            if cat == '0':
                guardar_datos(datos)
                return
            
            if cat not in [str(i) for i in range(1,8)]:
                raise ValueError
                
            menu_categoria(datos, cat)
            
        except ValueError:
            print("Categoría inválida")

def menu_categoria(datos, cat):
    while True:
        print(f"\n--- {CATEGORIAS[int(cat)].upper()} ---")
        print("1. Agregar ejemplo")
        print("2. Editar ejemplo")
        print("3. Eliminar ejemplo")
        print("4. Ver ejemplos")
        print("5. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_ejemplo(datos, cat)
        elif opcion == '2':
            editar_ejemplo(datos, cat)
        elif opcion == '3':
            eliminar_ejemplo(datos, cat)
        elif opcion == '4':
            ver_ejemplos(datos, cat)
        elif opcion == '5':
            return
        else:
            print("Opción inválida")

def agregar_ejemplo(datos, cat):
    if len(datos[cat]) >= 100:
        print("¡Límite de 100 ejemplos alcanzado!")
        return
    
    verbo = input("Verbo en infinitivo: ")
    conjugacion = input("Conjugación completa: ")
    ejemplo = input("Oración de ejemplo: ")
    
    nuevo = {
        "id": len(datos[cat]) + 1,
        "verbo": verbo,
        "conjugacion": conjugacion,
        "ejemplo": ejemplo
    }
    
    datos[cat].append(nuevo)
    print("¡Ejemplo agregado exitosamente!")

def editar_ejemplo(datos, cat):
    ver_ejemplos(datos, cat)
    try:
        ej_id = int(input("ID del ejemplo a editar: "))
        ejemplo = next((e for e in datos[cat] if e['id'] == ej_id), None)
        
        if not ejemplo:
            print("ID no encontrado")
            return
            
        print("\nDeje en blanco para no modificar")
        nuevo_verbo = input(f"Verbo actual ({ejemplo['verbo']}): ")
        nueva_conj = input(f"Conjugación actual ({ejemplo['conjugacion']}): ")
        nuevo_ej = input(f"Oración actual ({ejemplo['ejemplo']}): ")
        
        if nuevo_verbo:
            ejemplo['verbo'] = nuevo_verbo
        if nueva_conj:
            ejemplo['conjugacion'] = nueva_conj
        if nuevo_ej:
            ejemplo['ejemplo'] = nuevo_ej
            
        print("Ejemplo actualizado correctamente")
        
    except ValueError:
        print("ID debe ser numérico")

def eliminar_ejemplo(datos, cat):
    ver_ejemplos(datos, cat)
    try:
        ej_id = int(input("ID del ejemplo a eliminar: "))
        datos[cat] = [e for e in datos[cat] if e['id'] != ej_id]
        print("Ejemplo eliminado correctamente")
    except ValueError:
        print("ID debe ser numérico")

def ver_ejemplos(datos, cat):
    print("\n--- EJEMPLOS ---")
    if not datos[cat]:
        print("No hay ejemplos aún")
        return
    
    for e in datos[cat]:
        print(f"\nID: {e['id']}")
        print(f"Verbo: {e['verbo']}")
        print(f"Conjugación: {e['conjugacion']}")
        print(f"Ejemplo: {e['ejemplo']}")

if __name__ == "__main__":
    menu_principal()
