import json

# Archivo donde se guardarán los ejemplos personalizados
FILE_NAME = "ejemplos_negacion.json"

# Lista de ejemplos de incompatibilidad de negación con anteposición
ejemplos = [
    {"afirmativa": "Bastantes problemas tenemos.", "negativa": "Bastantes problemas no tenemos."},
    {"afirmativa": "Con poco se conforma María.", "negativa": "Con poco no se conforma María."},
    {"afirmativa": "Eso haría él.", "negativa": "Eso no haría él."},
    {"afirmativa": "En casa nos sentimos cómodos.", "negativa": "En casa no nos sentimos cómodos."},
    {"afirmativa": "Mucho ha trabajado para esto.", "negativa": "Mucho no ha trabajado para esto."}
]

# Cargar ejemplos guardados
def cargar_ejemplos():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return ejemplos

# Guardar ejemplos nuevos
def guardar_ejemplos(ejemplos):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(ejemplos, file, ensure_ascii=False, indent=4)

def practicar_ejercicios(ejemplos):
    for ejemplo in ejemplos:
        print(f"Oración afirmativa: {ejemplo['afirmativa']}")
        respuesta = input("Ingrese la versión negativa: ")
        
        if respuesta.strip() == ejemplo["negativa"]:
            print("✅ Correcto!")
        else:
            print(f"❌ Incorrecto. La versión correcta es: {ejemplo['negativa']}")
            nueva_version = input("Escriba nuevamente la versión correcta: ")
            if nueva_version.strip():
                ejemplo["negativa"] = nueva_version.strip()
    
    guardar_ejemplos(ejemplos)

def agregar_ejemplo(ejemplos):
    if len(ejemplos) >= 100:
        print("❌ Límite de ejemplos alcanzado (100). No se pueden agregar más.")
        return
    
    afirmativa = input("Ingrese la oración afirmativa: ")
    negativa = input("Ingrese la oración negativa incorrecta: ")
    ejemplos.append({"afirmativa": afirmativa, "negativa": negativa})
    guardar_ejemplos(ejemplos)
    print("✅ Ejemplo agregado correctamente.")

def menu():
    ejemplos = cargar_ejemplos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Practicar ejercicios")
        print("2. Agregar nuevo ejemplo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            practicar_ejercicios(ejemplos)
        elif opcion == "2":
            agregar_ejemplo(ejemplos)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

menu()
