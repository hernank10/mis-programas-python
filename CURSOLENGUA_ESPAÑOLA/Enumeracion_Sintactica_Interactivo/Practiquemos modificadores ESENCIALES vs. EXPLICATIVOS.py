import json
import random
from pathlib import Path

EJEMPLOS_ARCHIVO = "modificadores.json"
MAX_EJEMPLOS = 100

# Cargar/Crear archivo de ejemplos
def cargar_ejemplos():
    try:
        with open(EJEMPLOS_ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_ARCHIVO, "w") as f:
        json.dump(ejemplos[-MAX_EJEMPLOS:], f, indent=2)

# Ejemplos base
ejemplos_base = [
    {
        "oracion": "Los estudiantes que entran a la Biblioteca con su carnet pueden pedir hasta tres libros.",
        "tipo": "E",
        "corregida": "Los estudiantes pueden pedir hasta tres libros en préstamo. (E: Solo los con carnet)",
        "explicacion": "Modificador esencial: Restringe a un grupo específico."
    },
    {
        "oracion": "Las ventanas, que dan a la calle 9, serán reforzadas.",
        "tipo": "X",
        "corregida": "Las ventanas serán reforzadas. (X: Todas dan a la calle 9)",
        "explicacion": "Modificador explicativo: Información adicional."
    }
]

# Menú principal
def menu_principal():
    print("""
▓▓▓ Menú Modificadores ▓▓▓
1. ❓ Cuestionario interactivo
2. ✍️ Crear nuevos ejemplos
3. 📂 Ver ejemplos guardados
4. 🚪 Salir
""")
    return input("Selecciona una opción (1-4): ")

# Función para cuestionario
def cuestionario_interactivo():
    ejemplos_guardados = cargar_ejemplos()
    todos_ejemplos = ejemplos_base + ejemplos_guardados
    random.shuffle(todos_ejemplos)
    puntaje = 0

    for idx, ejemplo in enumerate(todos_ejemplos, 1):
        print(f"\n◆ Ejercicio {idx} ◆\nOración: {ejemplo['oracion']}")
        
        # Paso 1: Identificar tipo
        while True:
            respuesta = input("\n¿Es esencial (E) o explicativo (X)? ").upper()
            if respuesta in ("E", "X"):
                break
            print("Error: Solo se permite E o X")

        # Paso 2: Reescribir corrección
        correccion = input("\nReescribe la oración correctamente: ")

        # Verificación
        if respuesta == ejemplo["tipo"] and correccion.strip().lower() == ejemplo["corregida"].lower():
            puntaje += 20
            print(f"✅ ¡Doble acierto! +20 puntos\nExplicación: {ejemplo['explicacion']}")
        elif respuesta == ejemplo["tipo"]:
            puntaje += 10
            print(f"✓ Correcto tipo (+10)\nVersión ideal: {ejemplo['corregida']}\nExplicación: {ejemplo['explicacion']}")
        else:
            print(f"✗ Error. Respuesta correcta: {ejemplo['tipo']}\nVersión ideal: {ejemplo['corregida']}\nExplicación: {ejemplo['explicacion']}")

    print(f"\n▓ Puntaje final: {puntaje} puntos ▓")

# Función para crear ejemplos
def crear_ejemplos():
    ejemplos = cargar_ejemplos()
    
    print("\n✍️ Crear nuevo ejemplo:")
    while True:
        oracion = input("\nIngresa la oración con modificador: ")
        tipo = input("¿Es esencial (E) o explicativo (X)? ").upper()
        corregida = input("Escribe la versión corregida: ")
        explicacion = input("Explicación breve: ")
        
        ejemplos.append({
            "oracion": oracion,
            "tipo": tipo,
            "corregida": corregida,
            "explicacion": explicacion
        })
        
        guardar_ejemplos(ejemplos)
        print("¡Ejemplo guardado exitosamente!")
        
        if len(ejemplos) >= MAX_EJEMPLOS:
            print("⚠️ Has alcanzado el límite de 100 ejemplos.")
            break
            
        if input("¿Crear otro? (s/n): ").lower() != "s":
            break

# Función para ver ejemplos
def ver_ejemplos():
    ejemplos = cargar_ejemplos()
    print(f"\n📚 Ejemplos guardados ({len(ejemplos)}):")
    for i, ej in enumerate(ejemplos, 1):
        print(f"\n◆ Ejemplo {i} ◆")
        print(f"Original: {ej['oracion']}")
        print(f"Tipo: {'Esencial' if ej['tipo'] == 'E' else 'Explicativo'}")
        print(f"Corrección: {ej['corregida']}")
        print(f"Explicación: {ej['explicacion']}")

# Ejecución principal
if __name__ == "__main__":
    Path(EJEMPLOS_ARCHIVO).touch(exist_ok=True)  # Crear archivo si no existe
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            cuestionario_interactivo()
        elif opcion == "2":
            crear_ejemplos()
        elif opcion == "3":
            ver_ejemplos()
        elif opcion == "4":
            print("¡Hasta luego! ✨")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")
