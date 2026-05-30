import json
import os
import random

# Archivos de datos
EJEMPLOS_FILE = "ejemplos.json"
CUSTOM_FILE = "custom_ejemplos.json"
HISTORIAL_FILE = "oraciones_guardadas.txt"

# Cargar datos iniciales
ejemplos = [
    # ... (aquí irían los 50 ejemplos del listado anterior en formato JSON)
]

# Función para cargar/guardar datos
def cargar_datos(archivo, default=[]):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return default.copy()

def guardar_datos(archivo, datos):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

# Cargar datos iniciales
ejemplos = cargar_datos(EJEMPLOS_FILE, ejemplos)
custom_ejemplos = cargar_datos(CUSTOM_FILE)

# Menú principal
def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" ESTUDIO DE AUMENTATIVOS Y DIMINUTIVOS ".center(50))
        print("="*50)
        print("1. Ver ejemplos con práctica de oraciones")
        print("2. Diapositiva conceptual")
        print("3. Cuestionario interactivo")
        print("4. Gestionar ejemplos personalizados")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            practica_oraciones()
        elif opcion == "2":
            mostrar_diapositiva()
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            gestion_ejemplos()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Función para práctica de oraciones
def practica_oraciones():
    todos_ejemplos = ejemplos + custom_ejemplos
    random.shuffle(todos_ejemplos)
    
    for idx, ejemplo in enumerate(todos_ejemplos[:50], 1):
        print(f"\nEjemplo {idx}/50")
        print(f"Palabra base: {ejemplo['base']}")
        print(f"Forma modificada ({ejemplo['tipo'].upper()}): {ejemplo['modificado']}")
        
        while True:
            oracion = input("\nEscribe una oración usando la forma modificada: ").strip()
            if ejemplo['modificado'].lower() in oracion.lower():
                guardar_oracion(ejemplo, oracion)
                print("¡Correcto! Oración guardada.")
                break
            else:
                print(f"La oración debe contener: {ejemplo['modificado']}. Intenta nuevamente.")

# Función para guardar oraciones
def guardar_oracion(ejemplo, oracion):
    with open(HISTORIAL_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{ejemplo['base']},{ejemplo['modificado']},{ejemplo['tipo']},{oracion}\n")

# Diapositiva conceptual
def mostrar_diapositiva():
    print("\n" + "="*50)
    print(" CONCEPTOS CLAVE ".center(50))
    print("="*50)
    print("\nAUMENTATIVOS:")
    print("- Expresan aumento de tamaño/intensidad")
    print("- Sufijos comunes: -azo, -ón, -ote")
    print("- Ej: gigantazo (de gigante), señorón (de señor)")
    
    print("\nDIMINUTIVOS:")
    print("- Expresan pequeño tamaño o afecto")
    print("- Sufijos comunes: -ito, -illo, -ico")
    print("- Ej: florecilla (de flor), manecita (de mano)")
    
    print("\nSUPERLATIVOS:")
    print("- Expresan grado máximo (-ísimo/-ísima)")
    print("- Ej: grandísimo, blanquísimo")
    print("\n" + "="*50)
    input("\nPresione Enter para volver al menú...")

# Cuestionario interactivo
def cuestionario():
    todos_ejemplos = ejemplos + custom_ejemplos
    random.shuffle(todos_ejemplos)
    puntaje = 0
    
    for i, ejemplo in enumerate(todos_ejemplos[:10], 1):
        print(f"\nPregunta {i}/10")
        print(f"Palabra: {ejemplo['modificado']}")
        print("¿Qué tipo de modificación es?")
        print("1. Aumentativo")
        print("2. Diminutivo")
        print("3. Superlativo")
        
        respuesta = input("Seleccione (1-3): ")
        tipo_correcto = 1 if ejemplo['tipo'] == 'aumentativo' else 2 if ejemplo['tipo'] == 'diminutivo' else 3
        
        if respuesta == str(tipo_correcto):
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. Era: {ejemplo['tipo'].capitalize()}")
    
    print(f"\nPuntaje final: {puntaje}/10 ({puntaje*10}%)")

# Gestión de ejemplos personalizados
def gestion_ejemplos():
    while True:
        print("\nGESTIÓN DE EJEMPLOS PERSONALIZADOS")
        print("1. Crear nuevo ejemplo")
        print("2. Ver ejemplos guardados")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            crear_ejemplo()
        elif opcion == "2":
            ver_ejemplos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

def crear_ejemplo():
    if len(custom_ejemplos) >= 100:
        print("Límite de 100 ejemplos alcanzado.")
        return
    
    base = input("Palabra base: ").strip()
    modificado = input("Forma modificada: ").strip()
    
    while True:
        tipo = input("Tipo (aumentativo/diminutivo): ").lower()
        if tipo in ['aumentativo', 'diminutivo']:
            break
        print("Tipo no válido. Use 'aumentativo' o 'diminutivo'")
    
    custom_ejemplos.append({
        'base': base,
        'modificado': modificado,
        'tipo': tipo
    })
    guardar_datos(CUSTOM_FILE, custom_ejemplos)
    print("Ejemplo guardado exitosamente!")

def ver_ejemplos():
    print("\nEJEMPLOS PERSONALIZADOS GUARDADOS:")
    for idx, ejemplo in enumerate(custom_ejemplos, 1):
        print(f"{idx}. {ejemplo['base']} -> {ejemplo['modificado']} ({ejemplo['tipo']})")

# Inicializar archivos si no existen
if not os.path.exists(EJEMPLOS_FILE):
    guardar_datos(EJEMPLOS_FILE, ejemplos)

if __name__ == "__main__":
    menu_principal()
